from networking import Networking
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Settings
interval_ms = 1000  # 1 second update
duration_secs = 60  # Keep last 60 seconds

# Get all NICs
interfaces = list(Networking().net_io().keys())

# Data holders per NIC
data_sent = {nic: [] for nic in interfaces}
data_recv = {nic: [] for nic in interfaces}
prev_io = {nic: Networking().net_io()[nic] for nic in interfaces}

# Setup plot
fig, ax = plt.subplots()
lines = {}

# Assign a line for each NIC (sent and recv)
colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']
for i, nic in enumerate(interfaces):
    color = colors[i % len(colors)]
    line_sent, = ax.plot([], [], label=f'{nic} Sent', color=color, linestyle='-')
    line_recv, = ax.plot([], [], label=f'{nic} Recv', color=color, linestyle='--')
    lines[nic] = (line_sent, line_recv)


def net_plot():
    def update(frame):
        global prev_io

        current_io = Networking().net_io()

        for nic in interfaces:
            if nic not in current_io or nic not in prev_io:
                continue

            sent_diff = current_io[nic].bytes_sent - prev_io[nic].bytes_sent
            recv_diff = current_io[nic].bytes_recv - prev_io[nic].bytes_recv
            prev_io[nic] = current_io[nic]

            data_sent[nic].append(sent_diff)
            data_recv[nic].append(recv_diff)

            if len(data_sent[nic]) > duration_secs:
                data_sent[nic].pop(0)
            if len(data_recv[nic]) > duration_secs:
                data_recv[nic].pop(0)

            x_vals = list(range(len(data_sent[nic])))

        # Update lines
            lines[nic][0].set_data(x_vals, data_sent[nic])
            lines[nic][1].set_data(x_vals, data_recv[nic])

        ax.set_xlim(0, duration_secs - 1)
        max_val = max(
            [max(data_sent[nic] + data_recv[nic], default=0) for nic in interfaces],
            default=1
        )
        ax.set_ylim(0, max_val * 1.2)

    # X-axis: 10s, 20s... 1 min
        tick_positions = [9, 19, 29, 39, 49, 59]
        tick_labels = ["10 secs", "20 secs", "30 secs", "40 secs", "50 secs", "1 min"]
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(tick_labels)

        ax.set_title("Per-NIC Network Traffic (Bytes/sec)")
        ax.set_ylabel("Bytes/sec")
        ax.set_xlabel("Time Elapsed")
        ax.legend(loc='upper left', fontsize="small", ncol=2)

        return [line for pair in lines.values() for line in pair]

    ani = animation.FuncAnimation(fig, update, interval=interval_ms)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    net_plot()
