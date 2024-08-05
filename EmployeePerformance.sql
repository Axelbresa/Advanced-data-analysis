CREATE TABLE EmployeePerformance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    department VARCHAR(100),
    performance_score DECIMAL(5, 2),
    years_with_company INT,
    salary DECIMAL(10, 2)
);

insert into EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary) values (1, 'Katina', 'Scuse', 'kscuse0@drupal.org', 'Female', '158.52.54.200');
insert into EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary) values (2, 'Cullan', 'Mewett', 'cmewett1@php.net', 'Male', '197.108.17.84');
insert into EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary) values (3, 'Allene', 'Farden', 'afarden2@imdb.com', 'Female', '54.169.110.222');
insert into EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary) values (4, 'Marcel', 'Bernolet', 'mbernolet3@bloglovin.com', 'Male', '147.245.57.32');
insert into EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary) values (5, 'Vergil', 'Runge', 'vrunge4@squarespace.com', 'Male', '248.97.42.21');
insert into EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary) values (6, 'Kalinda', 'Peery', 'kpeery5@salon.com', 'Female', '216.7.193.66');
insert into EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary) values (7, 'Jillene', 'Wandrach', 'jwandrach6@un.org', 'Non-binary', '8.173.182.5');

