'''
Count Occurrences Of Words In Drafts


Last Updated: June 2025

Medium
ID 9817

100

Find the number of times each word appears in the contents column across all rows in the google_file_store dataset. Output two columns: word and occurrences.

Table
google_file_store
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

word	occurrences
market	6
a	5
investors	4
the	4
and	4
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
import pandas as pd
import pyspark
from pyspark.sql.functions import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()
dict1={}
# Start writing code
# google_file_store.show(truncate=False)
google_file_store1 = google_file_store.filter(col("filename").contains("draft"))
# google_file_store1.show(truncate=False)
contents=list(google_file_store1.select("contents").toPandas()["contents"])
# # print(contents,type(contents))
lst_contents=[]
for i in contents:
    i=i.replace('.','')
    i=i.replace(',','')
#     # print(i.split())
    lst_contents.extend(i.split())
# # print(lst_contents)
for i in lst_contents:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i]+=1
# print(dict1)
# lst_key = list(dict1.keys())
# lst_val = list(dict1.values())
# data = list(zip(lst_key,lst_val))
# print(data)
# google_file_store = spark.createDataFrame(data, ["word","occurrences"])
# google_file_store.show(truncate=False)
# To validate your solution, convert your final pySpark df to a pandas df
# google_file_store.toPandas()
dict2={'word':[],'occurrences':[]}
for i,j in dict1.items():
    dict2['word'].append(i)
    dict2['occurrences'].append(j)
# print(dict2)

df=pd.DataFrame(dict2)