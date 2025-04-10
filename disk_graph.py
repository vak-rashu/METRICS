from disk import disk_graph
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Previous snapshot
prev_disk_io = disk_graph().disk_io_graph()

# Settings
def disk_plot():
    interval_ms = 1000  # 1 second update
    duration_secs = 60  # Keep last 60 seconds

# Data holders
    read_data = []
    write_data = []

# Setup plot
    fig, ax = plt.subplots()
    line_read, = ax.plot([], [], label='Total Read', color='blue')
    line_write, = ax.plot([], [], label='Total Write', color='green')

    def update(frame):
        global prev_disk_io

        current_io = disk_graph().disk_io_graph()

        total_read = 0
        total_write = 0

        for disk in current_io:
            if disk in prev_disk_io:
                total_read += current_io[disk].read_bytes - prev_disk_io[disk].read_bytes
                total_write += current_io[disk].write_bytes - prev_disk_io[disk].write_bytes

        prev_disk_io = current_io

        read_data.append(total_read)
        write_data.append(total_write)

        if len(read_data) > duration_secs:
            read_data.pop(0)
        if len(write_data) > duration_secs:
            write_data.pop(0)

        x_vals = list(range(len(read_data)))

        line_read.set_data(x_vals, read_data)
        line_write.set_data(x_vals, write_data)

        ax.set_xlim(0, duration_secs - 1)
        max_val = max(read_data + write_data, default=1)
        ax.set_ylim(0, max_val * 1.2)

        tick_positions = [9, 19, 29, 39, 49, 59]
        tick_labels = ["10 secs", "20 secs", "30 secs", "40 secs", "50 secs", "1 min"]
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(tick_labels)

        ax.set_title("Total Disk IO (Bytes/sec)")
        ax.set_ylabel("Bytes/sec")
        ax.set_xlabel("Time Elapsed")
        ax.legend(loc='upper left')

        return line_read, line_write

    ani = animation.FuncAnimation(fig, update, interval=interval_ms)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    disk_plot()
