from __future__ import division

import sys
from optparse import OptionParser


from datatool import *
from knnlib import *
from pylab import *

parser = OptionParser()
parser.add_option("-k", dest="k", type="int", help="specify the k value")
parser.add_option("-w", "--weighted", dest="weighted", default = False, action="store_true", 
				   help="specify using weighted average or not")
parser.add_option("-s","--similarity_metric", dest="similarity_metric", type="int",
				  help="1 - inverse of euclidean distance; 2 - dot product; 3 - cosine distance")
parser.add_option("-u", "--user_query", dest="query_id", type="int",
				  help="specify the id for the user to query")
parser.add_option("-a", "--artist_query", dest="artist", type="string",
				  help = "specify the artist to query")

(options, args) = parser.parse_args()

k = options.k
weighted = options.weighted
print weighted
similarity_metric = options.similarity_metric
query_id = options.query_id
artist = options.artist

song_mapping = "../data/song_mapping.txt"
user_train = "../data/user_train.txt"
test_data = "../data/user_test.txt"

"""
k = 100
weighted = False
similarity_metric = 1

query_id = 100
"""

datatool = DataTool(song_mapping, user_train, test_data)
user_data = datatool.user_data

test_data = datatool.test_data[query_id]
#print test_data

print "Done with data collection"


print "Start training..."
knntool = KNN(k, weighted, similarity_metric, user_data,(query_id-1,user_data[query_id-1]))
recommended_songs =  knntool.run()

print recommended_songs


R = 10
R_rel = 0
for song in recommended_songs:
	if song in test_data:
		R_rel += 1
print "R_rel:"
print R_rel
P = float(R_rel/R)

print P

		

