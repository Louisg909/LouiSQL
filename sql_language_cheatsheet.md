# Ideas
Candiate keys? Closane Algorithm?
 -> Inconsitancies

# Cheat sheet
## Querying tables
### Getting all columns from a table
```sql
SELECT *
FROM airbnb_listings;
```
### Reutrn `city` column from the table
```sql
SELECT city
FROM airbnb_listings;
```
### Get the `city` and `year_listed` columns from the table
```sql
SELECT city, year_listed
FROM airbnb_listings;
```
### Get the listing `id`, `city`, ordered by the `number_of_rooms` in ascending order
```sql
SELECT id, city
FROM airbnb_listings
ORDER BY number_of_rooms ASC;
```
## Filtering Data
### Get all the listings where `number_of_rooms` is more or equal to 3
```sql
SELECT *
FROM airbnb_listings
WHERE number_of_rooms >= 3;
```
> Works for all comparitive symbols
### Get all the listings with 3 to 6 rooms
```sql
SELECT *
FROM airbnb_listings
WHERE number_of_rooms BETWEEN 3 AND 6;
```
> Works for all logical operators
### Get all listings in 'Paris' where `number_of_rooms` is bigger than 3
```sql
SELECT *
FROM airbnb_listings
WHERE city = 'Paris' AND number_of_rooms > 3;
```
## Grouping, filtering, and sorting
### Filtering on missing data
```sql
SELECT *
FROM airbnb_listings
WHERE number_of_rooms IS NULL;
```

### Get total number of rooms for each country
```sql
SELECT country, SUM(number_of_rooms)
FROM airbnb_listings
GROUP BY country;
```
> Works for functions like SUM, AVG, MAX, MIN, COUNT etc etc - could even maybe have it for custom functions too right? If a function isn't a defualt one, can pass it as an argument as a lambda function or something??



# Desinging python functions to do everything needed
## Querying tables
### Rules:
Need to state what to select, and the table to select from

### Ideas:
Seems simple enough - could just have a function that can be called as:
```python
# Initialising database and adding table
db = LouiSQL.Database(...)
db.add_table(....)

db.pull(table='{table_name}', columns=['column_names'])
```
And it could return a psuedo-database containing only the columns given?

```python
class Database:
    ...
    def pull(table:str = None, columns:list[str] = None) -> sql.Table:
        # finds table
        table0 = self.tables[table]
        # get columns
        return table0.get_columns(columns)

class sql.Table:
    ...
    def get_columns(requested_columns):
        # Find each column type for the columns, and find the indexes of them
        pulled_columns = []
        indexes = []
        for i, column in enumerate(self.columns):
            if column.name in requiested_columns:
                pulled_columns.append(column)
                indexes.append(i)

        # Create temperary table with these columns
        temp_table = sql.Table(*pulled_columns)

        # Go through table's rows, adding to the temporary table tuples with the data from indexes saved above
        for row in self.data:
            temp_table.add(row[i] for i in indexes)

        # return the temporary table
        return temp_table
```
For the filtering and stuff - could use the same code (will rename the function) and have additinoal parameters





## Filtering data

## Aggregating data


# Interpreting SQL language



