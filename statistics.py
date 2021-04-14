import math
import data


def sum(values):
    sum1 = 0
    for i in values:
        sum1 = sum1 + i
    return sum1


def mean(values):
    number_of_elem = len(values)
    sum1 = sum(values)
    mean1 = sum1 / number_of_elem
    return mean1


def median(values):
    number_of_elem = len(values)
    values_sorted = sorted(values)
    if number_of_elem % 2 == 0:
        median1 = (values_sorted[int(number_of_elem/2)]+values_sorted[(int(number_of_elem/2))-1])/2
    else:
        median1 = values_sorted[int(number_of_elem/2)+1]
    return median1


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
    print(feature_description,":")
    if is_above:
        vals = [j for i, j in enumerate(data[target]) if threshold < data[treatment][i]]
        print("cnt:", mean(vals), median(vals))
    else:
        vals = [j for i, j in enumerate(data[target]) if threshold >= data[treatment][i]]
        print("cnt:", mean(vals), median(vals))