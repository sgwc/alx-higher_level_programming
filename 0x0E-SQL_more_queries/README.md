# How To Manage MySQL Users And Databases From MySQL prompt
https://hostadvice.com/how-to/how-to-manage-mysql-users-and-databases-from-mysql-prompt/

This tutorial will show you how to manage your database and database user from the MySQL command line.

Before we start this tutorial, make sure you have installed the latest version of MySQL and MariaDB on your system. MySQL will be used as the root user to execute the appropriate commands.

To log into the MySQL command line, execute the command below and enter your username and root password.

$ mysql -u root -p

## Step 1 -

Creating a MySQL Database

Start by creating a new MySQL/MariaDB database. To do so, run the command below and replace the section  **database_name** with the database name you plan to create:

mysql> CREATE DATABASE database_name;

This will give you an output like the one below:

QueryOK, 1  rowaffected  (0.00sec)

In case there is an existing database, the error message below will appear:

ERROR 1007  (HY000): Can't createdatabase'database_name'; database exists

To ensure you don’t get this error even when you use the same name for your database, run the command below:

mysql> CREATE DATABASE IF NOT EXISTS database_name;

You should see the output below:

QueryOK, 1 rowaffected, 1  warning  (0.00sec)

In this case, the section Query Ok shows that the query was effected successfully. Then there is  _1 warning_ which means that your database is already in the system and no database was created.

## Step 2 -

Listing All MySQL Databases

To list all the databases on your MySQL/MariaDB server, run the command below:

mysql> SHOW DATABASES;

This will give you an output similar to this:

+--------------------+

| Database |

+--------------------+

| information_schema |

| database_name |

| mysql |

| performance_schema |

| sys |

+--------------------+

5 rows in  set  (0.00 sec)

From the output above, the following databases  **information_schema, mysql, performance_schema,** and  **sys** are created during the installation. They databases store information for the rest of the databases, users, system configuration, permissions, and other relevant data. The mentioned databases are important when installing MySQL.

## Step 3 -

Deleting A MySQL Database

If you want to delete a MySQL database, execute the command below:

mysql> DROP DATABASE database_name;

You should get the following output:

QueryOK, 0  rowsaffected  (0.00sec)

Any attempt to delete a non-existing database in the system will show an error message as shown below:

ERROR 1008  (HY000): Can'tdrop database 'database_name'; database doesn't exist

To ensure you don’t get this error, run the command below:

mysql> DROP DATABASE IF EXISTS database_name;

The output should look like this:

QueryOK, 0 rowsaffected, 1  warning  (0.00sec)

**Query OK** indicates that the query succeeded whereas  **1 warning** means the database is nonexistence.

## Step 4 -

Creating A New User Account In MySQL

A MySQL or MariaDB user account comprises two parts; the username and the hostname.

Execute the command below to create a new MariaDB or MySQL user account. replace the part _database_user can be replaced_ with your preferred username.

mysql> CREATE USER 'database_user'@'localhost' IDENTIFIED BY 'user_password';

In this command, the hostname is set to  **localhost** meaning that the user will find an easier connection to the MySQL server from the local host.

To grant another host(s) access, replace the value  **localhost** in the above command with the IP address for your remote machine or just use  _'%'_ for the host. This will grant the MySQL user account permission to connect easily from any host.

To avoid getting an error when creating a new user account which already exists in the database, execute the command below:

mysql> CREATE USER IF NOT EXISTS 'database_user'@'localhost' IDENTIFIED BY 'user_password';

The should give you an output like the one below:

QueryOK, 0 rowsaffected, 1  warning  (0.00sec)

## Step 5 -

Changing A Password For MySQL User Account

This topic has been covered comprehensively in our article  **[How to change my root MySQL password.](https://hostadvice.com/how-to/how-to-reset-a-mysql-root-password-on-ubuntu-18-04/)**

The plan to change a password for MySQL/MariaDB user account depends on the version of the server that is running on your virtual machine.

To find the version of your server, run the command below:

$ mysql --version

If your system is running on MySQL 5.7.6 or MariaDB 10.1.20 and newer versions for both, you can change the user password using the command below:

mysql> ALTER USER 'database_user'@'localhost' IDENTIFIED BY 'new_password';

For MySQL 5.7.5 or MariaDB 10.1.20 and older versions for both, use:

mysql> SET PASSWORD FOR  'database_user'@'localhost' = PASSWORD('new_password');

Both options will give you an output similar to the one below:

QueryOK, 0  rowsaffected  (0.00sec)

## Step 6 -

Listing All MySQL User Accounts

To list all MySQL/MariaDB user accounts, just execute the command below to query  _mysql.users_ table:

mysql> SELECT user, host FROM mysql.user;

You should see the output below. From the output, you can see a list of the default MySQL 5.7 server users that are running on an Ubuntu server. You will also see two other user accounts that were added previously,  _'database_user'@'%'_ and _'database_user'@'localhost'_

+------------------+-----------+

| user | host |

+------------------+-----------+

| database_user | % |

| database_user | localhost |

| debian-sys-maint | localhost |

| mysql.session  | localhost |

| mysql.sys  | localhost |

| root | localhost |

+------------------+-----------+

6 rows in  set  (0.00 sec)

## Step 7 -

Deleting MySQL User Account

If you want to delete any user account, run the command below:

mysql> DROP USER 'database_user@'localhost';

This will give you the following output:

DROPUSER'database_user@'localhost';

In case you attempt to delete a user account that doesn’t exist on your database, you will see the following error:

ERROR 1396  (HY000): Operation DROPUSERfailedfor'database_user'@'localhost'

To prevent this error from occurring, execute the command below:

mysql> DROP USER IF EXISTS 'database_user'@'localhost';

You should see the following output:

QueryOK, 0 rowsaffected, 1  warning  (0.00sec)

## Step 8 -

Granting Permissions To MySQL User Account

Any user account can be granted several types of privileges. You can access all the privileges granted by MySQL on this  [link](https://dev.mysql.com/doc/refman/5.7/en/grant.html). Let’s look at a few examples.

To grant a user account all privileges over all databases, run the command below:

mysql> GRANT ALL PRIVILEGES ON *.* TO 'database_user'@'localhost';

To grant a user account all privileges over a certain table from the database, run the command below:

mysql> GRANT ALL PRIVILEGES ON database_name.table_name TO 'database_user'@'localhost';

Now, to grant a user account specific privileges over a certain database type, use the command below:

mysql> GRANT SELECT, INSERT, DELETE ON database_name.* TO database_user@'localhost';

## Step 9 -

Cancelling Permissions From A MySQL User Account

To cancel privileges from any MySQL user account, the syntax used is almost the same as that in granting permissions. For example, to cancel all privileges from a certain user account for MySQL over a specific database, run the command below:

mysql> REVOKE ALL PRIVILEGES ON database_name.* TO 'database_user'@'localhost';

## Step 10 -

Displaying Privileges For MySQL User Account

To identify the specific privileges granted to a certain MySQL user account type, execute the command below:

mysql> SHOW GRANTS FOR  'database_user'@'localhost';

The output will be:

+---------------------------------------------------------------------------+

| Grants for database_user@localhost |

+---------------------------------------------------------------------------+

| GRANTUSAGEON *.* TO'database_user'@'localhost'  |

| GRANT ALL PRIVILEGESON`database_name`.* TO'database_user'@'localhost'  |

+---------------------------------------------------------------------------+

2rowsinset  (0.00 sec)

That’s it.
