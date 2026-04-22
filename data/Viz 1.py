# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = r"C:\Users\User\Downloads\02867112-7fbd-4bd3-8551-47f0e3f6d0c9_full_prediction.csv"
data = pd.read_csv(file_path)

# Sort the data by bankruptcy probability
sorted_data = data.sort_values(by='probability', ascending=False)

# Create the bar chart
plt.figure(figsize=(12, 8))
plt.barh(sorted_data['company'], sorted_data['probability'], color='skyblue')
plt.xlabel('Bankruptcy Probability')
plt.ylabel('Company')
plt.title('Bankruptcy Probability by Company')
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.show()
