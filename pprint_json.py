import argparse
import json
import os

def load_data(filepath):
    with open(filepath, 'r') as json_file:
        parsed_json = json.loads(json_file.read())              
    return parsed_json

def pretty_print_json(data):
    pretty_data = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    return pretty_data

def filepath_is_valid(filepath):
    if os.path.isfile(filepath) and filepath.endswith(".json"):
        return True
    else:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Расположение JSON файла.", type=str)
    args = parser.parse_args()
    filepath = args.filepath

    if filepath_is_valid(filepath):
        data = load_data(filepath)
        print(pretty_print_json(data))
    else:
        print("Некорректные входные данные!")

