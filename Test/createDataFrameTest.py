from pyspark.sql import SparkSession
from pyspark.sql import Row

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("DataFrame Example") \
    .master("local[*]") \
    .getOrCreate()

# Sample data as a list of dictionaries (simulating a class)
data = [
    {"id": 1, "name": "Alice", "age": 29, "salary": 100000, "height": 5.5, "weight": 60.0, "grade": 1},
    {"id": 2, "name": "Bob", "age": 31, "salary": 120000, "height": 6.0, "weight": 80.0, "grade": 2},
    {"id": 3, "name": "Cathy", "age": 25, "salary": 90000, "height": 5.3, "weight": 55.0, "grade": 1}
]

# Create RDD from the list
rdd = spark.sparkContext.parallelize(data)

# Convert RDD to DataFrame by mapping to Row objects
df = spark.createDataFrame(rdd.map(lambda x: Row(**x)))

# Show the DataFrame
df.show()

# Stop SparkSession
spark.stop()