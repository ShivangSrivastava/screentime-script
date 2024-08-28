#!/bin/bash

LOG_FILE="/tmp/screen_time_log.txt"
DATE_FORMAT="%Y-%m-%d %H:%M:%S"

# Function to calculate screen time for a given date range
calculate_time_for_date_range() {
    local start_time end_time
    local date_filter="$1"
    local filtered_log_file="/tmp/screen_time_log_filtered.txt"

    grep "$date_filter" "$LOG_FILE" > "$filtered_log_file"

    if [ ! -s "$filtered_log_file" ]; then
        echo "No log entries found for date filter: $date_filter!"
        return
    fi

    start_time=$(head -n 1 "$filtered_log_file" | xargs -I {} date -d "{}" +%s)
    end_time=$(tail -n 1 "$filtered_log_file" | xargs -I {} date -d "{}" +%s)

    if [ -z "$start_time" ] || [ -z "$end_time" ]; then
        echo "No valid log entries found for date filter: $date_filter!"
        return
    fi

    total_time=$((end_time - start_time))
    echo "Total active screen time for $date_filter: $((total_time / 3600)) hours $(((total_time % 3600) / 60)) minutes $(((total_time % 3600) % 60)) seconds"
}

# Update screentime
startscreentime

# Check for command-line arguments
if [ "$#" -eq 0 ]; then
    # Default behavior: current date
    CURRENT_DATE=$(date +"%Y-%m-%d")
    calculate_time_for_date_range "$CURRENT_DATE"
elif [ "$1" == "-a" ]; then
    # Show screen time for all dates
    awk '{print substr($1, 1, 10)}' "$LOG_FILE" | sort | uniq | while read date; do
        calculate_time_for_date_range "$date"
    done
else
    echo "Usage: $0 [-a]"
    echo "  -a     Show screen time for all dates"
    exit 1
fi
