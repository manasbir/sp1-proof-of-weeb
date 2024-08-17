import secrets
import base64
import hashlib
import requests
import keys
import json


def generate_code_verifier(length=43):
    # Ensure the length is within the allowed range
    if length < 43 or length > 128:
        raise ValueError("Length must be between 43 and 128 characters.")

    # Generate a random sequence of bytes
    random_bytes = secrets.token_bytes(32)

    # Base64 URL encode the bytes to get a string
    code_verifier = base64.urlsafe_b64encode(random_bytes).rstrip(b'=').decode('utf-8')

    # Truncate or pad the string to the desired length
    if len(code_verifier) > length:
        code_verifier = code_verifier[:length]
    elif len(code_verifier) < length:
        code_verifier += ''.join(secrets.choice('-._~') for _ in range(length - len(code_verifier)))

    return code_verifier

# Example usage

def create_code_challenge_s256(code_verifier):
    # Compute SHA-256 hash of the code verifier
    sha256_hash = hashlib.sha256(code_verifier.encode('ascii')).digest()

    # Base64 URL encode the hash
    code_challenge = base64.urlsafe_b64encode(sha256_hash).rstrip(b'=').decode('ascii')

    return code_challenge

code_verifier = generate_code_verifier()
code_challenge = code_verifier
print("code verifier:", code_verifier)
print(f"https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={keys.client_id}&code_challenge={code_challenge}")
code = input("Waiting for code... input here:")
r = requests.post('https://myanimelist.net/v1/oauth2/token', data={'client_id': f'{keys.client_id}', 'client_secret': f'{keys.client_secret}', 'grant_type': 'authorization_code', 'code': f'{code}', 'code_verifier': f'{code_verifier}'})
print(r.json())
