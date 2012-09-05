from __future__ import division

import sys
from optparse import OptionParser


from datatool import *
from knnlib import *
from pylab import *

parser = OptionParser()
parser.add_option("-w", "--weighted", dest="weighted", default = False, action="store_true", 
				   help="specify using weighted average or not")
parser.add_option("-s","--similarity_metric", dest="similarity_metric", type="int",
				  help="1 - inverse of euclidean distance; 2 - dot product; 3 - cosine distance")

(options, args) = parser.parse_args()

weighted = options.weighted
similarity_metric = options.similarity_metric

song_mapping = "../data/song_mapping.txt"
user_train = "../data/user_train.txt"
test_data = "../data/user_test.txt"

datatool = DataTool(song_mapping, user_train, test_data)

# load similarity_matrix
if similarity_metric == 1:
	similarity_matrix = loadtxt("inverse_euclidean.txt")
elif similarity_metric == 2:
	similarity_matrix = loadtxt("dot.txt")
else:
	similarity_matrix = loadtxt("cosine.txt")
print "file loaded"

user_data = datatool.user_data
num_users = len(user_data)

fname = "question3c_%d.txt" % similarity_metric
f = open(fname,"w")
similarity_str = " similarity metric is %d\n" % similarity_metric
f.write("unweighted ")
f.write(similarity_str)

print "Done with data collection"

def print_songs(song_index_list):
	for song in song_index_list:
		print datatool.get_song_info(song)
		
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
	
	
k_list = [1, 3, 5, 10, 25, 50, 100, 250, 500, 1000]
result = []
for k in k_list:
	result.append(single_k(k))


for (k,val) in zip(k_list,result):
	f.write(str(k)+ " " + str(val) + "\n")
f.close()

plot(k_list, result)
title("unweighted " + similarity_str)
yscale('log')
show()	



	
