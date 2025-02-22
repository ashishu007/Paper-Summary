from app import app
from flask import render_template, Flask, jsonify, request
from app.utilities import create_json, replace_data
from nltk.tokenize import word_tokenize  # to split sentences into words
from nltk.corpus import stopwords  # to get a list of stopwords
from collections import Counter  # to get words-frequency
import os, json

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cloud', methods=['GET'])
def word_cloud():
    with open('./app/output/data.json') as json_file:
        data = json.load(json_file)

    sentences = ""
    for paper in data:
        summary = paper["brief_summary"]
        method = paper["method_definition"]
        paper_name = paper["paper_name"]
        paper_category = paper["paper_category"]
        task_definition = paper["task_definition"]
        dataset_used = paper["dataset_used"]

        sentences = "{} {} {} {} {} {} {}".format(sentences, summary, method, paper_name, paper_category, task_definition, dataset_used)
    
    sentences = sentences.strip()
    words = word_tokenize(sentences)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and len(word) > 3]
    words_freq = Counter(words)
    words_json = [{'text': word, 'weight': count} for word, count in words_freq.items()]

    return json.dumps(words_json)

@app.route('/show', methods=['POST', 'GET'])
def hello_world():
    papers = os.listdir("./app/Papers")
    
    if "data.json" not in os.listdir("./app/output/"):
        print("json not found")
        create_json()

    complete = []
    non_complete = []

    with open('./app/output/data.json') as json_file:
        data = json.load(json_file)

    for i in data:
        if i["paper_name"] != "":
            complete.append(i["paper_name"])

    for i in papers:
        if i not in complete:
            non_complete.append(i)

    return render_template("table.html", c=complete, nc=non_complete)

@app.route('/form/<filename>', methods=['POST', 'GET'])
def show_form(filename):
    return render_template("add_data.html", filename=filename)

@app.route('/view/<filename>', methods=['POST', 'GET'])
def show_data(filename):

    with open('./app/output/data.json') as json_file:
        data = json.load(json_file)

    for i in data:
        if i["paper_name"] == filename:
            asked = {
                "Name": i["paper_name"],
                "Category": i["paper_category"],
                "Task": i["task_definition"],
                "Dataset Used": i["dataset_used"],
                "Method": i["method_definition"],
                "Brief Summary": i["brief_summary"]
            }

    return render_template("show_data.html", data=asked)

@app.route('/add', methods=['POST', 'GET'])
def add_data():
    if request.method == 'POST':
        result = request.form
        r = result.to_dict(flat=False)
        print(result)
        print(r)

    ftrs = {
        "paper_name": r["paper_name"][0],
        "paper_category": r["paper_category"][0],
        "task_definition": r["task_definition"][0],
        "dataset_used": r["dataset_used"][0],
        "method_definition": r["method_definition"][0],
        "brief_summary": r["brief_summary"][0]
    }

    with open('./app/output/data.json') as json_file:
        data = json.load(json_file)

    added_papers = [i["paper_name"] for i in data]

    if ftrs["paper_name"] not in added_papers:
        data.append(ftrs)
    elif ftrs["paper_name"] in added_papers:
        data = replace_data(data, ftrs)

    with open('./app/output/data.json', 'w') as outfile:
        json.dump(data, outfile)

    return render_template("index.html", msg="Data Added")

if __name__ == "__main__":
    app.run()