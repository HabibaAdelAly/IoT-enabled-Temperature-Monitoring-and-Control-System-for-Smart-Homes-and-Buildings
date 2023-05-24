# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:15:16 2022

@author: Hoda 
"""

import socket


def client_program():
    host = "127.0.0.1"  
    port = 2500  

    client_socket = socket.socket()  
    client_socket.connect((host, port))  

    message = input(" -> ")  

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  
        data = client_socket.recv(1024).decode()  

        print('Received from server: ' + data)  

        message = input(" -> ")  

    client_socket.close()  
    
client_program()


