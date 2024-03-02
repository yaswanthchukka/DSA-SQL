/* Write your PL/SQL query statement below 

select * from person as p
full outer join address as a
on p.personid=a.personid;
*/

select person.firstname,person.lastname,address.city,address.state
from person
left join address
on person.personid=address.personid;