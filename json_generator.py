import datetime
import json
from faker import Faker


def generate_json(size, sentence=False, word=False, file_name=f"generated"):
    result = {}
    f = Faker()
    if sentence:
        for i in range(size):
            result.update({i+1: f.text()})
    elif word:
        for i in range(size):
            result.update({i+1: f.word()})

    with open(f"{file_name}_{str(size)}_{datetime.datetime.now()}.json", "w") as file:
         file.write(json.dumps(result, indent=4))


def generate_json_simple(size=100, file_name="generated_simple"):
    result = {}
    for i in range(size):
        result.update({i+1: f"word {i+1}"})

    with open(f"{file_name}_{str(size)}_{datetime.datetime.now()}.json", "w") as file:
        file.write(json.dumps(result, indent=4))


def generate_list_of_jsons(size=100, sentence=False, word=False, file_name="generated_list"):
    result = []
    f = Faker()
    if sentence:
        for i in range(size):
            result.append({"Text": f.text()})
    elif word:
        for i in range(size):
            result.append({"Text": f.word()})

    with open(f"{file_name}_{str(size)}_{datetime.datetime.now()}.txt", "w") as file:
        file.write(str(result).replace("'", '"'))


if __name__ == "__main__":
    generate_json(size=100, word=True, file_name="generated_word")
    # generate_list_of_jsons(sentence=True)
