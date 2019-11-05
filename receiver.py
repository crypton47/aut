# -*- coding: utf-8 -*-
"""
Master CyberSecurite & CyberCriminalite  - Ensa Tanger
Author : BATALI OUALID 
Date : 31 Octobre 2019
Python version : Python 3.6.7
______________TP : Athentification using Hash function and symmetric encryption ____________
				
"""
import socket
import os
import cryptography
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


HOST = '0.0.0.0'  # server will bind to any IP
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates server TCP socket  # prevents from getting timeout iss
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # 5 connections max in queue
print("\n[*] Listening on port " +str(PORT)+ ", waiting for connexions.")

# see socket documentation to understand how socket.accept works
client_socket, (client_ip, client_port) = server_socket.accept()

print("[*] Device  " +client_ip+ " connected.\n")


data = client_socket.recv(1024)
data = data.split('|*|')
message = data[0]
pem_public = data[1]
signature = data[2]
# public_key = load_pem_public_key(pem_public, backend=default_backend())

#home/crypton/Desktop/dir/

file = open("publickey.txt","a")
file.write(pem_public)
file.close()



with open("publickey.txt", "r") as key_file:
    public_key = serialization.load_pem_public_key(
    key_file.read(),
    backend=default_backend())
print 'MESSAGE RECEIVED: ', data[0]
print ('Signature: ', data[2])


################## VERIFICATION DE LA SIGNATURE ###############################

try:
    public_key.verify(signature,message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
    salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())
    print '############ Success #########'
except:
    print '############### NOT SECURE #########'
server_socket.close()

