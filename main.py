import sys
import data
import statistics


def main(argv):
    #question 1
    data_dict=data.load_data(argv[1],argv[2])
    statistic_functions = [statistics.sum,statistics.mean,statistics.median]
    print ("Question 1:")
    feature_list = ["hum", "t1", "cnt"]
    name_list = ["Summer", "Holiday", "All"]
    j = 6
    for index, i in enumerate(name_list):
        if j<=8:
            data_name, data_not_name = data.filter_by_value(data_dict, feature_list[index], {1})
            data.print_details(data_name, feature_list, statistic_functions, i)
            j = j + 2
            continue
        data.print_details(data_dict, feature_list, statistic_functions, i)

    # question 2
    print ("Question 2:")
    is_above = 0
    title_list = ["Winter holiday records:", "Winter weekday records:"]
    print ("If t1<=13.0, then:")
    data_name, data_not_name = data.filter_by_value(data_dict, 'is_holiday', {1})
    dict_list = [data_name, data_not_name]
    for m,k in enumerate(title_list):
        statistics.population_statistics(k, dict_list[m], 't1', 'cnt', 13.0, is_above,
                              statistic_functions)
    is_above = 1
    print("If t1>13.0, then:")
    for n,l in enumerate(title_list):
        statistics.population_statistics(l, dict_list[n], 't1', 'cnt', 13.0, is_above,
                              statistic_functions)

if __name__ == '__main__':
    main(sys.argv)