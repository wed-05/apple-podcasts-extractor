thonimport json

def export_to_json(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)