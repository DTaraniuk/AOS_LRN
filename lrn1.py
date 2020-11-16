# first of all import the socket library 
import socket

def translate(k, res, mean):
   if(k==res):
      return mean;
   else:
      return "no";
   
def DICT(k):
   flag = False;
   result = ""
   for i in range (10):
      res = translate(k, words[i], translations[i])
      if (res != "no"):
         flag = True
         result = res
   if(flag):
      return result
   else:
      return "word not found"


global words
words=["table", "bed", "window", "cube", "glass", "bottle", "rubber", "cup", "lamp", "fork"]
global translations
translations=["стол", "кровать", "окно", "куб", "стакан", "бутылка", "резина", "чашка", "лампа", "вилка"]
  
# next create a socket object 
s = socket.socket()          
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port) )
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print ('Got connection from', addr) 
  
   # send a thank you message to the client.  
   c.send('Thank you for connecting'.encode())


  
   
   while(True):
      s.listen(5)
      k = c.recv(1024).decode()
      if(k=="end"):
         break;
      c.send(DICT(k).encode())
      print("query processed for "+k)
   # Close the connection with the client
   c.close()


