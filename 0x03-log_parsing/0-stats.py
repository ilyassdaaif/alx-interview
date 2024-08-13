#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys
import re
from signal import signal, SIGINT


def print_stats(file_size, status_counts):
    print(f"File size: {file_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    print_stats(total_file_size, status_counts)
    sys.exit(0)

signal(SIGINT, signal_handler)

log_pattern = re.compile(
    r'(\d{1,3}\.){3}\d{1,3} - \[\S+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
)

total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_file_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_file_size, status_counts)
    raise
