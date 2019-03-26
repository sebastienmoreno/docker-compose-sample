#!/usr/bin/env python  
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  
import socket
import time

#Create custom HTTPRequestHandler class  
class SleepHTTPRequestHandler(BaseHTTPRequestHandler):  

  #handle GET command  
  def do_GET(self):  
    self.send_response(200)
    self.send_header('Content-type','text-html')
    self.end_headers()
    self.wfile.write("Host:"+socket.gethostname() + ", time:" + time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()))  
    return

def run():  
  print('http server is starting...')  
  server_address = ('0.0.0.0', 8080)  
  httpd = HTTPServer(server_address, SleepHTTPRequestHandler)  
  print('http server is running...')  
  httpd.serve_forever()  

if __name__ == '__main__':  
  run()  
