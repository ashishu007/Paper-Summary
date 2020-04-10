from app import app
from flask import render_template, Flask, jsonify, request
from app.check_json import create_json
import os, json

@app.route('/')
def index():
    return render_template("index.html")

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
            asked = i

    return jsonify(asked)

@app.route('/add', methods=['POST', 'GET'])
def add_data():
    if request.method == 'POST':
        result = request.form
        r = result.to_dict(flat=False)
        print(result)

    ftrs = {
        "paper_name": r["paper_name"],
        "paper_category": r["paper_category"],
        "task_definition": r["task_definition"],
        "dataset_used": r["dataset_used"],
        "method_definition": r["method_definition"],
        "brief_summary": r["brief_summary"]
    }

    with open('./app/output/datat.json') as json_file:
        data = json.load(json_file)

    added_papers = [i for i in data["paper_name"]]

    if r["paper_name"] not in added_papers:
        data.append(ftrs)

    with open('./app/output/data.json', 'w') as outfile:
        json.dump(data, outfile)

    return render_template("index.html", msg="Data Added")

if __name__ == "__main__":
    app.run()