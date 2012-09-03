from datatool import *
from knnlib import *
from pylab import *

song_mapping = "../data/song_mapping.txt"
user_train = "../data/user_train.txt"
test_data = "../data/user_test.txt"

k = 3
weighted = False
similarity_metric = "dot_product"

datatool = DataTool(song_mapping, user_train, test_data)
user_data = datatool.user_data
print "Done with data collection"
knntool = KNN(k, weighted, similarity_metric, user_data)
recommended_songs =  knntool.run()

print recommended_songs

