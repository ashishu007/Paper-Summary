import json

def create_json():

    '''Function Name: create_json and Parameters: '''


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

    '''Function Name: replace_data and Parameters: data,'''

    for i in data:
        if i["paper_name"] == ftrs["paper_name"]:
            id = data.index(i)
    data[id] = ftrs
    return data