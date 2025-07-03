'''
Share of Active Users


Last Updated: June 2025

Medium
ID 2005

140

Calculate the percentage of users who are both from the US and have an 'open' status, as indicated in the fb_active_users table.

Table
fb_active_users
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

us_active_share
13.04
fb_active_users
Preview
user_id	name	status	country
33	Amanda Leon	open	Australia
27	Jessica Farrell	open	Luxembourg
18	Wanda Ramirez	open	USA
50	Samuel Miller	closed	Brazil
16	Jacob York	open	Australia
25	Natasha Bradford	closed	USA
34	Donald Ross	closed	China
52	Michelle Jimenez	open	USA
11	Theresa John	open	China
37	Michael Turner	closed	Australia
32	Catherine Hurst	closed	Mali
61	Tina Turner	open	Luxembourg
4	Ashley Sparks	open	China
82	Jacob York	closed	USA
87	David Taylor	closed	USA
78	Zachary Anderson	open	China
5	Tiger Leon	closed	China
56	Theresa Weaver	closed	Brazil
21	Tonya Johnson	closed	Mali
89	Kyle Curry	closed	Mali
7	Donald Jim	open	USA
22	Michael Bone	open	Canada
31	Sara Michaels	open	Denmark
user_id:
bigint
name:
string
status:
string
country:
string
'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *

# Start writing code
df = fb_active_users
df.filter(df.country=='USA')
cnt= df.count()
# print(cnt)
df1=df.filter(df.status=='open')
cnt1=df1.count()
# print(cnt1)
# print(cnt1/cnt)
df=df.withColumn("active_users_share",round(lit(cnt1/cnt),1))
df=df.select("active_users_share")
# To validate your solution, convert your final pySpark df to a pandas df
# fb_active_users.toPandas()
df.toPandas().head(1)