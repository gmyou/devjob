#Dev Job
======
##Python 2.7

##MySQL 5.7
change root password

	UPDATE mysql.user
	    SET authentication_string = PASSWORD('MyNewPass'), password_expired = 'N'
	    WHERE User = 'root' AND Host = 'localhost';
	FLUSH PRIVILEGES;

##PHP 7

##MongoDB 2.6
[https://www.liquidweb.com/kb/how-to-install-mongodb-on-centos-6/]
