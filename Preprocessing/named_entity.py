
import spacy
import Preprocessing.spell as sp
nlp = spacy.load('en_core_web_sm')



places=["Jaisalmer","Jaipur","Jodhpur","Bundi","Bikaner","Ajmer","Pushkar","Udaipur","Mount Abu","Sawai Madhopur","Bharatpur","Alwar","Pali","Chittorgarh",
"Hanumangarh","Jhunjhunu","Jhalawar","Churu","Kota","Sikar","Rajasthan","Amber Fort","Hawa Mahal","ranthambore national park","city palace","mehrangarh fort","Jaisalmer",
        "Ana Sagar Lake","Dargah Sharif","Brahma Temple","Nasiyan Temple","Mehrangarh Museum","Jaswant Thada","Umaid Bhawan Palace",
        "Umaid Bhawan Palace Museum","Junagarh Fort","Karni Mata Temple","Shri Laxminath Temple","Pichola Lake","Fateh Sagar",
        "Saheliyon Ki Bari","Jaisalmer Fort","Bada Bagh","Patwon ki Haveli"
        ]


def entity_recog(query):
    query = query.lower()
    queryList = []
    for i in query.split(" "):
        queryList.append(sp.correction(i))
    query1 = ' '.join(queryList)
    doc1 = nlp(query1)
    entity_list = []
    not_places_list = []
    flag = 0
    for i in places:
        if query1.find(i.lower()) !=-1:
            flag = 1
            entity_list.append(sp.correction(i.lower()))

    for token in doc1:
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
        return entity_list

