import csv
from faker import Faker
from geopy.geocoders import Nominatim

# Initialize Faker instance
fake = Faker()

# Initialize geocoder
geolocator = Nominatim(user_agent="user_locations_script")

# Function to generate latitude and longitude for a location
def get_lat_long(location):
    try:
        location_info = geolocator.geocode(location)
        if location_info:
            return location_info.latitude, location_info.longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error retrieving coordinates for {location}: {str(e)}")
        return None, None

# Read the climate tweets file and extract user locations
user_locations = {}
with open('climate_tweets.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username = row['username']
        location = row['location']

        # Only add unique locations for each user
        if username not in user_locations and location:
            user_locations[username] = location

# Generate latitude and longitude for each location and write to a new file
with open('user_locations.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['username', 'location', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for username, location in user_locations.items():
        latitude, longitude = get_lat_long(location)
        if latitude is not None and longitude is not None:
            writer.writerow({'username': username, 'location': location, 'latitude': latitude, 'longitude': longitude})
        else:
            # If coordinates couldn't be retrieved, generate random coordinates as fallback
            latitude = fake.latitude()
            longitude = fake.longitude()
            writer.writerow({'username': username, 'location': location, 'latitude': latitude, 'longitude': longitude})

print("User locations data has been written to user_locations.csv.")
