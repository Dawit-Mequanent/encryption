import hashlib
from encryption import *
import getpass
from decryption import *




# Maximum number of attempts before the system locks
MAX_ATTEMPTS = 3

# Preset password (for demonstration purposes)
# In a real application, the hashed password would be stored securely and not in plain text

hashed_password = hashlib.sha256(password.encode()).hexdigest()

def check_password(input_password):
    hashed_input = hashlib.sha256(input_password.encode()).hexdigest()
    hashed_password == hashed_input

def main():
    attempt_count = 0
    while attempt_count < MAX_ATTEMPTS:
        input_password = getpass.getpass('Please enter your password: ',password)
        if check_password(input_password):
            print("Access granted.")
            return
        else:
            attempt_count += 1
            print("Incorrect password. Please try again.")
    
    print("Possible tampering detected. System is locked.")

if __name__ == "__main__":
    main()