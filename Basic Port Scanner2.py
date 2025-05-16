import socket

def scan_port(target,port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1) # Set timeout for connection attempt
            result = s.connect_ex((target, port)) # Return 0 if port is open
            if result ==0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is cloed")
    except KeyboardInterrupt:
        print("Scanning interrupted by user.")
        exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()
    except socket.error:
        print("Could not connect to sever.")
        exit()

def scan_ports(target, ports):
    print(f"Scanning target: {target}") 
    for port in ports:
        scan_port(target, port)

if __name__ == "_main_":
    target = input("Enter target ip or hostname: ")
    ports = range(1-1025) # Scannin common ports 1-1024
    scan_ports(target,ports)                             
