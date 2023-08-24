import socket
import subprocess
import threading
from typing import Literal
from time import sleep


class NetworkScan:
    def __init__(self,start_address,end_address = ""):
        self.start_address = start_address
        self.end_address = end_address
        self.ip_address_list = []
        self.exec_count = 0
    def scan_network(self):
        try:
            if self.end_address == "":
                self.ping_ip(self.start_address)
            else:
                start_ip_decomp = self.decompond_ip_address(self.start_address)
                end_ip_decomp = self.decompond_ip_address(self.end_address)
                if start_ip_decomp[0] != end_ip_decomp[0]:
                    for i in range(start_ip_decomp[0],end_ip_decomp[0]+1):
                        for j in range(0,256):
                            for k in range(0,256):
                                for l in range(0,256):
                                    self.gera_Ip(i,j,k,l)
                else:
                    if start_ip_decomp[1] != end_ip_decomp[1]:
                        for j in range(start_ip_decomp[1],end_ip_decomp[1]+1):
                            for k in range(0,256):
                                for l in range(0,256):
                                    self.gera_Ip(start_ip_decomp[0],j,k,l)
                    else:
                        if start_ip_decomp[2] != end_ip_decomp[2]:
                            for k in range(start_ip_decomp[2],end_ip_decomp[2]+1):
                                for l in range(0,256):
                                    self.gera_Ip(start_ip_decomp[0],start_ip_decomp[1],k,l)
                        else:
                            for l in range(start_ip_decomp[3],end_ip_decomp[3]+1):
                                self.gera_Ip(start_ip_decomp[0],start_ip_decomp[1],start_ip_decomp[2],l)

            while self.exec_count >0:
                print(".")
                sleep(1)
        except Exception as e:
            print(e)
            return False

    def gera_Ip(self,i,j,k,l):
        ip_address = self.compond_ip_address(i,j,k,l)
        ip = Ip(ip_address)
        self.ip_address_list.append(ip)
        p = threading.Thread(target=self.ping_ip,args=(ip_address,len(self.ip_address_list)-1))
        p.start()


    def decompond_ip_address(self,ip):
        ip_splited = ip.split(".")
        return [int(ip_splited[0]),int(ip_splited[1]),int(ip_splited[2]),int(ip_splited[3])]

    def compond_ip_address(self,a,b,c,d):
        return f"{a}.{b}.{c}.{d}"

    def get_ip_address_list(self):
        print(len(self.ip_address_list))
        self.ip_address_list.sort(key=self.orderIP)
        return self.ip_address_list
    def orderIP(self,ip):
        return ip.oct4
    
    def ping_ip(self,ip_address:str,index:int):
        self.exec_count= self.exec_count + 1
        try:
            result = subprocess.run(["ping", "-n", "2", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            if result.returncode == 0:
                if result.stdout.count("TTL=") >0:
                    self.ip_address_list[index].status = "up"
                    self.ip_address_list[index].hostname = self.getHostName(ip_address)
                    self.ip_address_list[index].mac_address = self.getMACAddress(ip_address)
                else:
                    self.ip_address_list[index].status = "down"
            else:
                self.ip_address_list[index].status = "down"


        except Exception as e:
            print(e)
        self.exec_count= self.exec_count - 1  

    def getHostName(self,ip_address:str):
        try:
            host_name, _, _ = socket.gethostbyaddr(ip_address)
            return host_name
        except socket.herror:
            return ""
        
    def getMACAddress(self,ip_address:str):
        try:
            mac_address = subprocess.run(["arp", "-a", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            mac_address = mac_address.stdout.split("\n")[3].split()[1]
            return mac_address
        except Exception as e:
            print(e)
            return ""

class Ip:
    ip : str
    hostname : str
    mac_address : str
    status : str
    def __init__(self,ip:str,hostname:str="",mac_address:str="",status:Literal["up", "down","unknown"] = "unknown"):
        self.ip = ip
        self.hostname = hostname
        self.mac_address = mac_address
        self.status = status
        octs = self.ip.split(".")
        self.oct4 = int(octs[3])
        self.oct3 = int(octs[2])
        self.oct2 = int(octs[1])
        self.oct1 = int(octs[0])
    def __str__(self) -> str:
        return f"IP = {self.ip} Hostname = {self.hostname} MAC Address = {self.mac_address} Status = {self.status}"


if __name__ == "__main__":
    n = NetworkScan("192.168.2.1","192.168.2.20")
    n.scan_network()
    [print(a) for a in n.get_ip_address_list()]