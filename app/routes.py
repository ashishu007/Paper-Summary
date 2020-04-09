from app import app
from flask import render_template, Flask
import os, json

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    papers = os.listdir("./app/Papers")

    complete = []
    non_complete = []

    with open('./app/output/data.json') as json_file:
        data = json.load(json_file)

    for i in data:
        complete.append(i["paper_name"])

    for i in papers:
        if i not in complete:
            non_complete.append(i)

    # diction = {
    #     "complete": complete,
    #     "non_complete": non_complete
    # }

    return render_template("index.html", c=complete, nc=non_complete)

if __name__ == "__main__":
    app.run()