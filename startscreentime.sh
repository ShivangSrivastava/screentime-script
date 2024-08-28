#!/bin/bash

LOG_FILE="/tmp/screen_time_log.txt"
DATE_FORMAT="%Y-%m-%d %H:%M:%S"


IDLE_TIME=$(xprintidle)
TIMESTAMP=$(date +"$DATE_FORMAT")
if [ "$IDLE_TIME" -lt 60000 ]; then
    echo "$TIMESTAMP" >> $LOG_FILE
fi
