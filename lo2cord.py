import googlemaps

def geocode(address):
    api_key = 'AIzaSyCr1LGi2eQlyAaS_Il7rqRpbAI7dWSDYOY'  # Replace with your actual API key
    gmaps = googlemaps.Client(key=api_key)
    
    # Geocoding request
    geocode_result = gmaps.geocode(address)
    
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None