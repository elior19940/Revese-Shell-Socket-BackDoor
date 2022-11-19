import Cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from cryptography.fernet import Fernet
import base64
import hashlib
import os


class RSA_encryption(object):
        
    def generet_rsa_keys(self,bytes_length):
        key=RSA.generate(bytes_length)
        public=key.public_key()
        return [key.export_key('PEM'),public.export_key('PEM')]

    def import_rsa_private_key(self,private_pem):
        return RSA.import_key(private_pem)

    def import_rsa_public_key(self,public_pem):
        return RSA.import_key(public_pem).public_key()

    def rsa_encryt(self,public,data):
        if type(public)!=Cryptodome.PublicKey.RSA.RsaKey:
            public=self.import_rsa_private_key(public)
        cipher=PKCS1_OAEP.new(public)
        return cipher.encrypt(data)

    def rsa_decrypt(self,private,data):
        if type(private)!=Cryptodome.PublicKey.RSA.RsaKey:
            private=self.import_rsa_private_key(private)
        cipher=PKCS1_OAEP.new(private)
        return cipher.decrypt(data)

    
class Encryption():
    
    def __init__(self,key=False):
        if key != False:
            self.fer = Fernet(key)
            
    def encrypt(self,message):
        return self.fer.encrypt(message)
    
    def decrypt(self,data):
        return self.fer.decrypt(data)
    
    def genKey(self):
        return base64.b64encode(os.urandom(32))
