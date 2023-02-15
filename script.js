// Use jQuery's $.get() method to fetch the CSV file containing the quotes
$.get("https://raw.githubusercontent.com/dduyg/alchemyofsouls-quotes/main/data/alchemyofsoulsquotes.csv", function(data) {
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
        const randomIndex = getRandomIndex(quotes.length);
        const randomQuote = quotes[randomIndex];

        // Check if the random quote has any missing data
        if (!randomQuote.text || !randomQuote.character || !randomQuote.season || !randomQuote.episode) {
            // If the quote is missing data, show an error message and do not update the HTML elements
            alert("Error: The selected quote is missing data. Please try again.");
            return;
        }

        // Update the HTML elements with the quote data
        quoteText.textContent = randomQuote.text;
        quoteCharacter.textContent = randomQuote.character;
        quoteSeason.textContent = randomQuote.season;
        quoteEpisode.textContent = randomQuote.episode;
    }

    // Function to generate a random index between 0 and maxIndex (exclusive)
    function getRandomIndex(maxIndex) {
        return Math.floor(Math.random() * maxIndex);
    }

    // Show a random quote when the page loads
    showRandomQuote();

    // Show a new random quote when the button is clicked
    newQuoteButton.addEventListener("click", showRandomQuote);
});
