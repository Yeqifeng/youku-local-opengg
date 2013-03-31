#from urllib2 import urlopen
#import BaseHTTPServer
from urllib.request import urlopen
import http.server
import socketserver
import os
import re


class youkuvHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=UTF-8')

        if self.path == '/crossdomain.xml':
            self.send_header('Content-Type', 'text/xml')
            content = '<?xml version="1.0" encoding="UTF-8"?><cross-domain-policy><allow-access-from domain = "*"/></cross-domain-policy>'
        elif 'getPlayList' in self.path:
            content = urlopen('http://v.youku.com' + self.path).read()
        elif self.path.endswith('.swf'):
            self.send_header('Content-Type', 'application/x-shockwave-flash')
            if 'player' in self.path:
                path = '/player.swf'
            else:
                path = self.path
            print(path)
            hfile = open('player/' + path, 'rb')
            content = hfile.read()
            hfile.close()
        else:
            content = '<b>YoukuV!</b>'
        self.end_headers()
        self.wfile.write(content)
        #print(content)
        #self.wfile.close()

#默认返回("127.0.0.1","8008")
def readconfig(fildpath):
    hfile = open(fildpath)
    linesinfo = hfile.readlines()
    hfile.close()
    if not linesinfo:
        print('没有找到地址配置文件‘config.txt’!')
        return "localhost",8008
    if(len(linesinfo) == 2):
        i=0
        while (i<2):
            infolist = re.split('&',linesinfo[i])
            if len(infolist)==3:
                if(infolist[0] == "address"):
                    address = infolist[1]
                    print("找到地址IP信息："+infolist[1])
                elif(infolist[0] == "port"):
                    port = int(infolist[1])
                    print("找到地址port信息："+infolist[1])
                else:
                    print("地址信息:"+infolist[0]+"不存在")
            else:
                print("配置文件不正确，请确认配置文件！")
            i+=1
        return address,port
    else:
        return "localhost",8008
def main():
    print(os.getcwd())
    server_address = readconfig(os.getcwd()+"\\config.txt")
    httpd = socketserver.TCPServer(server_address, youkuvHandler)
    print('Server at ' + server_address[0] + ':' + str(server_address[1]) + ' ...')
    httpd.serve_forever()

if __name__ == '__main__':
    main()