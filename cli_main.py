import cmd
import os
import time
from cpu import Table, show
from networking import display_info
from memory import display_stat
from disk import Disk
from processes import Process
from sensors import Sensors
from cpu_graph import cpu_plot
from disk_graph import disk_plot
from network_graph import net_plot 



class metrics_cli(cmd.Cmd):
    prompt = ">>> "
    intro = f"---Welcome to METRICS---\nLogin to Continue."
    
    def do_login(self, line):
        """Logs into the account"""
    
    def do_cpu_graph(self, line):
        """Plots CPU graph representing the data of total time spent by CPU in each mode(in percentage)."""
        cpu_plot()
    
    def do_net_graph(self, line):
        """Plots Network graph representing data of total bytes sent and received per NIC."""
        net_plot()
    
    def do_disk_graph(self, line):
        """Plots Disk graph representing the data of total bytes being read and written."""
        disk_plot()

    """Defining CPU related metrics."""
    def do_cpu_time(self, line):
        """DIsplays the cuttent CPU time taken by it in each mode."""
        Table().display_cpu_times() 

    def do_cpu_loadavg(self, line):
        """Displays CPU Workload Average for the interval of 1min, 5min and 15min"""
        Table().display_loadavg()

    def do_cpu_count(self, line):
        """Displays number of CPU in the system."""
        show().show_cpu_count()
    
    def do_cpu_stats(self, line):
        """Display CPU Statistics."""
        show().show_stats()

    """Defining Disk related metrics."""
    def do_disk_dev_partition(self, line):
        """Displays Device Partition in the disk."""
        Disk().disk_dev_partition()
    
    def do_disk_partition(self, line):
        """Displays all the disk partitions."""
        Disk().disk_partition()
    
    def do_disk_usage(self, line):
        """Returns disk usage of the given partition."""
        Disk().disk_usage()
    
    def do_disk_io(self, line):
        """Displays Disk related I/O operations."""
        Disk().disk_io()

    """Network related metrics."""
    def do_net_io(self, line):
        """Displays Network related I/O operations."""
        display_info().display_io()

    def do_net_stats(self, line):
        """DIsplays network statistics."""
        display_info().display_stats()

    def do_net_connection(self, line):
        """Displays each socket connection details."""
        display_info().display_connections()
    
    def do_net_addr(self, line):
        """Displays the addr of each NIC."""
        display_info().display_addr()

    """Memory related metrics."""
    def do_virtual_mem(self, line):
        """Displays Virtual memory in the system."""
        display_stat().display_vm()
    
    def do_swap_mem(self, line):
        """Displays Swap memory in the system."""
        display_stat().display_sm()
    
    def do_cache(self, line):
        """Display Cache and Buffer metrics."""
        display_stat().cache()
    
    """Process related metrics."""
    def do_plist(self, line):
        """List the overall current processes in the system."""
        Process().process_list()
    
    def do_prun(self, line):
        """Lists the running processes in the system."""
        Process().show_runnable()
    
    def do_pshow(self, line):
        """Lists the time CPU has spent in user and system mode for each process."""
        Process().process_cpu_times()
    
    def do_pio(self, line):
        """Lists the I/O by the current process."""
        Process().proc_io()
    
    def do_ptime(self, line):
        """Displays the accumulated process time by the CPU."""
        Process().time_cpu()
    
    def do_threads(self, line):
        """Return threads opened by current process."""
        Process().threads()
    
    def do_help(self, arg):
        """Guide for the METRICS CLI."""
        return super().do_help(arg)
    
    """Battery"""
    def do_battery(self, line):
        """States the current Battery remaining."""
        Sensors().battery() 

    def do_clear(self, line):
        """Clear the Screen"""
        os.system("clear")
    
    def do_exit(self, line):
        """Exit the CLI."""
        print("--- Exiting METRICS CLI--- ")
        time.sleep(1)
        return True
    

if __name__ == "__main__":
    metrics_cli().cmdloop()
