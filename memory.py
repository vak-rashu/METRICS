import psutil
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import byte2human

class Memory:
    def virtual_mem(self):
        self.vm = psutil.virtual_memory()
        return self.vm

    def swap_memory(self):
        self.sm = psutil.swap_memory()
        return self.sm
    
class display_stat(Memory):
    def display_vm(self):
        self.stat = self.virtual_mem()
        print(f"\n---- Virtual Memory Statistics ----\nTotal = {byte2human.convert_bytes(self.stat.total)}\nAvailable = {byte2human.convert_bytes(self.stat.available)}\nPercent = {self.stat.percent}\nFree = {byte2human.convert_bytes(self.stat.free)}\nUsed = {byte2human.convert_bytes(self.stat.used)}\nActive = {byte2human.convert_bytes(self.stat.active)}\nInactive = {byte2human.convert_bytes(self.stat.inactive)}\nSlab = {byte2human.convert_bytes(self.stat.slab)}\n")

    def display_sm(self):
        self.stat = self.swap_memory()
        print(f"\n---- Swap Memory Statistics ----\nTotal = {byte2human.convert_bytes(self.stat.total)}\nUsed = {byte2human.convert_bytes(self.stat.used)}\nPercent = {self.stat.percent}\nFree = {byte2human.convert_bytes(self.stat.free)}\nSin = {byte2human.convert_bytes(self.stat.sin)}\nSout = {byte2human.convert_bytes(self.stat.sout)}\n")

    def cache(self):
        self.cache = self.virtual_mem()
        print(f"\nCached = {byte2human.convert_bytes(self.cache.cached)}\nBuffers = {byte2human.convert_bytes(self.cache.buffers)}\n")
