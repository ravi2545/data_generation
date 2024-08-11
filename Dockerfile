# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# If you have a requirements.txt, uncomment the following line
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install the required Python packages
RUN pip install pandas psycopg2-binary

# Expose the port the app runs on, if applicable (e.g., for Flask apps)
# EXPOSE 8000

# Run the script when the container launches
ENTRYPOINT ["python", "main_file.py"]

# If you want to pass arguments dynamically, you can use CMD to specify them later
CMD ["csv_file.csv", "table_name"]
