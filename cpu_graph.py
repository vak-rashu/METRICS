from cpu import CPU
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Settings
def cpu_plot():
    interval_ms = 1000  # 1 sec update
    duration_secs = 60  # 1 minute

    cpu_user = []
    cpu_system = []
    cpu_idle = []
    cpu_iowait = []
    cpu_nice = []           

# Setup plot
    fig, ax = plt.subplots()

# Multiple lines
    line_user, = ax.plot([], [], color='red', label='User')
    line_system, = ax.plot([], [], color='blue', label='System')
    line_idle, = ax.plot([], [], color='green', label='Idle')
    line_iowait, = ax.plot([], [], color='orange', label='IO Wait')
    line_nice, = ax.plot([], [], color='purple', label='Nice')

# Function to update the graph
    def update(frame):
        cpu = CPU().percent_graph()
        cpu_user.append(cpu.user)
        cpu_system.append(cpu.system)
        cpu_idle.append(cpu.idle)
        cpu_iowait.append(cpu.iowait)
        cpu_nice.append(cpu.nice)

    # Keep only the last 60 data points
        for data_list in [cpu_user, cpu_system, cpu_idle, cpu_iowait, cpu_nice]:
            if len(data_list) > duration_secs:
                data_list.pop(0)

        x_vals = list(range(len(cpu_user)))

    # Update data for each line
        line_user.set_data(x_vals, cpu_user)
        line_system.set_data(x_vals, cpu_system)
        line_idle.set_data(x_vals, cpu_idle)
        line_iowait.set_data(x_vals, cpu_iowait)
        line_nice.set_data(x_vals, cpu_nice)

        ax.set_xlim(0, duration_secs - 1)
        ax.set_ylim(0, 100)

    # X-axis ticks at every 10 seconds
        tick_positions = [9, 19, 29, 39, 49, 59]
        tick_labels = ["10 secs", "20 secs", "30 secs", "40 secs", "50 secs", "1 min"]
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(tick_labels)

        ax.legend(loc='upper right')
        ax.set_title("CPU Usage (per category)")
        ax.set_ylabel("% Usage")
        ax.set_xlabel("Time Elapsed")

        return line_user, line_system, line_idle, line_iowait, line_nice

    ani = animation.FuncAnimation(fig, update, interval=interval_ms)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    cpu_plot()
