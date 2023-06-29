# Write your MySQL query statement below

# select e1.name as Employee from Employee e1 where e1.salary > (
#     select e2.salary from Employee e2 where e2.id = e1.managerId
# )


select a.name as Employee from Employee as a, Employee as b where a.managerId = b.id and a.salary > b.salary;