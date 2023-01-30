import os
import pandas
import numpy as np


# choosing data for 90 or 0 deg position #


def separate_position(name, position):
    filename = '{}.dat'.format(name)
    data = pandas.read_csv(filename)
    dane_st = data[data['Position (Deg)'] == position]

    return dane_st


# mkdir to organize files #
# parent - path to project folder, dirname - folder we want to create, filename - the csv file #


def makedir(parent, dirname, filename):
    path = os.path.join(parent, dirname)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    filepath = os.path.join(path, filename)

    return filepath


# create csv file in new directory#


def position_csv(dane_st, parent_var, dirname, filename):
    dirname = str(dirname)
    name = '{}.csv'.format(filename)
    dane_st.to_csv(makedir(parent_var, dirname, name), index=False)


# saves row for constant field fast measurement to csv file and returns dataframe


def fast_separate(data, field, dirname):
    rounded_temp = data['Map23 (K)'].round(2)
    data['rounded temp'] = rounded_temp
    df_diff = (data['rounded temp'] - data['rounded temp'].shift(1))
    data['diff'] = df_diff
    fastmeasurement = data[(data['Field (Oe)'] == field)]
    fastmeasurement.to_csv(f'{dirname}/fastmeasurement.csv', index=False)

    return fastmeasurement


# manually check if fastmeasurement does not contain slow measurement for a given field #


def slow_separate(fastmeasurement, data, dirname):
    slowmeasurement = pandas.concat([fastmeasurement, data], ignore_index=True).drop_duplicates(keep=False)
    slowmeasurement.to_csv(f'{dirname}/slowmeasurement.csv', index=True)

    return slowmeasurement


# selecting by temperature: 2, 4, 6, 8, 10, 25, 50, 100
# searching for change points in the file


def separate_temp(slowmeasurement, dirname):
    change_points = slowmeasurement.loc[
        (slowmeasurement['diff'].abs() >= 1) | (slowmeasurement['diff'].apply(np.isnan))]
    change_points.sort_index(axis=0)
    indexes = change_points.index.tolist()
    names = []
    for index in indexes:
        names.append((change_points['Map23 (K)'][index]).round(1))

    i = 0
    for index in indexes:

        name = '{}/{} K.csv'.format(dirname, names[i])

        if index == indexes[-1]:

            newdf = slowmeasurement.loc[indexes[-1]:]
            newdf.to_csv(name, index=False)
        else:
            newdf = slowmeasurement.loc[indexes[i]: ((indexes[i + 1]) - 1)]
            newdf.to_csv(name, index=False)
        i += 1

    return None