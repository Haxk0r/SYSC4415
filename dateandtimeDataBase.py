import csv
import datetime
import random

# Create list of DSCP tag names
DSCP_TAGS = ['Gaming', 'Videoconferencing', 'Streaming', 'VoIP', 'VOD']

# Create list of dates from 1/1/2018 to 1/1/2023
start_date = datetime.datetime(2018, 1, 1)
end_date = datetime.datetime(2023, 1, 1)
dates = [start_date + datetime.timedelta(days=x) for x in range((end_date-start_date).days)]

# Generate data for each date
data = []
for date in dates:
    # Generate timestamps for each date
    timestamps = [date + datetime.timedelta(minutes=x) for x in range(0, 1440, 5)]
    for timestamp in timestamps:
        # Generate random number of DSCP tags for each timestamp
        num_tags = random.randint(1, len(DSCP_TAGS))
        # Generate random DSCP tags for each timestamp
        dscp_tags = random.sample(DSCP_TAGS, num_tags)
        for dscp_tag in dscp_tags:
            # Append data to list
            data.append([date.strftime('%m/%d/%Y'), timestamp.strftime('%I:%M %p'), dscp_tag])

# Write data to CSV
with open('database.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write headers
    writer.writerow(['Date', 'Timestamp', 'DSCP Tag', 'Gaming', 'Videoconferencing', 'Streaming', 'VoIP', 'VOD'])
    # Loop through data and write rows to CSV
    for row in data:
        # Initialize new columns to all 0s
        new_cols = [0] * 5
        # Set value of corresponding DSCP tag column to 1
        new_cols[DSCP_TAGS.index(row[2])] = 1
        # Write row to CSV
        writer.writerow(row + new_cols)
