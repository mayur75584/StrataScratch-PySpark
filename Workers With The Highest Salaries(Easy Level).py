'''
Workers With The Highest Salaries


Last Updated: July 2025

Easy
ID 10353

615

Find the job titles of the employees with the highest salary. If multiple employees have the same highest salary, include the job titles for all such employees.

Tables
worker
title
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

best_paid_title
Asst. Manager
Manager
worker
Preview
worker_id	first_name	last_name	salary	joining_date	department
1	Monika	Arora	100000	2014-02-20	HR
2	Niharika	Verma	80000	2014-06-11	Admin
3	Vishal	Singhal	300000	2014-02-20	HR
4	Amitah	Singh	500000	2014-02-20	Admin
5	Vivek	Bhati	500000	2014-06-11	Admin
6	Vipul	Diwan	200000	2014-06-11	Account
7	Satish	Kumar	75000	2014-01-20	Account
8	Geetika	Chauhan	90000	2014-04-11	Admin
9	Agepi	Argon	90000	2015-04-10	Admin
10	Moe	Acharya	65000	2015-04-11	HR
11	Nayah	Laghari	75000	2014-03-20	Account
12	Jai	Patel	85000	2014-03-21	HR
worker_id:
bigint
first_name:
string
last_name:
string
salary:
bigint
joining_date:
date
department:
string
title
Preview
worker_ref_id	worker_title	affected_from
1	Manager	2016-02-20
2	Executive	2016-06-11
8	Executive	2016-06-11
5	Manager	2016-06-11
4	Asst. Manager	2016-06-11
7	Executive	2016-06-11
6	Lead	2016-06-11
3	Lead	2016-06-11
worker_ref_id:
bigint
worker_title:
string
affected_from:
date
'''

# Import your libraries
import pyspark
from pyspark.sql.functions import *
# Start writing code
# worker.show(truncate=False)
# title.show(truncate=False)
df = worker.join(title, worker.worker_id == title.worker_ref_id,"right")
df1 = df.sort(col("salary").desc(), col("worker_title").asc()).select("salary").limit(1)
# df1.show(truncate=False)
df=df.sort(col("salary").desc(), col("worker_title").asc())
# df.show(truncate=False)
df1_lst = [data[0] for data in df1.select('salary').collect()]
# print(df1_lst)
df = df.where(col("salary")== df1_lst[0]).select("worker_title")
df=df.withColumnRenamed("worker_title","best_paid_title")
# df.show(truncate=False)
# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()