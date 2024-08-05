CREATE TABLE EmployeePerformance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    department VARCHAR(100),
    performance_score DECIMAL(5, 2),
    years_with_company INT,
    salary DECIMAL(10, 2)
);

-- Insertar empleados en el departamento Scuse
INSERT INTO `EmployeePerformance` (`employee_id`, `department`, `performance_score`, `years_with_company`, `salary`) VALUES
(101, 'Scuse', 85.75, 5, 55000.00),
(102, 'Scuse', 78.50, 3, 47000.00),
(103, 'Scuse', 92.20, 8, 60000.00),
(104, 'Scuse', 88.00, 4, 53000.00);

-- Insertar empleados en el departamento Tech
INSERT INTO `EmployeePerformance` (`employee_id`, `department`, `performance_score`, `years_with_company`, `salary`) VALUES
(201, 'Tech', 91.00, 6, 62000.00),
(202, 'Tech', 84.30, 2, 48000.00),
(203, 'Tech', 77.50, 4, 51000.00),
(204, 'Tech', 89.75, 7, 58000.00);

-- Insertar empleados en el departamento HR
INSERT INTO `EmployeePerformance` (`employee_id`, `department`, `performance_score`, `years_with_company`, `salary`) VALUES
(301, 'HR', 82.10, 3, 46000.00),
(302, 'HR', 76.25, 5, 49000.00),
(303, 'HR', 90.35, 6, 55000.00),
(304, 'HR', 87.40, 2, 47000.00);