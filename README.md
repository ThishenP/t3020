
# T3020   Repo for ELEN3020

Name: Scott Hazelhurst, Thishen Packirisamy
Date: 7 June


# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.

E1 - off by one error does not include t1 when adding all values. I changed the starting parameter of the loop to be 1 due to the fact that Python indexes from zero.

E2 - program was including values that stayed the same from previous row to current as non-monotonic. I therefore removed the equals from the >= for E2.

E3 - loops through all values in curr_str while the other column (the last value), should not be take into account fo these fucntions. I added [0:9] in the loop in order to only take the first 9 values in a row (Tall-T8).

Not an error with datamunger but I could not run tests using discovery because when 
importing in test_datamunger it tries to run datamunger which looks for a argument in the terminal for the data file path
since the code is run using discovery the value pulled from the terminal would be the word discover and the program would fail
I therefore added a if statement to check if the program is being run as main or not and if not it would default the path to the data.csv file
