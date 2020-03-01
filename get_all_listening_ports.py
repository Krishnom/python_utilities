import socket
import threading

listening_ports = []


def check_server(address, port):
    s = socket.socket()
    try:
        s.connect((address, port))
        print(port.__str__() + " is active")
        listening_ports.append(port)
        return True
    except socket.error as e:
        return False
    finally:
        s.close()


server = "localhost"
max_port_number = 36650
polling_t = list(range(max_port_number))
for port in range(max_port_number):
    polling_t[port] = threading.Thread(target=check_server, args=(server, port,))
    polling_t[port].start()

for port in range(max_port_number):
    polling_t[port].join()

print(listening_ports)