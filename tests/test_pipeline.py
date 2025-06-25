import pandas as pd

from src.pipeline.transform import concat_dataframe


def test_concat_list_df():
    df_1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df_2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

    arrange = pd.concat([df_1, df_2], ignore_index=True)

    act = concat_dataframe([df_1, df_2])

    assert arrange.equals(act)
