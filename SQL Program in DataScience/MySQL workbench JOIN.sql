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

create database companyid;
USE companyid;
CREATE TABLE Staff(Staff_ID INT PRIMARY KEY, Staff_Name VARCHAR(100), Staff_Dept VARCHAR(100));
CREATE TABLE Student(Student_ID INT PRIMARY KEY, Stu_Name VARCHAR(100), Staff_ID INT, C_hr INT, FOREIGN KEY(Staff_ID) REFERENCES Staff(Staff_ID));
INSERT INTO Staff VALUES (55001, 'SURYA', 'MS OFFICE'), (55003, 'DHIYA', 'AI TECH'), (55005, 'DHANYASRI', 'DATA SCIENCE'), (55008, 'JEEVA', 'PYTHON'), (55009, 'KEERTHI', 'JAVA');
INSERT INTO Student VALUES (10050, 'JENI', 55001, 190), (10083, 'KANISH', 55005, 250), (10190, 'LAVANYA', 55003, 60), (10110, 'DHIVYA', 55009, 90), (10068, 'NITHYA', 55003, 280), (10079, 'BARATHI', 55009, 85), (10085, 'KATHIR', 55008, 80);
SELECT * FROM Staff;
SELECT * FROM Student;
SELECT Stf.Staff_Name, Stu.Stu_Name FROM Staff Stf INNER JOIN Student Stu ON Stf.Staff_ID = Stu.Staff_ID;
SELECT Stf.Staff_Name, Stu.Stu_Name FROM Staff Stf LEFT JOIN Student Stu ON Stf.Staff_ID = Stu.Staff_ID;
SELECT Stf.Staff_Name, Stu.Stu_Name FROM Staff Stf RIGHT JOIN Student Stu ON Stf.Staff_ID = Stu.Staff_ID;

Drop Database companyid;

