from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

nums = sc.parallelize([1, 2, 3, 4])


print(nums.foreach())

