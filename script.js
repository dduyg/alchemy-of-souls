// Use jQuery's $.get() method to fetch the CSV file containing the quotes
$.get("https://raw.githubusercontent.com/duygudgd/alchemy-of-souls-quotes/main/data/alchemyofsoulsquotes.csv", function(data) {
    // Convert the CSV data to a 2D array
    const quotes = Papa.parse(data, { header: true }).data;

    // Select the quote-related elements from the HTML
    const quoteText = document.querySelector("#text");
    const quoteCharacter = document.querySelector("#character");
    const quoteSeason = document.querySelector("#season");
    const quoteEpisode = document.querySelector("#episode");
    const newQuoteButton = document.querySelector("#new-quote");

    // Function to display a random quote
    function showRandomQuote() {
      // Select a random quote from the array
      const randomIndex = Math.floor(Math.random() * quotes.length);
      const randomQuote = quotes[randomIndex];

      // Update the HTML elements with the quote data
      quoteText.textContent = randomQuote.text;
      quoteCharacter.textContent = randomQuote.character;
      quoteSeason.textContent = randomQuote.season;
      quoteEpisode.textContent = randomQuote.episode;
    }

    // Show a random quote when the page loads
    showRandomQuote();

    // Show a new random quote when the button is clicked
    newQuoteButton.addEventListener("click", showRandomQuote);
});
