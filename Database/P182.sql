select Email from
    (select Email,count(*) from Person group by Email having count(*)>1) t