import cryptography.fernet
import os

#test_key = b'jig-oaelcJoX2CtNdm6ZzFSmKy_yWXMMVDXpLBtMUFA='

class encryption:
    def __init__(self):
        self.key = os.getenv('ENC_KEY')
        self.fernet = cryptography.fernet.Fernet(self.key)

    def encrypt(self, content: str):
        return self.fernet.encrypt(content.encode())
    
    def decrypt(self, content: str):
        return self.fernet.decrypt(content).decode()