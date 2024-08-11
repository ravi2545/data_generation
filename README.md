# data_generation
Python data science project
===============================================
Steps to Build and Run the Docker Image:
```````````````````````````````````````````````
  Place the Dockerfile in the same directory as your Python script.

  Build the Docker image by running the following command in your terminal (inside the directory containing the Dockerfile):
    ``docker build -t your_docker_image_name .``

  Run the Docker container with your script by passing the CSV file name and table name as arguments:

    ``docker run --rm your_docker_image_name csv_file.csv table_name``