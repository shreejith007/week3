import socket
hostname=socket.gethostname()
IpAddr =socket.gethostbyname(hostname)
print(f'THE HOST NAME IS {hostname}')
print(f'THE IPADDRESS IS {IpAddr}')