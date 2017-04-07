drop table if exists users;
create table users (
  id integer primary key autoincrement,
  user_name string not null,
  hashed_name_passwd string not null,
  balance real DEFAULT 0
);

drop table if exists live_general;
create table live_general (
  id integer primary key autoincrement,
  title string not null,
  host_id integer not null,
  has_end integer not null DEFAULT 0
);

drop table if exists live_participants;
create table live_participants (
  id integer primary key autoincrement,
  live_id integer not null,
  participant_id integer not null
);