'''
Consecutive Days


Last Updated: June 2025

Hard
ID 2054

61

Find all the users who were active for 3 consecutive days or more.

Table
sf_events
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

user_id
U4
sf_events
Preview
record_date	account_id	user_id
2021-01-01	A1	U1
2021-01-01	A1	U2
2021-01-06	A1	U3
2021-01-02	A1	U1
2020-12-24	A1	U2
2020-12-08	A1	U1
2020-12-09	A1	U1
2021-01-10	A2	U4
2021-01-11	A2	U4
2021-01-12	A2	U4
2021-01-15	A2	U5
2020-12-17	A2	U4
2020-12-25	A3	U6
2020-12-25	A3	U6
2020-12-25	A3	U6
2020-12-06	A3	U7
2020-12-06	A3	U6
2021-01-14	A3	U6
2021-02-07	A1	U1
2021-02-10	A1	U2
2021-02-01	A2	U4
2021-02-01	A2	U5
2020-12-05	A1	U8
record_date:
date
account_id:
string
user_id:
string
'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *
from pyspark.sql.window import *
# Start writing code
df=sf_events

window_spec = Window.partitionBy("user_id").orderBy("account_id","record_date")

# df_window = df.withColumn("rw_num",row_number().over(window_spec))

df = df.withColumn("next_date",lead("record_date",1).over(window_spec)).withColumn("prev_date",lag("record_date",1).over(window_spec))
df = df.withColumn("date_diff_lead",datediff(to_date("next_date","yyyy-mm-dd"),to_date("record_date","yyyy-mm-dd"))).withColumn("date_diff_lag",datediff(to_date("record_date","yyyy-mm-dd"),to_date("prev_date","yyyy-mm-dd")))

df = df.filter((df.date_diff_lead == df.date_diff_lag) & (df.date_diff_lead ==1) & (df.date_diff_lag == 1))

# df.show(50,truncate=False)

result_df = df.select("user_id")

result_df.toPandas()
# To validate your solution, convert your final pySpark df to a pandas df
# sf_events.toPandas()