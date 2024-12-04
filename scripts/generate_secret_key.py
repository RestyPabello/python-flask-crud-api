import secrets

secret_key = secrets.token_hex(16)
print(f"Your new SECRET_KEY: {secret_key}")