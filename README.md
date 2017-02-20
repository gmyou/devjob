#Dev Job
======
##Python
### Install PYENV && Edit ~/.bash_profile && source ~/.bash_profile
	$ vim ~/.bash_profile 
	export PYENV_ROOT="$HOME/.pyenv"
	export PATH="$PYENV_ROOT/bin:$PATH"
	eval "$(pyenv init -)"

##MySQL
change root password

	UPDATE mysql.user
	    SET authentication_string = PASSWORD('MyNewPass'), password_expired = 'N'
	    WHERE User = 'root' AND Host = 'localhost';
	FLUSH PRIVILEGES;

##PHP
[https://www.liquidweb.com/kb/how-to-install-the-mongodb-php-driver-extension-on-centos-6/]
	
	$ pecl install mongo
php.ini	
	
	extension=mongo.so
	
	
	$ service httpd restart

![alt text](https://gmyou71.files.wordpress.com/2017/02/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-02-20-e1848be185a9e18492e185ae-5-46-16.png?w=680 "MAMP에서 PHP버전 변경하기")

### Install MongoDB Driver on MAMP
[http://lukepeters.me/blog/setting-up-mongodb-with-php-and-mamp]

or 

#### Install Not on MAMP
	$ curl -s http://php-osx.liip.ch/install.sh | bash -s 5.6
	$ brew install php56-mongo php56-memcache

#### Change PHP Version (Not on MAMP)
	$ cd /etc/apache2/other
	$ sudo rm +php-osx.conf 
	$ sudo ln -s /usr/local/{PHP_VERSION_YOU_WANT}/entropy-php.conf +php-osx.conf
	
#### Change PHP-CLI Version (Not on MAMP)
	$ brew install php70
	$ vim ~/.bash_profile

#### Add This Line on ~/.bash_profile && source ~/.bash_profile
	#php
	export PATH=/usr/local/Cellar/php70/7.0.15_8/bin:$PATH

##MongoDB 2.6
###Install
[https://www.liquidweb.com/kb/how-to-install-mongodb-on-centos-6/]
### Auth
#### Create User
[http://bloodguy.tistory.com/entry/MongoDB-%EC%82%AC%EC%9A%A9%EC%9E%90-%EA%B4%80%EB%A6%AC-User-Administration]
#### Auth Configuration
[mongo.conf]

	auth=ture
