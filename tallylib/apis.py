
import requests

def get_reviews_api(business_id):
    API_KEY = '-Io9W4bQSEfc3BxAwTvOV3B-aU9oS5j0F7LB7mWTXA79cRlMEmJzI7b_xIlqzSZd4b6IHiOlfp5APBsWNJt8cQRTV61u-r7DTKBCy1QTt91H9jjNjAEi0P6pjCTwXXYx'
    HEADERS = {'Authorization': f'Bearer {API_KEY}'}
    BUSINESS_ID = business_id
    URL = f'https://api.yelp.com/v3/businesses/{BUSINESS_ID}/reviews'

    req = requests.get(URL, headers=HEADERS)
    parsed = json.loads(req.text)
    reviews = parsed['reviews']
    reviews_json = []
    for review in reviews:
        output = {'id': review['id'], 'time': review['time_created'], 'text': review['text'], 'rating': review['rating']}
        reviews_json.append(output)