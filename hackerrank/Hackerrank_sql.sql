/*
    # -*- coding: UTF-8 -*-
    # Author: h1033742389
    # Date: 2019-09-17
    # Email: smLin97@outlook.com
    # Default: DB2
    # Number of Questions:

    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/


----------START Basic Select----------#
--->Revising the Select Query I
SELECT * FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;

--->Revising the Select Query II
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 120000;

--->Select All
SELECT * FROM CITY;

--->Select By ID
SELECT * FROM CITY WHERE ID = '1661';

--->Japanese Cities' Attributes
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';

--->Japanese Cities' Names
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';

--->Weather Observation Station 1
SELECT CITY,STATE FROM STATION;

--->Weather Observation Station 3
SELECT distinct(CITY) FROM STATION WHERE MOD(ID,2)= 0;
-- 注意: mod求余  %只适用于mysql

--->Weather Observation Station 4
SELECT COUNT(CITY)-COUNT(distinct(CITY)) FROM STATION;

--->Weather Observation Station 5
SELECT CITY,LENGTH(trim(CITY))
FROM STATION
WHERE LENGTH(trim(CITY)) IN
    (SELECT MIN(LENGTH(trim(CITY)))FROM STATION)
ORDER BY CITY
FETCH FIRST 1 ROWS ONLY;

SELECT CITY,LENGTH(trim(CITY))
FROM STATION
WHERE LENGTH(trim(CITY)) IN
    (SELECT MAX(LENGTH(trim(CITY)))FROM STATION)
ORDER BY CITY
FETCH FIRST 1 ROWS ONLY;

--->Weather Observation Station 6
SELECT distinct(CITY) FROM STATION WHERE CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' OR CITY LIKE 'U%';
-- 注意: db2没有自带正则, distinct一项的时候有没有括号都没问题

--->Weather Observation Station 7
SELECT distinct(CITY) FROM STATION WHERE CITY LIKE '%a' OR CITY LIKE '%e' OR CITY LIKE '%i' OR CITY LIKE '%o' OR CITY LIKE '%u';

--->Weather Observation Station 8
SELECT distinct CITY FROM STATION WHERE CITY LIKE 'A%a' OR CITY LIKE 'A%e' OR CITY LIKE 'A%i' OR CITY LIKE 'A%o' OR CITY LIKE 'A%u' OR CITY LIKE 'E%a' OR CITY LIKE 'E%e' OR CITY LIKE 'E%i' OR CITY LIKE 'E%o' OR CITY LIKE 'E%u' OR CITY LIKE 'I%a' OR CITY LIKE 'I%e' OR CITY LIKE 'I%i' OR CITY LIKE 'I%o' OR CITY LIKE 'I%u' OR CITY LIKE 'O%a' OR CITY LIKE 'O%e' OR CITY LIKE 'O%i' OR CITY LIKE 'O%o' OR CITY LIKE 'O%u' OR CITY LIKE 'U%a' OR CITY LIKE 'U%e' OR CITY LIKE 'U%i' OR CITY LIKE 'U%o' OR CITY LIKE 'U%u';

--->Weather Observation Station 9
-- MS SQL Server
SELECT distinct(CITY) FROM STATION WHERE CITY NOT LIKE '[AEIOU]%';
-- Oracle
SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(CITY, '^[^AEIOU]');

--->Weather Observation Station 10
-- Oracle
SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(CITY, '*[^aeiou]$');

--->Weather Observation Station 11
-- Oracle
SELECT distinct(CITY) FROM STATION WHERE REGEXP_LIKE(CITY, '^[^AEIOU]|[^aeiou]$');

--->Weather Observation Station 12
-- Oracle
SELECT distinct(CITY) FROM STATION WHERE REGEXP_LIKE(CITY, '^[^AEIOU].*[^aeiou]$');

--->Higher Than 75 Marks
-- Oracle
SELECT Name FROM STUDENTS WHERE Marks > 75 ORDER BY SUBSTR(NAME,-3) asc,ID asc;

--->Employee Names
SELECT name FROM Employee ORDER BY NAME ASC;

--->Employee Salaries
SELECT name FROM Employee WHERE salary > 2000 AND months < 10;

----------END Basic Select----------#


----------START Advanced Select----------#
--->Type of Triangle
SELECT
    CASE WHEN A+B>C AND B+C>A AND A+C>B
    THEN
        CASE
            WHEN A=B AND B=C THEN 'Equilateral'
            WHEN A=B OR B=C OR A=C THEN 'Isosceles'
        ELSE 'Scalene'
        END
    ELSE 'Not A Triangle'
    END
FROM TRIANGLES;

--->The PADS
SELECT CONCAT(CONCAT(CONCAT(NAME,'('),SUBSTR(OCCUPATION,1,1)),')') FROM OCCUPATIONS ORDER BY NAME;
SELECT CONCAT(CONCAT(CONCAT(CONCAT('There are a total of ',COUNT(1)),' '),LOWER(OCCUPATION)),'s.')
FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY COUNT(OCCUPATION),OCCUPATION;
-- 注意: CONCAT在DB2里只能拼接仅2个字符串,也不能拼接字符串和数字

--->Occupations
-- MySQL
set @r1=0, @r2=0, @r3=0, @r4=0;
-- @局部变量 @@全局变量
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
    select
        case when Occupation='Doctor' then (@r1:=@r1+1)
            when Occupation='Professor' then (@r2:=@r2+1)
            when Occupation='Singer' then (@r3:=@r3+1)
            when Occupation='Actor' then (@r4:=@r4+1)
        end as RowNumber,
        case when Occupation='Doctor' then Name end as Doctor,
        case when Occupation='Professor' then Name end as Professor,
        case when Occupation='Singer' then Name end as Singer,
        case when Occupation='Actor' then Name end as Actor
    from OCCUPATIONS order by Name
    -- 这里获得：行号、每行是一个名字的数据
    -- 1 Aamina NULL NULL NULL
    -- 1 NULL Ashley NULL NULL
    -- 2 NULL Belvet NULL NULL
    -- 3 NULL Britney NULL NULL
    -- 1 NULL NULL Christeen NULL
    -- 1 NULL NULL NULL Eve
    -- 2 NULL NULL Jane NULL
    -- 2 NULL NULL NULL Jennifer
    -- 3 NULL NULL Jenny NULL
    -- 2 Julia NULL NULL NULL
    -- 3 NULL NULL NULL Ketty
    -- 4 NULL NULL Kristeen NULL
    -- 4 NULL Maria NULL NULL
    -- 5 NULL Meera NULL NULL
    -- 6 NULL Naomi NULL NULL
    -- 3 Priya NULL NULL NULL
    -- 7 NULL Priyanka NULL NULL
    -- 4 NULL NULL NULL Samantha

) Temp
group by RowNumber; -- 以行号为分组，每个行号最少有1个数据，从名字和null填充
-- 得到结果：
-- Aamina Ashley Christeen Eve
-- Julia Belvet Jane Jennifer
-- Priya Britney Jenny Ketty
-- NULL Maria Kristeen Samantha
-- NULL Meera NULL NULL
-- NULL Naomi NULL NULL
-- NULL Priyanka NULL NULL

--->Binary Tree Nodes
SELECT N,
    CASE WHEN P IS NULL THEN 'Root'
         WHEN N IN (SELECT P FROM BST) THEN 'Inner'
         ELSE 'Leaf'
    END
FROM BST ORDER BY N;

--->New Companies
SELECT bc.company_code,c.founder,COUNT( DISTINCT l.lead_manager_code),COUNT(DISTINCT s.senior_manager_code),COUNT(DISTINCT m.manager_code),COUNT(DISTINCT e.employee_code )
FROM Company c,Lead_Manager l,Senior_Manager s,Manager m,Employee e
WHERE c.company_code=l.company_code AND c.company_code=s.company_code AND c.company_code=m.company_code AND c.company_code=e.company_code
GROUP BY c.company_code,c.founder ORDER BY c.company_code;
-- 注意: 使用group分组时候，需要分组上全部的select，在上述条件中，假如只加上company_code则会报错，需全部的select领域才行，mysql和db2是同一个答案。
-- 注意: where是对数据库表字段的筛选条件，having即在查询结果后再条件筛选！
----------END Advanced Select----------#


----------START Aggregation----------#
--->Revising Aggregations - The Count Function
SELECT COUNT(NAME) FROM CITY WHERE POPULATION>100000;

--->Revising Aggregations - The Sum Function
SELECT SUM(POPULATION) FROM CITY WHERE district='California';

--->Revising Aggregations - Averages
SELECT AVG(population) FROM CITY WHERE district='California';

--->Average Population
SELECT ROUND(AVG(population),0) FROM CITY;

--->Japan Population
SELECT SUM(population) FROM CITY WHERE countrycode='JPN';

--->Population Density Difference
SELECT MAX(population)-MIN(population) FROM CITY;

--->The Blunder
-- MySQL
SELECT CEIL(AVG(salary)-AVG(REPLACE(salary,'0',''))) FROM EMPLOYEES;
-- 注意: ceil为向上取整，round为四舍五入，floor为向下取整

--->Top Earners
SELECT salary*months as money,COUNT(salary*months) FROM Employee GROUP BY salary*months ORDER BY money DESC FETCH FIRST 1 ROWS ONLY;
-- 注意: group by money会错误，因为money不能直接获得

--->Weather Observation Station 2
SELECT CAST(ROUND(SUM(lat_n),2) AS DECIMAL(10,2)), CAST(ROUND(SUM(long_w),2) AS DECIMAL(10,2)) FROM STATION ;
-- 注意: cast到整数并不会四舍五入，而是舍去小数部分，因此需要先round一下，再取出两位小数作为输出

--->Weather Observation Station 13
SELECT CAST(ROUND(SUM(lat_n),4) AS DECIMAL(12,4)) FROM STATION WHERE lat_n BETWEEN 38.7880 AND 137.2345;

--->Weather Observation Station 14
SELECT CAST(MAX(LAT_N) AS DECIMAL(10,4)) FROM STATION WHERE LAT_N<137.2345;
-- 注意: 这里是直接截断小数部分，不是四舍五入

--->Weather Observation Station 15
SELECT CAST(ROUND(LONG_W,4) AS DECIMAL(10,4)) FROM STATION WHERE LAT_N<137.2345 ORDER BY LAT_N DESC FETCH FIRST 1 ROWS ONLY;

--->Weather Observation Station 16
SELECT CAST(ROUND(MIN(LAT_N),4) AS DECIMAL(10,4)) FROM STATION WHERE LAT_N>38.7780;

--->Weather Observation Station 17
SELECT CAST(ROUND(LONG_W,4) AS DECIMAL(10,4)) FROM STATION WHERE LAT_N>38.7780 ORDER BY LAT_N ASC FETCH FIRST 1 ROWS ONLY;

--->Weather Observation Station 18
SELECT CAST(ROUND(MAX(LAT_N)+MAX(LONG_W)-MIN(LAT_N)-MIN(LONG_W),4) AS DECIMAL(10,4)) FROM STATION;
-- Manhattan distance曼哈顿距离：直角距离

--->Weather Observation Station 19
SELECT CAST(ROUND(POWER(POWER(MAX(LAT_N)-MIN(LAT_N),2)+POWER(MAX(LONG_W)-MIN(LONG_W),2),0.5),4) AS DECIMAL(10,4)) FROM STATION;
-- Euclidean Distanc欧几里得距离：直线距离

--->Weather Observation Station 20
SELECT CAST(ROUND(AVG(LAT_N),4) AS DECIMAL(10,4))
FROM
    (SELECT LAT_N,
            ROW_NUMBER() OVER(ORDER BY LAT_N ASC) rn1,
            ROW_NUMBER() OVER(ORDER BY LAT_N DESC) rn2
    FROM STATION
     ) X(LAT_N,rn1,rn2)
WHERE rn1 in (rn2,rn2-1,rn2+1);
-- 注意: 别名有无as均无问题。
-- 这里是求中位数的例子，以下是简化版：
-- select avg(nodes)
-- from (
--     select nodes
--      , row_number() over(order by nodes asc) as rn1
--      , row_number() over(order by nodes desc) as rn2
--     from table
-- ) as x(nodes, rn1, rn2)
-- where rn1 in (rn2, rn2 - 1, rn2 + 1)

----------END Aggregation----------#


----------START Basic Join----------#
--->Asian Population
-- MySQL
SELECT SUM(CITY.POPULATION) FROM CITY,COUNTRY WHERE CITY.COUNTRYCODE=COUNTRY.CODE AND CONTINENT='Asia';

--->African Cities
-- MySQL
SELECT CITY.NAME FROM CITY,COUNTRY WHERE CITY.COUNTRYCODE=COUNTRY.CODE AND CONTINENT='Africa';

--->Average Population of Each Continent
-- MySQL
SELECT COUNTRY.CONTINENT,FLOOR(AVG(CITY.POPULATION)) FROM CITY,COUNTRY WHERE CITY.COUNTRYCODE=COUNTRY.CODE GROUP BY COUNTRY.CONTINENT;

--->The Report
SELECT
    CASE WHEN GRADE<8 THEN 'NULL' ELSE NAME END,
    GRADE,MARKS
FROM STUDENTS,GRADES
WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK
ORDER BY GRADE DESC,NAME ASC;
-- 注意: case用法
-- case
--     when then
--     when then
--     else
-- end,

--->Top Competitors
SELECT h.hacker_id,h.name
FROM Hackers h,Difficulty d,Challenges c,Submissions s
WHERE h.hacker_id=s.hacker_id AND d.difficulty_level=c.difficulty_level AND d.score=s.score AND c.challenge_id=s.challenge_id
GROUP BY h.hacker_id,h.name
HAVING COUNT(s.challenge_id)>1
ORDER BY COUNT(s.challenge_id) DESC,h.hacker_id ASC;
-- 注意: db2的分隔符技巧SELECT CHAR(h.hacker_id) ||','|| CHAR(h.name)可以以,分隔

--->Ollivander's Inventory
SELECT w.id,w_p.age,w.coins_needed,w.power
FROM
    (SELECT w_p.code,w_p.age,MIN(w.coins_needed)
    FROM Wands w,Wands_Property w_p
    WHERE w.code=w_p.code AND w_p.is_evil=0
    GROUP BY w_p.age,w_p.code,w.power
    ) X(group_code,group_age,min_coins_needed),Wands w,Wands_Property w_p
WHERE w_p.age=X.group_age AND w.coins_needed=X.min_coins_needed AND X.group_code=w.code
ORDER BY w.power DESC,w_p.age DESC;
-- 与以下等价：上面是是WHERE关联，然后父子查询，下面是先多查询列再列关联取数
SELECT id,age,coins_needed,power
FROM (
    SELECT
        id,age,coins_needed,power,
        MIN(coins_needed) OVER (PARTITION BY w.code,age,power) AS min_coins
    FROM wands w
    INNER JOIN wands_property wp ON w.code = wp.code
    WHERE wp.is_evil =0
    )
WHERE coins_needed = min_coins
ORDER BY power DESC,age DESC;
-- 注意:INNER JOIN 与 JOIN 是相同的。
-- JOIN 按照功能大致分为如下三类：
-- INNER JOIN（内连接,或等值连接）：取得两个表中存在连接匹配关系的记录。
-- LEFT JOIN（左连接）：取得左表（table1）完全记录，即是右表（table2）并无对应匹配记录。
-- RIGHT JOIN（右连接）：与 LEFT JOIN 相反，取得右表（table2）完全记录，即是左表（table1）并无匹配对应记录。

--->Challenges
SELECT hacker_id,name,c_count
FROM
    (
        SELECT h.hacker_id,h.name,COUNT(c.hacker_id) c_count
        FROM Hackers h
        INNER JOIN Challenges c ON h.hacker_id=c.hacker_id
        GROUP BY c.hacker_id,h.hacker_id,h.name
    )X(hacker_id,name,c_count)
GROUP BY hacker_id,name,c_count
HAVING
    c_count =
        (
            SELECT MAX(count_num)
            FROM
                (
                    SELECT COUNT(hacker_id) count_num
                    FROM Challenges
                    GROUP BY hacker_id
                )X(count_num)
         )
    OR c_count in
        (
            SELECT DISTINCT count_num
            FROM
                (
                    SELECT COUNT(*)
                    FROM Challenges
                    GROUP BY hacker_id
                )X(count_num)
            GROUP BY count_num
            HAVING COUNT(count_num)=1
        )
ORDER BY c_count DESC,hacker_id ASC;
-- 注意: 这里是取最大数或唯一数

--->Contest Leaderboard
SELECT hacker_id,name,SUM(s_score) sum_s_score
FROM
    (
        SELECT h.hacker_id,h.name,MAX(s.score) s_score
        FROM Hackers h
        INNER JOIN Submissions s ON h.hacker_id=s.hacker_id
        GROUP BY h.hacker_id,h.name,s.challenge_id
    )X(hacker_id,name,s_score)
GROUP BY hacker_id,name
HAVING SUM(s_score) != 0
ORDER BY sum_s_score DESC,hacker_id ASC;
-- 注意: HAVING这里不能用别名，需要直接使用源数据

----------END Basic Join----------#


----------START Advanced Join----------#
--->SQL Project Planning
SELECT Start_Date, MIN(End_Date)
FROM
    (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) a,
    (SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) b
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY MIN(End_Date)-Start_Date, Start_Date;

--->Placements
-- SELECT f.id, s.name, f.friend_id, p.salary,friend_p.salary,friend_s.name
SELECT s.name
FROM Students s, Friends f, Packages p,Packages friend_p, Students friend_s
WHERE s.id=f.id AND f.id=p.id AND f.friend_id=friend_p.id AND friend_p.salary>p.salary AND friend_s.id=friend_id
ORDER BY friend_p.salary ASC;
-- 技巧: 自身多列联查

--->Symmetric Pairs
SELECT x,y
FROM Functions f1
WHERE EXISTS (SELECT * FROM Functions f2 WHERE f1.x=f2.y AND f1.y=f2.x AND f1.x<f2.x)
UNION
SELECT x,y
FROM  Functions f3
WHERE f3.x=f3.y AND (SELECT COUNT(*) FROM Functions f4 WHERE f4.x=f4.y AND f3.x=f4.x)>1
ORDER BY x;
-- 技巧: select distinct a,b,c from tableA ==等价于== select a,b,c from tableA group by a,b,c
-- 技巧: UNION SELECT的时候吧ORDER BY放后面是先UNION查询再ORDER排序。
-- 注意: union会过滤掉两个结果集中重复的行，而union all不会过滤掉重复行。

--->Interviews
-- MySQL参考答案
SELECT CT.contest_id,
       CT.hacker_id,
       CT.name,
       Sum(ts),
       Sum(tas),
       Sum(tv),
       Sum(tuv)
FROM   contests CT
       INNER JOIN colleges AS CL
               ON CL.contest_id = CT.contest_id
       INNER JOIN challenges AS CH
               ON CH.college_id = CL.college_id
       LEFT JOIN (SELECT challenge_id,
                         Sum(total_submissions)          AS TS,
                         Sum(total_accepted_submissions) AS TAS
                  FROM   submission_stats
                  GROUP  BY challenge_id) S
              ON S.challenge_id = CH.challenge_id
       LEFT JOIN (SELECT challenge_id,
                         Sum(total_views)        AS TV,
                         Sum(total_unique_views) AS TUV
                  FROM   view_stats
                  GROUP  BY challenge_id) V
              ON V.challenge_id = CH.challenge_id
GROUP  BY CT.contest_id, CT.hacker_id, CT.name
ORDER  BY CT.contest_id;

--->15 Days of Learning SQL
-- MySQL参考答案
select
    submission_date ,
    (SELECT COUNT(distinct hacker_id)
            FROM Submissions s2
            WHERE s2.submission_date = s1.submission_date AND
                (SELECT COUNT(distinct s3.submission_date)
                        FROM Submissions s3
                        WHERE s3.hacker_id = s2.hacker_id AND
                            s3.submission_date < s1.submission_date)
            =
            dateDIFF(s1.submission_date , '2016-03-01')) ,
    (select hacker_id
            from submissions s2
            where s2.submission_date = s1.submission_date
            group by hacker_id
            order by count(submission_id) desc , hacker_id limit 1) as hack,
    (select name
            from hackers
            where hacker_id = hack)
from
    (select distinct submission_date from submissions) s1
group by submission_date;
-- 技巧: 选择最高的可以使用ORDER BY COUNT DESC LIMIT 1

----------END Advanced Join----------#


----------START Alternative Queries----------#
--->Draw The Triangle 1
-- MySQL
SELECT REPEAT('* ', @P := @P - 1)
FROM information_schema.tables, (SELECT @P:=21) t LIMIT 20;
-- 注意: 这里使用一个技巧，就是借用information_schema.tables这个表（多于20行），逐次查询并递减，如果去掉那个系统表，会只输出一行。
-- 这里的REPEAT会带有空格。
-- Output:
-- * * *
-- * *
-- *

--->Draw The Triangle 2
-- MySQL
SELECT REPEAT('* ', @P := @P + 1)
FROM information_schema.tables, (SELECT @P:=0) t LIMIT 20;

--->Print Prime Numbers
SELECT '2&3&5&7&11&13&17&19&23&29&31&37&41&43&47&53&59&61&67&71&73&79&83&89&97&101&103&107&109&113&127&131&137&139&149&151&157&163&167&173&179&181&191&193&197&199&211&223&227&229&233&239&241&251&257&263&269&271&277&281&283&293&307&311&313&317&331&337&347&349&353&359&367&373&379&383&389&397&401&409&419&421&431&433&439&443&449&457&461&463&467&479&487&491&499&503&509&521&523&541&547&557&563&569&571&577&587&593&599&601&607&613&617&619&631&641&643&647&653&659&661&673&677&683&691&701&709&719&727&733&739&743&751&757&761&769&773&787&797&809&811&821&823&827&829&839&853&857&859&863&877&881&883&887&907&911&919&929&937&941&947&953&967&971&977&983&991&997';

----------END Alternative Queries----------#

