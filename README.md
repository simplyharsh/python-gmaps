Just import API endpoint of your choice and start querying:

```python
from gmaps import Geocoding
api = Geocoding()

api.geocode("somwhere")
api.reverse(51.123, 21.123)

from gmaps import Place
place_api = Place(api_key='your_secret_api_key`)

results = place_api.textsearch('dublin') # can return multiple results
```

If you need to use Google Maps API for Business then instantiate your endpoint
with `api_key` param

```python
from gmaps import Geocoding
api = Geocoding(api_key='your_secret_api_key`)
```

Each endpoint method raises adequate exception when status of query is different
than `OK`. It also unpacks results list from Google API output dict so you have
one key less to access but it does nothing more.
So if Google geocoding api outputs something like:

```
{
    results: [
    ...
    ],
    status: 'OK'
}
```

You will get only get list that was inside `result` value. At least one element
returned is always assured, otherwise `gmnaps.errors.NoResults` exception is
raised.

For each API endpoint you can specify:
* default `sensor` value
* protocol (http/https)
* api key (only for http)

Available endpoints:
* `Geocoding()`
* `Directions()`
* `Timezone()`
* `Place()`
