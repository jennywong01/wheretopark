import requests
import pandas as pd


def find_places(keyword):
    lat, lng = 47.6062, -122.3321
    api_key = "AIzaSyBRHz--MwYpTNPjYTRjAK5yXo-g7yZhDa0"
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    url = f"{base_url}&keyword={keyword}&location={lat}%2C{lng}&radius=16000&key={api_key}"

    response = requests.request("GET", url, headers={}, data={})
    df = pd.json_normalize(response.json(), record_path=['results'])
    df = df[['place_id', 'name', 'vicinity', 'geometry.location.lat', 'geometry.location.lng']]
    return df



