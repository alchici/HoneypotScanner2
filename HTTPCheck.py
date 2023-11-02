import requests

HTTPList = {"<h2>My Resource</h2>":"Glastopf",
    "<h2>Blog Comments</h2>\n <label for=\"comment\">Please post your comments for the blog</label>\n <br />\n <textarea name=\"comment\" id=\"comment\" rows=\"4\" columns=\"300\"></textarea>\n <br />\n <input type=\"submit\" name=\"submit\" id=\"submit_comment\" value=\"Submit\" />\n":"Glastopf",
    "<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\"><html><head><title>It works!</title></head><html><body><h1>It works!</h1><br>tim\.bohn@gmx\.net<br>johan83@freenet\.de</body></html>\n\n":"Amun",
    "<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\"><html>\n<title>Directory listing for /</title>\n<body>\n<h2>Directory listing for /</h2>\n":"Dionaea",
    "Last-Modified: Tue, 19 May 1993 09:00:00 GMT":"Conpot",
    "Technodrome":"Conpot",
    "Mouser Factory":"Conpot",
    "Server: nginx":"Dionaea",
    "Server: Apache/1.3.29":"Amun",
    "Server: BaseHTTP/0.3 Python/2.5.1":"Glastopf"}

def stringifyHeaders(headers):
    res = ""
    for h in headers:
        res += "%s: %s\n" % (h, headers[h])
    return res    


def checkHTTP(ip, port):
    url1 = "http://%s/" % (ip)
    url2 = "http://%s/index.html" % (ip)

    response1 = requests.get(url1)
    response2 = requests.get(url2)

    headers1 = stringifyHeaders(response1.headers)
    headers2 = stringifyHeaders(response1.headers)

    totalString = headers1 + response1.content.decode() + headers2 + response2.content.decode()

    for item in HTTPList:
        if (item in totalString):
            print("Match: %s\t%s" % (HTTPList[item], item))

if __name__ == '__main__':
    checkHTTP("127.0.0.1",80)


