#/usr/bin/python2.7.3
from __future__ import division

import os
import exceptions
from numpy import *

NUM_PICK = 10

class DataTool(object):
	
	def __init__(self, song_mapping, user_train, test_data):
		self.user_data = []
		self.song_info = []
		self.test_data = []
		self.num_songs = 0
		self.num_users = 0
		self.__import_song_mappings(song_mapping)
		self.__import_train_data(user_train)
		self.__import_test_data(test_data)


	def __import_song_mappings(self,filename):
		with open(filename,"r") as f:
			total_songs = f.readlines()
			self.num_songs = len(total_songs)
			self.song_info = ["" for i in range(0, self.num_songs)]
			for line in total_songs:
				[song_id, info] = line.strip().split("\t", 1)
				self.song_info[int(song_id)-1] = info
				

	def __import_train_data(self,filename):
		with open(filename, "r") as f:
			total_users = f.readlines()
			self.num_users = len(total_users)
			self.user_data= [[] for i in range(0, self.num_users)]
			for line in total_users:
				data = line.strip().split()
				user_id = int(data[0])
				features = data[2:]
				self.user_data[user_id-1] = zeros(self.num_songs)
				for feature in features:
					[song_id, freq] = feature.split(":")
					self.user_data[user_id-1][int(song_id)-1] = int(freq)
			
				
	def __import_test_data(self,filename):
		with open(filename,"r") as f:
			self.test_data = [map(lambda x: int(x),line.split("-")[1].strip().split()) for line in f.readlines()]
			
			
	def get_user_data(self, id):
		return self.user_data[id-1]
		
		
	def get_artist_collection(self,artist):
		collection = []
		for i in range(0, self.num_songs):
			if artist in self.song_info[i]:
				collection.append(i+1)
		return collection # real song id
		
		
	def create_artist_feature(self,song_list):
		return [1 if (i+1) in song_list else 0 for i in range(0, self.num_songs)]
		
		
	def get_song_info(self, id):
		return self.song_info[id-1]
			
		
	
