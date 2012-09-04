
from datatool import *

song_mapping = "song_mapping.txt"
user_train = "user_train.txt"
test_data = "user_test.txt"

datatool = DataTool(song_mapping, user_train, test_data)
# datatool.song_info

print datatool.song_info
print datatool.get_artist_collection("adfa")

