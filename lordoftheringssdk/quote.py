from lordoftheringssdk.api_methods import ApiMethods

class Quote(ApiMethods):
    """Class representing a quote from a Lord of the Rings movie"""

    def __init__(
        self, _id: str, dialog: str, movie_id: str, character_id: str, id: str
    ):
        """
        Initializes a Quote object with relevant attributes

        :param _id: quote's unique identifier
        :param dialog: the contents of the quote
        :param movie_id: identifier for the movie the quote is from
        :param character_id: identifier for which character says the quote
        :param id: redundant quote identifier
        """
        self._id = _id
        self.dialog = dialog
        self._movie_id = movie_id
        self._character_id = character_id
        self.id = id
        self.name = dialog

    @property
    def movie(self):
        from .movie import Movie
        return Movie.get(self._movie_id)[0]
