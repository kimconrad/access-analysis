-- Creating cleaner tables for access-analysis-db

-- ID & Geographic Area Name Dictionary
SELECT id, geographic_area_name
INTO id_dict
FROM total_pop;

SELECT * FROM id_dict;

-- Cleaner total_pop
SELECT id, total
INTO cleaner_total_pop
FROM total_pop;

SELECT * FROM cleaner_total_pop;

-- Cleaner int_access
SELECT id, total, computer_dialup, computer_broadband, computer_no_internet
INTO cleaner_int_access
FROM int_access;

ALTER TABLE cleaner_int_access
RENAME COLUMN computer_dialup TO dialup;
ALTER TABLE cleaner_int_access
RENAME COLUMN computer_broadband TO broadband;
ALTER TABLE cleaner_int_access
RENAME COLUMN computer_no_internet TO no_internet;

SELECT * FROM cleaner_int_access;

-- Cleaner income
SELECT id, total, i_under_050, i_050_074, i_075_099, i_100_124, i_125_149, i_150_174, i_175_184, i_185_199, i_200_299, i_300_399, i_400_499, i_500_over
INTO cleaner_income
FROM income;

SELECT * FROM cleaner_income;
