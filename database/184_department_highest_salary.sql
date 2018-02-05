 # The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

# +----+-------+--------+--------------+
# | Id | Name  | Salary | DepartmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Henry | 80000  | 2            |
# | 3  | Sam   | 60000  | 2            |
# | 4  | Max   | 90000  | 1            |
# +----+-------+--------+--------------+

# The Department table holds all departments of the company.

# +----+----------+
# | Id | Name     |
# +----+----------+
# | 1  | IT       |
# | 2  | Sales    |
# +----+----------+

# Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.

# +------------+----------+--------+
# | Department | Employee | Salary |
# +------------+----------+--------+
# | IT         | Max      | 90000  |
# | Sales      | Henry    | 80000  |
# +------------+----------+--------+

Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, DepartmentId int)
Create table If Not Exists Department (Id int, Name varchar(255))
Truncate table Employee
insert into Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '70000', '1')
insert into Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2')
insert into Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2')
insert into Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1')
Truncate table Department
insert into Department (Id, Name) values ('1', 'IT')
insert into Department (Id, Name) values ('2', 'Sales')


## 错误的答案, 用salary对比会出问题
select distinct b.`Name` as Department, a.name as Employee, a.`Salary` as Salary  from `Employee` a, `Department` b, (select max(`Salary`) as s from `Employee` group by `DepartmentId`) c where c.s=a.`Salary`and a.`DepartmentId`=b.id;


## 一个低效的答案, 先找出最大salary的employee id，然后再join之类的
select distinct b.`Name` as Department, a.name as Employee, a.`Salary` as Salary from `Employee` a, `Department` b, (select c.`Id` as id from `Employee` c where c.`Salary`=(select max(`Salary`) from `Employee` where `DepartmentId`=c.`DepartmentId`)) d where a.`Id`=d.id and a.`DepartmentId`=b.`Id`


## 一个更高效的答案，group by的时候，max和被group by的项是正确返回的,而其他列就不一定正确，举例如下：
select `DepartmentId`, max(`Salary`) from `Employee` group by `DepartmentId`  -- departmentid是和max结果吻合的
select `Id`, max(`Salary`) from `Employee` group by `DepartmentId`  -- id和max结果不吻合，id仅仅只是group by后的顺序行，不是employee的id

## group by 和 max的结合
select * from `Employee` a where a.`Salary`=(select max(`Salary`) from `Employee` where `DepartmentId`=a.`DepartmentId`)
## 这个效率太低，不要用, 而且会漏掉同是最高分的几个行
select * from (select * from `Employee` order by `Salary` desc) b group by DepartmentId

