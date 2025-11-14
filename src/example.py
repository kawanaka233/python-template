import json
import os

def load_json():
    src_dir = os.path.dirname(__file__)
    json_path = os.path.join(src_dir,"setting.json")
    try:
        setting_dict = json.load(open(json_path,"r"))
    except FileNotFoundError as e:
        print(f"setting.jsonが見つかりません: {e}")
    
    username = setting_dict["username"]
    print_username = eval(setting_dict["print_username"])
    
    if print_username:
        print(username)

if __name__ == "__main__":
    load_json()