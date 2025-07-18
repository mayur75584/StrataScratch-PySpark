'''
Finding User Purchases


Last Updated: July 2025

Medium
ID 10322

559

Identify returning active users by finding users who made a second purchase within 1 to 7 days after their first purchase. Ignore same-day purchases. Output a list of these user_ids.

Table
amazon_transactions
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

user_id
130
143
103
114
111
amazon_transactions
Preview
id	user_id	item	created_at	revenue
1	109	milk	2020-03-03	123
2	139	biscuit	2020-03-18	421
3	120	milk	2020-03-18	176
4	108	banana	2020-03-18	862
5	130	milk	2020-03-28	333
6	103	bread	2020-03-29	862
7	122	banana	2020-03-07	952
8	125	bread	2020-03-13	317
9	139	bread	2020-03-30	929
10	141	banana	2020-03-17	812
11	116	bread	2020-03-31	226
12	128	bread	2020-03-04	112
13	146	biscuit	2020-03-04	362
14	119	banana	2020-03-28	127
15	142	bread	2020-03-09	503
16	122	bread	2020-03-06	593
17	128	biscuit	2020-03-24	160
18	112	banana	2020-03-24	262
19	149	banana	2020-03-29	382
20	100	banana	2020-03-18	599
21	130	milk	2020-03-16	604
22	103	milk	2020-03-31	290
23	112	banana	2020-03-23	523
24	102	bread	2020-03-25	325
25	120	biscuit	2020-03-21	858
26	109	bread	2020-03-22	432
27	101	milk	2020-03-01	449
28	138	milk	2020-03-19	961
29	100	milk	2020-03-29	410
30	129	milk	2020-03-02	771
31	123	milk	2020-03-31	434
32	104	biscuit	2020-03-31	957
33	110	bread	2020-03-13	210
34	143	bread	2020-03-27	870
35	130	milk	2020-03-12	176
36	128	milk	2020-03-28	498
37	133	banana	2020-03-21	837
38	150	banana	2020-03-20	927
39	120	milk	2020-03-27	793
40	109	bread	2020-03-02	362
41	110	bread	2020-03-13	262
42	140	milk	2020-03-09	468
43	112	banana	2020-03-04	381
44	117	biscuit	2020-03-19	831
45	137	banana	2020-03-23	490
46	130	bread	2020-03-09	149
47	133	bread	2020-03-08	658
48	143	milk	2020-03-11	317
49	111	biscuit	2020-03-23	204
50	150	banana	2020-03-04	299
51	131	bread	2020-03-10	155
52	140	biscuit	2020-03-17	810
53	147	banana	2020-03-22	702
54	119	biscuit	2020-03-15	355
55	116	milk	2020-03-12	468
56	141	milk	2020-03-14	254
57	143	bread	2020-03-16	647
58	105	bread	2020-03-21	562
59	149	biscuit	2020-03-11	827
60	117	banana	2020-03-22	249
61	150	banana	2020-03-21	450
62	134	bread	2020-03-08	981
63	133	banana	2020-03-26	353
64	127	milk	2020-03-27	300
65	101	milk	2020-03-26	740
66	137	biscuit	2020-03-12	473
67	113	biscuit	2020-03-21	278
68	141	bread	2020-03-21	118
69	112	biscuit	2020-03-14	334
70	118	milk	2020-03-30	603
71	111	milk	2020-03-19	205
72	146	biscuit	2020-03-13	599
73	148	banana	2020-03-14	530
74	100	banana	2020-03-13	175
75	105	banana	2020-03-05	815
76	129	milk	2020-03-02	489
77	121	milk	2020-03-16	476
78	117	bread	2020-03-11	270
79	133	milk	2020-03-12	446
80	124	bread	2020-03-31	937
81	145	bread	2020-03-07	821
82	105	banana	2020-03-09	972
83	131	milk	2020-03-09	808
84	114	biscuit	2020-03-31	202
85	120	milk	2020-03-06	898
86	130	milk	2020-03-06	581
87	141	biscuit	2020-03-11	749
88	147	bread	2020-03-14	262
89	118	milk	2020-03-15	735
90	136	biscuit	2020-03-22	410
91	132	bread	2020-03-06	161
92	137	biscuit	2020-03-31	427
93	107	bread	2020-03-01	701
94	111	biscuit	2020-03-18	218
95	100	bread	2020-03-07	410
96	106	milk	2020-03-21	379
97	114	banana	2020-03-25	705
98	110	bread	2020-03-27	225
99	130	milk	2020-03-16	494
100	117	bread	2020-03-10	209
id:
bigint
user_id:
bigint
item:
string
created_at:
date
revenue:
bigint
'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *
from pyspark.sql import *
# Start writing code
# amazon_transactions.show(50,truncate=False)
df=amazon_transactions
window_spec = Window.partitionBy(col("user_id")).orderBy(col("created_at"))
df=df.withColumn("flag",datediff(col("created_at"),lag(col("created_at")).over(window_spec)))
df=df.filter(col("flag")<=7).select("user_id").distinct()
# df.show(50,truncate=False)
df.toPandas()
# To validate your solution, convert your final pySpark df to a pandas df
# amazon_transactions.toPandas()