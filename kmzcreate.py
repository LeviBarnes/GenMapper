import simplekml

def create_kmz_file(data):
    kml = simplekml.Kml()

    for item in data:
        name = item['name']
        location = item['location']
        color = item['color']

        placemark = kml.newpoint(name=name, coords=[(location[1], location[0])])
        placemark.style.iconstyle.color = simplekml.Color.hex(color)

    kmz_file = 'output.kmz'
    kml.savekmz(kmz_file)
    print(f'KMZ file "{kmz_file}" created successfully.')

# Example usage
if __name__ == "__main__":
   data = [
    {'name': 'Location 1', 'location': (40.7128, -74.0060), 'color': 'FF0000FF'},  # New York
    {'name': 'Location 2', 'location': (51.5074, -0.1278), 'color': 'FFFF0000'},  # London
    {'name': 'Location 3', 'location': (35.6895, 139.6917), 'color': 'FF00FF00'},  # Tokyo
   ]

   create_kmz_file(data)
