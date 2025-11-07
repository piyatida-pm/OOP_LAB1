# OOP Lab 1: CSV Data Processing

## Lab Overview  
This lab demonstrates how to use **Object-Oriented Programming (OOP)** in Python to handle and analyze data stored in CSV files.  

In this project, we create two main classes:  
- `DataLoader` — responsible for loading CSV files.  
- `Table` — allows filtering and aggregating data with custom conditions and functions.  

You will learn how to:  
- Read CSV data into Python.  
- Use OOP principles to make code modular and reusable.  
- Apply lambda functions for filtering and aggregation.  

**Example of `Cities.csv`:**
```csv
city,country,temperature
Berlin,Germany,13.5
Madrid,Spain,15.2
Rome,Italy,18.4
Munich,Germany,11.9
Barcelona,Spain,14.8
 
```

---

## Project Structure


This is the structure of this project

- **`oop_lab_1/`**: Contains every file for this program
    - **`README.md`**: # This file
    - **`Cities.csv`**: # The dataset
    - **`data_processing.py`**: # The analysis code


# Design Overview
## Class: DataLoader

This class is responsible for reading CSV data from the specified directory.

### Attributes:

base_path: The base folder path where data files are located.

### Methods:

__init__(base_path=None): Initializes the loader. If no path is given, it uses the current file’s directory.

load_csv(filename): Loads the specified CSV file and returns a list of dictionaries (each representing a row).

## Class: Table

### **Overview**
The `Table` class represents a dataset (table) and provides methods for **filtering** and **aggregating** data.  
It stores the table’s data as a list of dictionaries, making it easy to apply conditions and summary functions dynamically.

---

### **Attributes**
| Attribute | Type | Description |
|------------|------|-------------|
| `name` | `str` | Name of the table (e.g., `"cities"`) |
| `table` | `list[dict]` | List of dictionaries where each item represents a row of the dataset |

---

### **Methods**

####  `__init__(self, cities, city_table)`
**Purpose:**  
Initializes a new instance of the `Table` class.

**Parameters:**  
- `cities` *(str)* – Name of the table.  
- `city_table` *(list)* – Data loaded from CSV (list of dictionaries).

**Example:**
```python
my_table = Table("cities", cities_data)


##  How to Use

To run the demonstration script, execute `data_processing.py` from your terminal:

```bash
python data_processing.py