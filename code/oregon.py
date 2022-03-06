-- Create a starter draft table that only grabs Oregon counties
SELECT id, county, state
INTO oregon_draft
FROM county_state
WHERE state = 'Oregon';

SELECT * FROM oregon_draft;


-- Join oregon_draft on comp_types, inner join on id, only keep total, desktop total
SELECT o.id,
	o.county,
	o.state,
	c.total,
	c.desktop_laptop
INTO oregon_draft_1
FROM oregon_draft as o
INNER JOIN comp_types as c
ON o.id = c.id;

SELECT * FROM oregon_draft_1;

-- Join oregon_draft on income_internet, inner join on id, only keep total, broadband total
SELECT o.id,
	o.county,
	o.state,
	o.total,
	o.desktop_laptop,
	i.less_10000_broadband,
	i._10000_19900_broadband,
	i._20000_34999_broadband,
	i._35000_49999_broadband,
	i._50000_74900_broadband, 
	i.greater_75000_broadband
INTO oregon_draft_2
FROM oregon_draft_1 as o
INNER JOIN income_internet as i
ON o.id = i.id;

ALTER TABLE oregon_draft_2
ADD COLUMN broadband INT;

UPDATE oregon_draft_2 SET broadband = less_10000_broadband + _10000_19900_broadband + _20000_34999_broadband + _35000_49999_broadband + _50000_74900_broadband + greater_75000_broadband

ALTER TABLE oregon_draft_2
DROP COLUMN less_10000_broadband;
ALTER TABLE oregon_draft_2
DROP COLUMN _10000_19900_broadband;
ALTER TABLE oregon_draft_2
DROP COLUMN _20000_34999_broadband;
ALTER TABLE oregon_draft_2
DROP COLUMN _35000_49999_broadband;
ALTER TABLE oregon_draft_2
DROP COLUMN _50000_74900_broadband;
ALTER TABLE oregon_draft_2
DROP COLUMN greater_75000_broadband;

SELECT * FROM oregon_draft_2;

-- Join oregon_draft on income_internet, inner join on id, only keep total, and income levels
-- SELECT o.id,
-- 	o.county,
-- 	o.state,
-- 	o.total,
-- 	o.desktop_laptop,
-- 	o.broadband,
-- 	i.less_10000_total,
-- 	i._10000_19900_total,
-- 	i._20000_34999_total,
-- 	i._35000_49999_total,
-- 	i._50000_74900_total, 
-- 	i.greater_75000_total
-- INTO oregon_draft_3
-- FROM oregon_draft_2 as o
-- INNER JOIN income_internet as i
-- ON o.id = i.id;

-- SELECT * FROM oregon_draft_3;

-- Join oregon_draft on avg_income, inner join on id, only keep avg_income
SELECT o.id,
	o.county,
	o.state,
	o.total,
	o.desktop_laptop,
	o.broadband,
	a.avg_household_income_dollars
INTO oregon_draft_3
FROM oregon_draft_2 as o
INNER JOIN avg_income as a
ON o.id = a.id;

SELECT * FROM oregon_draft_3;

-- Create a formula to determine percent of broadband users
ALTER TABLE oregon_draft_3
ADD COLUMN perc_broadband REAL;

ALTER TABLE oregon_draft_3
ALTER COLUMN total TYPE FLOAT;

UPDATE oregon_draft_3 SET perc_broadband = broadband / total * 100

-- Create a formula to determine percent of desktop users

ALTER TABLE oregon_draft_3
ADD COLUMN perc_desktop_laptop FLOAT;

UPDATE oregon_draft_3 SET perc_desktop_laptop = desktop_laptop / total * 100

SELECT * FROM oregon_draft_3;

-- Manually add rural/urban coding for each county

ALTER TABLE oregon_draft_3
ADD COLUMN rural_urban VARCHAR;

UPDATE oregon_draft_3 SET rural_urban = 'urban'
WHERE county = 'Yamhill County'
OR county = 'Polk County'
OR county = 'Benton County'
OR county = 'Lane County'
OR county = 'Jackson County'
OR county = 'Deschutes County'
OR county = 'Marion County'
OR county = 'Clackamas County'
OR county = 'Multnomah County'
OR county = 'Washington County';

UPDATE oregon_draft_3 SET rural_urban = 'rural'
WHERE county = 'Douglas County'
OR county = 'Josephine County'
OR county = 'Klamath County'
OR county = 'Linn County'
OR county = 'Umatilla County';

-- COMBINE ALL INTO FINAL TABLE
SELECT id, county, state, total AS total_households, avg_household_income_dollars, desktop_laptop, 
perc_desktop_laptop, broadband, perc_broadband, rural_urban
INTO oregon
FROM oregon_draft_3;

SELECT * FROM oregon;

DROP TABLE oregon_draft_3;

