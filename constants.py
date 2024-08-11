class TablesNames:
    store_random_data = 'data_extraction.store_random_data'
    bike_specifications = 'data_extraction.bike_specifications'
    ipl_players_data = 'data_extraction.ipl_players_data'

    to_tables = {
        store_random_data: "data_extraction.store_random_data",
        bike_specifications: "data_extraction.bike_specifications",
        ipl_players_data: "data_extraction.ipl_players_data"
    }

    to_colums = {
        "data_extraction.store_random_data": ['column1', 'column2', 'column3'],
        "data_extraction.bike_specifications": ['Brand', 'Model', 'BikeType', 'FrameSize', 'Weight', 'Price'],
        "data_extraction.ipl_players_data": ['Team', 'Player', 'Age', 'Jersey_number', 'Country', 'Price']
    }

