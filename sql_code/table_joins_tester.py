-- Join cleaner_income and cleaner_int_access tables
SELECT cit.id, cit.dialup, cit.broadband, cit.no_internet,
		ci.i_under_050, ci.i_050_074, ci.i_075_099, ci.i_100_124, 
		ci.i_125_149, ci.i_150_174, ci.i_175_184, ci.i_185_199, 
		ci.i_200_299, ci.i_300_399, ci.i_400_499, ci.i_500_over
INTO income_int_access
FROM cleaner_int_access as cit
LEFT JOIN cleaner_income as ci
ON cit.id = ci.id;

SELECT * FROM income_int_access;

-- JOIN income_int_access and cleaner_total_pop
SELECT iit.id, ctp.total, iit.dialup, iit.broadband, iit.no_internet,
		iit.i_under_050, iit.i_050_074, iit.i_075_099, iit.i_100_124, 
		iit.i_125_149, iit.i_150_174, iit.i_175_184, iit.i_185_199, 
		iit.i_200_299, iit.i_300_399, iit.i_400_499, iit.i_500_over
INTO income_int_access_pop
FROM income_int_access as iit
LEFT JOIN cleaner_total_pop as ctp
ON iit.id = ctp.id;

ALTER TABLE income_int_access_pop
RENAME COLUMN total TO total_population;

SELECT * FROM income_int_access_pop;