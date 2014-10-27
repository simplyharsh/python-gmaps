# -*- coding: utf-8 -*-
from gmaps.client import Client

class Place(Client):

    def textsearch(self, query, location=None, radius=None, opennow=None,
                   language=None, types=None, sensor=None, zagatselected=None,
                   minprice=None, maxprice=None):
        """The Google Places API Text Search Service is a web service that returns information about a set of places based on a string — for example "pizza in New York" or "shoe stores near Ottawa". The service responds with a list of places matching the text string and any location bias that has been set. The search response will include a list of places, you can send a Place Details request for more information about any of the places in the response. For full details see
        `Google docs <https://developers.google.com/places/documentation/search#TextSearchRequests>`_.

        :param query: query string
        :param location: The latitude/longitude around which to retrieve place
            information.
        :param radius: Defines the distance (in meters) within which to bias
            place results
        :param opennow: Returns only those places that are open for business at
            the time the query is sent.
        :param language: The language code, indicating in which language the
            results should be returned, if possible
        :param types: Restricts the results to places matching at least
            one of the specified types. (type1|type2|etc)
        :param sensor: override default client sensor parameter
        :param zagatselected: Add this parameter to restrict your search to
            locations that are Zagat selected businesses.
        """
        parameters = dict(
            query=query,
            location=location,
            radius=radius,
            opennow=opennow,
            language=language,
            types=types,
            sensor=sensor,
            zagatselected=zagatselected,
        )
        return self._make_request("place/textsearch/", parameters, "results")
