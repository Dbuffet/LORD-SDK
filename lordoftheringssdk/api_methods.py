import requests
from lordoftheringssdk.conf import BASE_URL, API_KEY

# Create a session and add authorization header
session = requests.Session()
session.headers.update({"Accept": "application/json", "Authorization": f"Bearer {API_KEY}"})
    
class ApiMethods:
    """Class containing methods for making API calls"""

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"

    @property
    def endpoint(self):
        return f"{BASE_URL}/{self.__class__.__name__.lower()}"

    @classmethod
    def serialize(cls, json):
        """
        Serializes a response into an object and returns a list of objects if multiple objects are present in the response
        """
        results = []
        for item in json:            
            item = cls(*item.values())
            results.append(item)
        return results[0] if len(results) == 1 else results

    @classmethod
    def get(cls, id=None):
        """
        Retrieves data from the API and returns the result of the query
        :param id (str): the unique identifier to query
        """
        url = f"{BASE_URL}/{cls.__name__.lower()}"
        url = f"{url}/{id}" if id else url
        resp = session.get(url)
        results = resp.json()["docs"] if "docs" in resp.json() else [resp.json()]
        result = cls.serialize(results)
        return result[0] if isinstance(result, list) and len(result) == 1 else result