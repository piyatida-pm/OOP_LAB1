import csv, os
from pathlib import Path

class DataLoader:    
    """Handles loading CSV data files."""
        
    def __init__(self, base_path=None):        
        """Initialize the DataLoader with a base path for data files."""
        if base_path is None:            
            # Resolve the path to the directory containing this file
            self.base_path = Path(__file__).parent.resolve()        
        else:            
            self.base_path = Path(base_path)        
            
    def load_csv(self, filename):        
        """Load a CSV file and return its contents as a list of dictionaries."""
        filepath = self.base_path / filename
        data = []                
        with filepath.open(encoding='utf-8') as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))                
        return data

class DB:
    """A simple database class where tables can be inserted and searched for."""
    
    def __init__(self):
        """Initializes the database with an empty dictionary to hold Table objects."""
        # Use a dictionary to store tables: {table_name: Table_object}
        self.tables = {}

    def insert(self, table_obj):
        """Inserts a Table object into the database."""
        # Use the table's name attribute as the key
        self.tables[table_obj.table_name] = table_obj

    def search(self, table_name):
        """Searches for and returns a Table object by its name."""
        return self.tables.get(table_name)
    
class Table:
    """Represents a data table (a list of dictionaries)."""
    
    def __init__(self, table_name, table_data):
        """Initialize the Table with a name and data (list of dicts)."""
        self.table_name = table_name
        self.table = table_data
    
    def get_data(self):
        """Returns the raw table data."""
        return self.table

    def filter(self, condition):
        """
        Filters the table data based on a given lambda condition.
        Returns a new Table object with the filtered data.
        """
        filtered_data = [row for row in self.table if condition(row)]
        return Table(self.table_name + '_filtered', filtered_data)

    def aggregate(self, func, attribute):
        """
        Performs an aggregation function (func) on a specific attribute.
        Attempts to convert data to float for numerical attributes.
        """
        data_to_aggregate = []
        for row in self.table:
            
            try:
                data_to_aggregate.append(float(row[attribute]))
            except (ValueError, KeyError):
                
                data_to_aggregate.append(row.get(attribute))
        

        return func(data_to_aggregate)

    def join(self, other_table, common_key):
        """
        Performs an inner join with another Table object on a common_key.
        Returns a new Table object containing the merged data.
        """
        joined_data = []
        other_data = other_table.get_data()
        
       
        for row1 in self.table:
            for row2 in other_data:
                # Check for the join condition
                if row1.get(common_key) == row2.get(common_key):
                    
                    merged_row = {**row1, **row2}
                    joined_data.append(merged_row)
                    
        new_name = f"{self.table_name}_{other_table.table_name}_joined"
        # Return a new Table object
        return Table(new_name, joined_data)

    def __str__(self):
        # Adjusted for the required output format in the test
        if self.table_name.endswith('_filtered'):
             return self.table_name + ':' + str(self.table)
        else:
            return self.table_name


loader = DataLoader()

cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)

countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")

print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")

my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()