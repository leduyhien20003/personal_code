import nmap

class NmapScanner:
    def __init__(self):
        self.portScanner = nmap.PortScanner()
    def nmapScan(self, ip_address, port):
        self.portScanner.scan(ip_address, port)
        print(" [+] Executing command: ", self.portScanner.command_line())
def main():
    ip_address = input('IP scan: ')
    ports = ["21", "22", "23", "25", "80", "443"]
    for port in ports:
        NmapScanner().nmapScan(ip_address, port)           

if __name__ == "__main__":
    main()
         