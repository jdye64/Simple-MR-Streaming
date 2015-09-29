#!/usr/bin/env python

import os, sys, csv

# Hadoop Streaming - each line from input file is read from stdin here
for line in sys.stdin:
  data = line.strip() # Data received from the input file. Format depends on InputFormat used when invoking MR-Streaming job.
  
  # At this point do whatever you desire with the data. 
  # "print" will emit the data to the "reducer" task or if no "reducer" is set directly to the output file.
  print str(data) # Simply write all of the data to file for demonstration purposes.