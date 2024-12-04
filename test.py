# test_load_dotenv.py
import os
from dotenv import load_dotenv

# Load the .env file explicitly
load_dotenv(os.path.join(os.getcwd(), '.env'))  # Adjust path as needed

print("Load dotenv result:", load_dotenv())  # Should print True if successful
print("DATABASE_URL:", os.getenv("DATABASE_URL"))  # Should show your database URL
print("SECRET_KEY:", os.getenv("SECRET_KEY"))  # Should show your secret key
