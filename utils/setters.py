import json
import shutil
import os


def save(data={}, file_name='data.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

        # Move the json file to data directory
        old_path = os.path.join(os.getcwd(), file_name)
        new_path = os.path.join(os.getcwd(), 'data/'+file_name)

    # Prevent permissionError
    shutil.move(old_path, new_path)
