'''
Customer Tracking


Last Updated: June 2025

Shopify
Amazon
Hard
ID 2136

41

Data Engineer
Data Scientist
BI Analyst
Data Analyst
ML Engineer
Given the users' sessions logs on a particular day, calculate how many hours each user was active that day.


Note: The session starts when state=1 and ends when state=0.

Table: cust_tracking
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

cust_id	sum(time_diff)
c001	5
c002	4.5
c003	1.5
c004	2
c005	7.5
cust_tracking
Preview
cust_id	state	timestamp
c001	1	2024-11-26 07:00:00
c001	0	2024-11-26 09:30:00
c001	1	2024-11-26 12:00:00
c001	0	2024-11-26 14:30:00
c002	1	2024-11-26 08:00:00
c002	0	2024-11-26 09:30:00
c002	1	2024-11-26 11:00:00
c002	0	2024-11-26 12:30:00
c002	1	2024-11-26 15:00:00
c002	0	2024-11-26 16:30:00
c003	1	2024-11-26 09:00:00
c003	0	2024-11-26 10:30:00
c004	1	2024-11-26 10:00:00
c004	0	2024-11-26 10:30:00
c004	1	2024-11-26 14:00:00
c004	0	2024-11-26 15:30:00
c005	1	2024-11-26 10:00:00
c005	0	2024-11-26 14:30:00
c005	1	2024-11-26 15:30:00
c005	0	2024-11-26 18:30:00
cust_id:
string
state:
bigint
timestamp:
timestamp
'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *
from pyspark.sql.window import *
# Start writing code
df=cust_tracking
window_spec = Window.orderBy("cust_id","timestamp")

df=df.withColumn("next",lead("timestamp",1).over(window_spec))
df=df.filter(df.state==1)
# df.show(truncate=False)
df=df.withColumn("time_diff_hours",round((unix_timestamp(col("next"))-unix_timestamp(col("timestamp"))))) #Dividing by 3600 so that to get difference in hours
df=df.groupBy("cust_id").agg((sum("time_diff_hours")/3600).alias("sum(time_diff)"))
# df.show(truncate=False)
df.toPandas()
# To validate your solution, convert your final pySpark df to a pandas df
# cust_tracking.toPandas()