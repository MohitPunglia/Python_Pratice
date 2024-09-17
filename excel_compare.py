import pandas as pd

# Load the Excel file
file_path = "filepath"
df = pd.read_excel(file_path)

# Fetch distinct values from column1 and column2
list1 = df['New'].tolist()
list2 = df['old'].tolist()

# Print the distinct values
#print("Distinct values in column1:", distinct_column1)
#print("Distinct values in column2:", distinct_column2)


def find_combined_distinct_values(list1, list2):
    # Convert lists to sets to find unique values
    set1 = set(list1)
    set2 = set(list2)
    
    # Find distinct values from both lists combined
    combined_distinct_values = set1.symmetric_difference(set2)
    
    return combined_distinct_values

# Example usage
#list1 = [1, 2, 3, 4, 5]
#list2 = [4, 5, 6, 7, 8]

distinct_values = find_combined_distinct_values(list1, list2)

print("Distinct values from both lists combined:", distinct_values)
