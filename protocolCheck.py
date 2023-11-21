import socket
import snap7 
from pymodbus.client import ModbusTcpClient
from pymodbus import mei_message


SSHList = {
    "SSH-2.0-OpenSSH \n\n\n\n\n\n\n\n\n\n": ["bad packet length *","protocol mismatch", "Protocol mismatch","Kippo"],
    "SSH-2.0-OpenSSH_6.0p1 Debian-4+deb7u2 \n": ["protocol mismatch", "Cowrie"]
}

TelnetList = {
    "I30100": ["9999FF1B", "Gaspot"],
    "WILL (251) Linemode": ["Won’t (252) Linemode", "MTPot"]
}

S7List = {
    0x0011: ["6ES7 315-2EH14-0AB0", "Conpot"],
    0x001C: ["Technodrome", "88111222", "Mouser Factory", "Conpot"]
}

def ModbusRequest(ip, port):
    success = True
    client = ModbusTcpClient(ip, port=port)
    # try: Lo quitamos por usar sudo
    client.connect()
    req = mei_message.ReadDeviceInformationRequest(unit=5,read_code=0x02)
    res = client.execute(req)
    # except:
    if res.isError():
        success = False
    # finally:
    client.close()
    return success

def S7Request(ip, port, data):
    client = snap7.client.Client()
    client.connect(ip, 0, 0)
    data = client.read_szl(data,1)
    szl_data = bytearray(data.Data)
    return szl_data
    


def SSHRequest(ip, port, data):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        s.recv(1024)
        s.send(data.encode())
        res = s.recv(4096)
        s.close()

        return res
    except:
        return b''

def TelnetRequest(ip, port, data):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        s.recv(1024)
        s.send(data.encode())
        res = s.recv(4096)
        s.close()

        return res
    except:
        return b''
    
def checkModbus(ip, port):
    # Si falla la request es probablemente un Conpot
    if (not ModbusRequest(ip, port)):
         print("Match: %s\t%s" % ("Conpot", "Disconected when Read Device Information"))

def checkS7(ip, port):
    for item in S7List:
        res = S7Request(ip, port, item)
        for i in range(0,len(S7List[item])-1):
            if (S7List[item][i].encode() in res):
                print("Match: %s\t%s" % (S7List[item][len(S7List[item])-1], S7List[item][i]))


def checkSSH(ip, port):
    for item in SSHList:
        res = SSHRequest(ip, port, item)
        for i in range(0,len(SSHList[item])-1):
            if (SSHList[item][i].encode() in res):
                print("Match: %s\t%s" % (SSHList[item][len(SSHList[item])-1], SSHList[item][i]))

def checkTelnet(ip, port):
    for item in TelnetList:
        res = TelnetRequest(ip, port, item)
        for i in range(0,len(TelnetList[item])-1):
            if (TelnetList[item][i].encode() in res):
                print("Match: %s\t%s" % (TelnetList[item][len(TelnetList[item])-1], TelnetList[item][i]))


if __name__ == '__main__':
    # checkTelnet("127.0.0.1", 10001)
    #S7Request("127.0.0.1", 102,"a")
    checkS7("5.196.14.176", 102)
    #checkModbus("127.0.0.1", 502)