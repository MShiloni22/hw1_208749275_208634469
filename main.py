import sys
import pandas
import data
import statistics


def main(argv):
    #question 1
    data_dict=data.load_data(argv[1],argv[2])
    statistic_functions = [statistics.sum,statistics.mean,statistics.median]
    print ("Question 1:")
    feature_list = ["hum", "t1", "cnt"]
    name_list = ["Summer", "Holiday", "All"]
    j = 3
    for i in name_list:
        if j<=4:
            data_name, data_not_name = data.filter_by_value(data_dict, argv[2][j], {1})
            data.print_details(data_name, feature_list, statistic_functions, i)
            j = j + 1
        data.print_details(data_dict, feature_list, statistic_functions, i)

    # question 2
    print ("Question 2:")
    is_above = 0
    title_list = ["Winter holiday records:", "Winter weekday records:"]
    print ("If t1<=13.0, then:")
    data_name, data_not_name = data.filter_by_value(data_dict, argv[2][4], {1})
    dict_list = [data_name, data_not_name]
    for m,k in enumerate(title_list):
        statistics.population_statistics(k, dict_list[m], argv[2][1], argv[2][2], 13.0, is_above,
                              statistic_functions)
    is_above = 1
    print("If t1>13.0, then:")
    for n,l in enumerate(title_list):
        statistics.population_statistics(l, dict_list[n], argv[2][1], argv[2][2], 13.0, is_above,
                              statistic_functions)

if __name__ == '__main__':
    main(sys.argv)