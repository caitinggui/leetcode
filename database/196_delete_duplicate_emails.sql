-- Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- Id is the primary key column for this table.

-- For example, after running your query, the above Person table should have the following rows:

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+

DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND
p1.Id > p2.Id


-- 不允许这样使用，因为You can't specify target table 'person' for update in FROM clause
delete from person where id not in (select min(id) from person group by email)
-- 可中间加个临时表，如下
delete from person where id not in (select t.tid from (select min(id) as tid from person group by email) t)
-- 或者
create table t1 as select min(id) as id from person group by email;
delete from person where id not in (select id from t1);
drop table t1;
