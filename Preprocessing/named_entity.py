# import nltk
#
#
#
#
#
# query="What are the places to visit in Rajhasthan"
#
# lst=[]
# for p in places:
#     lst.append(p.lower())
# print(lst)
#
# pl = []
# d = {}
#
# ##### Places ka name
# def entity_recog(text):
#     text = nltk.word_tokenize(text)
#     text = [i.lower() for i in text]
#     pos_tag = nltk.pos_tag(text)
#     #     print(pos_tag)
#     d = {i: j for j, i in pos_tag}
#     print(d)
#     for key, val in d.items():
#         if key in ['NN', 'NNP','JJ']:
#             text = []
#             # print(key,"---------->",d[key])
#             text.append(d[key])
#             for k in text:
#                 #   print("k",k)
#                 for place in lst:
#                     #  print("place",place)
#                     if k in place:
#                         # res = []
#                         # res.append(k)
#                         #   print(res)
#                         return k


import spacy
import Preprocessing.spell as sp
nlp = spacy.load('en_core_web_sm')



places=["Jaisalmer","Jaipur","Jodhpur","Bundi","Bikaner","Ajmer","Pushkar","Udaipur","Mount Abu","Sawai Madhopur","Bharatpur","Alwar          ","Pali           ","Chittorgarh    ",
"Hanumangarh","Jhunjhunu","Jhalawar","Churu","Kota","Sikar","Rajasthan","Amber Fort","Hawa Mahal","ranthambore national park","city palace","mehrangarh fort"]


def entity_recog(query):
    query = query.lower()
    queryList = []
    for i in query.split(" "):
        queryList.append(sp.correction(i))
    query1 = ' '.join(queryList)
    print(query1)
    doc1 = nlp(query1)
    entity_list = []
    not_places_list = []
    flag = 0
    for i in places:
        if query1.find(i.lower()) !=-1:
            flag = 1
            entity_list.append(sp.correction(i.lower()))

    for token in doc1:
        print(token.text, '\t', token.pos_, )
        if token.text in map(lambda x:x.lower(),places):
                if flag == 0:
                    correct = sp.correction(token.text)
                    entity_list.append(correct)
        elif token.pos_ == "NOUN":
                not_places_list.append(token.text)
    if len(entity_list) == 0:
        return not_places_list
    else:
        for i in not_places_list:
            entity_list.append(i)
        print(entity_list)
        return entity_list

