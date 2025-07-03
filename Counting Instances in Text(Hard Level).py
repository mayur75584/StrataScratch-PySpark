'''
Counting Instances in Text


Last Updated: July 2025

Hard
ID 9814

125

Find the number of times the exact words bull and bear appear in the contents column.


Count all occurrences, even if they appear multiple times within the same row. Matches should be case-insensitive and only count exact words, that is, exclude substrings like bullish or bearing.


Output the word (bull or bear) and the corresponding number of occurrences.

Table
google_file_store
More about this question
Hints
Expected Output
google_file_store
Preview
filename	contents
draft1.txt	The stock exchange predicts a bull market which would make many investors happy.
draft2.txt	The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market.
final.txt	The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market. As always predicting the future market is an uncertain game and all investors should follow their instincts and best practices.
filename:
string
contents:
string
'''

# Import your libraries
import pyspark
from pyspark.sql.functions import *
# Start writing code
x=google_file_store.select(split("contents","\\s+").alias('w_contents'))
# print(x)
y=x.select(explode(col("w_contents")).alias("word"))
# y.show(truncate=False)
z=y.groupBy(col("word")).count()
bull=z.where(col("word")=="bull").withColumnRenamed("count","nentry")
# bull.show(truncate=False)
bear=z.where(col("word")=="bear").withColumnRenamed("count","nentry")
# bear.show(truncate=False)
df=bull.unionAll(bear)
# df.show(truncate=False)

# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()