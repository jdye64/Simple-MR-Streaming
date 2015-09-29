# Simple-MR-Streaming

To run a MR-Streaming job invoke the following command with your desired values.

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapreduce.map.memory.mb=256 \
-files map.py \
-mapper 'map.py' \
-reducer NONE \
-input /DesiredHDFSDirectory/inputs \
-output /DesiredHDFSDirectory/Output \