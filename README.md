This is a script that prints a mutliplication table of the first 10 primes. It uses
python 2.7. To run this script, simply run:
```
python mult_table.py
```
There are also tests for this script, to run the tests, run
```
python unit_test.py
```
Currently, this code runs in O(n**2) time, due to the fact that it loops through
the number passed to it squared. This time limitation could be removed by adding
Redis to the code. Using Redis, a lookup table of the primes could be stored
which would enable constant time lookup for primes.
