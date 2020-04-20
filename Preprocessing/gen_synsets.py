from Preprocessing.find_similarity import get_similarity_score
from nltk.corpus import wordnet as wn

def gen_synsets():
	qry_terms = dict()
	# want to travel from Mumbai to Mount Abu guide me
	query = "tell me the details about places to visit in Rajasthan"
	# use pos tagged list, prepared in parse_query.py file

	list_of_terms = query.split(" ")
	for term in list_of_terms:
		for i in wn.synsets(term):
			key = wn.morphy(term)
			for j in i.lemmas():  # Iterating through lemmas for each synset.
			# append synonyms
				syn = str(j.name())
				if key in qry_terms:
					qry_terms[key].append(syn)
				else:
					qry_terms[key] = [syn]


	for c in qry_terms:
		qry_terms[c] = list(set(qry_terms[c]))
	# print c, ':', qry_terms[c]
	# print(qry_terms)


	for cat, val_lst in qry_terms.items():
		place_count=0
		reach_count=0
		rating_count=0
		review_count=0
		time_count=0
		categories = {'places': place_count,
					  'reach': reach_count,
					  'ratings': rating_count,
					  'reviews': review_count,
					  'time':time_count}

		for entry in val_lst:
			print( entry, "   |  Score ", get_similarity_score(entry))
			if len(get_similarity_score(entry)[1] )>0:
				if get_similarity_score(entry)[1] in 'ratings':
					rating_count=rating_count+1
				if get_similarity_score(entry)[1] in 'reach':
					reach_count=reach_count+1
				if get_similarity_score(entry)[1] in 'places':
					place_count=place_count+1
				if get_similarity_score(entry)[1] in 'reviews':
					review_count=review_count+1
				if get_similarity_score(entry)[1] in 'time':
					time_count=time_count+1
			res=max(place_count,time_count,rating_count,review_count,reach_count)
			for key,val in categories.items():
				if max(place_count,time_count,rating_count,review_count,reach_count):
					return key







if __name__ == "__main__":
	gen_synsets()