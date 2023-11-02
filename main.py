import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):

    dates_ser = pd.Series([tup[1] for tup in date_info],[tup[0] for tup in date_info])
    ser_1 = pd.Series([tup[1] for tup in aud_usd_info], [tup[0] for tup in aud_usd_info])
    ser_2 = pd.Series([tup[1] for tup in eur_aud_info], [tup[0] for tup in eur_aud_info])
    df = pd.DataFrame(data={'Date': dates_ser, 'aud_usd_info': ser_1, 'eur_aud_info': ser_2})
    new_df = pd.DataFrame(data={'aud_usd_info': df['aud_usd_info'].values, 'eur_aud_info': df['eur_aud_info'].values}, index=df['Date'].values)
    new_df.sort_index(inplace=True)
    print(new_df)

    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """
dates_ser = pd.Series(data=[tup[1] for tup in date_info], index=[tup[0] for tup in date_info])
ser_1 = pd.Series(data=[tup[1] for tup in aud_usd_info], index=[tup[0] for tup in aud_usd_info])
ser_2 = pd.Series(data=[tup[1] for tup in eur_aud_info], index=[tup[0] for tup in eur_aud_info])
print(dates_ser)
print(ser_1)
print(ser_2)
df = pd.DataFrame(data={'Date': dates_ser, 'col 1': ser_1, 'col 2': ser_2})
new_df = pd.DataFrame(data={'col 1': df['col 1'].values, 'col 2': df['col 2'].values}, index=df['Date'].values)
print(new_df)

# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]



# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

