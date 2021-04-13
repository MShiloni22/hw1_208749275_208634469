import math
import data


def sum(values):
    sum = 0
    for i in values:
        sum = sum + i
    return sum


def mean(values):
    number_of_elem = len(values)
    sum1 = sum(values)
    mean = sum1 / number_of_elem
    return mean


def median(values):
    median1 = 0
    number_of_elem = len(values)
    values_sorted = sorted(values)
    if number_of_elem % 2 == 0:
        median1 = (values_sorted[int(number_of_elem/2)]+values_sorted[(int(number_of_elem/2))+1])/2
    else:
        median1 = values_sorted[int(number_of_elem/2)+1]
    return median1


def population_statistics(feature_description, data, treatment, target, threshold, is_above,
                      statistic_functions):
    """
    This function prints central tendency statistics about 'population'.
    """
    if is_above:
        vals = [j for i, j in enumerate(data[target]) if threshold < data[treatment][i]]