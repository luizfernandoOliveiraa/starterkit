from pipeline.extract import extract_data_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_dataframe

if __name__ == '__main__':
    data_frame_list = extract_data_from_excel(path='data/input')
    combined_data = concat_dataframe(data_frame_list)
    load_excel(
        data_frame=combined_data,
        output_path='data/output',
        file_name='combined_data',
    )

    print(
        "Data processing complete. The combined data has been saved to 'data/output/combined_data.xlsx'."
    ) 
