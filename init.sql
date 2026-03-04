create schema oltp;

create table oltp.deployments (
    id integer not null
    db_name varchar not null
    status varchar not null
    username varchar not null
    creation_time timestamp without time zone not null default (current_timestamp at time zone 'utc')
);

