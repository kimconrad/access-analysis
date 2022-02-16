-- Creating tables for access-analysis-db
CREATE TABLE total_pop (
	total INT,
	id INT NOT NULL,
	geographic_area_name VARCHAR NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (geographic_area_name)
);

CREATE TABLE int_access (
	total INT,
	has_computer INT,
	computer_dialup INT,
	computer_broadband INT,
	computer_no_internet INT,
	no_computer INT,
	id INT NOT NULL,
	geographic_area_name VARCHAR,
	FOREIGN KEY (id) REFERENCES total_pop (id),
	PRIMARY KEY (id)
);

CREATE TABLE income (
	total INT,
	i_under_050 INT,
	i_050_074 INT,
	i_075_099 INT,
	i_100_124 INT,
	i_125_149 INT,
	i_150_174 INT,
	i_175_199 INT,
	i_200_224 INT,
	i_225_249 INT,
	i_250_274 INT,
	i_275_299 INT,
	i_300_324 INT,
	i_325_349 INT,
	i_350_374 INT,
	i_375_399 INT,
	i_400_424 INT,
	i_425_449 INT,
	i_450_474 INT,
	i_475_499 INT,
	i_500_over INT,
	id INT NOT NULL,
	geographic_area_name VARCHAR,
	FOREIGN KEY (id) REFERENCES total_pop (id),
	PRIMARY KEY (id)
);

-- Confirmation that tables were created correctly
SELECT * FROM income;
SELECT * FROM total_pop;
SELECT * FROM int_access;