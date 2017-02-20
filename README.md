#Dev Job
======
##Python 2.7

##MySQL 5.7
change root password

	UPDATE mysql.user
	    SET authentication_string = PASSWORD('MyNewPass'), password_expired = 'N'
	    WHERE User = 'root' AND Host = 'localhost';
	FLUSH PRIVILEGES;

##PHP
[https://www.liquidweb.com/kb/how-to-install-the-mongodb-php-driver-extension-on-centos-6/]
	
	# pecl install mongo
php.ini	
	
	extension=mongo.so
	
	
	# service httpd restart

![alt text](https://gmyou71.files.wordpress.com/2017/02/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-02-20-e1848be185a9e18492e185ae-5-46-16.png?w=680 "MAMP에서 PHP버전 변경하기")

### Install MongoDB Driver on MAMP
[http://lukepeters.me/blog/setting-up-mongodb-with-php-and-mamp]


##MongoDB 2.6
###Install
[https://www.liquidweb.com/kb/how-to-install-mongodb-on-centos-6/]
### Auth
#### Create User
[http://bloodguy.tistory.com/entry/MongoDB-%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B4%80%EB%A6%AC-User-Administration]
#### Auth Configuration
[mongo.conf]

	auth=ture
