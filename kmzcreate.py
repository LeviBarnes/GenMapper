import simplekml

colordict = {
"Red": "FF0000FF",
"Yellow" : "FF00FFFF" ,
"Blue" : "FFFF0000" ,
"Green" : "FF00FF00" ,
"Purple" : "FF800080" ,
"Orange" : "FF0080FF" ,
"Brown" : "FF336699" ,
"Pink" : "FFFF00FF"}

def create_kmz_file(data):
    kml = simplekml.Kml()

    for item in data:
        name = item['name']
        location = item['location']
        color = item['color']
        begin = item['begin']
        end = item['end']

        placemark = kml.newpoint(name=name, coords=[(location[1], location[0])])
        placemark.style.iconstyle.color = simplekml.Color.hex(color)
        placemark.timespan.begin = begin
        placemark.timespan.end = end

    kmz_file = 'output.kmz'
    kml.savekmz(kmz_file)
    print(f'KMZ file "{kmz_file}" created successfully.')

# Example usage
if __name__ == "__main__":
   data = [
    {'name': 'Location 1', 'location': (40.7128, -74.0060), 'color': colordict["Red"], 'begin': '1975-06-19', 'end': '1999-08-14'},  # New York
    {'name': 'Location 2', 'location': (51.5074, -0.1278), 'color': 'FFFF0000', 'begin': '1980-01-01', 'end': '2013-11-09'}, # London
    {'name': 'Location 3', 'location': (35.6895, 139.6917), 'color': 'FF00FF00', 'begin': '1965-03-24', 'end': '1979-03-12'},  # Tokyo
   ]

   create_kmz_file(data)
