create database NewDepEmp;
use NewDepEmp;
create table Departmentone(DeptID int primary key, DeptName varchar(100));
create table Employee(EmpID int primary key, EmpName varchar(100), DeptID int, Salary decimal(10,2), ManagerID int, foreign key(DeptID) references Departmentone(DeptID), foreign key (ManagerID) references Employee(EmpID));
insert into Departmentone values (1, 'InfoTech'), (2, 'Finance'), (3, 'HR');
insert into Employee value
(101, 'Nancy', 1, 50000, null),
(102, 'Hanvika', 2, 60000, 101),
(103, 'Ashwin', 2, 50000, 102),
(104, 'Dhivya', 3, 75000, 101), 
(105, 'Mithun', 1, 80000, 101);
select * from Employee;
select * from Departmentone;
select DeptID, count(*) as TotalEmployees, avg(salary) as AvgSalary from Employee group by DeptID;
select * from Employee where Salary > 60000;
select * from Employee order by Salary desc;
update Employee set Salary = Salary + 5000 where EmpID = 103;
drop database NewDepEmp;-- 