# Nädal 2 – kalju individuaalne töö

## Ülesanne
-Customers tabel analyzes and cleaning.

## Mida tegin
-1) Created a temporary table to work on. To make sure orginal files are safe.
-2) Created a codes that found out duplicate emails and empty emails and NULL emails.
-3) Different codes give different type of output. Some give full table as output but added there a extra columns that show emails occurance. Other give result type output table that shows exactly what type of email problems. 

What i learned
-1) FILTER vs CASE (IF type of functions, they have their differences one acts like more complete analyzing tool while other is more optimized for result presentation and selection). Learned that there are functions (CASE) that need END keyword/function.
-2) GROUP BY vs PARTITION BY (GROUP BY removes rows while it groups PARTITION BY does not). Meaning PARTITION BY is safer while you do data analyze because it keeps data seen while analyzing. That helps to notice logic errors and other problems.
-3) CREATE TABLE (Creates a table)
-4) LIKE (Gives table exactly same data types as orginal table makes sure its as similar as possible)
-5) INSERT INTO (Copies data from orginal table)
-6) WITH I learned that you use one WITH block for multiple CTEs. 
-7) CROSS JOIN I learned how cross join works. It produces table that is multiplication of two input tabels in size. Because it adds to table A each row Table B rows. But it does not change inside values of tabels.
-8) Learned that in from line its common to name some tabels shorter to make in the end selection shorter. For example FROM summary s is same as FROM summary AS s. And in the select then you dont need to write summary.email but just s.emails.

## SQL päringud / failid
_Lisa lingid_
