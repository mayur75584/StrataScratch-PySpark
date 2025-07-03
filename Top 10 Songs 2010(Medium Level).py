'''
Top 10 Songs 2010


Last Updated: July 2025

Medium
ID 9650

118

Find the top 10 ranked songs in 2010. Output the rank, group name, and song name, but do not show the same song twice. Sort the result based on the rank in ascending order.

Table
billboard_top_100_year_end
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

year_rank	group_name	song_name
1	Ke$ha	TiK ToK
2	Lady Antebellum	Need You Now
3	Train	Hey, Soul Sister
4	Katy Perry feat. Snoop Dogg	California Gurls
5	Usher feat. will.i.am	OMG
billboard_top_100_year_end
Preview
year:
bigint
year_rank:
bigint
group_name:
string
artist:
string
song_name:
string
id:
bigint
'''

# Import your libraries
import pyspark
from pyspark.sql.functions import *

# Start writing code
billboard_top_100_year_end1 = billboard_top_100_year_end.filter(billboard_top_100_year_end.year == 2010)

# billboard_top_100_year_end1.show(truncate=False)

# To validate your solution, convert your final pySpark df to a pandas df
billboard_top_100_year_end1.toPandas()