'''
Election Results


Last Updated: June 2025

Medium
ID 2099

190

The election is conducted in a city and everyone can vote for one or more candidates, or choose not to vote at all. Each person has 1 vote so if they vote for multiple candidates, their vote gets equally split across these candidates. For example, if a person votes for 2 candidates, these candidates receive an equivalent of 0.5 vote each. Some voters have chosen not to vote, which explains the blank entries in the dataset.


Find out who got the most votes and won the election. Output the name of the candidate or multiple names in case of a tie.
To avoid issues with a floating-point error you can round the number of votes received by a candidate to 3 decimal places.

Table
voting_results
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

candidate
Christine 
voting_results
Preview
voter	candidate
Kathy	
Charles	Ryan 
Charles	Christine 
Charles	Kathy 
Benjamin	Christine 
Anthony	Paul 
Anthony	Anthony 
Edward	Ryan 
Edward	Paul 
Edward	Kathy 
Terry	
Nancy	Ryan 
Nancy	Nicole 
Nancy	Paul 
Nancy	Christine 
Nancy	Kathy 
Evelyn	Anthony 
Evelyn	Christine 
Evelyn	Paul 
Evelyn	Nicole 
Shirley	Ryan 
Shirley	Nicole 
Shirley	Kathy 
Shirley	Anthony 
Victor	
Bobby	Ryan 
Bobby	Christine 
Helen	Ryan 
Helen	Christine 
Helen	Kathy 
Helen	Nicole 
Kevin	Ryan 
Kevin	Kathy 
Kevin	Paul 
Betty	
Andrew	Ryan 
Andrew	Christine 
Martha	Ryan 
Martha	Anthony 
Marie	Anthony 
Alan	Christine 
Matthew	Nicole 
Matthew	Christine 
Arthur	
Joyce	
Ryan	Ryan 
Nicole	Nicole 
Paul	
Christine	Christine 
Christine	Ryan 
Kathy	Kathy 
Kathy	Christine 
Kathy	Ryan 
Kathy	Nicole 
Anthony	Anthony 
Anthony	Ryan 
Anthony	Paul 
voter:
string
candidate:
string
'''

# Import your libraries
import pyspark
from pyspark.sql import *
from pyspark.sql.functions import *
# Start writing code
df = voting_results

df1 = df.filter(col("candidate").isNotNull())
# df1.show(50,truncate=False)

df2 = df1.groupby("voter").agg((1/count(df.voter)).alias("cnt"))
# df2.show(truncate=False)

df3 = df1.join(df2, df1["voter"]==df2["voter"])
# df3.show(truncate=False)
df3 = df3.groupby("candidate").agg(sum(col("cnt")).alias("sum_cnt"))
df3 = df3.orderBy(["sum_cnt"],ascending=[False])
# df3.show(truncate=False)

# To validate your solution, convert your final pySpark df to a pandas df
df3.toPandas()["candidate"].head(1)