#### DEM PUMPKINS: Emily Ortiz, Diana Akhmedova, May Qiu
#### SoftDev
#### K17 -- Shell Game
#### 2022-10-24
#### time spent: 1 hour

#### QCC
* We accidently input a text instead of a number in a field we assigned as numbers. 
However, no error occured. We are confused to why there are no consequences of doing 
so. Are the datatypes simply for organization purposes?

* To create a new SQLite database, we do:
```sqlite3 nameOfDatabase```
* After doing so, the next line should say 
``` sqlite>```
* To create a table, we do
```create table nameOfTable(columnName datatype, columnName datetype...);```

* To populate this table:
``` insert into nameOfTablE values(input,input...);```

* We can terminate the sqlite3 by entering Control + D
* Semicolons are important, without semicolons, the sqlite3 program will ask you to finish that command.

* To show all the fields in a table, we do:
``` SELECT * FROM nameOfTable```

* For one field, we do:
``` Select fieldName FROM tableName```

* To filter results we can do:
```Select name FROM tableName WHERE id = value```
