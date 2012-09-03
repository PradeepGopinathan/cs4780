from pylab import *
from heapq import *

NUM_PICK = 10

class KNN(object):
	
	def __init__(self, k, weighted, similarity_metric, user_data, query_user):
		self.k = k
		self.weighted = weighted
		self.similarity_metric = similarity_metric.lower()
		self.user_data = user_data
		self.num_users = len(self.user_data)
		self.num_songs = len(self.user_data[1])
		self.query_user_features = query_user[1]  # query user has type (id, feature list)
		self.query_id = query_user[0]
		
	def __similarity_measure(self, x, y):
		if self.similarity_metric == "euclidean":
			return 1/(norm(x-y,2)**2)
		elif self.similarity_metric == "dot_product":
			return dot(x,y)
		else:
			return dot(x,y)/(norm(x)*norm(y))
	
	def _reset(self):	
		self.similarities = []  #initialize everything to be negative
		self.k_NN = None
		# ranking vectors store the the song index as a row vector
		self.ranking_vector = zeros(min(self.num_songs,NUM_PICK))
			
	def _find_similarity_measures(self):
		for y in range(0, self.num_users): 
				self.similarities[y] = self.__similarity_measure(self.query_user_features,
																 self.user_data[y])
		self.smilarities[self.query_id] = -1		
				
	def _find_k_NN(self):
		top_k = []
		for y in range(0,self.num_users):
			if not (self.query_id==y):
				heappush(top_k,(self.similarities[y],y))
				if len(top_k) > self.k: # to save memory, pop out the smallest one
					heappop(top_k)
				self.k_NN = map(lambda (similarity, user_ind):user_ind, top_k)
	
	def _find_unweighted_ranking_vectors(self):
		v = zeros(self.num_songs)
		for i in range(0, self.k):
			v = v+ self.user_data[int(self.NN_matrix[row][i])]
		raw = list(v / self.k)		# average play freq vector for songs
		print raw
		self.ranking_vector = map(lambda x: raw.index(x), nlargest(NUM_PICK, raw))
	
	
	def _find_weighted_ranking_vectors(self):
		v = zeros(self.num_songs)
		for i in range(0, self.k):
			v = v+ self.user_data[int(self.NN_matrix[row][i])] * self.similarity_matrix[row,i] 
		raw = list(v / sum(self.similarity_matrix[row][:k]))
		self.ranking_vector = map(lambda x: raw.index(x), nlargest(NUM_PICK, raw))

	def print_attr(self):
		print"++++++++++++++++++++++++++++++++++++"
		print "similarity_matrix: "
		print self.similarities
		print "k_NN:"
		print self.k_NN
		print "ranking_vectors:"
		print self.ranking_vectors
		print"++++++++++++++++++++++++++++++++++++"
		
	def run(self):
		self._reset()
		self.print_attr()
		self._find_similarity_measures()
		self.print_attr()
		self._find_NN_matrix()
		self.print_attr()
		if self.weighted:
			self._find_weighted_ranking_vectors()
		else:
			self._find_unweighted_ranking_vectors()
		self.print_attr()
		return self.ranking_vectors
