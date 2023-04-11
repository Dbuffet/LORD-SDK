# Lord of the Rings SDK

The Lord of the Rings SDK is a Python package that provides easy access to the Lord of the Rings API. It includes modules for interacting with the movies, and quotes from the Lord of the Rings movies.

## Installation

To get started, you'll need to install the DR_lotr_sdk package.

```bash
pip install DR_lotr_sdk
```

This will install all the necessary dependencies.


## Configuration

1. Go to the website [https://the-one-api.dev/](https://the-one-api.dev/) and sign up to obtain an API key.
2. Open a configuration file (e.g., `conf.py`).
3. Update the configuration file with your API key.

```python
  API_KEY: "YOUR_API_KEY"
```


## Importing the SDK

You can import the Lord of the Rings SDK in your Python script using the following import statement:

```python
from lordoftheringssdk import Movie, Quote
```

This will allow you to use the Movie, and Quote classes from the SDK in your code.



## Usage

Here are some basic examples of how to use the Lord of the Rings SDK:

```python
from lordoftheringssdk import Movie, Quote

# Get all the movies
movies = Movie.get()
print(movies[1])
print()

# Get a specific quote
print(movies[5].quotes[2])
print()

# Get the names of all the movies
movies_list = Movie.get()
for movie in movies:
    print(movie.name)
print()

# Get all the quotes
quotes = Quote.get()
for quote in quotes:
    print(quotes)
print()

# Get a specific quote
print(quotes[3])
print()

# Get information about a specific movie
movie_id = Movie.get(id="5cd95395de30eff6ebccde5d")
print(movie_id.name)
print()

# Get all the quotes from a specific movie
print(movie_id.quotes)
print()
```

## Endpoints

The SDK interacts with the following endpoints:

- `/movies`: This endpoint returns a list of all the movies from the Lord of the Rings series.

- `/movies/<id>`: This endpoint returns information about a specific movie, identified by the id parameter.

- `/movie/<id>/quotes`: This endpoint returns a list of all the quotes from a specific movie, identified by the id parameter.

- `/movie/<id>/quotes/<id>`: This endpoint returns a specific quote from a specific movie, identified by the id parameter.

- `/quotes`: This endpoint returns a list of all the quotes from the Lord of the Rings movies.

- `/quotes/<id>`: This endpoint returns information about a specific quote, identified by the id parameter.



## Running Tests

The tests directory in the package contains a test.py file that you can use to run tests for the SDK. To run the tests, navigate to the root directory of the package and run the following command:

```bash
python tests/test.py
```
This will execute the tests and provide the test results.