import csv

def srt_to_csv(srt_file, csv_file):
    with open(srt_file, 'r') as srt:
        lines = srt.readlines()

    csv_data = []
    serial = 1  # Initialize serial as 1
    time_in = ''
    time_out = ''
    duration = ''
    text = ''

    for line in lines:
        line = line.strip()

        if line.isdigit():
            serial = int(line)
        elif '-->' in line:
            timecodes = line.split(' --> ')
            time_in = timecodes[0]
            time_out = timecodes[1]
            duration = calculate_duration(time_in, time_out)
        elif line:
            text += ' ' + line
        else:
            csv_data.append([serial, time_in, time_out, duration, text.strip()])
            text = ''

    with open(csv_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['number', 'timecode_in', 'timecode_out', 'duration', 'text'])
        writer.writerows(csv_data)

    print(f"Conversion completed. CSV file '{csv_file}' has been created.")

def calculate_duration(time_in, time_out):
    in_parts = time_in.split(':')
    out_parts = time_out.split(':')

    in_seconds = int(in_parts[0]) * 3600 + int(in_parts[1]) * 60 + float(in_parts[2].replace(',', '.'))
    out_seconds = int(out_parts[0]) * 3600 + int(out_parts[1]) * 60 + float(out_parts[2].replace(',', '.'))

    duration = round(out_seconds - in_seconds, 2)
    return "{:.2f}".format(duration)


# Example usage

srt_file = 'path/to/input.srt'
csv_file = 'path/to/output.csv'

srt_to_csv(srt_file, csv_file)

