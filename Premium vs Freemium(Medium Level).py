'''
Premium vs Freemium


Last Updated: July 2025

Medium
ID 10300

282

Find the total number of downloads for paying and non-paying users by date. Include only records where non-paying customers have more downloads than paying customers. The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads. Hint: In Oracle you should use "date" when referring to date column (reserved keyword).

Tables
ms_user_dimension
ms_acc_dimension
ms_download_facts
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

date	non_paying	paying
2020-08-16	15	14
2020-08-17	45	9
2020-08-18	10	7
2020-08-21	32	17
ms_user_dimension
Preview
user_id	acc_id
1	716
2	749
3	713
4	744
5	726
6	706
7	750
8	732
9	706
10	729
11	748
12	731
13	739
14	740
15	705
16	706
17	701
18	746
19	726
20	748
21	701
22	707
23	710
24	702
25	720
26	730
27	721
28	733
29	732
30	729
31	716
32	722
33	745
34	737
35	730
36	729
37	723
38	710
39	707
40	737
41	717
42	741
43	718
44	736
45	720
46	743
47	707
48	721
49	748
50	715
51	709
52	732
53	732
54	712
55	701
56	721
57	744
58	724
59	727
60	743
61	744
62	717
63	723
64	713
65	706
66	731
67	722
68	744
69	705
70	703
71	725
72	740
73	713
74	732
75	720
76	709
77	739
78	703
79	732
80	728
81	737
82	711
83	745
84	734
85	723
86	718
87	702
88	718
89	744
90	710
91	727
92	739
93	728
94	740
95	744
96	737
97	726
98	722
99	727
100	712
user_id:
bigint
acc_id:
bigint
ms_acc_dimension
Preview
acc_id	paying_customer
700	no
701	no
702	no
703	no
704	no
705	no
706	no
707	no
708	no
709	no
710	no
711	no
712	no
713	no
714	no
715	no
716	no
717	no
718	no
719	no
720	no
721	no
722	no
723	no
724	no
725	yes
726	yes
727	yes
728	yes
729	yes
730	yes
731	yes
732	yes
733	yes
734	yes
735	yes
736	yes
737	yes
738	yes
739	yes
740	yes
741	yes
742	yes
743	yes
744	yes
745	yes
746	yes
747	yes
748	yes
749	yes
750	yes
acc_id:
bigint
paying_customer:
string
ms_download_facts
Preview
date	user_id	downloads
2020-08-24	1	6
2020-08-22	2	6
2020-08-18	3	2
2020-08-24	4	4
2020-08-19	5	7
2020-08-21	6	3
2020-08-24	7	1
2020-08-24	8	8
2020-08-17	9	5
2020-08-16	10	4
2020-08-22	11	8
2020-08-19	12	6
2020-08-15	13	3
2020-08-21	14	0
2020-08-24	15	0
2020-08-15	16	5
2020-08-18	17	5
2020-08-23	18	8
2020-08-15	19	6
2020-08-25	20	4
2020-08-16	21	1
2020-08-25	22	4
2020-08-22	23	7
2020-08-21	24	4
2020-08-25	25	5
2020-08-23	26	6
2020-08-19	27	9
2020-08-24	28	3
2020-08-20	29	0
2020-08-25	30	8
2020-08-20	31	5
2020-08-21	32	8
2020-08-15	33	6
2020-08-24	34	4
2020-08-25	35	1
2020-08-24	36	7
2020-08-17	37	8
2020-08-16	38	8
2020-08-17	39	1
2020-08-20	40	8
2020-08-18	41	3
2020-08-16	42	0
2020-08-23	43	9
2020-08-25	44	9
2020-08-16	45	2
2020-08-15	46	2
2020-08-21	47	1
2020-08-21	48	4
2020-08-22	49	8
2020-08-17	50	6
2020-08-21	51	4
2020-08-20	52	7
2020-08-16	53	7
2020-08-20	54	6
2020-08-20	55	0
2020-08-21	56	8
2020-08-18	57	5
2020-08-17	58	2
2020-08-24	59	3
2020-08-20	60	7
2020-08-22	61	8
2020-08-15	62	6
2020-08-23	63	3
2020-08-17	64	4
2020-08-16	65	4
2020-08-16	66	3
2020-08-19	67	1
2020-08-18	68	2
2020-08-17	69	4
2020-08-22	70	7
2020-08-20	71	6
2020-08-15	72	2
2020-08-17	73	7
2020-08-22	74	1
2020-08-17	75	8
2020-08-19	76	0
2020-08-25	77	1
2020-08-25	78	0
2020-08-17	79	8
2020-08-23	80	7
2020-08-24	81	2
2020-08-21	82	0
2020-08-24	83	4
2020-08-21	84	0
2020-08-25	85	7
2020-08-22	86	1
2020-08-20	87	2
2020-08-19	88	3
2020-08-22	89	8
2020-08-24	90	0
2020-08-22	91	9
2020-08-25	92	7
2020-08-25	93	0
2020-08-17	94	1
2020-08-23	95	2
2020-08-24	96	3
2020-08-21	97	8
2020-08-24	98	0
2020-08-21	99	9
2020-08-25	100	7
date:
date
user_id:
bigint
downloads:
bigint
'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *
# Start writing code

ms_user_dimension = ms_user_dimension.join(ms_acc_dimension,ms_user_dimension.acc_id == ms_acc_dimension.acc_id, "inner")
ms_user_dimension = ms_user_dimension.join(ms_download_facts, ms_user_dimension.user_id == ms_download_facts.user_id, "inner")
# ms_user_dimension.show(truncate=False)
df_no =  ms_user_dimension.filter(ms_user_dimension.paying_customer == "no")
df_no = df_no.groupBy("date").sum("downloads")
df_no = df_no.withColumnRenamed("sum(downloads)","no")
df_yes = ms_user_dimension.filter(ms_user_dimension.paying_customer == "yes")
df_yes = df_yes.groupBy("date").sum("downloads")
df_yes = df_yes.withColumnRenamed("sum(downloads)","yes")
df_yes_no = df_yes.join(df_no, df_yes.date == df_no.date, "inner").drop(df_no.date)
df = df_yes_no.filter(df_yes_no.no > df_yes_no.yes).sort(col("date"))
df = df.select(["date","no","yes"])
# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()