# Preston Tighe
# Programming Languages
# 10-25-16
# Assignment 11
# With threads

# 1 thread takes: 0.47901 secs
# Global: 186050305000

# 100 threads takes: 2.08004 secs
# Global: 62725600

import time
from threading import Thread
import urllib.request

run_times = 1
triangle_range = 10000
offset = 61
threads = []
total_sum = 0


def global_triangular(end_range):
    global total_sum

    result = urllib.request.urlopen("https://cse3345-assignment11-toosick.c9users.io"
                                    "/global_triangular.php?"
                                    "total_sum=" + str(total_sum)
                                    + "&end_range=" + str(end_range)).read()

    total_sum = int(result)

initial_start = time.time()

# Run function 100 times
for i in range(offset, run_times + offset):

    input_value = int(i * (triangle_range / run_times))

    t = Thread(target=global_triangular, args=[input_value])
    threads.append(t)

# Start all threads
for x in threads:
    x.start()

# Wait for all of them to finish
for x in threads:
    x.join()

final_stop = time.time()
print("     Total time: " + str(final_stop - initial_start) + " seconds" + " - total_sum: " + str(total_sum))
