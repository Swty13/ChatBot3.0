from nltk.corpus import wordnet as wn

categories = {'places' : wn.synsets('places')[0],
			 'reach' : wn.synsets('reach')[0],
              'ratings' : wn.synsets('ratings')[0],
              'reviews' : wn.synsets('reviews')[0],
			  'time' : wn.synsets('time')[0]}

#find out the similarity score between terms from query and the keys in our data store of states
def get_similarity_score(term):
	try:
		wn_term = wn.synsets(term)[0]
	except:
		return
	max_score = 0
	max_sim = ''
	for cat, value in categories.items():
		sim_score = wn.wup_similarity(wn_term, value)
		if sim_score> max_score:
			max_score = sim_score
			max_sim = cat

	temp = []
	temp.append(max_sim)
	temp.append(max_score)


	if temp[1] >= 0.5:
		return temp




