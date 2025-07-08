import socket

#configuration
try:
 target_ip = "127.0.0.1"
 target_port= 8080

 s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(1)

#connect target ip
 result = s.connect_ex((target_ip, target_port))

 if result == 0:
    print(f"Port {target_port} is OPEN")
 else:
    print(f"Port {target_port} is CLOSED")

#close the connection
 s.close()
except Exception as e:
 print(f"an error occured {e}")
