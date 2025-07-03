'''
Users By Average Session Time


Last Updated: July 2025

Medium
ID 10352

752

Calculate each user's average session time, where a session is defined as the time difference between a page_load and a page_exit. Assume each user has only one session per day. If there are multiple page_load or page_exit events on the same day, use only the latest page_load and the earliest page_exit, ensuring the page_load occurs before the page_exit. Output the user_id and their average session time.

Table
facebook_web_log
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

user_id	avg_session_duration
0	1883.5
1	35
facebook_web_log
Preview
user_id	timestamp	action
0	2019-04-25 13:30:15	page_load
0	2019-04-25 13:30:18	page_load
0	2019-04-25 13:30:40	scroll_down
0	2019-04-25 13:30:45	scroll_up
0	2019-04-25 13:31:10	scroll_down
0	2019-04-25 13:31:25	scroll_down
0	2019-04-25 13:31:40	page_exit
1	2019-04-25 13:40:00	page_load
1	2019-04-25 13:40:10	scroll_down
1	2019-04-25 13:40:15	scroll_down
1	2019-04-25 13:40:20	scroll_down
1	2019-04-25 13:40:25	scroll_down
1	2019-04-25 13:40:30	scroll_down
1	2019-04-25 13:40:35	page_exit
2	2019-04-25 13:41:21	page_load
2	2019-04-25 13:41:30	scroll_down
2	2019-04-25 13:41:35	scroll_down
2	2019-04-25 13:41:40	scroll_up
1	2019-04-26 11:15:00	page_load
1	2019-04-26 11:15:10	scroll_down
1	2019-04-26 11:15:20	scroll_down
1	2019-04-26 11:15:25	scroll_up
1	2019-04-26 11:15:35	page_exit
0	2019-04-28 14:30:15	page_load
0	2019-04-28 14:30:10	page_load
0	2019-04-28 13:30:40	scroll_down
0	2019-04-28 15:31:40	page_exit
user_id:
bigint
timestamp:
timestamp
action:
string
'''

# Not able to solve getting wrong answer
# Import your libraries
import pyspark
from pyspark.sql.window import Window
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark.sql.types import *
# Start writing code
# facebook_web_log
df=facebook_web_log
# print(df.count())
df=df.filter((df.action == "page_load") |  (df.action == "page_exit") )
# print(df.count())
df=df.withColumn("timestamp1",df["timestamp"].cast(DateType()))
# df.show(truncate=False)
window = Window.partitionBy("user_id","action","timestamp1").orderBy("user_id","timestamp1")
df1=df.withColumn("rnk",row_number().over(window))
# df1.show(50,truncate=False)
df2=df1.filter(df1.action == "page_load")
df3=df1.filter(df1.action == "page_exit")
# df2.show(truncate=False)
# df3.show(truncate=False)
df2=df2.withColumn("max_rnk",max("rnk").over(window))
df3=df3.withColumn("min_rnk",min("rnk").over(window))
# df2.show(truncate=False)
# df3.show(truncate=False)
# df2=df2.filter(df2.rnk == df2.max_rnk)
# df3=df3.filter(df3.rnk == df3.min_rnk)
df3=df3.withColumnRenamed("action","action1")
df3=df3.withColumnRenamed("timestamp","timestamp2")
df2_alias = df2.alias("df2")
df3_alias = df3.alias("df3")
# df2.show(truncate=False)
# df3.show(truncate=False)
# df4=df2.join(df3,(df2.user_id==df3.user_id) ,"left").filter(df3.timestamp2<df2.timestamp)
df4=df2_alias.join(df3_alias,(df2_alias.user_id == df3_alias.user_id),"left").filter(df2_alias.timestamp<df3_alias.timestamp2)
# df4.show(truncate=False)
df4=df4.groupBy("df2.user_id","df2.timestamp1").agg({"timestamp":"max","timestamp2":"min"})
df4=df4.withColumn("duration",col("min(timestamp2)").cast("long")-col("max(timestamp)").cast("long"))
df4=df4.groupBy("user_id").agg(mean("duration")).withColumnRenamed("avg(duration)","avg_session_duration")
# df4.show(truncate=False)
df4.toPandas()