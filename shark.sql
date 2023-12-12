select * from SharkAttack;

-- -- Number of surfers attacked in Mexico
select * from SharkAttack
where Country='AUSTRALIA';

-- Number of surfers attacked in Mexico
select Country, count(*) AS "Number of Attacks" 
from SharkAttack
where Country='Mexico'
AND Activity='Surfing';

-- ordering By activity of deceased
select * from SharkAttack
order by Activity DESC;




