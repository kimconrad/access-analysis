-- Creating Statistics tables

-- Has or does not have a computer
SELECT id, total, has_computer, no_computer
INTO aux_computers
FROM int_access;

SELECT * FROM aux_computers;




-- Percentages of survey results compared to total population of each county
SELECT ctp.id, ctp.total AS "total (total_pop)", cia.total AS "total (int_access)", ci.total AS "total (income)"
INTO aux_perc_response
FROM cleaner_total_pop as ctp
LEFT JOIN cleaner_int_access as cia
ON ctp.id = cia.id
LEFT JOIN cleaner_income as ci
ON ctp.id = ci.id;

-- Change total (total_pop) to FLOAT data type, to avoid integer division
ALTER TABLE aux_perc_response
ALTER COLUMN "total (total_pop)" TYPE FLOAT;

-- Add empty column for perc_int_access
ALTER TABLE aux_perc_response
ADD COLUMN perc_int_access REAL;

-- Fill new column with Percent of Internet Access responses / Total Population for each county
UPDATE aux_perc_response SET perc_int_access = "total (int_access)"/"total (total_pop)" * 100;

ALTER TABLE aux_perc_response
ALTER COLUMN perc_int_access SET NOT NULL;

-- Repeat for Income Percentages
ALTER TABLE aux_perc_response
ADD COLUMN perc_income REAL;

UPDATE aux_perc_response SET perc_income = "total (income)"/"total (total_pop)" * 100;

ALTER TABLE aux_perc_response
ALTER COLUMN perc_income SET NOT NULL;

SELECT * FROM aux_perc_response;

