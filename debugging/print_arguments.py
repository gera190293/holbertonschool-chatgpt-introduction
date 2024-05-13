#!/usr/bin/python3
import sys

# Start the loop from index 1, as sys.argv[0] contains the script name
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
