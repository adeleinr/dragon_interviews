"""
You are given a web server log file /root/devops/server.log, where each line has the following format:

request date, time, and time zone
request line from the client in the format: HTTP request, file name requested, protocol version
HTTP status code returned to the client
size (in bytes) of the returned object
For example: [01/Aug/1995:00:54:59 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511.

Your task is to output the 10 most frequently requested files, with their
cumulative bytes transferred in the format:

file_name bytes_transferred
You should only take into account GET requests with a successful status (2xx).

The output should be sorted in descending order of requests' frequency.
If there are two files with the same number of requests, you should sort them
by file_names in lexicographical order. If there are less than 10 files satisfying
all the above conditions, print them all in the correct order.

Example

Consider the following files on your computer:

/root/devops/server.log
/root/devops/server.log contains the following information:

[01/Aug/1995:00:54:59 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
[01/Aug/1995:00:55:04 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
[01/Aug/1995:00:55:06 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 403 298
[01/Aug/1995:00:55:09 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
[01/Aug/1995:00:55:18 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
[01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
The output for this test should be as follows:

/images/ksclogosmall.gif 10905
/images/opf-logo.gif 65022
Note that the output should be sorted in descending order not by the amount of transfered bytes, but by the requests' frequency: for /images/ksclogosmall.gif it is 4 and for /images/opf-logo.gif it is 2, thus the first file goes before the second one in the output.
"""
from collections import defaultdict

file = open("/root/devops/server.log", "r")

request_frecuency_map = defaultdict(dict)

for line in file.readlines():
    data = line.split()
    filename = data[3]
    status_code = int(data[5])
    size = int(data[6])

    if 200 <= status_code < 300:
        item = request_frecuency_map.get(filename)
        if item is not None:
            count = item[0]
            old_size = item[1]
            request_frecuency_map[filename] = (count + 1, old_size + size)
        else:
            request_frecuency_map[filename] = (1, size)

sorted_summary = dict(
    sorted(request_frecuency_map.items(), key=lambda item: (-item[1][0], item[0].split("/")[-1]))
)
result = ""
for key, value in sorted_summary.items():
    print(key + " " + str(value[1]))











