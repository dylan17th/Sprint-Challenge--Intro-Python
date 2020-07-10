import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
  
    with open("cities.csv", "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            cities.append(City(row[0], row[3], row[4]))
        return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(f"City: {c.name}, Lat: {c.lat}, Lon:{c.lon}")

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
trying_to_find = True

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []
    with open("cities.csv", "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if float(row[3]) > lat1 and float(row[4]) > lon1 and float(row[3]) < lat2 and float(row[4]) < lon2:
                within.append(City(row[0], row[3], row[4]))
            else:
              pass



    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    return within

while trying_to_find: 
  lat_lon1 = input("[lat1min] [lon1min] [lat2max] [lon2max]: ")
  lat_lon_splitter = lat_lon1.split(" ")
  lat1 = int(lat_lon_splitter[0])
  lon1 = int(lat_lon_splitter[1])
  lat2 = int(lat_lon_splitter[2])
  lon2 = int(lat_lon_splitter[3])

  # try:
  if type(lat1) == int and type(lon1) == int and type(lat2) == int and type(lon2) == int:
      print("valid numbers and the right amount")
      cityreader_stretch(lat1,lon1,lat2,lon2, cities)

  elif len(lat_lon_splitter) == 1:
      print("need to put spaces between the numbers")
  # except ValueError: 
  #     print("you need to enter valid numbers")

  

