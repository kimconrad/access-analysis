-- Make a copy of income_internet table
SELECT * 
INTO income_int_no_int
FROM income_internet;

SELECT * FROM income_int_no_int;

-- Alter table to combine columns - ending with "has internet" vs "no internet" for each income bracket
ALTER TABLE income_int_no_int
ADD COLUMN less_10000_internet INT;

UPDATE income_int_no_int SET less_10000_internet = less_10000_dialup + less_10000_broadband;

-- Drop columns for dialup and broadband
ALTER TABLE income_int_no_int
DROP COLUMN less_10000_dialup;
ALTER TABLE income_int_no_int
DROP COLUMN less_10000_broadband;

SELECT * FROM income_int_no_int;


-- Alter table to combine columns - ending with "has internet" vs "no internet" for each income bracket
ALTER TABLE income_int_no_int
ADD COLUMN _10000_19900_internet INT;

UPDATE income_int_no_int SET _10000_19900_internet = _10000_19900_dialup + _10000_19900_broadband;

-- Drop columns for dialup and broadband
ALTER TABLE income_int_no_int
DROP COLUMN _10000_19900_dialup;
ALTER TABLE income_int_no_int
DROP COLUMN _10000_19900_broadband;

SELECT * FROM income_int_no_int;


-- Alter table to combine columns - ending with "has internet" vs "no internet" for each income bracket
ALTER TABLE income_int_no_int
ADD COLUMN _20000_34999_internet INT;

UPDATE income_int_no_int SET _20000_34999_internet = _20000_34999_dialup + _20000_34999_broadband;

-- Drop columns for dialup and broadband
ALTER TABLE income_int_no_int
DROP COLUMN _20000_34999_dialup;
ALTER TABLE income_int_no_int
DROP COLUMN _20000_34999_broadband;

SELECT * FROM income_int_no_int;


-- Alter table to combine columns - ending with "has internet" vs "no internet" for each income bracket
ALTER TABLE income_int_no_int
ADD COLUMN _35000_49999_internet INT;

UPDATE income_int_no_int SET _35000_49999_internet = _35000_49999_dialup + _35000_49999_broadband;

-- Drop columns for dialup and broadband
ALTER TABLE income_int_no_int
DROP COLUMN _35000_49999_dialup;
ALTER TABLE income_int_no_int
DROP COLUMN _35000_49999_broadband;

SELECT * FROM income_int_no_int;


-- Alter table to combine columns - ending with "has internet" vs "no internet" for each income bracket
ALTER TABLE income_int_no_int
ADD COLUMN _50000_74900_internet INT;

UPDATE income_int_no_int SET _50000_74900_internet = _50000_74900_dialup + _50000_74900_broadband;

-- Drop columns for dialup and broadband
ALTER TABLE income_int_no_int
DROP COLUMN _50000_74900_dialup;
ALTER TABLE income_int_no_int
DROP COLUMN _50000_74900_broadband;

SELECT * FROM income_int_no_int;


-- Alter table to combine columns - ending with "has internet" vs "no internet" for each income bracket
ALTER TABLE income_int_no_int
ADD COLUMN greater_75000_internet INT;

UPDATE income_int_no_int SET greater_75000_internet = greater_75000_dialup + greater_75000_broadband;

-- Drop columns for dialup and broadband
ALTER TABLE income_int_no_int
DROP COLUMN greater_75000_dialup;
ALTER TABLE income_int_no_int
DROP COLUMN greater_75000_broadband;

SELECT * FROM income_int_no_int;
