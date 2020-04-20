from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import responses
import pandas as pd
import pymongo



client = pymongo.MongoClient()
db = client.traveldata
app = Flask(__name__)


def tag_model(inp):

    df = pd.read_json("intent_new.json")

    tags = []
    pattern = []

    for i in range(0, 13):

        #     for j in range(0,30+6+7+5+5+5+4):
        #         for token in df['intents'][i]['patterns']:
        for j in range(0, len(df['intents'][i]['patterns'])):
            tags.append(df['intents'][i]['tag'])
            pattern.append(df['intents'][i]['patterns'][j])

    list_of_tuples = list(zip(tags, pattern))
    df = pd.DataFrame(list_of_tuples, columns=['tags', 'pattern'])
    X = df['pattern']
    y = df['tags']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=20)

    text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])
    text_clf.fit(X_train, y_train)
    return text_clf.predict([inp])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    tag = tag_model(userText)
    user_data = {}
    # user_data['user_data'] = userText
    # user_data['tag'] = tag
    # db.user_data.insert(user_data)
    print(tag)
    bot_response = responses.query_handling(userText, tag)


    bot_response = str(bot_response)
    return bot_response


if __name__ == "__main__":
    app.run()
