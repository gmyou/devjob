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
###Install
[https://www.liquidweb.com/kb/how-to-install-mongodb-on-centos-6/]
### Auth
#### Create User
[http://bloodguy.tistory.com/entry/MongoDB-%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B4%80%EB%A6%AC-User-Administration]
#### Auth Configuration
[mongo.conf]

	auth=ture
