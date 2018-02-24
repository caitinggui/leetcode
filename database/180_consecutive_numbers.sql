-- Write a SQL query to find all numbers that appear at least three times consecutively.

-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+

-- For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+


Create table If Not Exists Logs (Id int, Num int)
Truncate table Logs
insert into Logs (Id, Num) values ('1', '1')
insert into Logs (Id, Num) values ('2', '1')
insert into Logs (Id, Num) values ('3', '1')
insert into Logs (Id, Num) values ('4', '2')
insert into Logs (Id, Num) values ('5', '1')
insert into Logs (Id, Num) values ('6', '2')
insert into Logs (Id, Num) values ('7', '2')

# 会超时
select distinct  a.Num from Logs a, Logs b, Logs c where a.Num=b.Num and b.Num=c.Num and abs(a.id-b.id)=1 and abs(c.id-b.id)=1 and a.id!=c.id

# 次好的方法
select distinct l1.Num as ConsecutiveNums
from
logs l1,
logs l2,
logs l3
where 
l1.Id = l2.Id -1 and
l2.Id = l3.Id -1 and
l1.Num = l2.Num and
l2.Num = l3.Num;

# 更好的方法
select distinct a.Num from Logs a where a.Num = (select b.Num from Logs b where b.id=a.id+1) and a.Num=(select c.Num from Logs c where c.id=a.id+2)
