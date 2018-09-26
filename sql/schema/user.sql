
create table "user" (
    "id" serial,
    "nick" varchar(64) not null,
    "email" varchar(128) not null,
    "status" tinyint not null default 0
)
