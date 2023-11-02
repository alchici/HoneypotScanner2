import nmap

def portScan(ip):

    scanner = nmap.PortScanner()

    # scanner.scan(ip, '1-1000')
    scanner.scan(ip,arguments='-n -sS -p-')

    for host in scanner.all_hosts():
     print('Host : %s (%s)' % (host, scanner[host].hostname()))
     print('State : %s' % scanner[host].state())
     for proto in scanner[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)
 
         lport = scanner[host][proto].keys()
         for port in lport:
             print('port : %s\t %s\t %s\t %s %s' % (port, scanner[host][proto][port]['state'], scanner[host][proto][port]['name'], scanner[host][proto][port]['product'], scanner[host][proto][port]['version']))
    
    return scanner[scanner.all_hosts()[0]]

if __name__ == '__main__':
    ip = '127.0.0.1'
    portScan(ip)