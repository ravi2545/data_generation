class TablesNames:
    store_random_data = 'data_extraction.store_random_data'
    bike_specifications = 'data_extraction.bike_specifications'

    to_tables = {
        store_random_data: "data_extraction.store_random_data",
        bike_specifications: "data_extraction.bike_specifications"
    }

    to_colums = {
        "data_extraction.store_random_data": ['column1', 'column2', 'column3'],
        "data_extraction.bike_specifications": ['Brand', 'Model', 'BikeType', 'FrameSize', 'Weight', 'Price']
    }

