from pyspark import SparkContext, SparkConf
import shutil
from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.util import MLUtils
sc =SparkContext()



data = MLUtils.loadLibSVMFile(sc, "e:\data\\old25000_complete.txt")

training, test = data.randomSplit([0.7, 0.3])


model = NaiveBayes.train(training, 1.0)


predictionAndLabel = test.map(lambda p: (model.predict(p.features), p.label))
accuracy = 1.0 * predictionAndLabel.filter(lambda (x, v): x == v).count() / test.count()

print('model accuracy {}'.format(accuracy))
result=predictionAndLabel.collect()
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

data1=MLUtils.loadLibSVMFile(sc, "e:\data\\test.txt")

predictionAndLabel = data1.map(lambda p: (model.predict(p.features), p.label))
result=predictionAndLabel.collect()
for (prediction,reality) in result:
	print "Prediction Value:",prediction,"Reality Value:",reality

output_dir = 'target/NaiveBayesModel'
shutil.rmtree(output_dir, ignore_errors=True)
model.save(sc, output_dir)

