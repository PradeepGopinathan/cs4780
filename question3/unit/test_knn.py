
from knnlib import *
from pylab import *

user_data = []
for i in range(0,6):
	user_data.append(zeros(6))
	user_data[i][5] = 1
	user_data[i][i] = i
	print user_data[i]

k = 3
weighted = False
similarity_metric = 1
knntool = KNN(k, weighted, similarity_metric, user_data,(0,user_data[0]))
print knntool.run()
knntool.print_attr()

