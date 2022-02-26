-- View and show both table structures and data to make sure they are set up correctly

SELECT * FROM music_school.teachers;
EXPLAIN music_school.teachers;

SELECT * FROM music_school.students;
EXPLAIN music_school.students;

-- Enter records into both tables and view them. 

insert into teachers ( id, `name`, surname, mobile)
values ('L.Smith', 'Lucy', 'Smith', '07712348649'),
('Jaroslav', 'Jaroslav', 'Gavrilovs', '07845278056'),
('L.Jones', 'Lucy', 'Jones', '07641968467'),
('Julie', 'Julie', 'Moss', '07649408749');

select * from teachers;

insert into students (id, `name`, surname, par_name, par_surname, mobile, teacher_id)
values ('Maria', 'Maria', 'Jones', 'Mary', 'Jones', '0753967824', 'L.Smith'),
('Rose', 'Rose', 'Potter', 'Ann', 'Potter', '07485217909', 'L.Jones'),
('Darryl', 'Darryl', 'Barber', 'James', 'Barber', '07488305694', 'Julie'),
('Anna', 'Anna', 'Black', 'Joanna', 'Black', '07576429789', 'Jaroslav'),
('Amy', 'Amy', 'Barber', 'James', 'Barber', '07488305694', 'Julie'),
('Frank', 'Frank', 'Josef', 'Lily', 'Josef', '07839567014', 'L.Jones'),
('Yan', 'Yan', 'Chi', null, null, '07829567456', 'Jaroslav'),
('Alvena', 'Alvena', 'Hayter', 'Dora', 'Hayter', '07846395892', 'L.Jones'),
('Shirley', 'Shirley', 'Long', null, null, '07894572156', 'Jaroslav'),
('Ivy', 'Ivy', 'Holland', null, null, '07846318679', 'L.Smith');

select * from students;

-- Update a record

update students
set mobile = '07846542789'
where id = 'Anna';
select * from students;

-- Delete a record

delete from students
where id = 'Alvena';
select * from students;

-- Join tables

select students.id, teachers.id
from teachers
inner join students
on students.teacher_id = teachers.id;

-- Run a simple query (one field/column) searching one table

select * from students
where surname = 'Jones';

-- Run a complex query (more than one field/column) to demonstrate the relations between the 2 tables

select * from students, teachers
where students.teacher_id = teachers.id and teachers.surname = 'Smith';

-- Retrieve all your data sorted in ascending order on an appropriate field (one table)

select surname from students
order by surname;

-- Filter data using comparison operator (one table)

select * from students
where teacher_id != 'L.Smith';






