#WE have an insurance data set and we need to predict the values according to the linear regression and will have to get the error
#between the values of actual and predicted

#In this tutorial we will learn following things
#estinamte linear regression coeficents
#prediction using linear regression 

#We will run this example on insurence data, we got it from internet

#There are some important formullas we weill use to estimate following things
#We will have to calculate following formulla as we discussed in tutorial
#y = b0 + b1 * x
# In above formulla b0 and b1 are the coeficents
#We will also discuss how to calculatw these things

#In ABove formulla we need to find out following B0 and B1 using following formulla

#B1 = sum((x(i) - mean(x)) * (y(i) - mean(y))) / sum( (x(i) - mean(x))^2 )
#B0 = mean(y) - B1 * mean(x)

#Here x is the value we will get from the file and y will be the predicted value on x which we also got from the file
#1=>
#To start with the example the most thing we are in need of is mean and variance.
#We wrote methods to do that in our code
#2=>
#Next thins is to calculate covariance 
#The covariance of two groups of numbers describes how those numbers change together.
#Formulla to  calculate the covariance 
#covariance = sum((x(i) - mean(x)) * (y - mean(y)))

#3=> 
#Now we need to find coeficents B0 and B1
#B1 = covariance(x, y) / variance(x)
#B0 = mean(y) - B1 * mean(x)

#After done with everything above, now we are ready to predict using our formulla y = b0+b1*x

# Simple Linear Regression on the Swedish Insurance Dataset
from random import seed
from random import randrange
from csv import reader
from math import sqrt

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Split a dataset into a train and test set
def train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy

# Calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)

# Evaluate an algorithm using a train/test split
#Here we are aveluating acutal and predicted values
def evaluate_algorithm(dataset, algorithm, split, *args):
	train, test = train_test_split(dataset, split)
	test_set = list()
	#We are creaiting test set here
	for row in test:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)

	#simple_linear_regression will be called here
	predicted = algorithm(train, test_set, *args)
	actual = [row[-1] for row in test]
	rmse = rmse_metric(actual, predicted)
	return rmse

# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])

# Calculate coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]

# Simple linear regression algorithm
def simple_linear_regression(train, test):
	#Here we have all training and testing data
	#and we make preddictions here

	predictions = list()
	b0, b1 = coefficients(train) #Getting b0 and b1 from training data

	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)

	#Returing predictions
	return predictions

# Simple linear regression on insurance dataset
seed(1)
# load and prepare data
filename = 'insurance.csv'
dataset = load_csv(filename) # Loading dataset
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i) #Simppley converting values into float points from strings
# evaluate algorithm
split = 0.6 #Here we are splitting out data in 40 and 60%, train our system with 60 and predict with 40% although we have all autual values for other 40% too
rmse = evaluate_algorithm(dataset, simple_linear_regression, split)

#AT the end we are simple shoing Error of the predictions called rmse
print("\nError in prediction vs training data\n")

print('RMSE: %.3f' % (rmse))