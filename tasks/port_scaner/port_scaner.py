import socket

def scan_ports(host_port, start_port, end_port):
    print(f'Scanning ports on {host_port}...')

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host_port, port))

        # if result == 0:
        #     print(f"Port {port} is opem")
        print (result)
        
        sock.close()

if __name__ == "__main__":
    target_hosts = input("Enter the host IP address: ")
    first_port = int(input("Enter the starting port: "))
    last_port = int(input("Enter the ending port: "))

    scan_ports(target_hosts, first_port, last_port)


# def parse_ports(port_input):
#     ports = set()  # set avoids duplicates
#     for part in port_input.split(","):
#         part = part.strip()
#         if "-" in part:
#             start, end = part.split("-")
#             ports.update(range(int(start), int(end) + 1))
#         else:
#             ports.add(int(part))
#     return sorted(ports)

# # Example usage
# user_input = "20-25,80,443"
# ports_list = parse_ports(user_input)
# print(ports_list)