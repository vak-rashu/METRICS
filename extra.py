import psutil
from prettytable import PrettyTable

'''import psutil
print(psutil.getloadavg())'''

'''load = psutil.getloadavg()
interval = ["1 min", "5 min", "15 min"]
zip_file = zip(interval, load)
dic = dict(zip_file)
print(dic)
for item in dic:
    print((item, dic[item]))'''

'''def loop():
    for item in dic:
        print(item, dic[item])
loop()'''

'''def display_loadavg():
        table = PrettyTable(["Time Interval", "Avg Load" ])
        for item in dic:
            table.add_row([item, dic[item]]) 
        print(table)

display_loadavg()'''


'''def display_loadavg(self):
        table = PrettyTable(["Time Interval", "Avg Load" ])
        interval = ["1 min", "5 min", "15 min"]
        for val, inter in self.load, interval:
            table.add_row(inter, val)
        print(table)  '''   


'''p = psutil.disk_partitions()
print(p) '''


 
'''for i in load :
     ind= i 
     inter= interval [ load.index( i ) ]
     print(inter, ind)

for i in interval :
    ind = load [ interval.index( i ) ]
    inter= i 
    print(inter, ind)
    
for i in range(len(interval)) :
    ind = load[i]
    inter= interval[i]
    print(inter, ind)'''    

'''d = psutil.disk_usage("/")
print(d) '''

'''p = psutil.Process()
a = p.pid
pid = psutil.Process(a)
for i in psutil.process_iter(["name", "pid"]):
    print(i.info["name"], i.info["pid"])
print(p.open_files())
print(a)
print(pid.io_counters()) '''