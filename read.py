import serial
import matplotlib.pyplot as plt
from collections import deque
import numpy as np

ser = serial.Serial('/dev/cu.usbmodem1201', 115200)
plt.ion()
fig, ax = plt.subplots()
WINDOW_SIZE = 500
SAMPLE_PERIOD = 0.05
x = np.arange(WINDOW_SIZE) * SAMPLE_PERIOD
data = deque([0] * WINDOW_SIZE, maxlen=WINDOW_SIZE)
line, = ax.plot(x, data)
ax.set_ylim(0, .1)
ax.set_xlim(0, WINDOW_SIZE * SAMPLE_PERIOD)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title("Voltage Seismogram")

while True:
    try:
        line_in = ser.readline().decode().strip()
        voltage = float(line_in)
        data.append(voltage)
        line.set_ydata(data)
        fig.canvas.draw()
        fig.canvas.flush_events()
    except ValueError:
        pass
