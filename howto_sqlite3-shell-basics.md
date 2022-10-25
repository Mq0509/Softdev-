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
