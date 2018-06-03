"""
Socket server for Configuration the IoT-Device
"""
from com.modules import *

import socket, select

import com.Tool as Tool
import dev.Cmd as Cmd

#######
# Globals:

CONNECTION_LIST = []    # list of socket clients
CONNECTION_SOURCE = {}    # list of socket prop
RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
PORT = 23101

LOGO = b'''\r\n\
                       _|_|_|    _|     _|_|_|\r\n\
    _|_|    _|_|_|_|   _|    _|       _|\r\n\
  _|    _|        _|   _|    _|  _|   _|\r\n\
  _|_|_|_|      _|     _|_|_|    _|   _|\r\n\
  _|          _|       _|        _|   _|\r\n\
    _|_|_|  _|_|_|_|   _|        _|     _|_|_|\r\n\
 \r\n\
 ezPiC IoT-Device - github.com/fablab-wue/ezPiC\r\n\r\n'''

#######

def init():
    """ Prepare module vars and load plugins """
    pass

# =====

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
                print (str(addr))
                print (addr)

                CONNECTION_LIST.append(sockfd)
                source = addr[0] + ':' + str(addr[1])
                print (source)
                print(sockfd.fileno())
                CONNECTION_SOURCE[sockfd.fileno()] = source
                print ("Client (%s) connected" % source)

                sockfd.send(LOGO)

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
                        data_filtered = bytearray()
                        while i<len(data):
                            if data[i] == 255:
                                i += 2   #skip next 2 bytes from telnet command
                            #elif data[i] == 10 or data[i] == 13:
                            #    data_filtered.append(32)
                            elif data[i] < 32:
                                pass   # eat control characters
                            else:
                                data_filtered.append(data[i])
                            i += 1
                        if data_filtered:
                            data_filtered = bytes(data_filtered)   # bytearray -> bytes
                            cmd_str = data_filtered.decode('utf-8', 'backslashreplace')   # bytes -> str
                            print (cmd_str)
                            print(sock.fileno())
                            source = CONNECTION_SOURCE[sock.fileno()]   # hash for sock
                            ret = Cmd.excecute(cmd_str, source)
                            if G.MICROPYTHON:
                                ret_str = json.dumps(ret) + '\r\n\r\n'   # object -> json-str
                            else:
                                ret_str = json.dumps(ret, indent=2) + '\n\n'   # object -> json-str
                                ret_str = ret_str.replace('\n', '\r\n')
                            print (ret_str)
                            data = ret_str.encode('utf-8')   # str -> bytes
                            print (data)
                            sock.send(data)
                 
                # client disconnected, so remove from socket list
                except Exception as e:
                    print (str(e))
                    #broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print ("Client (%s, %s) is offline" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
         
    server_socket.close()
    print ("Telnet server closed")
 
#######
