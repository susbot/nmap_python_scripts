import nmap

# Prompt the user to enter the target IP address
target_ip = input("Enter the target IP address: ")

# Initialize the Nmap scanner
nm = nmap.PortScanner()

# Perform a basic TCP SYN scan
# You can customize the scan options as needed
nm.scan(target_ip, arguments='-sS')

# Print open ports and services
for host, result in nm.all_hosts().items():
    print(f"Host: {host}")
    for port, info in result['tcp'].items():
        print(f"Port {port}: {info['name']} - {info['state']}")
