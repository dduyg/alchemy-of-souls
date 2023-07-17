# Data

- To create the data, I turned to the English subtitles per episode, which where available in `srt` format on opensubtitles.org[^1], an platform providing multilingual subtitles.
- Prepped data for analyzing in `aos-episodes`, using the [Python script](../scripts/srt2csv.py)

[^1]: Please note that the English subtitles sourced from opensubtitles.org, are used under the assumption of fair use for non-commercial purposes. All rights, including copyright, belong to their respective owners. Any analysis, processing, and presentation of the data were conducted solely for non-commercial purposes as part of a personal project.

## data/aos-episodes
g

## The final dataset used in the application  alchemyofsoulsquotes.csv

| variable  | type    | description                    |
|-----------|---------|--------------------------------|
| text      | string  | Lines spoken in the scene      |
| character | string  | Name of the character speaking |
| season    | integer | Season number                  |
| episode   | integer | Episode number                 |

