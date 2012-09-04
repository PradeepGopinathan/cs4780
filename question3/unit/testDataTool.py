
from datatool import *

song_mapping = "../../data/song_mapping.txt"
user_train = "../../data/user_train.txt"
test_data = "user_test.txt"

datatool = DataTool(song_mapping, user_train, test_data)
# datatool.song_info

print datatool.user_data[0][31115]

