import json


def read_file(filename: str) -> str:
    file = open(filename)
    content = file.read()
    file.close()
    return content


def convert_to_string(content: dict) -> str:
    return json.dumps(content, indent=2)


def is_float(value: any) -> bool:
    try:
        float(value)
        return True
    except:
        return False


def is_int(value: any) -> bool:
    try:
        int(value)
        return True
    except:
        return False


def is_positive_number(value: int) -> bool:
    if value > 0:
        return True
    return False
