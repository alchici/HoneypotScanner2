from portScanner import portScan
from bannerCheck import checkBanner
from protocolCheck import checkSSH, checkTelnet, checkModbus, checkS7
from HTTPCheck import checkHTTP
from TLSCheck import checkTLS

interestingProtocols = [
    "ftp", "ssh", "http", "https", "iso-tsap", "mbap", "imap", "smtp"
]



def scan(ip):
    ports = portScan(ip)

    print("----------")

    testProtocols = {}
    stringProtocols = ""

    # EtherNetIP-1 por si ponen ssh en el puerto 2222
    # if ports["tcp"][2222]:
    #     ports["tcp"][2222]["name"] = "ssh"


    for port in ports["tcp"]:
        if ports["tcp"][port]["name"] in interestingProtocols:
            testProtocols[ports["tcp"][port]["name"]] = port
            stringProtocols += "%s: %s\n" % (ports["tcp"][port]["name"],port)

    print("Chosen protocols and ports: \n%s" % (stringProtocols.strip()))

    print("----------")

    print("Banner check:")
    for protocol in testProtocols:
        checkBanner(ip,testProtocols[protocol])

    print("----------")

    print("Protocol check:")

    if "ssh" in testProtocols:
        checkSSH(ip,testProtocols["ssh"])

    if "mbap" in testProtocols:
        checkModbus(ip,testProtocols["mbap"])

    if "iso-tsap" in testProtocols:
        checkS7(ip,testProtocols["iso-tsap"])

    #falta telnet y s7

    print("----------")

    print("HTTP check:")

    if "http" in testProtocols:
        checkHTTP(ip,testProtocols["http"])
    
    if "https" in testProtocols:
        checkHTTP(ip,testProtocols["https"],True)

    print("----------")

    print("TLS Certificate check: ")

    if "https" in testProtocols:
        checkTLS(ip,testProtocols["https"])

    print("----------")
    


if __name__ == '__main__':
    scan("5.196.14.176")