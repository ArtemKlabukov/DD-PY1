import json
INPUT_FILE = "input.csv"
def csv_to_list_dict(input_file) -> list[dict]:
    line_list = []
    values = []
    line_list_values = []
    delimiter = ','
    dict1 = {}
    list1 = []
    with open(input_file) as file:
        for line in file:
            line_list.append(line.rsplit())
    for item in line_list:
        if item == line_list[0]:
            keys_list = item[0].split(delimiter)
        else:
            values.append(item)
    for item in values:
        line_list_values.append(item[0].split(delimiter))
    for item in range(len(line_list)-1):
        line_list_item = line_list_values[item]
        for k in range(len(keys_list)):
            dict1[keys_list[k]] = line_list_item[k]
        list1.append(dict1.copy())

    return list1
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))