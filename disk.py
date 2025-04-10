import psutil
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
import sys

class Disk:
    def disk_dev_partition(self):
        self.df_dev = psutil.disk_partitions(all = False)
        print("\n --Disk Device Partition--\n")
        for part in self.df_dev:
            print(part)
            print("-"*75)
    
    def disk_partition(self):
        print("\n --Disk Partitions-- \n")
        self.df = psutil.disk_partitions(all = True)
        for part in self.df:
            print(part)
            print("-"*125)
    
    def disk_usage(self):
        print("\n-- Check Disk Usage --\n")
        path_var = input("Enter path to check disk usage for")
        try:
            self.du = psutil.disk_usage(path_var)
            table = PrettyTable(["Total DiskSpace(GB)", "Used DiskSpace(GB)", "Free DiskSpace(GB)", "DiskSpace used %"])
            power = pow(1000,3)
            total_space = (self.du.total / power)
            used_space = (self.du.used / power)
            free_space = (self.du.free / power)
            used_space_per = self.du.percent 
            table.add_row([total_space, used_space, free_space , used_space_per])
            print(table)
        
        except Exception as e:
            print(f"{e}")

    def disk_io(self): 
        self.io = psutil.disk_io_counters(perdisk = True)
        print("Disk I/O Rate\n")
        for i in self.io:
            print(i, self.io[i], sep = "--> ")
            print("-"*75) 

class disk_graph:
    def disk_io_graph(self): 
        self.io = psutil.disk_io_counters(perdisk = True)
        return self.io

