# server_with_encryption_display.py
import socket
import os
from Crypto.Cipher import PKCS1_OAEP, DES
from Crypto.PublicKey import RSA

BLOCK_SIZE = 8

def pad(data):
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + chr(padding_len) * padding_len

def unpad(data):
    padding_len = ord(data[-1])
    return data[:-padding_len]

def to_base64(data):
    """Helper untuk mencetak dalam Base64 agar lebih mudah dibaca."""
    import base64
    return base64.b64encode(data).decode('utf-8')

def server_program():
    host = socket.gethostname()
    port = 5000

    # Setup server socket
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("[SERVER] Menunggu koneksi...")

    # Generate RSA key pair (sebagai PKA)
    key_pair = RSA.generate(2048)
    private_key = key_pair.export_key()
    public_key = key_pair.publickey().export_key()
    print("[SERVER] Public Key RSA:\n", public_key.decode())

    conn, address = server_socket.accept()
    print("[SERVER] Connection from:", str(address))

    # Kirim public key ke client
    conn.send(public_key)
    print("[SERVER] Public key RSA dikirim ke client.")

    # Terima DES key terenkripsi dari client
    encrypted_des_key = conn.recv(256)
    print("[SERVER] DES Key (encrypted):", to_base64(encrypted_des_key))

    cipher_rsa = PKCS1_OAEP.new(key_pair)
    try:
        des_key = cipher_rsa.decrypt(encrypted_des_key)
        print("[SERVER] DES Key berhasil didekripsi:", des_key)
    except ValueError:
        print("[SERVER] Gagal mendekripsi DES Key.")
        conn.close()
        return

    # Generate IV dan kirim ke client
    iv = os.urandom(8)
    print("[SERVER] IV yang dihasilkan:", to_base64(iv))
    conn.send(iv)

    while True:
        encrypted_data = conn.recv(1024)
        if not encrypted_data:
            break

        print("[SERVER] Pesan terenkripsi diterima:", to_base64(encrypted_data))

        # Decrypt data dengan DES
        cipher_des = DES.new(des_key, DES.MODE_CBC, iv)
        try:
            decrypted_message = unpad(cipher_des.decrypt(encrypted_data).decode())
            print(f"[SERVER] Pesan setelah didekripsi: {decrypted_message}")
        except Exception as e:
            print("[SERVER] Error saat mendekripsi:", e)
            continue

        # Balas pesan
        response = input("Balas pesan -> ")
        cipher_des = DES.new(des_key, DES.MODE_CBC, iv)
        encrypted_response = cipher_des.encrypt(pad(response).encode())
        print("[SERVER] Pesan terenkripsi ke client:", to_base64(encrypted_response))
        conn.send(encrypted_response)

    conn.close()

if __name__ == '__main__':
    server_program()
