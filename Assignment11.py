# Preston Tighe
# Programming Languages
# 10-25-16
# Assignment 11

# 1 thread takes: .1114 secs
# 100 threads takes: .1767 secs

import time
import json
from threading import Thread

run_times = 4
factorial_range = 10000
offset = 61
threads = []

# Initial total_sum to file
with open('test.json', 'w') as initial_file:
    initial_file.write(json.dumps({"total_sum": 0}))


def global_factorial(end_range):
    with open('test.json', 'r') as read_file:
        data = json.load(read_file)

    total_sum = data['total_sum']
    for j in range(end_range):
        total_sum += j

    test = 1
    with open('test.json', 'w') as write_file:
        write_file.write(json.dumps({"total_sum": total_sum}))


initial_start = time.time()

# Run function 100 times
for i in range(offset, run_times + offset):

    input_value = int(i * (factorial_range / run_times))

    t = Thread(target=global_factorial, args=[input_value])
    threads.append(t)

# Start all threads
for x in threads:
    x.start()

# Wait for all of them to finish
for x in threads:
    x.join()

final_stop = time.time()

with open('test.json', 'r') as final_file:
    data = json.load(final_file)
print("     Total time: " + str(final_stop - initial_start) + " seconds" + " - total_sum: " + str(data['total_sum']))
