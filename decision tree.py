from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
from pyspark import SparkContext, SparkConf
import shutil
sc =SparkContext()
# Load and parse the data file into an RDD of LabeledPoint.
data = MLUtils.loadLibSVMFile(sc, "e:\data\\old25000_no_rate.txt")

# Split the data into training and test sets (30% held out for testing)
(trainingData, testData) = data.randomSplit([0.7, 0.3])

# Train a DecisionTree model.
#  Empty categoricalFeaturesInfo indicates all features are continuous.
model = DecisionTree.trainClassifier(trainingData, numClasses=2, categoricalFeaturesInfo={},
                                     impurity='gini', maxDepth=5, maxBins=32)

# Evaluate model on test instances and compute test error
predictions = model.predict(testData.map(lambda x: x.features))
labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
accuracy = labelsAndPredictions.filter(lambda (v, p): v == p).count() / float(testData.count())
print('Test Accuracy = ' + str(accuracy))
result=labelsAndPredictions.collect()
num1=0
num0=0
true1=0
true0=0 
for (prediction,reality) in result:
	if reality == 1:
		num1=num1+1
		if prediction == reality:
			true1=true1+1
	if reality == 0:
		num0=num0+1
		if prediction == reality:
			true0=true0+1

print "True Accuracy:",float(true1)/num1,"False Accuracy",float(true0)/num0


model.save(sc, "target/DecisionTreeModel")