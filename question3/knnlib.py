from pylab import *
from heapq import *

NUM_PICK = 10

class KNN(object):
	
	def __init__(self, k, weighted, similarity_metric, user_data, query_user=None):
		self.k = k
		self.weighted = weighted
		self.similarity_metric = similarity_metric
		self.user_data = user_data
		self.num_users = len(self.user_data)
		self.num_songs = len(self.user_data[1])
		self.query_user_features = query_user[1]  # query user has type (id, feature list)
		self.query_id = query_user[0]
		
	def __similarity_measure(self, x, y):
		if self.similarity_metric == 1:
			return 1/(norm((x-y),2)**2)
		elif self.similarity_metric == 2:
			return dot(x,y)
		else:
			return dot(x,y)/(norm(x,2)*norm(y,2))
	
	def _reset(self):	
		self.similarities = []  #initialize everything to be negative
		self.k_NN = None
		# ranking vectors store the the song index as a row vector
		self.ranking_vector = None
			
	def _find_similarity_measures(self):
		for y in range(0, self.num_users):
			if y == self.query_id:
				self.similarities.append(-1)
			else:	
				self.similarities.append(self.__similarity_measure(self.query_user_features,
															       self.user_data[y]))
				
	def _find_k_NN(self):
		raw = nlargest(self.k,enumerate(self.similarities), key=lambda x: x[1])
		self.k_NN = map(lambda x: x[0],raw)
	
	def _find_unweighted_ranking_vector(self):
		v = zeros(self.num_songs)
		for i in range(0, self.k):
			v = v+ self.user_data[self.k_NN[i]]
		raw = list(v / self.k)		# average play freq vector for songs
		raw = nlargest(NUM_PICK, enumerate(raw), key=lambda x: x[1])
		self.ranking_vector = map(lambda x: x[0],raw)
		
	def _find_weighted_ranking_vector(self):
		v = zeros(self.num_songs)
		denominator = 0
		for i in range(0, self.k):
			v = v+ self.user_data[self.k_NN[i]] * self.similarities[self.k_NN[i]]
			denominator += (self.similarities[self.k_NN[i]])	
		raw = list(v / denominator)
		raw = nlargest(NUM_PICK, enumerate(raw), key=lambda x: x[1])
		self.ranking_vector = map(lambda x: x[0],raw)
		
	def print_attr(self):
		print"++++++++++++++++++++++++++++++++++++"
		print "similarity_matrix: "
		print self.similarities
		print "k_NN:"
		print self.k_NN
		print "ranking_vector:"
		print self.ranking_vector
		print"++++++++++++++++++++++++++++++++++++"
		
	def run(self):
		self._reset()
#		self.print_attr()
		self._find_similarity_measures()
#		self.print_attr()
		self._find_k_NN()
#		self.print_attr()
		if self.weighted:
			self._find_weighted_ranking_vector()
		else:
			self._find_unweighted_ranking_vector()
#		self.print_attr()
		return self.ranking_vector
