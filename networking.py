import psutil
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import byte2human


class Networking:
    def net_io(self):
        self.net_io = psutil.net_io_counters(pernic = True) #io counters
        return self.net_io

    def net_connections(self):
        self.net_connections = psutil.net_connections() #socket connections 
        return self.net_connections
    
    def address(self):
        self.net_addr = psutil.net_if_addrs() #NIC addr
        return self.net_addr 
    
    def net_stat(self): 
        self.net_stat = psutil.net_if_stats() #NIC stats
        return self.net_stat
    
class display_info(Networking):
    def display_io(self):
        self.io = self.net_io()
        table = PrettyTable(["NIC", "Bytes Sent", "Bytes received", "Packet Sent", "Packets received", "Error In", "Error Out", "Drop in", "Drop Out"])
        for val in self.io :
            table.add_row([val, byte2human.convert_bytes(self.io[val].bytes_sent), byte2human.convert_bytes(self.io[val].bytes_recv), self.io[val].packets_sent, self.io[val].packets_recv, self.io[val].errin, self.io[val].errout, self.io[val].dropin, self.io[val].dropout])
        print(table)

    def display_stats(self):
        self.stats = self.net_stat()
        table = PrettyTable(["Name", "Status", "Speed(MB)", "MTU(bytes)", "Flags"])
        status = None
        for val in self.stats:
            status = "Up" if self.stats[val].isup == True else "Down"
            table.add_row([val, status, self.stats[val].speed, self.stats[val].mtu, self.stats[val].flags])
        print(table)
            
    def display_addr(self):
        self.addr = self.address()
        for val in self.addr:
            print(f"{val}: {self.addr[val]}\n")

    def display_connections(self):
        self.connections = self.net_connections()
        for val in self.connections:
            print(f"{val}")
            print("-------")
            