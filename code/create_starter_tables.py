-- Creating tables for access-analysis-heroku database and server
CREATE TABLE comp_types (
	total INT,
	one_or_more INT,
	desktop_laptop INT,
	only_desktop_laptop INT,
	smartphone INT,
	only_smartphone INT,
	tablet_portable INT,
	only_tablet_portable INT,
	other INT,
	only_other INT,
	no_computer INT,
	id INT,
	geographic_area_name VARCHAR,
	PRIMARY KEY (id),
	UNIQUE (geographic_area_name)
);

SELECT * FROM comp_types;


CREATE TABLE income_internet (
	total INT,
	less_10000_total INT,
	less_10000_dialup INT,
	less_10000_broadband INT,
	less_10000_none INT,
	_10000_19900_total INT,
	_10000_19900_dialup INT,
	_10000_19900_broadband INT,
	_10000_19900_none INT,
	_20000_34999_total INT,
	_20000_34999_dialup INT,
	_20000_34999_broadband INT,
	_20000_34999_none INT,
	_35000_49999_total INT,
	_35000_49999_dialup INT,
	_35000_49999_broadband INT,
	_35000_49999_none INT,
	_50000_74900_total INT,
	_50000_74900_dialup INT,
	_50000_74900_broadband INT,
	_50000_74900_none INT,
	greater_75000_total INT,
	greater_75000_dialup INT,
	greater_75000_broadband INT,
	greater_75000_none INT,
	id INT,
	geographic_area_name VARCHAR,
	FOREIGN KEY (id) REFERENCES comp_types (id),
	PRIMARY KEY (id)
);

SELECT * FROM income_internet;
