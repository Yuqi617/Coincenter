# Coincenter
A digital coin trading web application

Please type the follwing codes to mysql to create database and tables

create database coincenter;

use coincenter;

create table blotter (
    blotter_id int not null auto_increment primary key,
    coin_id int not null,
    askbid varchar(4),
    qty decimal (10,2),
    price decimal(10,2),
    time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    balance decimal(10,2)    
);

create table coins (
 coin_id int not null auto_increment primary key,
 coin_type varchar(3)
);

create table pnl(
    pnl_id int not null auto_increment primary key,
    coin_id int,
    inventory decimal(10,2),
    VWAP decimal (10,2),
    RPL  decimal (10,2),
    URPL decimal (10,2),
    time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    constraint pnl_coin_id_fk foreign key (coin_id) references coins (coin_id) on delete cascade
);

create table graph(
  graph_id int not null auto_increment primary key,
  coin_id int not null,
  RPL  decimal (10,2),
  URPL decimal (10,2),
  pnl_id int not null,
  time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  constraint graph_coin_id_fk foreign key (coin_id) references coins (coin_id) on delete cascade,
  constraint graph_pnl_id_fk foreign key (pnl_id) references pnl (pnl_id) on delete cascade
  );

insert into coins values (1,'BTC'),(2,'ETH'),(3,'LTC');

insert into pnl (coin_id,inventory,VWAP,RPL,URPL) values (1,0,0,0,0);
insert into pnl (coin_id,inventory,VWAP,RPL,URPL) values (2,0,0,0,0);
insert into pnl (coin_id,inventory,VWAP,RPL,URPL) values (3,0,0,0,0);
