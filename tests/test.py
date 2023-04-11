import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lordoftheringssdk.movie import Movie
from lordoftheringssdk.quote import Quote

class TestApiMethods(unittest.TestCase):
    
    def test_movie(self):
        movies = Movie.get()
        self.assertIsInstance(movies, list)
        self.assertIsInstance(movies[0], Movie)
        self.assertIsInstance(movies[3], Movie)
        print("Movie test Passed")
        
    def test_quote(self):
        quotes = Quote.get()
        self.assertIsInstance(quotes, list)
        self.assertIsInstance(quotes[3], Quote)
        print("Quote test Passed")

    def test_movie_get_one(self):
        movie = Movie.get(id="5cd95395de30eff6ebccde5d")
        self.assertIsInstance(movie, Movie)
        self.assertEqual(movie.name, "The Return of the King")
        print("test_movie_get_one Passed")

    
if __name__ == '__main__':
    unittest.main()
