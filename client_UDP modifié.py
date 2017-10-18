# -*- coding: utf-8 -*-
#!/usr/bin/env python
import socket

UDP_IP = "192.168.0.202"
UDP_PORT = 5005



MESSAGE = "cinema"

print "",
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT



sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


trameReponse, addr = sock.recvfrom(1024)






print "Réception de la trame de réponse", trameReponse.encode("hex")


print "le code de la carte est : " , (ord(trameReponse[3])<<24)+(ord(trameReponse[2])<<16)+(ord(trameReponse[1])<<8)+(ord(trameReponse[0])<<0);
