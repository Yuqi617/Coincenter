# Coincenter
A digital coin trading web application

Please type the follwing codes to mysql to create database and tables

create database coincenter;

use coincenter;

create table users (
user_name VARCHAR(255),
email VARCHAR(255),
user_id INTEGER AUTO_INCREMENT PRIMARY KEY);

create table coins (
coin_name VARCHAR(255),
price DECIMAL(10,2),
coin_id INTEGER PRIMARY KEY);

create table blotter (
blotter_id INTEGER AUTO_INCREMENT PRIMARY KEY, 
user_id INTEGER, 
price DECIMAL(10,2), 
amount DECIMAL(10,2),
askbid VARCHAR(255),
qty INTEGER,
blotter_time time, 
coin_id INTEGER,
constraint blotter_user_id_fk foreign key (user_id) references users (user_id) on delete cascade,
constraint blotter_coin_id_fk foreign key (coin_id) references coins (coin_id) on delete cascade
);

create table pnl (
pnl_id INTEGER PRIMARY KEY, 
coin_id INTEGER, 
asset DECIMAL(10,2),
total_qty INTEGER,
vwap DECIMAL(10,2),
rpl DECIMAL(10,2), 
urpl DECIMAL(10,2), 
pnl_time TIME,
constraint pnl_coin_id_fk foreign key (coin_id) references coins (coin_id) on delete cascade
);

create table graph (
graph_id INTEGER AUTO_INCREMENT PRIMARY KEY, 
coin_id INTEGER, 
pnl_id INTEGER,
rpl DECIMAL(10,2), 
urpl DECIMAL(10,2),
pnl_time TIME,
constraint graph_coin_id_fk foreign key (coin_id) references coins (coin_id) on delete cascade,
constraint graph_pnl_id_fk foreign key (pnl_id) references pnl (pnl_id) on delete cascade
)
