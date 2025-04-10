import psutil
import matplotlib.pyplot as plt
import numpy as np
import sys
from prettytable import PrettyTable


class CPU:
    #return number of logical CPU 
    def cpu_count(self):
        self.count = psutil.cpu_count(logical = True)
        return self.count
    
    #CPU utilisation percents
    def cpu_times(self):
        self.time = psutil.cpu_times(percpu = False)
        return self.time
        #print(self.time.user, self.time.nice)

    def cpu_percents(self):
        self.per = psutil.cpu_percent()
        print(self.per)

    def percent(self):
        self.perc = psutil.cpu_times_percent(interval=None, percpu= False)
        return self.perc

    def percent_graph(self):
        self.perc = psutil.cpu_times_percent(interval=1, percpu= False)
        return self.perc

    def cpu_stats(self):
        self.stats = psutil.cpu_stats()
        return self.stats

    def getloadavg(self):
        self.load = psutil.getloadavg() 
        return self.load
    
class Table(CPU):
    def __init__(self):
        self.times = self.percent()
        self.load = self.getloadavg()
    def display_cpu_times(self):
        table = PrettyTable(["user", "nice", "system", "idle", "iowait" ])
        table.add_row([self.times.user,self.times.nice, self.times.system, self.times.idle, self.times.iowait]) 
        print(table)
    
    def display_loadavg(self):
        table = PrettyTable(["Time Interval", "Avg Load" ])
        interval = ["1 min", "5 min", "15 min"]
        for item in self.load:
            inter = interval[self.load.index(item)]
            table.add_row([inter, item])
        print(table) 

class show(CPU):
    def __init__(self):
        self.count = self.cpu_count()
        self.stats = self.cpu_stats()

    def show_cpu_count(self):
        print(f"The number of CPU is {int(self.count/2)}\nThe number of Logical CPU is {self.count}")

    def show_stats(self):
        print()
        attr = ["ctx_switches", "interrupts", "soft_interrupts", "syscalls" ]
        for item in self.stats:
            val = attr[self.stats.index(item)]
            print(f"{val} =  {item}")
        print()
