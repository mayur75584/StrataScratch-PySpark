'''
Highest Salary In Department


Last Updated: June 2025

Medium
ID 9897

147

Find the employee with the highest salary per department.
Output the department name, employee's first name along with the corresponding salary.

Table
employee
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

department	first_name	salary
Audit	Shandler	1100
Management	Richerd	250000
Sales	Mick	2200
employee
Preview
id	first_name	last_name	age	sex	employee_title	department	salary	target	bonus	email	city	address	manager_id
5	Max	George	26	M	Sales	Sales	1300	200	150	Max@company.com	California	2638 Richards Avenue	1
13	Katty	Bond	56	F	Manager	Management	150000	0	300	Katty@company.com	Arizona		1
11	Richerd	Gear	57	M	Manager	Management	250000	0	300	Richerd@company.com	Alabama		1
10	Jennifer	Dion	34	F	Sales	Sales	1000	200	150	Jennifer@company.com	Alabama		13
19	George	Joe	50	M	Manager	Management	100000	0	300	George@company.com	Florida	1003 Wyatt Street	1
18	Laila	Mark	26	F	Sales	Sales	1000	200	150	Laila@company.com	Florida	3655 Spirit Drive	11
20	Sarrah	Bicky	31	F	Senior Sales	Sales	2000	200	150	Sarrah@company.com	Florida	1176 Tyler Avenue	19
21	Suzan	Lee	34	F	Sales	Sales	1300	200	150	Suzan@company.com	Florida	1275 Monroe Avenue	19
22	Mandy	John	31	F	Sales	Sales	1300	200	150	Mandy@company.com	Florida	2510 Maryland Avenue	19
23	Britney	Berry	45	F	Sales	Sales	1200	200	100	Britney@company.com	Florida	3946 Steve Hunt Road	19
25	Jack	Mick	29	M	Sales	Sales	1300	200	100	Jack@company.com	Hawaii	3762 Stratford Drive	19
26	Ben	Ten	43	M	Sales	Sales	1300	150	100	Ben@company.com	Hawaii	3055 Indiana Avenue	19
27	Tom	Fridy	32	M	Sales	Sales	1200	200	150	Tom@company.com	Hawaii	801 Stratford Drive	1
29	Antoney	Adam	34	M	Sales	Sales	1300	180	150	Antoney@company.com	Hawaii	3533 Randall Drive	1
28	Morgan	Matt	25	M	Sales	Sales	1200	200	150	Morgan@company.com	Hawaii	2641  Randall Drive	1
6	Molly	Sam	28	F	Sales	Sales	1400	100	150	Molly@company.com	Arizona	3632 Polk Street	13
7	Nicky	Bat	33	F	Sales	Sales	1400	400	100	Molly@company.com	Arizona	3461 Preston Street	13
9	Monika	William	33	F	Sales	Sales	1000	200	100	Molly@company.com	Alabama		13
17	Mick	Berry	44	M	Senior Sales	Sales	2200	200	150	Mick@company.com	Florida		11
12	Shandler	Bing	23	M	Auditor	Audit	1100	200	150	Shandler@company.com	Arizona		11
14	Jason	Tom	23	M	Auditor	Audit	1000	200	150	Jason@company.com	Arizona		11
16	Celine	Anston	27	F	Auditor	Audit	1000	200	150	Celine@company.com	Colorado		11
15	Michale	Jackson	44	F	Auditor	Audit	700	150	150	Michale@company.com	Colorado		11
24	Adam	Morris	30	M	Sales	Sales	1300	200	100	Adam@company.com	Alabama	4541  Ferry Street	19
30	Mark	Jon	28	M	Sales	Sales	1200	200	150	Mark@company.com	Alabama	2522  George Avenue	1
8	John	Ford	26	M	Senior Sales	Sales	1500	140	100	Molly@company.com	Alabama	4832  New Creek Road	13
1	Allen	Wang	55	F	Manager	Management	200000	0	300	Allen@company.com	California	1069 Ventura Drive	1
2	Joe	Jack	32	M	Sales	Sales	1000	200	150	Joe@company.com	California	995 Jim Rosa Lane	1
3	Henry	Ted	31	M	Senior Sales	Sales	2000	200	150	Henry@company.com	California	1609 Ford Street	1
4	Sam	Mark	25	M	Sales	Sales	1000	120	150	Sam@company.com	California	4869 Libby Street	1
id:
bigint
first_name:
string
last_name:
string
age:
bigint
sex:
string
employee_title:
string
department:
string
salary:
bigint
target:
bigint
bonus:
bigint
email:
string
city:
string
address:
string
manager_id:
bigint
'''


# Import your libraries
import pyspark
from pyspark.sql import *
from pyspark.sql.functions import *

# Start writing code
df=employee
df1=df.groupBy(col("department")).agg(max(col("salary")).alias("salary"))
df1=df1.withColumnRenamed("department","dpt").withColumnRenamed("salary","sal")
# df1.show(truncate=False)
df=df1.join(df,df1.sal==df.salary,"left")
# df.show(truncate=False)
df=df.drop("department","salary")
df=df.withColumnRenamed("dpt","department").withColumnRenamed("sal","salary")
df=df.select("department","first_name","salary")
# df.show(truncate=False)
# To validate your solution, convert your final pySpark df to a pandas df
# employee.toPandas()
df.toPandas()