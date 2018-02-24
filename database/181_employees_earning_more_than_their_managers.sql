-- The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

-- +----+-------+--------+-----------+
-- | Id | Name  | Salary | ManagerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | NULL      |
-- | 4  | Max   | 90000  | NULL      |
-- +----+-------+--------+-----------+

-- Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

-- +----------+
-- | Employee |
-- +----------+
-- | Joe      |
-- +----------+


Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, ManagerId int)
Truncate table Employee
insert into Employee (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3')
insert into Employee (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4')
insert into Employee (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', 'None')
insert into Employee (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', 'None')

# 一不小心变成最快的解法了
select `Name` as Employee from (select a.Name, a.`Salary`, a.`ManagerId` from `Employee` a where `Salary` > (select b.`Salary` from `Employee` b where b.`Id`=a.ManagerId)) c


# 其他方法如下：
select name as Employee from employee a
inner join
(select distinct id, salary as mana_salary from employee) b
on a.managerID=b.id
where salary > mana_salary

# where对比的条件可以不一定出现在select中
SELECT e1.Name as Employee FROM Employee as e1, Employee as e2 WHERE e1.ManagerId IS NOT NULL AND e2.Id = e1.ManagerId AND e1.Salary > e2.Salary;
