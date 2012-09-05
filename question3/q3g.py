from __future__ import division

import sys
from optparse import OptionParser


from datatool import *
from knnlib import *
from pylab import *

weighted = True
similarity_metric = 3

song_mapping = "../data/song_mapping.txt"
user_train = "../data/user_train.txt"
test_data = "../data/user_test.txt"

datatool = DataTool(song_mapping, user_train, test_data)

similarity_matrix = loadtxt("cosine.txt")
print "file loaded"

user_data = datatool.user_data
num_users = len(user_data)

print "Done with data collection"

def test(recommended_songs, test_data):
	R = 10
	R_rel = 0
	for song in recommended_songs:
		if song in test_data:
			R_rel += 1
	return (R_rel/R)	

def user_query(k, weighted, similarity_metric, user_data,(query_id,query_features)):
	knntool = KNN(k, weighted, similarity_metric, user_data,(query_id,query_features),similarity_matrix)
	recommended_songs =  map(lambda x:x+1, knntool.run()) # translate shifted id to real id	
	return recommended_songs
		
print "Start training..."

def single_k(k):
	p = zeros(num_users)
	for query_id in range(0, num_users):
		print "k = %d User_id = %d " % (k, query_id+1)
		test_data = datatool.test_data[query_id]
		rec = user_query(k, weighted, similarity_metric, user_data, (query_id,user_data[query_id]))
		p[query_id] = test(rec, test_data)
	print p
	return sum(p)/num_users
		
result = single_k(10)
print ("Weighted cosine for k=10, result P = %f" % result)



	
