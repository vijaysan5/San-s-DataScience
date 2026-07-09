CREATE DATABASE JoinData;
USE JoinData;
CREATE TABLE Departmentone(DeptID INT PRIMARY KEY, DeptName varchar(100));
CREATE TABLE Employee(EmpID INT PRIMARY KEY, EmpName varchar(100), DeptID int, Salary decimal(10,2), ManagerID int, foreign key(DeptID) references Departmentone(DeptID), foreign key (ManagerID) references Employee(EmpID));
INSERT INTO Departmentone VALUES (1, 'InfoTech'), (2, 'Finance'), (3, 'HR');
INSERT INTO Employee VALUES
(101, 'Nancy', 1, 50000, NULL),
(102, 'Hanvika', 2, 60000, 101),
(103, 'Ashwin', 2, 50000, 102),
(104, 'Dhivya', 3, 75000, 101), 
(105, 'Mithun', 1, 80000, 101);
SELECT * FROM Employee;
SELECT * FROM Departmentone;
SELECT E.EmpName, D.DeptName FROM Employee E INNER JOIN Departmentone D ON E.DeptID = D.DeptID;
SELECT E.EmpName, D.DeptName FROM Employee E LEFT JOIN Departmentone D ON E.DeptID = D.DeptID;
SELECT E.EmpName, D.DeptName FROM Employee E RIGHT JOIN Departmentone D ON E.DeptID = D.DeptID;
SELECT E.EmpName AS Employee, M.EmpName AS Manager FROM Employee E LEFT JOIN Employee M ON M.ManagerID = M.EmpID;

Drop Database JoinData;