import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def scan_target(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(f"IP Address: {ip}, Host Name: {host[0]}")
    except(socket.herror, socket.gaierror):
        pass

def scan_network(network):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for ip in network.hosts():
            executor.submit(scan_target, str(ip))

if __name__ == "__main__":
    network_cidr = "192.168.29.221/24"

    try:
        network = ipaddress.ip_network(network_cidr, strict=False)
        scan_network(network)
    except ValueError as e:
        print(f"Invalid Network CIDR: {e}")