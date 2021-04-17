


def sum_f(values):
    """
    Calculates sum
    :param values: list of values
    :return: sum of values
    """
    sum1 = 0
    for i in values:
        sum1 = sum1 + i
    return sum1


def mean(values):
    """
    Calculates mean, using 'sum' function
    :param values: list of values
    :return: mean
    """
    number_of_elem = len(values)
    sum1 = sum_f(values)
    mean1 = sum1 / number_of_elem
    return mean1


def median(values):
    """
    Returns the median value in the list
    :param values: list of values
    :return: median value
    """
    number_of_elem = len(values)
    values_sorted = sorted(values)
    # split to two cases, determined by the total number of values - odd/even
    if number_of_elem % 2 == 0:
        median1 = (values_sorted[int(number_of_elem/2)]+values_sorted[(int(number_of_elem/2))-1])/2
    else:
        median1 = values_sorted[int(number_of_elem/2)]
    return median1*1.0


def population_statistics(feature_description, data, treatment, target, threshold, is_above,
                          statistic_functions):
    """
    Prints statistics measures about 'target', using statistic functions
    :param feature_description: a string to print
    :param data: dataset from which we take the values
    :param treatment: a special feature, determining by it which values to take
    :param target: the feature we want to print statistic measures about
    :param threshold: a special value of 'treatment', divides feature 'treatment' to two groups
    :param is_above: boolean value, goes along with 'threshold'
    :param statistic_functions: sum, mean and median functions
    """
    print(feature_description)
    if not is_above:
        # insert relevant values to a list, according the given condition
        vals = [j for i, j in enumerate(data[target]) if threshold >= data[treatment][i]]
        print("cnt: ", statistic_functions[1](vals), ", ", statistic_functions[2](vals), sep="")
    else:
        vals = [j for i, j in enumerate(data[target]) if threshold < data[treatment][i]]
        print("cnt: ", statistic_functions[1](vals), ", ", statistic_functions[2](vals), sep="")
