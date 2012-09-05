from __future__ import division

import sys
import random
from optparse import OptionParser


from datatool import *
from knnlib import *
from pylab import *
from numpy import *

NUM_PICK = 10

song_mapping = "../data/song_mapping.txt"
user_train = "../data/user_train.txt"
test_data = "../data/user_test.txt"

datatool = DataTool(song_mapping, user_train, test_data)
user_data = datatool.user_data

print "Done with data collection"

def test(recommended_songs, test_data):
	R = 10
	R_rel = 0
	for song in recommended_songs:
		if song in test_data:
			R_rel += 1
	return  R_rel/R

print "\n**************************** baselines ***********************************************"
# popularity
popularity = zeros(len(user_data[1]))
for data in user_data:
	popularity += data

P_pop = 0
P_rand = 0
for query_id in range(0, datatool.num_users):
	print query_id
	#popularity based P
	raw = enumerate(popularity)
	raw = filter(lambda (index,val): user_data[query_id][index]==0, raw) # filter out the songs the user has already played
	raw = nlargest(NUM_PICK, raw, key=lambda x: x[1])
	ranking_vector = map(lambda x: x[0],raw)
	pop_songs =  map(lambda x:x+1, ranking_vector)
	test_data = datatool.test_data[query_id]
	P_pop += test(pop_songs, test_data)
	
	# randomized
	inventory = filter(lambda index: user_data[query_id][index]==0, range(0, datatool.num_songs))
	random.shuffle(inventory)
	recommended_songs = map(lambda x:x+1, inventory[:NUM_PICK])
	P_rand += test(recommended_songs, test_data)
P_pop = P_pop / datatool.num_users
P_rand = P_rand / datatool.num_users
print "Popularity based P: %f" % P_pop
print "Random recommendation P: %f" % P_rand

"""
result:
Popularity based P: 0.081673
Random recommendation P: 0.001986
"""
		

