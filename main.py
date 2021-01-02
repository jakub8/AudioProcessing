import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# data = stream.read(CHUNK)
# data_int = struct.unpack(str(CHUNK) + 'h', data)
# fig, ax = plt.subplots()
# ax.plot(data_int, '-')
# plt.show()

fig, ax = plt.subplots()

x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(-4096, 4096)
ax.set_xlim(0, CHUNK)

# fig.show()

start = False
start_counter = 0
hit_counter = 0

while True:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(CHUNK) + 'h', data)

    if start_counter > CHUNK:
        start = True

    for num in data_int:
        if num > 500:
            start_counter = 0
            if start:
                start = False
                hit_counter += 1
                print('HIT: ' + str(hit_counter))
        elif -20 < num < 20:
            start_counter += 1

    # changes graph  MAKE SURE TO UNCOMMENT SHOW()
    # line.set_ydata(data_int)
    # fig.canvas.draw()
    # fig.canvas.flush_events()
    # changes graph


