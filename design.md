# SDK Design Overview

This software development kit (SDK) provides a way to interact with an API for retrieving information about Lord of the Rings movies and quotes. The SDK is written in Python and utilizes the requests library for HTTP requests and API authentication.

## API Credentials

The API credentials are stored in a configuration file called conf.py. This file contains the base URL for the API and the API key necessary for authentication.

## API Methods

The ApiMethods class is the base class for all API calls. It contains a method for serializing API responses into Python objects, as well as a method for making API GET requests.

## Movie Class

The Movie class represents a Lord of the Rings movie and extends the ApiMethods class. It has attributes for the movie's unique identifier, name, run time, budget, revenue, number of nominations, number of nominations won, and Rotten Tomatoes rating. It also has a property method for retrieving all quotes from the movie.

## Quote Class

The Quote class represents a quote from a Lord of the Rings character or movie and extends the ApiMethods class. It has attributes for the quote's unique identifier, contents of the quote, identifier for the movie the quote is from, identifier for which character says the quote, and a redundant quote identifier. It also has a property method for retrieving the movie associated with the quote.
