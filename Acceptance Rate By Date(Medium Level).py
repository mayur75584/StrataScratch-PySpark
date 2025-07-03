'''
Acceptance Rate By Date


Last Updated: July 2025

Medium
ID 10285

363

Calculate the friend acceptance rate for each date when friend requests were sent. A request is sent if action = sent and accepted if action = accepted. If a request is not accepted, there is no record of it being accepted in the table. The output will only include dates where requests were sent and at least one of them was accepted, as the acceptance rate can only be calculated for those dates. Show the results ordered from the earliest to the latest date.

Table
fb_friend_requests
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

request_date	percentage_acceptance
2020-01-04	0.75
2020-01-06	0.67
fb_friend_requests
Preview
user_id_sender	user_id_receiver	date	action
ad4943sdz	948ksx123d	2020-01-04	sent
ad4943sdz	948ksx123d	2020-01-06	accepted
dfdfxf9483	9djjjd9283	2020-01-04	sent
dfdfxf9483	9djjjd9283	2020-01-15	accepted
ffdfff4234234	lpjzjdi4949	2020-01-06	sent
fffkfld9499	993lsldidif	2020-01-06	sent
fffkfld9499	993lsldidif	2020-01-10	accepted
fg503kdsdd	ofp049dkd	2020-01-04	sent
fg503kdsdd	ofp049dkd	2020-01-10	accepted
hh643dfert	847jfkf203	2020-01-04	sent
r4gfgf2344	234ddr4545	2020-01-06	sent
r4gfgf2344	234ddr4545	2020-01-11	accepted
user_id_sender:
string
user_id_receiver:
string
date:
date
action:
string
'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *
from pyspark.sql import *
# Start writing code
df=fb_friend_requests
df_sent=df.filter(col("action")=="sent")
df_accepted=df.filter(col("action")=="accepted")
df_accepted=df_accepted.withColumnRenamed("date","date1").withColumnRenamed("user_id_sender","user_id_sender1").withColumnRenamed("user_id_receiver","user_id_receiver1")
# df_sent.show(truncate=False)
# df_accepted.show(truncate=False)
df_sent_cnt=df_sent.groupBy(col("date")).agg(count(col("user_id_sender")).alias("cnt"))
# df_sent_cnt.show(truncate=False)
df_sent_accepted = df_sent.join(df_accepted,df_sent.user_id_sender==df_accepted.user_id_sender1,"right")
df_sent_accepted=df_sent_accepted.groupBy(col("date")).agg(count(col("user_id_sender")).alias("cnt1"))
df_sent_accepted=df_sent_accepted.withColumnRenamed("date","date2")
# df_sent_accepted.show(truncate=False)
df_sent_accepted=df_sent_accepted.join(df_sent_cnt,df_sent_accepted.date2==df_sent_cnt.date,"left").select("date","cnt","cnt1")
df_sent_accepted=df_sent_accepted.withColumn("percentage_acceptance",round(col("cnt1")/col("cnt"),2)).withColumnRenamed("date","request_date")
df_sent_accepted=df_sent_accepted.select("request_date","percentage_acceptance")
# df_sent_accepted.show(truncate=False)
df_sent_accepted.toPandas()
# To validate your solution, convert your final pySpark df to a pandas df
# fb_friend_requests.toPandas()