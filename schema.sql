drop table if exists users;
create table users (
  id integer primary key autoincrement,
  name string not null,
  passwd string not null
);

drop table if exists live_general;
create table live_general (
  id integer primary key autoincrement,
  title string not null,
  host_id integer not null
);

drop table if exists live_participants;
create table live_participants (
  id integer primary key autoincrement,
  live_id integer not null,
  participant_id integer not null
);

drop table if exists live_content;
create table live_content (
  id integer primary key autoincrement,
  live_id integer not null,
  time string not null,
  content string not null
);