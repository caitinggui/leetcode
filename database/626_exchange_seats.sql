-- Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.
-- The column id is continuous increment.

-- Mary wants to change seats for the adjacent students.

-- Can you write a SQL query to output the result for Mary?

-- +---------+---------+
-- |    id   | student |
-- +---------+---------+
-- |    1    | Abbot   |
-- |    2    | Doris   |
-- |    3    | Emerson |
-- |    4    | Green   |
-- |    5    | Jeames  |
-- +---------+---------+

-- For the sample input, the output is:

-- +---------+---------+
-- |    id   | student |
-- +---------+---------+
-- |    1    | Doris   |
-- |    2    | Abbot   |
-- |    3    | Green   |
-- |    4    | Emerson |
-- |    5    | Jeames  |
-- +---------+---------+

-- Note:
-- If the number of students is odd, there is no need to change the last one's seat. 

Create table If Not Exists seat(id int, student varchar(255))
Truncate table seat
insert into seat (id, student) values ('1', 'Abbot')
insert into seat (id, student) values ('2', 'Doris')
insert into seat (id, student) values ('3', 'Emerson')
insert into seat (id, student) values ('4', 'Green')
insert into seat (id, student) values ('5', 'Jeames')


-- 理解题意有误，不是要修改表，而是要得出结果，这里修改了表，蛋疼
create table tmp1 as select a.id, b.student from seat a, seat b where a.id+1=b.id and a.id%2=1
create table tmp2 as select a.id, b.student from seat a, seat b where a.id-1=b.id and a.id%2=0
update seat a, tmp1 b set a.student=b.student where a.id=b.id
update seat a, tmp2 b set a.student=b.student where a.id=b.id
drop table tmp1
drop table tmp2
select * from seat
-- 不过这里也给出一下如果从一个表更新另一个表
-- Solution 1:  修改1列
update student s, city c
set s.city_name = c.name
where s.city_code = c.code;
-- Solution 2:  修改多个列
update  a,  b
set a.title=b.title, a.name=b.name
where a.id=b.id
-- Solution 3: 采用子查询, 这里有个问题，如果 s表的code不全，那么student一些行会被置为null
update student s set city_name = (select name from city where code = s.city_code);


-- 这里有个较好的方法, 这里改变id但不改变student
SELECT (CASE 
        WHEN (id % 2) != 0 AND counts != id THEN id + 1                                  
        WHEN (id % 2) != 0 AND counts = id THEN id
        ELSE id - 1 END
        ) as id, student
FROM seat, (SELECT COUNT(*) AS counts FROM seat) AS seat_counts
ORDER BY id ASC;

-- 一个次好的方法, 分3段合并
select a.id, b.student from seat a, seat b where a.id+1=b.id and a.id%2=1 union select a.id, b.student from seat a, seat b where a.id-1=b.id and a.id%2=0 union select id, student from seat , (select count(*) as counts from seat) b where id=b.counts and id%2=1 order by id
