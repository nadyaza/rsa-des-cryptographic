# client_with_encryption_display.py
import socket
from Crypto.Cipher import PKCS1_OAEP, DES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

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

def client_program():
    host = socket.gethostname()
    port = 5000

    # Setup client socket
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # Terima public key RSA dari server (PKA)
    public_key_rsa = client_socket.recv(2048)
    rsa_key = RSA.import_key(public_key_rsa)
    print("[CLIENT] Public key RSA diterima:\n", public_key_rsa.decode())

    # Generate DES key dan encrypt dengan RSA
    des_key = get_random_bytes(8)  # DES key (8-byte)
    print("[CLIENT] DES Key yang dihasilkan:", des_key)

    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    encrypted_des_key = cipher_rsa.encrypt(des_key)
    print("[CLIENT] DES Key (terenkripsi):", to_base64(encrypted_des_key))
    client_socket.send(encrypted_des_key)

    # Terima IV dari server
    iv = client_socket.recv(8)
    print("[CLIENT] IV diterima:", to_base64(iv))

    while True:
        message = input("Kirim pesan -> ")
        if message.lower().strip() == 'bye':
            break

        # Enkripsi pesan dengan DES dan kirim
        cipher_des = DES.new(des_key, DES.MODE_CBC, iv)
        encrypted_message = cipher_des.encrypt(pad(message).encode())
        print("[CLIENT] Pesan terenkripsi ke server:", to_base64(encrypted_message))
        client_socket.send(encrypted_message)

        # Terima dan dekripsi respons dari server
        encrypted_response = client_socket.recv(1024)
        print("[CLIENT] Pesan terenkripsi dari server:", to_base64(encrypted_response))

        cipher_des = DES.new(des_key, DES.MODE_CBC, iv)
        decrypted_response = unpad(cipher_des.decrypt(encrypted_response).decode())
        print(f"[CLIENT] Pesan setelah didekripsi: {decrypted_response}")

    client_socket.close()

if __name__ == '__main__':
    client_program()
