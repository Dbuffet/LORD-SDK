from lordoftheringssdk.api_methods import ApiMethods, session
from lordoftheringssdk.conf import BASE_URL, API_KEY
from .quote import Quote

class Movie(ApiMethods):
    """Class representing a Lord of the Rings movie"""

    def __init__(
        self,
        id: str,
        name: str,
        run_time: int,
        budget: int,
        revenue: int,
        nominations: int,
        nomination_wins: int,
        score: int,
    ):
        """
        Initializes a Movie object with relevant attributes

        :param id: movies unique identifier
        :param name: name of movie
        :param run_time: the movie's run time in minutes
        :param budget: the movie's budget in millions
        :param nominations: the number of nominations 
        :param nomination_wins: the number of nominations won
        :param score: Rotten Tomatoes rating
        """
        self.id = id
        self.name = name
        self.run_time = run_time
        self.budget = budget
        self.revenue = revenue
        self.nominations = nominations
        self.nomination_wins = nomination_wins
        self.score = score

    @property
    def quotes(self):
        """Returns all quotes from movie"""
        url = f"{self.endpoint}/{self.id}/quote"
        resp = session.get(url)
        return Quote.serialize(resp.json()["docs"])


