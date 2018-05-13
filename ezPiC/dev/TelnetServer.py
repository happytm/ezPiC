# Socket server in python using select function
# https://www.binarytides.com/python-socket-server-code-example/
# http://www.tcpipguide.com/free/t_TelnetProtocolCommands-3.htm
# https://github.com/cpopp/MicroTelnetServer/blob/master/utelnet/utelnetserver.py
# https://www.hackster.io/rob-braggaar/pycom-simple-telnet-fbbabc

#  

"""
...TODO
"""
try:   # CPython
    import os
    import re
    import json
    import random
except:   # MicroPython
    import uos as os
    import ure as re
    import ujson as json
    import urandom as random

import socket, select
import logging
import G
import Tool
import dev.Cmd as Cmd

###################################################################################################
# Globals:

CONNECTION_LIST = []    # list of socket clients
CONNECTION_SOURCE = {}    # list of socket prop
RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
PORT = 2101

###################################################################################################
###################################################################################################
###################################################################################################

def init():
    """ Prepare module vars and load plugins """
    pass

###################################################################################################

def run():
    global CONNECTION_LIST, RECV_BUFFER, PORT
         
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print ("Telnet server started on port " + str(PORT))
 
    while G.RUN:
        # Get the list sockets which are ready to be read through select
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
             
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                source = addr[0] + ':' + str(addr[1])
                CONNECTION_SOURCE[sockfd] = source
                print ("Client (%s) connected" % source)

                sockfd.send(b'\r\nezPiC-Service V0.0.?\r\n')
                 
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    # echo back the client message
                    if data:
                        i = 0
                        dataf = bytearray()
                        while i<len(data):
                            if data[i] == 255:
                                i += 2   #skip next 2 bytes from telnet command
                            elif data[i] == 10 or data[i] == 13:
                                dataf.append(32)
                            else:
                                dataf.append(data[i])
                            i += 1
                        if dataf:
                            cmd_str = dataf.decode('utf-8', 'backslashreplace')
                            #raddr, rport = sock.getpeername()
                            source = CONNECTION_SOURCE[sock]
                            ret = Cmd.excecute(cmd_str, source)
                            ret_str = json.dumps(ret) + '\r\n'
                            data = ret_str.encode('utf-8')
                            sock.send(data)
                 
                # client disconnected, so remove from socket list
                except Exception as e:
                    #broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print ("Client (%s, %s) is offline" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
         
    server_socket.close()
    print ("Telnet server closed")
 
###################################################################################################
