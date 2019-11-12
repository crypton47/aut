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
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes



############################### MD5 <OK> ########################################
def hash1(size):
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
digest1 = hashes.Hash(hashes.MD5(), backend=default_backend())
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
digest1.update(plaintext)
hash1 = digest1.finalize()
 '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   MD5 HASH TIME OF {} IS : {}'.format(size, min(times)))

############################### SHA1 <OK> ########################################
def hash2(size):
    setupCode = '''   
import cryptography
from cryptography.hazmat.primitives import hashes
import os
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
digest1 = hashes.Hash(hashes.SHA1(), backend=default_backend())
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
digest1.update(plaintext)
hash1 = digest1.finalize()
 '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   SHA1 HASH TIME OF {} IS  : {}'.format(size, min(times)))

############################### SHA224 <OK> ########################################
def hash3(size):
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
digest1 = hashes.Hash(hashes.SHA224(), backend=default_backend())
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
digest1.update(plaintext)
hash1 = digest1.finalize()
 '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   SHA224 HASH TIME OF {} IS: {}'.format(size, min(times)))

############################### SHA256 <OK> ########################################
def hash4(size):
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
digest1 = hashes.Hash(hashes.SHA256(), backend=default_backend())
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
digest1.update(plaintext)
hash1 = digest1.finalize()
 '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   SHA256 HASH TIME OF {} IS  : {}'.format(size, min(times)))

############################### SHA384 <OK> ########################################
def hash5(size):
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
digest1 = hashes.Hash(hashes.SHA384(), backend=default_backend())
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
digest1.update(plaintext)
hash1 = digest1.finalize()
 '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   SHA384 HASH TIME OF {} IS : {}'.format(size, min(times)))

############################### THE LAST ONE : SHA512 <OK> ########################################
def hash6(size):
    setupCode = '''   
import cryptography
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend '''
    testCode = ''' 
digest1 = hashes.Hash(hashes.SHA512(), backend=default_backend())
file = open('publickey1.txt', 'r')
plaintext = file.read()
file.close()
digest1.update(plaintext)
hash1 = digest1.finalize()
 '''
    times = timeit.repeat(setup=setupCode, stmt=testCode, number=10, repeat=3)
    print('[*]   SHA512 HASH TIME OF {} IS : {}'.format(size, min(times)))
    

if __name__ =="__main__":
    intro = """ 
##############################################################################
             Master CyberSecurite & CyberCriminalite  - Ensa Tanger
                         Author : BATALI OUALID 
                          Date : 30 Octobre 2019
                        Python version : Python 3.6.7
####################### Comparaison SHA FAMILY ALGORITHMS###################### """
    print(intro)
    size = '4KB'
    hash1(size)
    hash2(size)
    hash3(size)
    hash4(size)
    hash5(size)
    hash6(size)

Intel® Core™ i5-3320M CPU @ 2.60GHz × 4 
