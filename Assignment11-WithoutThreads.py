# Preston Tighe
# Programming Languages
# 10-25-16
# Assignment 11
# Without threads

# 1 thread takes: .31788
# Global: 186050305000

# 100 threads takes: 19.82325
# Global: 6522302500

import time
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

    global_triangular(input_value)

final_stop = time.time()
print("     Total time: " + str(final_stop - initial_start) + " seconds" + " - total_sum: " + str(total_sum))
