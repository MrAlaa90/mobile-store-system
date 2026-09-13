import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

class LicenseVerifier:
    def __init__(self, public_key_path: str = "keys/public_key.pem"):
        with open(public_key_path, "rb") as f:
            self.public_key = load_pem_public_key(f.read())

    def verify_signature(self, payload: bytes, signature_base64: str) -> bool:
        try:
            signature = base64.b64decode(signature_base64)
            self.public_key.verify(
                signature,
                payload,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
