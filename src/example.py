import json, os

def load_json():
    src_dir = os.path.dirname(__file__)
    json_path = os.path.join(src_dir,"setting.json")
    setting_dict = json.load(open(json_path,"r"))
    
    username = setting_dict["username"]
    print_username = setting_dict["print_username"]
    
    if print_username:
        print(username)

if __name__ == "__main__":
    load_json()