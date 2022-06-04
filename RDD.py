from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("koochooloo").setMaster("local")  # master is a Spark, Mesos or YARN cluster URL, or a
# special “local” string to run in local mode
sc = SparkContext(conf=conf)  # which tells Spark how to access a cluster.

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)  # the distributed dataset can be operated on in parallel

distFile = sc.textFile("data/data.txt")
print(distFile.map(lambda s: len(s)).reduce(lambda a, b: a + b))

pairs = distFile.map(lambda s: (s, 1))
counts = pairs.reduceByKey(lambda a, b: a + b)
print(pairs)
print(counts)