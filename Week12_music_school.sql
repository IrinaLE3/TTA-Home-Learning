create database music_school;
use music_school;

create table teachers(
id varchar(20) not null,
`name` varchar(45) not null,
surname varchar(45) not null,
mobile varchar(15) not null,
primary key (id)
);

create table students(
id varchar(20) not null,
`name` varchar(45) not null,
surname varchar(45) not null,
par_name varchar(45) not null,
par_surname varchar(45) not null,
mobile varchar(15) not null,
teacher_id varchar(20) not null,
primary key (id)
);

insert into teachers ( id, `name`, surname, mobile)
values ('L.Smith', 'Lucy', 'Smith', '07712348649'),
('Jaroslav', 'Jaroslav', 'Gavrilovs', '07845278056'),
('L.Jones', 'Lucy', 'Jones', '07641968467');

insert into students (id, `name`, surname, par_name, par_surname, mobile, teacher_id)
values ('Maria', 'Maria', 'Jones', 'Mary', 'Jones', '0753967824', 'L.Smith'),
('Rose', 'Rose', 'Potter', 'Ann', 'Potter', '07485217909', 'L.Jones');

select * from teachers;
select * from students;
select * from students where teacher_id = 'L.Smith';









