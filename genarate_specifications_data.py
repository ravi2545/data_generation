import csv
import random
import os

def generate_bike_data(num_rows):
    """Generate synthetic bike specifications data."""
    brands = ['Giant', 'Trek', 'Specialized', 'Cannondale', 'Bianchi']
    models = ['ModelA', 'ModelB', 'ModelC', 'ModelD', 'ModelE']
    types = ['Mountain', 'Road', 'Hybrid', 'Electric', 'Cruiser']
    
    data = []
    for _ in range(num_rows):
        brand = random.choice(brands)
        model = random.choice(models)
        bike_type = random.choice(types)
        frame_size = f"{random.randint(14, 22)} inches"
        weight = f"{random.uniform(5.0, 15.0):.2f} kg"
        price = f"${random.uniform(300, 3000):.2f}"
        
        data.append([brand, model, bike_type, frame_size, weight, price])
    
    return data

def write_to_csv(file_path, data, columns):
    """Write data to a CSV file."""
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(columns)  # Write header
            writer.writerows(data)    # Write data rows
        print(f"Data written to {file_path}")
    except Exception as error:
        print("Error occured du to: {}".format(str(error)))

if __name__ == "__main__":
    # Define parameters
    file_path = 'bikes_data.csv'
    num_rows = 100000  # Number of rows to generate
    columns = ['Brand', 'Model', 'BikeType', 'FrameSize', 'Weight', 'Price']
    
    # Generate data
    data = generate_bike_data(num_rows)
    
    # Write data to CSV
    write_to_csv(file_path, data, columns)