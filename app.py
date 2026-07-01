from scanner import scan_port

host = input("Enter IP Address: ")
port = int(input("Enter Port Number: "))

scan_port(host, port)