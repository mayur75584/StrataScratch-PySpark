'''
Processed Ticket Rate By Type


Last Updated: June 2025

Medium
ID 9781

105

Find the processed rate of tickets for each type. The processed rate is defined as the number of processed tickets divided by the total number of tickets for that type. Round this result to two decimal places.

Table
facebook_complaints
More about this question
Hints
Expected Output
facebook_complaints
Preview
complaint_id	type	processed
0	0	TRUE
1	0	TRUE
2	0	FALSE
3	1	TRUE
4	1	TRUE
5	1	FALSE
complaint_id:
bigint
type:
bigint
processed:
boolean
'''

# Import your libraries
import pyspark
from pyspark.sql.functions import *

# Start writing code
df = facebook_complaints
df_total = df.groupBy(col("type")).count()
df_total = df_total.withColumnRenamed("count","cnt_total")
# df_total.show(truncate=False)
df_processed = df.filter(df.processed==True)
df_processed = df_processed.groupBy(col("type")).count()
df_processed = df_processed.withColumnRenamed("count","cnt_processed")
df_processed = df_processed.withColumnRenamed("type","type1")
# df_processed.show(truncate=False)
df_ans = df_total.join(df_processed, df_total.type == df_processed.type1, "outer")
df_ans = df_ans.select("type","cnt_total","cnt_processed")
df_ans = df_ans.withColumn("processed_rate",round(col("cnt_processed")/col("cnt_total"),2))
df_ans = df_ans.select("type","processed_rate")
# df_ans.show(truncate=False)
df_ans.toPandas()
# To validate your solution, convert your final pySpark df to a pandas df
# facebook_complaints.toPandas()