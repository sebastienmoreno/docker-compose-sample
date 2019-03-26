#!/usr/bin/env python    
import httplib  
import time

#get http server ip  
http_server = "provider:8080"  
#create a connection
print('Connecting to '+http_server)
conn = httplib.HTTPConnection(http_server)  

while True:
    time.sleep(5)

    #request command to server  
    conn.request("GET", "/")
    
    #get response from server  
    rsp = conn.getresponse()  

    #print server response and data  
    #print(rsp.status, rsp.reason)  
    print('Info from provider: '+rsp.read())

conn.close()  