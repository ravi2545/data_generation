-- create schema
create schema data_extraction;

-- Create table in a schema
create table data_extraction.store_random_data (column1 int, column2 real, column3 varchar);

-- Show table structure a single table
SELECT * FROM information_schema.columns WHERE table_name = 'store_random_data';

-- Select store_random_data data 
SELECT * FROM data_extraction.store_random_data

-- create bike specifications
create table data_extraction.bike_specifications(Brand varchar(20), Model varchar(20), BikeType varchar(20), FrameSize varchar(20), Weight varchar(20), Price varchar(20));

-- IPL team data
create table data_extraction.ipl_players_data(Team varchar(50), Player Varchar(50), Age int, Jersey_number int, Country varchar(20), Price varchar(20))