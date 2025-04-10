import psutil
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import sys

class Process:
    def process_list(self):
            table = PrettyTable(["PID", "Name", "Status"])
            for proc in psutil.process_iter(["pid", "name", "status"]):
                 table.add_row([proc.info['pid'], proc.info['name'], proc.info['status']])
            print(table)

    def show_runnable(self):
            table = PrettyTable(["PID", "Name", "Status"])
            for proc in psutil.process_iter(["pid", "name", "status"]):
                 if proc.info['status'] == 'running':
                    table.add_row([proc.info['pid'], proc.info['name'], proc.info['status']])
            print(table)

    def process_cpu_times(self):
        table = PrettyTable(["PID", "Name", "User", "System"])
        for proc in psutil.process_iter(["pid", "name", "cpu_times"]):
            table.add_row([proc.info["pid"], proc.info["name"], proc.info["cpu_times"].user, proc.info["cpu_times"].system])
        print(table)

    def proc_io(self):
        pid = int(input("Enter PID"))
        if pid>=0:
            pid = pid
            p_io = psutil.Process(pid = pid)
            print("Process: ", p_io.io_counters())
        else:
            pid = None
            p_io = psutil.Process(pid = pid)
            print("Current Process: ", p_io.io_counters())

    def time_cpu(self):
        p_time = psutil.Process()
        print(p_time.cpu_times())
    
    def threads(self):
        pid = int(input("Enter PID"))
        if pid>=0:
            pid = pid
            p_threads = psutil.Process()
            print("Process:", p_threads.threads())
        
        else:
            pid = None
            p_threads = psutil.Process()
            print("Current Process:", p_threads.threads())
            