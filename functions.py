import os
import pandas
import numpy as np


# separating data based on sample position #
# position: int value, name: assumed that extension is .dat #

def separate_pos(name, position):
    filename = '{}.dat'.format(name)
    data = pandas.read_csv(filename)
    data_st = data[data['Position (Deg)'] == position]

    return data_st


# mkdir to organize files #
# parent - path to project folder, dirname - name of a folder we want to create #


def makedir(parent, dirname):
    path = os.path.join(parent, dirname)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    return path


# creation of a csv file in new directory based on sample position #


def position_csv(dane_st, parent, dirname, filename):
    path = makedir(parent, dirname)
    name = '{}.csv'.format(filename)
    filepath = os.path.join(path, name)
    dane_st.to_csv((filepath), index=False)


# saving rows for constant field measurement to csv file and returning dataframe #
# field: int value #


def fast_csv(data, field, dirname):
    rounded_temp = data['Map23 (K)'].round(2)
    data['rounded temp'] = rounded_temp
    df_diff = (data['rounded temp'] - data['rounded temp'].shift(1))
    data['diff'] = df_diff
    fastmeasurement = data[(data['Field (Oe)'] == field)]
    fastmeasurement.to_csv(f'{dirname}/fastmeasurement.csv', index=False)

    return fastmeasurement


# manually check if fastmeasurement does not contain slow measurements for a given field! #
# saving rows for alternating field measurement to csv file and returning dataframe #


def slow_csv(fastmeasurement, data, dirname):
    slowmeasurement = pandas.concat([fastmeasurement, data], ignore_index=True).drop_duplicates(keep=False)
    slowmeasurement.to_csv(f'{dirname}/slowmeasurement.csv', index=True)

    return slowmeasurement


# selecting by temperature and saving to the new directory for each temp value #


def temp_csv(slowmeasurement, parent):
    change_points = slowmeasurement.loc[
        (slowmeasurement['diff'].abs() >= 1) | (slowmeasurement['diff'].apply(np.isnan))]
    change_points.sort_index(axis=0)
    indexes = change_points.index.tolist()

    names = []
    for index in indexes:
        names.append((change_points['Map23 (K)'][index]).round(1))

    i = 0
    for index in indexes:

        name = '{} K.csv'.format(names[i])
        newdir = '{} K'.format(names[i])
        path = makedir(parent, newdir)
        filepath = os.path.join(path, name)

        if index == indexes[-1]:

            newdf = slowmeasurement.loc[indexes[-1]:]
            newdf.to_csv(filepath, index=False)
        else:
            newdf = slowmeasurement.loc[indexes[i]: ((indexes[i + 1]) - 1)]
            newdf.to_csv(filepath, index=False)
        i += 1
        # newdf.to_csv(name, index=False)?

    return names


# separating each temperature csv file depending on [Oe] sign #
# creating csv files for positive and negative values in previously created directory #
def signs_csv(inputpath, names):
    for name in names:
        dirpath = '{}/{} K'.format(inputpath, name)
        inputfilepath = '{}/{} K.csv'.format(dirpath, name)

        data = pandas.read_csv(inputfilepath)
        neg_K = data[data['Field (Oe)'] < 0]
        neg_name = '{}/{}_neg.csv'.format(dirpath, name)
        neg_K.to_csv(neg_name, index=False)
        pos_K = data[data['Field (Oe)'] > 0]
        pos_name = '{}/{}_pos.csv'.format(dirpath, name)
        pos_K.to_csv(pos_name, index=False)

    return None