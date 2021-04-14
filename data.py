import pandas


# load_data function
def load_data(path, features):
    """
    This function turns the .csv dataset into a dictionary, using pandas
    :param path: the path of the csv file
    :param features: list of the relevant features
    :return: dictionary - data
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    return data


# filter_by_value function
def filter_by_value(data, feature, value):
    """
    This function splits a dictionary to two separate ones,
    according to whether a row's 'feature' value is in a set of 'special values' or not.
    In the end, all the rows with a special value are in data1 and all the others
    are in data2.
    :return: two dictionaries - data1 and data2
    """
    data1 = {}
    data2 = {}
    for i in data:
        data1.update({i: []})
        data2.update({i: []})
    for i in range(len(data[feature])):
        if data[feature][i] in value:
            for j in data:
                data1[j].append(data[j][i])
        else:
            for j in data:
                data2[j].append(data[j][i])
    return data1, data2


# print_details function
def print_details(data, features, statistic_functions,name):
    print (name,":")
    for i in features:
        leng = len(statistic_functions)
        print(i, ":", end="")
        for j in statistic_functions:
            if leng == 1:
                print(" ", j(data[i]), sep="")
            else:
                print(" ", j(data[i]), ",", sep="", end="")
            leng -= 1