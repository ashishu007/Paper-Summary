import json

def create_json():

    data = [
        {
        "paper_name": "",
        "paper_category": "",
        "task_definition": "",
        "dataset_used": "",
        "method_definition": "",
        "brief_summary": ""
        }
    ]

    with open('./app/output/data.json', 'w') as outfile:
        json.dump(data, outfile)

def replace_data(data, ftrs):
    for i in data:
        if i["paper_name"] == ftrs["paper_name"]:
            id = data.index(i)
    data[id] = ftrs
    return data