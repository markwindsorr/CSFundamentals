-- =========================================================================
-- SQL Fundamentals
-- 
-- 
-- =========================================================================
-- Creating a Database

-- Create a new database called 'TutorialDB'
-- Connect to the 'master' database to run this snippet
USE master
GO
IF NOT EXISTS (
   SELECT name
   FROM sys.databases
   WHERE name = N'TutorialDB'
)
CREATE DATABASE [TutorialDB]
GO

-- =========================================================================
-- Creating a Table 

-- Create a new table called 'CompanyProfile' in schema 'SchemaName'
-- Drop the table if it already exists
IF OBJECT_ID('SchemaName.CompanyProfile', 'U') IS NOT NULL
DROP TABLE SchemaName.CompanyProfile
GO
-- Create the table in the specified schema
CREATE TABLE SchemaName.CompanyProfile
(
    symbol [NVARCHAR] NOT NULL PRIMARY KEY, -- primary key column
    CEO [NVARCHAR](50),
    companyAddress [NVARCHAR](50),
    city [NVARCHAR](50),
    companyName [NVARCHAR](50),
    country [NVARCHAR](50),
    companyDescription [NVARCHAR](MAX),
    employees INT,
    exchange [NVARCHAR](50),
    industry [NVARCHAR](50),
    issueType [NVARCHAR](50),
    phone [NVARCHAR](50),
    sector [NVARCHAR](50),
    tags [NVARCHAR](50),
    website [NVARCHAR](50),
    zip [NVARCHAR](50)

    -- specify more columns here
);
GO

-- =========================================================================
-- Insert & Query

-- Insert rows into table 'Employees'
INSERT INTO Employees
   ([EmployeesId],[Name],[Location])
VALUES
   ( 1, N'Jared', N'Australia'),
   ( 2, N'Nikita', N'India'),
   ( 3, N'Tom', N'Germany'),
   ( 4, N'Jake', N'United States')
GO
-- Query the total count of employees
SELECT COUNT(*) as EmployeeCount FROM dbo.Employees;
-- Query all employee information
SELECT e.EmployeesId, e.Name, e.Location
FROM dbo.Employees as e
GO


-- =========================================================================
-- List Tables in your Database


select schema_name(t.schema_id) as schema_name,
       t.name as table_name,
       t.create_date,
       t.modify_date
from sys.tables t
order by schema_name,
         table_name;


-- =========================================================================
-- Drop/Delete table in your database


DROP TABLE dbo.PurchaseOrderDetail;