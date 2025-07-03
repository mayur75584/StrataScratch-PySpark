'''
Matching Similar Hosts and Guests


Last Updated: June 2025

Medium
ID 10078

135

Find matching hosts and guests pairs in a way that they are both of the same gender and nationality.
Output the host id and the guest id of matched pair.

Tables
airbnb_hosts
airbnb_guests
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

host_id	guest_id
11	11
4	0
0	9
10	6
8	3
airbnb_hosts
Preview
host_id	nationality	gender	age
0	USA	M	28
1	USA	F	29
2	China	F	31
3	China	M	24
4	Mali	M	30
5	Mali	F	30
6	Luxembourg	M	25
7	Luxembourg	F	25
8	Australia	F	33
9	Australia	M	35
10	Brazil	M	39
11	Brazil	F	42
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
1	USA	F	29
2	China	F	31
3	China	M	24
4	Mali	M	30
5	Mali	F	30
6	Luxembourg	M	25
7	Luxembourg	F	25
8	Australia	F	33
9	Australia	M	35
10	Brazil	M	39
11	Brazil	F	42
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
1	USA	F	29
2	China	F	31
3	China	M	24
4	Mali	M	30
5	Mali	F	30
6	Luxembourg	M	25
7	Luxembourg	F	25
8	Australia	F	33
9	Australia	M	35
10	Brazil	M	39
11	Brazil	F	42
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
1	USA	F	29
2	China	F	31
3	China	M	24
4	Mali	M	30
5	Mali	F	30
6	Luxembourg	M	25
7	Luxembourg	F	25
8	Australia	F	33
9	Australia	M	35
10	Brazil	M	39
11	Brazil	F	42
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
1	USA	F	29
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
1	USA	F	29
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
1	USA	F	29
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
1	USA	F	29
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
0	USA	M	28
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
6	Luxembourg	M	25
7	Luxembourg	F	25
host_id:
bigint
nationality:
string
gender:
string
age:
bigint
airbnb_guests
Preview
guest_id	nationality	gender	age
0	Mali	M	21
1	China	F	23
2	Mali	F	27
3	Australia	F	24
4	Luxembourg	M	19
5	USA	F	33
6	Brazil	M	32
7	China	M	27
8	Australia	M	37
9	USA	M	29
10	Luxembourg	F	28
11	Brazil	F	24
guest_id:
bigint
nationality:
string
gender:
string
age:
bigint
'''

# Import your libraries
import pyspark

# Start writing code
df=airbnb_hosts
df1=airbnb_guests

df2 = df.join(df1,(df.nationality == df1.nationality) & (df.gender == df1.gender), "left")
df2 = df2.select("host_id","guest_id").distinct()
# df2.show(truncate=False)
# To validate your solution, convert your final pySpark df to a pandas df
# airbnb_hosts.toPandas()
df2.toPandas()