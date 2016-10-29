#!/usr/bin/env python    
# -*- coding: utf-8 -*
# Created by Leo on 2016/10/16.

import sys, os

import socket
import asyncore
import threading

MAX_RECV = 4096
#負責接受client socket連線
class AgentServer(asyncore.dispatcher):
   def __init__(self, port):
       #asyncore.dispatcher的constructor
       asyncore.dispatcher.__init__(self)
       #client socket
       self.clientSocket = None
       #server port
       self.port = port
       #建立等待的socket
       self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
       self.bind(('', self.port))
       self.listen(5)

   def handle_accept(self):
       #接受client socket的連線
       self.clientSocket, address = self.accept()
       print 'New client from : ' + address[0]
       #將和client連線的socket加上一些功能 (自訂socket)
       self.clientSocket = ClientAgent(self.clientSocket)

#自訂的client連線socket
class ClientAgent(asyncore.dispatcher):
   def __init__(self, socket):
       asyncore.dispatcher.__init__(self, socket)
       #要送出的data
       self.SendData = ""

   #從client收到的data
   def handle_read(self):
       self.RecvData = self.recv(MAX_RECV)
       if len(self.RecvData) > 0:
           print "recv : " + self.RecvData
   #送出data到client
   def handle_write(self):
       send_byte = self.send(self.SendData)
       #一次可能不會全部送完(一次最多送出512 bytes ?)
       if send_byte > 0:
           send_out = self.SendData[:send_byte]
           self.SendData = self.SendData[send_byte:]
           self.handle_write()
       else:
           print "send all!!"
           self.SendData = ""

   #不自動執行handle_write
   def writable(self):
       return False

   def handle_close(self):
       print "close connection : " + self.getpeername()[0]
       self.close()
#產生等待client連線的thread
class listen_client_thread(threading.Thread):
   def __init__(self,port):
       self.agentServer = AgentServer(port)
       threading.Thread.__init__ ( self )

   def run(self):
       print "Listen Client ..."
       asyncore.loop()
#產生處理輸入的thread
class input_thread(threading.Thread):
   def __init__(self,listen_thread):
       self.listen_thread = listen_thread
       threading.Thread.__init__ ( self )
   def run(self):
       while 1:
           send_data = raw_input()
           self.listen_thread.agentServer.clientSocket.SendData = send_data
           self.listen_thread.agentServer.clientSocket.handle_write()

if __name__ == "__main__":
   #產生等待client連線的thread
   listen_thread = listen_client_thread(111)
   listen_thread.start()
   #產生處理輸入的thread
   input_thread(listen_thread).start()

