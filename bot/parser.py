import json
import csv

# def parse_squad_data():
#     file = json.load(open("/mnt/c/Users/Harrys/Gaspardesk/chatbot/dev-v2.0.json"))
#     data = file["data"]
#     results = []

#     for dt in data:
#         parsed_data = {}
#         tag = dt["title"]
#         parsed_data["tag"] = tag

#         parsed_questions = []
#         for paragraph in dt["paragraphs"]:
#             response = paragraph["context"]
#             parsed_data["responses"] = [response]

#             for p in paragraph["qas"]:
#                 question = p.get("question")
#                 parsed_questions.append(question)

#             parsed_data["patterns"] = parsed_questions

#         results.append(parsed_data)

#     return results


def parse_csv_data():
    """ 
    tag: str
    pattern: list
    responses: list
    """
    file = open("data.csv")
    csv_reader = csv.reader(file, delimiter=',')
    line_count = -1
    results = []
    tags = []
    for row in csv_reader:
        
        line_count += 1
        if line_count == 0:
            continue
        

        question = row[1]
        answer = row[2]
        p_tag = row[5].split("-")

        if not (question and answer):
            continue
        
        for tag in p_tag:
            tag = tag.strip()
            tag.replace(" ", "_")
            
            if not tag:
                continue

            p_data = {
                "tag": tag,
                "patterns": [],
                "responses": []
            }
            if tag not in tags:
                tags.append(tag)
                p_data["tag"] = tag
                p_data["patterns"].append(question)
                p_data["responses"].append(answer)
                results.append(p_data)
            else:
                for res in results:
                    if tag != res.get("tag", None):
                        continue
                    res["patterns"].append(question)
                    res["responses"].append(answer)    
    
    return {
        "intents": results
    }


with open("generic.json", "w") as outfile:
    dt = parse_csv_data()
    json.dump(dt, outfile)
    outfile.close()