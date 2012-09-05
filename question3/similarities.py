from __future__ import division

from pylab import *
from numpy import *
from heapq import *

from datatool import *

song_mapping = "../data/song_mapping.txt"
user_train = "../data/user_train.txt"
test_data = "../data/user_test.txt"

datatool = DataTool(song_mapping, user_train, test_data)

user_data = datatool.user_data
num_users = datatool.num_users
"""
# similarity_metric == 1, inverse euclidean:
similarity_matrix = zeros([num_users, num_users])
for i in range(0, num_users):
	print i
	x = user_data[i]
	for j in range(i+1, num_users):
		y = user_data[j]
		similarity_matrix[i][j] = 1/(norm((x-y),2)**2)
		similarity_matrix[j][i] = similarity_matrix[i][j]
	similarity_matrix[i][j] = -1
savetxt("inverse_euclidean.txt", similarity_matrix)
"""
# similarity_metric == 2, dot:
similarity_matrix = zeros([num_users, num_users])
for i in range(0, num_users):
	print i
	x = user_data[i]
	for j in range(i+1, num_users):
		y = user_data[j]
		similarity_matrix[i][j] = dot(x,y)
		similarity_matrix[j][i] = similarity_matrix[i][j]
	similarity_matrix[i][j] = -1
savetxt("dot.txt", similarity_matrix)	
	
# similarity_metric == 3, cosine:
similarity_matrix = zeros([num_users, num_users])
for i in range(0, num_users):
	print i
	x = user_data[i]
	for j in range(i+1, num_users):
		y = user_data[j]
		similarity_matrix[i][j] = dot(x,y)/(norm(x,2)*norm(y,2))
		similarity_matrix[j][i] = similarity_matrix[i][j]
	similarity_matrix[i][j] = -1
savetxt("cosine.txt", similarity_matrix)
