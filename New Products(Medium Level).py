'''
New Products


Last Updated: June 2025

Medium
ID 10318

232

Calculate the net change in the number of products launched by companies in 2020 compared to 2019. Your output should include the company names and the net difference.
(Net difference = Number of products launched in 2020 - The number launched in 2019.)

Table
car_launches
More about this question
Hints
Expected Output
All required columns and the first 5 rows of the solution are shown

company_name	net_products
Chevrolet	2
Ford	-1
Honda	-3
Jeep	1
Toyota	-1
car_launches
Preview
year	company_name	product_name
2019	Toyota	Avalon
2019	Toyota	Camry
2020	Toyota	Corolla
2019	Honda	Accord
2019	Honda	Passport
2019	Honda	CR-V
2020	Honda	Pilot
2019	Honda	Civic
2020	Chevrolet	Trailblazer
2020	Chevrolet	Trax
2019	Chevrolet	Traverse
2020	Chevrolet	Blazer
2019	Ford	Figo
2020	Ford	Aspire
2019	Ford	Endeavour
2020	Jeep	Wrangler
2020	Jeep	Cherokee
2020	Jeep	Compass
2019	Jeep	Renegade
2019	Jeep	Gladiator
year:
bigint
company_name:
string
product_name:
string

'''


# Import your libraries
import pyspark
from pyspark.sql.functions import *

# Start writing code
car_launches_2020 = car_launches.filter(car_launches.year == 2020).groupBy("company_name").agg(count("*").alias("cnt1"))
car_launches_2019 = car_launches.filter(car_launches.year == 2019).groupBy("company_name").agg(count("*").alias("cnt2"))
car_launches_df1 = car_launches_2020.join(car_launches_2019, car_launches_2020['company_name'] == car_launches_2019['company_name'],"full").drop(car_launches_2019.company_name)
car_launches_df1 = car_launches_df1.withColumn("net_products",car_launches_df1["cnt1"]-car_launches_df1["cnt2"]).drop("cnt1","cnt2").drop()
# car_launches_df1.show(truncate=False)
# To validate your solution, convert your final pySpark df to a pandas df
car_launches_df1.toPandas()