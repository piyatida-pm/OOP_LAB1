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

# # Print the average temperature of all the cities
# print("The average temperature of all the cities:")
# temps = []
# for city in cities:
#     temps.append(float(city['temperature']))
# print(sum(temps)/len(temps))
# print()

# # Print the average temperature of all the cities
# print("The average temperature of all the cities:")
# temps = [float(city['temperature']) for city in cities]
# print(sum(temps)/len(temps))
# print()

# # Print all cities in Germany

# print("All cities in Germany:")
# all_city = []
# for city in cities:
#     if city["country"] == "Germany":
#         all_city.append(city["city"])
# print(all_city)
# print()

# # Print all cities in Spain with a temperature above 12°C

# print("All cities in Spain with a temperature above 12°C")
# all_city = []
# for city in cities:
#     if city["country"] == "Spain" and float(city["temperature"]) > 12:
#         all_city.append(city["city"])
# print(all_city)
# print()

# # Count the number of unique countries

# print("Number of unique countries:")
# all_city = []
# for city in cities:
#     if city["country"] not in all_city:
#         all_city.append(city["country"])
# print(len(all_city))
# print()

# # Print the average temperature for all the cities in Germany

# print("The average temperature of all the cities in Germany:")
# all_city = []
# for city in cities:
#     if city["country"] == "Germany":
#         all_city.append(float(city["temperature"]))
# print(sum(all_city) / len(all_city))
# print()

# # Print the max temperature for all the cities in Italy

# print("The max temperature for all the cities in Italy:")
# all_city = []
# for city in cities:
#     if city["country"] == "Italy":
#         all_city.append(float(city["temperature"]))
# print(max(all_city))
# print()

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)
    
# Print the average temperature of all the cities
my_value = aggregate('temperature', lambda x: sum(x)/len(x), cities)
print(my_value)
print()

# Print all cities in Germany
my_cities = filter(lambda x: x['country'] == 'Germany', cities)
cities_list = [[city['city'], city['country']] for city in my_cities]
print("All the cities in Germany:")
for city in cities_list:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
my_cities = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0, cities)
cities_list = [[city['city'], city  ['country'], city['temperature']] for city in my_cities]
print("All the cities in Spain with temperature above 12°C:")
for city in cities_list:
    print(city)
print()

# Count the number of unique countries
my_value = aggregate('country', lambda x: len(set(x)), cities)
print("The number of unique countries is:")
print(my_value)
print()

# Print the average temperature for all the cities in Germany
my_value = aggregate('temperature', lambda x: sum(x)/len(x), filter(lambda x: x['country'] == 'Germany', cities))
print("The average temperature of all the cities in Germany:")
print(my_value)
print()

# Print the max temperature for all the cities in Italy
my_value = aggregate('temperature', lambda x: max(x), filter(lambda x: x['country'] == 'Italy', cities))
print("The max temperature of all the cities in Italy:")
print(my_value)
print()