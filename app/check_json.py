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