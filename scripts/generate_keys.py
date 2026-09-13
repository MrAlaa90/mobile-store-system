import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_key_pair():
    os.makedirs("secrets", exist_ok=True)
    os.makedirs("desktop/keys", exist_ok=True)

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("secrets/private_key.pem", "wb") as f:
        f.write(private_pem)

    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("desktop/keys/public_key.pem", "wb") as f:
        f.write(public_pem)

if __name__ == "__main__":
    generate_key_pair()
    print("RSA Keys generated: secrets/private_key.pem and desktop/keys/public_key.pem")
