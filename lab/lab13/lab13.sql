.read sp17data.sql
.read su17data.sql

CREATE TABLE obedience AS
  select seven, image from students;

CREATE TABLE smallest_int AS
  select time, smallest from students where smallest > 5 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select a.date, a.color, a.pet, a.number, b.number from students as a, sp17students as b
          where a.date = b.date and a.color = b.color and a.pet = b.pet;

CREATE TABLE sevens AS
  select students.seven from students, checkboxes where students.number = 7 and checkboxes.'7'='True' and students.time = checkboxes.time;

CREATE TABLE matchmaker AS
  select first.pet, first.beets, first.color, second.color from students as first, students as second
        where first.pet = second.pet and first.beets = second.beets and first.time < second.time;
