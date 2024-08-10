-- create schema
create schema data_extraction;

-- Create table in a schema
create table data_extraction.store_random_data (column1 int, column2 real, column3 varchar);

-- Show table structure a single table
SELECT * FROM information_schema.columns WHERE table_name = 'store_random_data';

-- Select store_random_data data 
SELECT * FROM data_extraction.store_random_data

-- create bike specification