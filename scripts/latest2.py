"""
Written by Duygu Dağdelen, 2023
************************************

Make sure to name the input SRT file following a format like "aos_S01E14.srt" or a similar one (e.g. "aos_s01e14.srt"),
where "s" represents the season number and "e" represents the episode number.
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
    duration_line = ''
    text_line = ''
    line_order = 0  # Initialize line_order as 0

    for line in lines:
        line = line.strip()

        if line.isdigit():
            serial = int(line)
            line_order += 1  # Increment line_order for each new line of text
        elif '-->' in line:
            timecodes = line.split(' --> ')
            time_in = timecodes[0]
            time_out = timecodes[1]
            duration_line = calculate_duration(time_in, time_out)
        elif line:
            # Check if the current line can be considered a continuation of the previous line
            if csv_data and is_continuation(csv_data[-1], line):
                csv_data[-1][3] = time_out  # Update timecode_out
                csv_data[-1][4] = calculate_duration(csv_data[-1][2], time_out)  # Update duration_line
                csv_data[-1][6] += ' ' + line.strip()  # Merge lines
            else:
                if csv_data:
                    line_order = csv_data[-1][5] + 1  # Increment line_order based on the previous line
                # Remove hyphen at the start of the line if it exists
                line = line.lstrip('-')
                csv_data.append([season, episode, time_in, time_out, duration_line, line_order, line.strip()])
                line_order += 1  # Increment line_order for the current line
        else:
            text_line = ''

    with open(csv_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['season', 'episode', 'timecode_in', 'timecode_out', 'duration_line', 'line_order', 'text_line'])
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

def is_continuation(prev_line, curr_line):
    # Check if the current line can be considered a continuation of the previous line
    if prev_line[6][-1] not in ['.', '!', '?', '…'] and curr_line[0].islower():
        return True
    if prev_line[6][-1] in [',']:
        return True
    if prev_line[6].endswith('…') and curr_line[0].islower():
        return True

    # If there are at least two uppercase characters consecutively, the previous line will be treated as an independent element,
    # such as signs, titles, or headers seen in the scene.
    if any(char.isupper() for i, char in enumerate(prev_line[6]) if char.isalpha() and char.isupper() and i < len(prev_line[6])-1 and prev_line[6][i+1].isupper()):
        return False

    # Check if the current line starts with a lowercase word (ignoring symbols at the beginning)
    first_word = re.search(r'\b[a-zA-Z]+\b', curr_line)
    if first_word and first_word.group(0)[0].islower():
        return True  
    if curr_line[0].isupper() and (prev_line[6][-1] not in ['.', '!', '?', '…']):
        return True
    return False


# EXAMPLE USAGE

srt_file = 'path/to/input.srt'
csv_file = 'path/to/output.csv'

srt_to_csv(srt_file, csv_file)
