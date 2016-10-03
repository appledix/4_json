import json
import sys

def read_console_args():
    return sys.argv[1:]

def load_data(filepath):
    parsed_json = None
    json_file = open(filepath, 'r')
    parsed_json = json.loads(json_file.read())
    json_file.close()                
    return parsed_json


def pretty_print_json(data):
    data = str(data)
    pretty_data = ""
    current_indentation = 0
    quote_is_open = False
    tab = " " * 4
    for symbol in data:
        if symbol == "{":
            current_indentation += 1
            pretty_data += symbol + "\n" + (tab * current_indentation)

        elif symbol == "}":
            current_indentation -= 1
            pretty_data += "\n" + (tab * current_indentation) + symbol

        elif symbol == "]":
            current_indentation -= 1
            pretty_data += "\n" + (tab * current_indentation) + symbol
        
        elif symbol == "[":
            current_indentation += 1
            pretty_data += symbol + "\n" + (tab * current_indentation)

        elif symbol == ",":
            if not quote_is_open:
                pretty_data += symbol + "\n" + (tab * current_indentation)[:-1]
            else:
                pretty_data += symbol

        elif symbol == "'":
            if quote_is_open:
                quote_is_open = False
            else:
                quote_is_open = True
            pretty_data += symbol   
        
        else:
            pretty_data += symbol
    return pretty_data


if __name__ == '__main__':
    parameters = read_console_args()
    try:
        if len(parameters) != 1:
            raise Exception
        filepath = parameters[0]
        data = load_data(filepath)
    except Exception:
        print\
        ("Для работы скрипта необходимо передать ему валидный адрес JSON файла.")
    else:
        print(pretty_print_json(data))

