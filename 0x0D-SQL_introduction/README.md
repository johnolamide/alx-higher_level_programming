# 0x0D SQL Introduction

## Task 0
- [x] `0-list_databases.sql`
> Write a script that lists all databases of your MySQL server

## Task 1
- [x] `1-create_database_if_missing.sql`
> Write a script that creates the database `hbtn_0c_0` in your MySQL server.
> - If the database `hbtn_0c_0` already exists, your script should not fail
> - You are not allowed to use the `SELECT` or `SHOW` statements

## Task 2
- [x] `2-remove_database.sql`
> Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
> - If the database `hbtn_0c_0` doesn’t exist, your script should not fail
> - You are not allowed to use the `SELECT` or `SHOW` statements

## Task 3
- [x] `3-list_tables.sql`
> Write a script that lists all the tables of a database in your MySQL server.
> - The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

## Task 4
- [x] `4-first_table.sql`
> Write a script that creates a table called `first_table` in the current database in your MySQL server.
> `first_table` description:
> - id `INT`
> - name `VARCHAR(256)`
> - The database name will be passed as an argument of the `mysql` command
> If the table `first_table` already exists, your script should not fail

## Task 5
- [x] `5-full_table.sql`
> Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
> - The database name will be passed as an argument of the mysql command

## Task 6
- [x] `6-list_values.sql`
> Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

## Task 7
- [x] `7-insert_values.sql`
> Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
> - New row:
> - id = 89
> - name = Best School

## Task 8
- [x] `8-count_89.sql`
> Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

## Task 9
- [x] `9-full_creation.sql`
> Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
> `second_table` description:
> - id INT
> - name VARCHAR(256)
> - score INT
> The database name will be passed as an argument to the mysql command
> If the table `second_table` already exists, your script should not fail
> Your script should create these records:
> - id = 1, name = “John”, score = 10
> - id = 2, name = “Alex”, score = 3
> - id = 3, name = “Bob”, score = 14
> - id = 4, name = “George”, score = 8

## Task 10
- [x] `10-top_score.sql`
> Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

## Task 11
- [x] `11-best_score.sql`
> Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

## Task 12
- [x] `12-no_cheating.sql`
> Write a script that updates the score of Bob to `10` in the table `second_table`.

## Task 13
- [x] `13-change_class.sql`
> Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

## Task 14
- [x] `14-average.sql`
> Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
> - The result column name should be `average`

## Task 15
- [x] `15-groups.sql`
> Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
> The result should display:
> - the `score`
> - the number of records for this `score` with the label `number`

## Task 16
- [x] `16-no_link.sql`
> Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
> - Don’t list rows without a `name` value
> - Results should display the score and the name (in this order)
> - Records should be listed by descending score
i
