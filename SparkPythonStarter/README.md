# Spark Python Starter Project

A simple Python project that reads in a local CSV file from "/tmp/people.txt". File should have 1 header line and 3 columns representing name, age, and department.

## File Example
```
Name,Age,Dept
Tim,36,Data Engineering
```

## Running The Example Program

From the project directory, eg, /home/tim/SparkPythonStarter:

```
spark-submit \
--master local[1] \
--num-executors 1 \
main.py
```
