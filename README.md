# Generating quotes from Alchemy of Souls

This application returns a random line from the Korean series [*Alchemy of Souls*](https://www.imdb.com/title/tt20859920/) upon the click of a button, and displays it in the browser.

<a href="https://dduyg.github.io/alchemy-of-souls/"><img src="/images/project-image.png" width="245px"></a>

It is built using HTML, CSS, and JavaScript. The *jQuery library* is used to fetch the CSV file containing the quotes/lines, which is also supported by older browsers contrary to the fetch API method. It uses the `$.get()` method to retrieve the CSV file, parse it and display the quotes. You need a *csv parser library* for this to work. This application uses `Papa Parse`. You should include the library in your HTML file before the script.

| Status   | Details       |
|----------|---------------|
| Complete | Episodes `S01E01` to `S01E18` integrated  |
| To-Do    | Integrating episodes `S01E19` to `S02E10`        |
