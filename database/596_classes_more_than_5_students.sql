"""
 There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+

Should output:

+---------+
| class   |
+---------+
| Math    |
+---------+

Note:
The students should not be counted duplicate in each course. 
"""

Create table If Not Exists courses (student varchar(255), class varchar(255))
Truncate table courses
insert into courses (student, class) values ('A', 'Math')
insert into courses (student, class) values ('B', 'English')
insert into courses (student, class) values ('C', 'Math')
insert into courses (student, class) values ('D', 'Biology')
insert into courses (student, class) values ('E', 'Math')
insert into courses (student, class) values ('F', 'Computer')
insert into courses (student, class) values ('G', 'Math')
insert into courses (student, class) values ('H', 'Math')
insert into courses (student, class) values ('I', 'Math')

-- distinct是针对student和class一起去重，有distinct就对列举的全部变量去重
-- select id,name from user group by name; 这里仅要求名字不同
-- select distinct id, name from user;  这里id和名字均要求不同
select b.class from (select distinct a.student, a.class from courses as a) as b group by b.class having count(*)>4;

-- 另一种解法
SELECT class FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student)>=5
