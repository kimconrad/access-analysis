SELECT 
	total,
	less_10000_total, less_10000_internet, less_10000_none,
	_10000_19900_total, _10000_19900_internet, _10000_19900_none,
	_20000_34999_total, _20000_34999_internet, _20000_34999_none,
	_35000_49999_total, _35000_49999_internet, _35000_49999_none,
	_50000_74900_total, _50000_74900_internet, _50000_74900_none,
	greater_75000_total, greater_75000_internet, greater_75000_none,
	id,
	geographic_area_name
INTO inc_int_no_int
FROM income_int_no_int;

SELECT * FROM inc_int_no_int;

DROP TABLE income_int_no_int;