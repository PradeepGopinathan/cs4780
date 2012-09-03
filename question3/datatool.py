#/usr/bin/python2.7.3

import os
import exceptions
from numpy import *

class DataTool(object):
	
	def __init__(self, song_mapping, user_train, test_data):
		self.user_data = []
		self.song_info = []
		self.__import_song_mappings(song_mapping)
		self.__import_train_data(user_train)
		#self.__import_test_data(test_data)

	def __import_song_mappings(self,filename):
		with open(filename,"r") as f:
			total_songs = f.readlines()
			self.num_songs = len(total_songs)
			for i in range(0, self.num_songs):
				self.song_info.append("")
			for line in total_songs:
				[song_id, info] = line.split("\t", 1)
				self.song_info[int(song_id)-1] = info


	def __import_train_data(self,filename):
		with open(filename, "r") as f:
			total_users = f.readlines()
			self.num_users = len(total_users)
			for i in range(0, self.num_users):
				self.user_data.append([])
			for line in total_users:
				data = line.split()
				user_id = int(data[0])
				features = data[2:]
				feature_values = zeros(self.num_songs)
				for feature in features:
					[song_id, freq] = feature.split(":")
					feature_values[int(song_id)-1] = int(freq)
				self.user_data[user_id-1] = feature_values
			
	def get_user_data(self, id):
		return self.user_data[id-1]
		
	def get_song_info(self, id):
		return self.song_info[id-1]
			
		
	
