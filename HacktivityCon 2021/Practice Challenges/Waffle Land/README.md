# Waffle Land | Web

*We got hacked, but our waffles are now safe after we mitigated the vulnerability.*

There appears to be only to main functionalities to this webpage, searching using the search bar or signing in using a username and a password, as we don't have any credentials let's try to fiddle with the search option.

The search option returns only the waffles that has the search parameter in them, trying to insert the character `'` gives an error:

```
Bad Request

(sqlite3.OperationalError) unrecognized token "'"
[SQL: select * from product where name like '%'%']
(Background on this error at: http://sqlalche.me/e/13/e3q8)
```

This gives us information about two things.  Firstly, we know that the search option uses SQL to filter data, SQL is a language designed for managing and querying databases (with SQL it is common to think of databases as tables with rows of data and columns of attributes).  In this case, an SQL query is used to sellect all the products with a value in the name attribute similar to the input given.

Secondly, we know that the web server uses SQLite3 management system.  This has someinfluence on the version of SQL and on the operations we can use or exploit.

A common attack against SQL is SQL injection (SQLi).  Computers cannot differentiate between data and commands and as such it is sometimes possible to inject commands where data is requested, for example we can search for `' limit 1 -- -` and this will cause the SQL management system to execute the following (if it is vulnerable to SQLi):

```
select * from product where name like '' limit 1
```

This query should return the first row of data in the `product` table.  To prevent this attack, there are mechanisms put in place to filter/sanitise the input given, for example a Web Application Firewall (WAF).  This type of system monitors the HTTP traffic of a web server and prevents attacks such as SQLi by blocking traffic.

Trying to access the `users` table with `' union select 1,2,3,4,5 -- -` reveals that we are up against a WAF.  To filter this I used `/**/union/**/select`.  The `/**` symbol signifies the start of a comment and `*/` signifies the end of a comment.  This gives us the following:

```
2
$4
3
```

So now we have a way to add data to the output, we still need to get data about the users so we need to know the name of table which stores users data and the attributes of the table, checking if we can select data from a table named `users` by using `'/**/union/**/select 1,2,3,4,5 from users -- -` gives us an error but by checking for `user` seems to work so we can guess there is a table named `user` in the database, we need to get usernames and passwords from this table, I discovered through trial and error that there attributes named `password` and `username` so we can search for the following to get the data we need from this table:

```
' and 0=1/**/union/**/select/**/1,username,password,4,5 from user -- -
```

The query will be:

```
select * from product where name like '' and 0=1/**/union/**select/**/1,username,password,4,5 from user -- -
```

this will first select the data from the product table and filter only the data that satisfy the condition `0=1`, so the query will filter all the data from the product table, then it adds the data in the username and the password columns of the table user and uses number 1,4 and 5 to pad the data so we can use union, from the search we get the password and the username for admin:

```
admin
$4
NT7b#ed4$J?eZ#m_
```

We can now login and retrieve the flag:

```
Congratulations here is your flag: flag{check_your_WAF_rules}
```

```
flag{check_your_WAF_rules}
```