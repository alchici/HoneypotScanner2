import ssl
import OpenSSL

TLSList = {
    "dionaea.carnivore.it":"Dionaea"
}

def stringifyCert(info):
    res = ""
    for i in info:
        res += "%s: %s\n" % (i[0].decode(),i[1].decode())
    return res.strip()

def checkTLS(ip, port):
    cert = ssl.get_server_certificate((ip, port))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    cert_info = x509.get_subject().get_components()
    info = stringifyCert(cert_info)

    for item in TLSList:
        if (item in info):
            print("Match: %s\t%s" % (TLSList[item], item))

if __name__ == '__main__':
    checkTLS("127.0.0.1",443)