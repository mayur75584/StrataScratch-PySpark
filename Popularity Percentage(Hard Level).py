'''
Popularity Percentage


Last Updated: June 2025

Hard
ID 10284

242

Find the popularity percentage for each user on Meta/Facebook. The dataset contains two columns, user1 and user2, which represent pairs of friends. Each row indicates a mutual friendship between user1 and user2, meaning both users are friends with each other. A user's popularity percentage is calculated as the total number of friends they have (counting connections from both user1 and user2 columns) divided by the total number of unique users on the platform. Multiply this value by 100 to express it as a percentage.


Output each user along with their calculated popularity percentage. The results should be ordered by user ID in ascending order.

Table
facebook_friends
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

user1	popularity
1	55.56
2	33.33
3	33.33
4	11.11
5	11.11
facebook_friends
Preview
user1	user2
2	1
1	3
4	1
1	5
1	6
2	6
7	2
8	3
3	9
user1:
bigint
user2:
bigint
'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *
# Start writing code

facebook_friends1 = facebook_friends.select("user1").union(facebook_friends.select("user2"))
cnt=facebook_friends1.distinct().count()
# print(cnt)
facebook_friends1=facebook_friends1.distinct().orderBy("user1")
# facebook_friends1.show(truncate=False)
facebook_friends=facebook_friends.unionAll(facebook_friends.select("user2","user1"))
# facebook_friends.show(truncate=False)
facebook_friends=facebook_friends.groupBy("user1").agg(count("user2").alias("number_of_users"))
facebook_friends=facebook_friends.withColumn("popularity",round((col("number_of_users")/cnt)*100,3))
facebook_friends = facebook_friends.select("user1","popularity").orderBy("user1")
facebook_friends.show(truncate=False)
# To validate your solution, convert your final pySpark df to a pandas df
facebook_friends.toPandas()