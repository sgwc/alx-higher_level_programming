--  script that creates the database hbtn_0d_2 and the user user_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
<<<<<<< HEAD
GRANT SELECT ON 'hbtn_0d_2' * . * TO 'user_0d_2'@'localhost';
=======
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
>>>>>>> 7ed3ff9c2d3d5f3832d6ab71ef07f98731ded317
