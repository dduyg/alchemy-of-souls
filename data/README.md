# Data

- To create the data, I turned to the English subtitles per episode, which where available in `srt` format on opensubtitles.org[^*], an platform providing multilingual subtitles.
- Prepped data for analyzing in `aos-episodes`, using the Python script `alchemy-of-souls/scripts/srt2csv.py`

[^*]: Please note that the English subtitles sourced from opensubtitles.org, are used under the assumption of fair use for non-commercial purposes. All rights, including copyright, belong to their respective owners. Any analysis, processing, and presentation of the data were conducted solely for non-commercial purposes as part of a personal project. 

## The final dataset alchemyofsoulsquotes.csv

| variable  | type    | description                    |
|-----------|---------|--------------------------------|
| text      | string  | Lines spoken in the scene      |
| character | string  | Name of the character speaking |
| season    | integer | Season number                  |
| episode   | integer | Episode number                 |

