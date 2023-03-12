'''import modules'''
import requests
import pandas as pd


def find_places(keyword):
    """this function is used to search place by user input"""
    if not isinstance(keyword, str):
        raise TypeError("Input location is not string")
    if len(keyword)==0:
        raise ValueError("Empty input")
    lat, lng = 47.6062, -122.3321
    api_key = "AIzaSyBRHz--MwYpTNPjYTRjAK5yXo-g7yZhDa0"
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    url = f"{base_url}&keyword={keyword}&location={lat}%2C{lng}&radius=16000&key={api_key}"
    response = requests.request("GET", url, headers={}, data={}, timeout=30)
    # pylint: disable=invalid-name
    df = pd.json_normalize(response.json(), record_path=['results'])
    if df.shape[0]==0:
        raise KeyError("Invalid input")
        
    # pylint: disable=invalid-name
    df = df[['place_id', 'name', 'vicinity', 'geometry.location.lat', 'geometry.location.lng']]
    return df
