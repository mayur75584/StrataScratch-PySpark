'''
Customer Revenue In March


Last Updated: June 2025

Medium
ID 9782

142

Calculate the total revenue from each customer in March 2019. Include only customers who were active in March 2019. An active user is a customer who made at least one transaction in March 2019.


Output the revenue along with the customer id and sort the results based on the revenue in descending order.

Table
orders
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

cust_id	revenue
3	210
15	150
7	80
12	20
orders
Preview
id	cust_id	order_date	order_details	total_order_cost
1	3	2019-03-04	Coat	100
2	3	2019-03-01	Shoes	80
3	3	2019-03-07	Skirt	30
4	7	2019-02-01	Coat	25
5	7	2019-03-10	Shoes	80
6	15	2019-02-01	Boats	100
7	15	2019-01-11	Shirts	60
8	15	2019-03-11	Slipper	20
9	15	2019-03-01	Jeans	80
10	15	2019-03-09	Shirts	50
11	5	2019-02-01	Shoes	80
12	12	2019-01-11	Shirts	60
13	12	2019-03-11	Slipper	20
14	4	2019-02-01	Shoes	80
15	4	2019-01-11	Shirts	60
16	3	2019-04-19	Shirts	50
17	7	2019-04-19	Suit	150
18	15	2019-04-19	Skirt	30
19	15	2019-04-20	Dresses	200
20	12	2019-01-11	Coat	125
21	7	2019-04-01	Suit	50
22	7	2019-04-02	Skirt	30
23	7	2019-04-03	Dresses	50
24	7	2019-04-04	Coat	25
25	7	2019-04-19	Coat	125
26	3	2019-04-20	Gloves	20
27	3	2019-04-21	Tie	25
28	3	2019-04-22	Cap	15
29	3	2019-04-23	Jacket	120
30	1	2019-04-19	Jacket	150
31	1	2019-04-19	Shoes 	125
id:
bigint
cust_id:
bigint
order_date:
date
order_details:
string
total_order_cost:
bigint
'''

# Import your libraries
import pyspark
from pyspark.sql.functions import *
from pyspark.sql import *
# Start writing code
df=orders
df=df.withColumn("date",date_format(to_date("order_date","yyyy-MM-dd"),"yyyy-MM"))
df=df.filter(col("date")=="2019-03")
# df.show(truncate=False)
df=df.groupBy(col("cust_id")).agg(sum(col("total_order_cost")).alias("revenue"))
df=df.orderBy(col("revenue").desc())
# df.show(truncate=False)
# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()
# orders.toPandas()