
#! -*- coding:utf-8 -*-
""" 
Master CyberSecurite & CyberCriminalite  - Ensa Tanger
Author : BATALI OUALID 
Date : 30 Octobre 2019
Python version : Python 3.6.7
____Comparaison du temps de Calcul entre AES, Blowfish, ChaCha et TriplesDES __
		
"""
import timeit
import cryptography
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


############################### AES <OK> ########################################
def aesTime():
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
backend = default_backend()
key = os.urandom(32)
nonce = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(nonce), backend=backend)
encryptor = cipher.encryptor()
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
padder = padding.PKCS7(128).padder()
plaintext_padded = padder.update(plaintext)
plaintext_padded += padder.finalize()
ct = encryptor.update(plaintext_padded) + encryptor.finalize()
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize() '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   AES encryption/decryption time [size:1MB] : {}'.format(min(times)))


############################### TripleDES <OK> ###################################
def tripledesTime():
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
backend = default_backend()
key = os.urandom(8)
nonce = os.urandom(8)
cipher = Cipher(algorithms.TripleDES(key), modes.CBC(nonce), backend=backend)
encryptor = cipher.encryptor()
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
padder = padding.PKCS7(128).padder()
plaintext_padded = padder.update(plaintext)
plaintext_padded += padder.finalize()
ct = encryptor.update(plaintext_padded) + encryptor.finalize()
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize() '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   3DES encryption/decryption time [taille:1MB] : {}'.format(min(times)))




############################# blowfish <OK> #######################################
def blowfishTime():
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
backend = default_backend()
key = os.urandom(32)
iv = os.urandom(8)
cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
padder = padding.PKCS7(64).padder()
plaintext_padded = padder.update(plaintext)
plaintext_padded += padder.finalize()
ct = encryptor.update(plaintext_padded) + encryptor.finalize()
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize() '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   Blowfish encryption/decryption time [size:1MB]   : {}'.format(min(times)))


################################### ChaCha <OK> ######################################    
def ChaChaTime():
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
backend = default_backend()
key = os.urandom(32)
nonce = os.urandom(16)
cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=backend)
encryptor = cipher.encryptor()
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
padder = padding.PKCS7(128).padder()
plaintext_padded = padder.update(plaintext)
plaintext_padded += padder.finalize()
ct = encryptor.update(plaintext_padded) + encryptor.finalize()
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize() '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   ChaCha encryption/decryption Time [size:1MB] )  : {}'.format(min(times)))


    

if __name__ =="__main__":
    intro = """ 
##############################################################################
             Master CyberSecurite & CyberCriminalite  - Ensa Tanger
                         Author : BATALI OUALID 
                          Date : 30 Octobre 2019
                        Python version : Python 3.6.7
####################### Comparaison du temps de Calcul ########################

"""
    print(intro)
    blowfishTime()
    tripledesTime()
    aesTime()
    ChaChaTime()
    # rsaTime()

## print("ici", timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
