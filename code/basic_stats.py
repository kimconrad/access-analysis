-- Create basic_stats tables

SELECT * FROM avg_income

-- Percent Broadband
SELECT a.id,
	a.geographic_area_name,
	a.households,
	i.total,
	a.avg_household_income_dollars,
	i.less_10000_broadband,
	i._10000_19900_broadband,
	i._20000_34999_broadband,
	i._35000_49999_broadband,
	i._50000_74900_broadband, 
	i.greater_75000_broadband
INTO basic_draft
FROM avg_income as a
INNER JOIN income_internet as i
ON a.id = i.id;

ALTER TABLE basic_draft
ADD COLUMN broadband INT;

UPDATE basic_draft SET broadband = less_10000_broadband + _10000_19900_broadband + _20000_34999_broadband + _35000_49999_broadband + _50000_74900_broadband + greater_75000_broadband;

ALTER TABLE basic_draft
DROP COLUMN less_10000_broadband;
ALTER TABLE basic_draft
DROP COLUMN _10000_19900_broadband;
ALTER TABLE basic_draft
DROP COLUMN _20000_34999_broadband;
ALTER TABLE basic_draft
DROP COLUMN _35000_49999_broadband;
ALTER TABLE basic_draft
DROP COLUMN _50000_74900_broadband;
ALTER TABLE basic_draft
DROP COLUMN greater_75000_broadband;


ALTER TABLE basic_draft
ADD COLUMN perc_broadband REAL;

ALTER TABLE basic_draft
ALTER COLUMN total TYPE FLOAT;

UPDATE basic_draft SET perc_broadband = broadband / total * 100;

SELECT * FROM basic_draft;



-- Percent Desktop/Laptop
SELECT b.id,
	b.geographic_area_name,
	b.total,
	b. avg_household_income_dollars,
	b.broadband,
	b.perc_broadband,
	c.desktop_laptop
INTO basic_draft_1
FROM basic_draft as b
INNER JOIN comp_types as c
ON b.id = c.id;


ALTER TABLE basic_draft_1
ADD COLUMN perc_desktop_laptop FLOAT;

UPDATE basic_draft_1 SET perc_desktop_laptop = desktop_laptop / total * 100;

SELECT * FROM basic_draft_1;

-- Top Internet Access Type


-- Top Computer Type