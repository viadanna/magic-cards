#!/bin/sh

# Start the first process
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
fi

# Start the second process
python3 app.py &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  exit $status
fi

# Naive check runs checks once a minute to see if either of the processes exited.
while sleep 60; do
  ps aux |grep "consumer.py" |grep -q -v grep
  PROCESS_1_STATUS=$?
  if [ $PROCESS_1_STATUS -ne 0 ]; then
    echo "Starting consumer."
    python3 consumer.py &
  fi
  ps aux |grep "app.py" |grep -q -v grep
  PROCESS_1_STATUS=$?
  if [ $PROCESS_1_STATUS -ne 0 ]; then
    echo "Starting app."
    python3 app.py &
  fi
done
