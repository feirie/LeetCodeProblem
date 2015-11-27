select t1.Name from Customers t1
left join Orders t2
on t1.ID=t2.CustomerId
where t2.ID is null