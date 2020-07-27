database

CREATE TABLE download_manager 
(
	id integer auto_increment primary key,
	file_name varchar(40) not null,
	link varchar(300) not null,
	file_size varchar(10) not null,
	date_download date not null
)


