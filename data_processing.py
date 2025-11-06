


import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All cities in Germany:")
all_city = []
for city in cities:
    if city["country"] == "Germany":
        all_city.append(city["city"])
print(all_city)
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C")
all_city = []
for city in cities:
    if city["country"] == "Spain" and float(city["temperature"]) > 12:
        all_city.append(city["city"])
print(all_city)
print()

# Count the number of unique countries

print("Number of unique countries:")
all_city = []
for city in cities:
    if city["country"] not in all_city:
        all_city.append(city["country"])
print(len(all_city))
print()

# Print the average temperature for all the cities in Germany

print("The average temperature of all the cities in Germany:")
all_city = []
for city in cities:
    if city["country"] == "Germany":
        all_city.append(float(city["temperature"]))
print(sum(all_city) / len(all_city))
print()

# Print the max temperature for all the cities in Italy

print("The max temperature for all the cities in Italy:")
all_city = []
for city in cities:
    if city["country"] == "Italy":
        all_city.append(float(city["temperature"]))
print(max(all_city))
print()

