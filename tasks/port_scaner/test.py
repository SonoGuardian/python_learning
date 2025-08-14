
def parse_ports(port_input):
    ports = set()  # set avoids duplicates
    for part in port_input.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-")
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))
    return sorted(ports)



if __name__ == "__main__":
    port_range = input("Enter all ports for scanning (20-22,80,443): ")
    ports_list = parse_ports(port_range)
    print(ports_list)

   # scan_ports(target_hosts, port_range)






# # Example usage
# user_input = "20-25,80,443"
# ports_list = parse_ports(user_input)
# print(ports_list)