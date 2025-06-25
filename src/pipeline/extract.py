import os 
import glob
import pandas as pd



def extract_data_from_excel(path: str) -> pd.DataFrame: # type: ignore
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file, engine='openpyxl'))

    return data_frame_list # type: ignore

if __name__ == "__main__":
    data = extract_data_from_excel(path="data/input")  
    print(data)     # type: ignore