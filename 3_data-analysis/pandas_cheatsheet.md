# Pandas cheatsheet

## Loading files
```python
df = pd.read_csv() # reads a local or online csv and puts it in the variable 'df'
df = pd.read_excel() # reads an excel
df = pd.read_json() # reads a json
```

## Basics
```python
df.info() # information on the column names and non-zero values
df.shape # number of rows and columns
len(df) # returns the number of rows
```

## Slicing
```python
df.sample(3) # returns 3 sample rows from the data
df.head(3) # returns the first 3 rows of the data
df.tail(3) # guess :)
```

## Rows (index) & Columns
```python
df.columns # all the column names as a list
df["column"] # isolates the column from the dataset
df[["column", "column2"]] # isolates two or more columns from the dataset
```

## Unique values and Distributions

```python
# for categorical variables
df["column"].unique() # all the unique values of the column
df["column"].value_counts() # how often does a value occur

# for numeric variables
df.describe() # descriptive statistics for all numeric variables
df["column"].describe() # descriptive statistics for a single column
df.hist(column='column') # makes a histogram
```

## Filtering

```python
df.query("industry == 'chemicals'") # Filter rows where a string column matches a specific value
df.query("status != 'active'") # Filter rows where a string column is not a specific value

df.query("energy_intensity > 50") # Filter rows where a column value is greater than a threshold

# Filter using string operators
df.query("country.str.startswith('Ger')") # Filter countries that start with 'Ger'
df.query("country.str.contains('republic')") # Filter countries that contain the word 'republic'

# Filter rows with multiple conditions
df.query("country == 'Germany' and emissions < 1000") 
df.query("energy_cost > 1000 or emissions > 500")

# Use a variable inside the query
threshold = 200
df.query("energy_cost > @threshold") 
```

## Transforming
```python
# Example 1: Apply a Function to a Column
# Convert temperatures from Fahrenheit to Celsius
df = pd.DataFrame({'temperature_f': [32, 68, 104]})
df['temperature_c'] = df['temperature_f'].apply(lambda x: (x - 32) * 5.0 / 9.0)

print(df)
# Output:
#    temperature_f  temperature_c
# 0             32      0.000000
# 1             68     20.000000
# 2            104     40.000000

# Example 2: Apply a Function to Each Row
# Calculate BMI (Body Mass Index) based on weight and height
df = pd.DataFrame({'weight_kg': [70, 80], 'height_m': [1.75, 1.8]})
df['BMI'] = df.apply(lambda row: row['weight_kg'] / (row['height_m'] ** 2), axis=1)

print(df)
# Output:
#    weight_kg  height_m        BMI
# 0         70      1.75  22.857143
# 1         80      1.80  24.691358

# Example 3: Apply a Function with Conditional Logic
# Categorize numbers as 'Even' or 'Odd'
df = pd.DataFrame({'number': [1, 2, 3, 4, 5]})
df['category'] = df['number'].apply(lambda x: 'Even' if x % 2 == 0 else 'Odd')

print(df)
# Output:
#    number category
# 0       1     Odd
# 1       2    Even
# 2       3     Odd
# 3       4    Even
# 4       5     Odd
```

## Grouping
Examples of possibilities for grouping in pandas

### Grouping and sum calculation
```python
df.groupby('Category').sum()
```
Group by 'Category' and sum all numeric columns.

### Grouping and Mean Calculation:

```python
df.groupby('Department')['Salary'].mean()
```
Group by 'Department' and calculate the mean of 'Salary'.

### Grouping by Multiple Columns
```python
df.groupby(['Region', 'Department']).mean()
```
Group by 'Region' and 'Department', and calculate mean of all numeric columns.

### Grouping and Counting Unique Values

```python
df.groupby('Department')['EmployeeID'].nunique()
```
Group by 'Department' and count unique 'EmployeeID' values.

### Grouping with Aggregation

```python
df.groupby('Category').agg({'Price': 'mean', 'Quantity': 'sum'})
```
Group by 'Category', then calculate mean of 'Price' and sum of 'Quantity'.

### Grouping and Size

```python
df.groupby('Category').size()
```
Group by 'Category' and get the size of each group.

### Grouping and Descriptive Statistics

```python
df.groupby('Category')['Price'].describe()
```
Group by 'Category' and get descriptive statistics for 'Price'.

### Grouping with Custom Function

```python
df.groupby('Department')['Salary'].apply(lambda x: x.max() - x.min())
```

Group by 'Department' and calculate the salary range (max - min) in each department.

### Grouping by Date Components

```python

df.groupby(df['Date'].dt.year)['Sales'].sum()
```
Group by year of 'Date' and sum 'Sales'.

### Grouping and Filtering

```python
df.groupby('Category').filter(lambda x: x['Price'].mean() > 20)
```

Filter groups in 'Category' where average 'Price' is greater than 20.

### Grouping with Sorting

```python
df.groupby('Category')['Price'].mean().sort_values(ascending=False)
```

Group by 'Category', calculate the mean 'Price', and sort the results in descending order.

### Grouping and Getting the First Entry

```python
df.groupby('Department').first()
```
Group by 'Department' and return the first row of each group.

### Grouping and Sampling

```python
df.groupby('Category').apply(lambda x: x.sample(n=1))
```

Group by 'Category' and randomly sample one row from each group.

### Nested Grouping

```python
df.groupby(['Region', 'Department'])['Sales'].sum()
```

Group by both 'Region' and 'Department', then sum 'Sales'.

### Grouping by Index

```python
df.groupby(df.index.month)['Revenue'].sum()
```

Group by the month of the index (assuming it's a datetime index) and sum 'Revenue'.

### Cumulative Sum within Groups

```python
df.groupby('Category')['Sales'].cumsum()
```

Group by 'Category' and calculate the cumulative sum of 'Sales' within each category.


### Grouping with Multiple Aggregations

```python
df.groupby('Category').agg({'Price': ['mean', 'sum'], 'Quantity': 'max'})
```
Group by 'Category', calculate mean and sum of 'Price', and max of 'Quantity'.

### Grouping and Percentage Change

```python
df.groupby('Department')['EmployeeCount'].pct_change()
```

Group by 'Department' and calculate the percentage change of 'EmployeeCount'.
