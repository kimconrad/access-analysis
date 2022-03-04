SELECT id, 
	split_part(geographic_area_name, ', ', 1) AS County,
	split_part(geographic_area_name, ', ', 2) AS State
	INTO county_state
	FROM comp_types;
	
	
	
SELECT geographic_area_name FROM comp_types;

SELECT * FROM county_state;