import telnetlib
import time


class networkElement:
    def __init__(self,  name, ipAddress, vendor):
        self.ipAddress = ipAddress
        self.name = name
        self.vendor = vendor
    def showName(self):
        print  self.name
    def showIp(self):
        print  self.ipAddress
    def showVendor(self):
        print  self.vendor











ne1 = networkElement("elemento1","192.168.0.1","cisco")

ne1.showVendor()
ne1.showIp()
ne1.showName()
