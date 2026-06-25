SELECT COUNT (*) - COUNT (first_name) AS "Puuduvad_eesnimed",
         COUNT (*) - COUNT (last_name) AS "Puuduvad_perekonnanimed",
         COUNT (*) - COUNT (email) AS "Puuduvad_emailid"
FROM "Customers";
