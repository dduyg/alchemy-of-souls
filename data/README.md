# Data
To create the data, I turned to the English subtitles per episode, which where available in `srt` format on opensubtitles.org, an platform providing multilingual subtitles.
> Please note that the English subtitles sourced from opensubtitles.org, are used under the assumption of fair use for non-commercial purposes. Any analysis, processing, and presentation of the data were conducted solely for non-commercial purposes as part of a personal project. All rights, including copyright, belong to their respective owners.

## /aos-episodes
The prepped data for analyzing is accessible in `/aos-episodes`. It is created using [`../scripts/srt2csv.py`](../scripts/srt2csv.py)

## /alchemyofsouls_valuable_lines.csv
This is the final dataset used in the application.

| variable  | type    | description                    |
|-----------|---------|--------------------------------|
| text      | string  | Lines spoken in the scene      |
| character | string  | Name of the character speaking |
| season    | integer | Season number                  |
| episode   | integer | Episode number                 |

