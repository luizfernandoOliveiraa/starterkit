import pandas as pd


def concat_dataframe(data_frame_list: list[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)
