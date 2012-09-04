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
similarity_metric = options.similarity_metric
query_id = options.query_id
artist = options.artist

song_mapping = "../data/song_mapping.txt"
user_train = "../data/user_train.txt"
test_data = "../data/user_test.txt"

datatool = DataTool(song_mapping, user_train, test_data)
user_data = datatool.user_data

print "Done with data collection"

def print_songs(song_index_list):
	for song in song_index_list:
		print datatool.get_song_info(song)
		
def test(recommended_songs, test_data):
	R = 10
	R_rel = 0
	print "\n================ Songs match: ====================="
	for song in recommended_songs:
		if song in test_data:
			R_rel += 1
			print datatool.get_song_info(song)
	print "P = %f" %  (R_rel/R)	

def user_query(k, weighted, similarity_metric, user_data,(query_id,query_features)):
	knntool = KNN(k, weighted, similarity_metric, user_data,(query_id,query_features))
	recommended_songs =  map(lambda x:x+1, knntool.run()) # translate shifted id to real id 	
	print "\n=============== Most played songs ================="
	print_songs(knntool.most_frequent())
	print "\n=============== Recommended songs: ================"
	print recommended_songs
	print_songs(recommended_songs)	
	return recommended_songs
	
	
def artist_query(artist):
	song_list = datatool.get_artist_collection(artist)
	query_features = datatool.create_artist_feature(song_list)
	query_data = (-1, query_features)
	user_query(k, weighted, similarity_metric, user_data, query_data)
	

print "Start training..."

# user query
if query_id is not None:
	print "User query..."
	test_data = datatool.test_data[query_id-1]
	rec = user_query(k, weighted, similarity_metric, user_data, (query_id-1,user_data[query_id-1]))
	test(rec, test_data)
	
# artist query
if artist is not None:
	print "Artist query..."
	artist_query(artist)

		

