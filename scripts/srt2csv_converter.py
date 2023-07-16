"""
Written by Duygu Dağdelen, 2023
************************************

Make sure to name the input SRT file following a format like "AoS_S01E14.srt" or a similar one,
where "S” represents the season number and "E" represents the episode number.
This naming convention is necessary to extract the season and episode from the SRT file name.

"""

import csv
import re

def srt_to_csv(srt_file, csv_file):
    # Extract season and episode from the SRT file name
    season, episode = extract_season_episode(srt_file)

    with open(srt_file, 'r') as srt:
        lines = srt.readlines()

    csv_data = []
    serial = 1  # Initialize serial as 1
    time_in = ''
    time_out = ''
    duration = ''
    text = ''
    number_line = 0  # Initialize number_line as 0

    for line in lines:
        line = line.strip()

        if line.isdigit():
            serial = int(line)
            number_line += 1  # Increment number_line for each new line of text
        elif '-->' in line:
            timecodes = line.split(' --> ')
            time_in = timecodes[0]
            time_out = timecodes[1]
            duration = calculate_duration(time_in, time_out)
        elif line:
            text += ' ' + line
        else:
            csv_data.append([season, episode, time_in, time_out, duration, number_line, text.strip()])
            text = ''

    with open(csv_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['season', 'episode', 'timecode_in', 'timecode_out', 'duration', 'number_line', 'text'])
        writer.writerows(csv_data)

    print(f"Conversion completed. CSV file '{csv_file}' has been created.")

def extract_season_episode(srt_file):
    # Extract season and episode from the SRT file name using regular expressions (case-insensitive)
    match = re.search(r's(\d+)e(\d+)', srt_file, re.IGNORECASE)
    if match:
        season = int(match.group(1))
        episode = int(match.group(2))
        return season, episode
    else:
        raise ValueError("Invalid SRT file name format. Unable to extract season and episode.")

def calculate_duration(time_in, time_out):
    # Calculate the duration in seconds based on the timecodes
    in_parts = time_in.split(':')
    out_parts = time_out.split(':')

    in_seconds = int(in_parts[0]) * 3600 + int(in_parts[1]) * 60 + float(in_parts[2].replace(',', '.'))
    out_seconds = int(out_parts[0]) * 3600 + int(out_parts[1]) * 60 + float(out_parts[2].replace(',', '.'))

    duration = round(out_seconds - in_seconds, 2)
    return "{:.2f}".format(duration)


# EXAMPLE USAGE

srt_file = 'path/to/input.srt'
csv_file = 'path/to/output.csv'

srt_to_csv(srt_file, csv_file)
