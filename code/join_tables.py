-- Join comp_types and income_internet tables
SELECT 
	ct.total,
	ct.one_or_more,
	ct.desktop_laptop,
	ct.only_desktop_laptop,
	ct.smartphone,
	ct.only_smartphone,
	ct.tablet_portable,
	ct.only_tablet_portable,
	ct.other,
	ct.only_other,
	ct.no_computer,
	ii.less_10000_total,
	ii.less_10000_dialup,
	ii.less_10000_broadband,
	ii.less_10000_none,
	ii._10000_19900_total,
	ii._10000_19900_dialup,
	ii._10000_19900_broadband,
	ii._10000_19900_none,
	ii._20000_34999_total,
	ii._20000_34999_dialup,
	ii._20000_34999_broadband,
	ii._20000_34999_none,
	ii._35000_49999_total,
	ii._35000_49999_dialup,
	ii._35000_49999_broadband,
	ii._35000_49999_none,
	ii._50000_74900_total,
	ii._50000_74900_dialup,
	ii._50000_74900_broadband,
	ii._50000_74900_none,
	ii.greater_75000_total,
	ii.greater_75000_dialup,
	ii.greater_75000_broadband,
	ii.greater_75000_none,
	ct.id,
	ct.geographic_area_name
INTO inc_int_comp
FROM comp_types as ct
LEFT JOIN income_internet as ii
ON ct.id = ii.id;

SELECT * FROM inc_int_comp;