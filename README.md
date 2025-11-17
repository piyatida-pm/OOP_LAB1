# OOP Lab: Data Processing with Custom Database, Table, and CSV Loader

## Lab Overview
This lab focuses on building a lightweight data-processing framework in Python using Object-Oriented Programming principles.  
Students implement 3 core components:

1. **DataLoader** — Reads CSV files into Python dictionaries  
2. **Table** — Represents a dataset with filtering, aggregation, and joining capabilities  
3. **DB (Database)** — Stores and retrieves table objects  

The goal is to simulate how databases work internally while practicing class design, method creation, and data manipulation.


## Project Structure

OOP_LAB3

├── data_processing.py # Main implementation (DataLoader, DB, Table, tests).

├── Cities.csv # Input dataset 1

├── Countries.csv # Input dataset 2

└── README.md # Project documentation


- `Cities.csv` — Contains city name, country, and temperature  
- `Countries.csv` — Contains country name, EU membership, coastline info  

---

## Design Overview

### 1. **DataLoader**
Handles reading CSV files from the project directory.

**Attributes**
```
base_path : directory where CSV files are located
```

**Key Methods**
```
- load_csv(filename)
  - Opens a CSV file  
  - Converts each row into a dictionary  
  - Returns a list of dictionaries (table data)
  ```

---

### 2. **DB (Database)**
A simple database storing multiple `Table` objects.

**Attributes**
```
- `tables` : dictionary mapping table_name → Table object
```
**Key Methods**
```
- `insert(table_obj)`  
  Stores a Table inside the DB.

- `search(table_name)`  
  Returns a table by name (or `None` if not found)
```
---

### 3. **Table**
Represents a dataset (list of dicts) and provides data manipulation functions.

**Attributes**
```
- `table_name` : name of the dataset  
- `table` : actual list of dictionaries  
```
**Key Methods**
```
- get_data()
Returns raw data for use in joins or external processing.
```
```
filter(condition)
- Accepts a lambda expression  
- Returns a new Table containing rows that satisfy the condition  
- Example:  
  filtered = cities.filter(lambda x: x['country'] == 'Italy')
  filtered = cities.filter(lambda x: x['country'] == 'Italy')
```
```
aggregate(func, attribute)

- Performs an aggregation on a specific attribute
- Converts values to float when possible
- Works with: min, max, sum, len, averages, etc.
- Example:
  avg_temp = filtered.aggregate(lambda x: sum(x)/len(x),'temperature')
```
```
join(other_table, common_key)

Performs an inner join between two tables on a shared attribute
Combines dictionaries using {**row1, **row2}
Returns a new Table with merged data
```
### 4. **How to Test and Run the Code**

1.Make sure Cities.csv and Countries.csv are in the same folder as data_processing.py.

2.Run the script in your terminal:

```
python3 data_processing.py
```
3.The program will execute the following tests automatically:

- List all cities in Italy
- Calculate average temperature in Italy
- List all non-EU countries
- Count countries with coastlines
- Perform a join between cities and countries
- Filter cities by temperature and EU status
- Find min/max temperature of cities in non-coastline EU countries

### **example:**
```
List all cities in Italy:
- cities_filtered:[...]
Average temperature for all cities in Italy:
- 12.7
List all non-EU countries:
- countries_filtered:[...]
Number of countries that have coastline:
- 8
First 5 entries of the joined table:
- {...}
Cities whose temperatures are below 5.0 in non-EU countries:
- [...]

Min temp: ...
Max temp: ...
```
---
### 5.**Final Notes**

After completing the lab, commit all changes with a clear message, e.g.:

- git add .
- git commit -m "Completed OOP Lab 3 with DataLoader, Table, DB classes and README"
- git push
