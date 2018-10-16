
#1. Select, for each boat, the sailor who made the highest number of reservations for that boat.

SELECT DISTINCT b.bname, s.sname, COUNT(*) 
FROM boats b JOIN reserves r ON b.bid = r.bid 
JOIN sailors s ON s.sid = r.sid GROUP BY b.bid, b.bname, s.sid, s.sname 
HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM reserves ra 
WHERE ra.bid = b.bid GROUP BY ra.sid) ORDER BY b.bname, s.sname;


#2.List, for every boat, the number of times it has been reserved, 
#  excluding those boats that have never been reserved (list the id and the name).

SELECT b.bid, b.bname, count(r.sid) as Reserve_Times 
from boats b JOIN reserves r ON b.bid = r.bid 
group by b.bid, b.bname ORDER BY b.bid;


#3.List those sailors who have reserved every red boat
SELECT s.sname FROM sailors s 
WHERE NOT EXISTS (SELECT * FROM boats b WHERE b.color = 'red' AND NOT EXISTS 
	       (SELECT * FROM reserves r WHERE r.sid = s.sid AND r.bid = b.bid));


#4.List those sailors who have reserved only red boat

SELECT sname FROM sailors s WHERE 'red'= ALL 
(SELECT b.color FROM reserves r JOIN boats b ON r.bid=b.bid WHERE r.sid = s.sid);

#5.For which boat are there there the most reservations?
SELECT bid, count(bid) as NUMBER_OF_RESERVATIONS FROM reserves 
GROUP BY bid ORDER BY NUMBER_OF_RESERVATIONS DESC LIMIT 1;

#6.Select all sailors who have never reserved a read boat
SELECT s.sname FROM sailors s WHERE s.sid NOT IN 
(SELECT r.sid FROM reserves r JOIN boats b ON r.bid=b.bid WHERE b.color='red');

#7.Find the average age of sailors with a rating of 10.
SELECT avg(s.age) from sailors s where s.rating = 10;




