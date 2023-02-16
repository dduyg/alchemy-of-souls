# Generating quotes from Alchemy of Souls

This application returns a random quote from the Korean series *Alchemy of Souls* upon the click of a button, and displays it in the browser.
<a href="https://dduyg.github.io/alchemyofsouls-quotes/"><img align="right" width="160" src="/images/alchemyofsouls.png"></a>

It is built using HTML, CSS, and JavaScript. The *jQuery library* is used to fetch the CSV file containing the quotes/lines, which is also supported by older browsers contrary to the fetch API method. It uses the `$.get()` method to retrieve the CSV file, parse it and display the quotes. You need a *csv parser library* for this to work. This application uses `Papa Parse`. You should include the library in your HTML file before the script.

Here’s a screenshot of what the finished application looks like: 
<a href="https://dduyg.github.io/alchemyofsouls-quotes/"><img src="/images/project-image-2.png" width="245px"></a>

| Status   | Details       |
|----------|---------------|
| Complete | Episodes `S01E01` to `S01E14` integrated  |
| To-Do    | Integrating episodes `S01E15` to `S02E10`        |


## Data
- The original raw data scraped as English Subtitles (`.srt`) for Alchemy of Souls, per episode accessible in `data/raw-data/`.  
- Cleaned the raw English subtitles data into `alchemyofsoulsquotes.csv` dataset.

### data/alchemyofsoulsquotes.csv
| variable  | type    | description                    |
|-----------|---------|--------------------------------|
| text      | string  | Lines spoken in the scene      |
| character | string  | Name of the character speaking |
| season    | integer | Season number                  |
| episode   | integer | Episode number                 |
