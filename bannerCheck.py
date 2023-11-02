import socket

BannerList = {"SSH-2.0-OpenSSH_5.1p1 Debian-5":"Kippo",
"SSH-1.99-OpenSSH_4.3":"Kippo",
"SSH-1.99-OpenSSH_4.7":"Kippo",
"SSH-1.99-Sun_SSH_1.1":"Kippo",
"SSH-2.0-OpenSSH_4.2p1 Debian-7ubuntu3.1":"Kippo",
"SSH-2.0-OpenSSH_4.3":"Kippo",
"SSH-2.0-OpenSSH_4.6":"Kippo",
"SSH-2.0-OpenSSH_5.1p1 Debian-5":"Kippo",
"SSH-2.0-OpenSSH_5.1p1 FreeBSD-20080901":"Kippo",
"SSH-2.0-OpenSSH_5.3p1 Debian-3ubuntu5":"Kippo",
"SSH-2.0-OpenSSH_5.3p1 Debian-3ubuntu6":"Kippo",
"SSH-2.0-OpenSSH_5.3p1 Debian-3ubuntu7":"Kippo",
"SSH-2.0-OpenSSH_5.5p1 Debian-6":"Kippo",
"SSH-2.0-OpenSSH_5.5p1 Debian-6+squeeze1":"Kippo",
"SSH-2.0-OpenSSH_5.5p1 Debian-6+squeeze2":"Kippo",
"SSH-2.0-OpenSSH_5.8p2_hpn13v11 FreeBSD-20110503":"Kippo",
"SSH-2.0-OpenSSH_5.9p1 Debian-5ubuntu1":"Kippo",
"SSH-2.0-OpenSSH_5.9":"Kippo",
"Debian GNU/Linux 7":"Cowrie",
"\xff\xfd\x1flogin:":"Cowrie",
"SSH-2.0-OpenSSH_6.0p1 Debian-4+deb7u2":"Cowrie",
"Apache httpd":"Glastopf",
"220 Welcome to the ftp service":"Dionaea",
"220 DiskStation FTP server ready.":"Dionaea",
"220 mail.example.com SMTP Mailserver":"Amun",
"a001 OK LOGIN completed":"Amun",
"220 Welcome to my FTP Server":"Amun",
"SSH-2.0-OpenSSH_6.7p1 Ubuntu-5ubuntu1.3":"Conpot",
"Connected to [00:13:EA:00:00:0]":"Conpot",
"Linux 3.X|4.X":"Gaspot",
"220 —freeFTPd 1\.0—warFTPd 1\.65—":"Nepenthes",
"\xff\xfb\x01\xff\xfb\x03\xff\xfc’\xff\xfe\x01\xff\xfd\x03\xff\xfe\"\xff\xfd’\xff \xfd\x18\xff\xfe\x1f":"MTPot"}



def getBanner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024)
        s.close()
        return banner
    except:
        return b''

# def getBannerList():
#     res = {}
#     file = open('bannerList.txt', 'r')
#     lines = file.readlines()
#     for line in lines:
#         res[line.split(",")[0]] = line.strip().split(",")[1]

#     file.close()
#     return res
    
def checkBanner(ip, port):
    banner = getBanner(ip, port).decode().strip()
    # bans = getBannerList()

    for ban in BannerList:
        if (ban in banner):
            print("Match:\t%s\t%s" % (BannerList[ban], ban))


if __name__ == '__main__':
    checkBanner("127.0.0.1",44818)
