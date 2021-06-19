#!/usr/bin/env python
# coding: utf-8

__author__ = 'monika_bisht'

# importing pandas package for usage
import pandas as pd


def down_sampling(data_frame, key_column):
    """
    This function reduces the sampling of provided data from 1 sample/second to 1 sample/minute.
    :param data_frame: Pandas Dataframe that needs to resampled
    :param key_column: DateTime column on which the sampling will be based on
    :return: Downsampled dataframe
    """
    min_time_entry = data_frame[key_column].min()
    max_time_entry = data_frame[key_column].max()
    time_series = pd.Series(pd.date_range(min_time_entry, max_time_entry, freq='T'))
    date_time_df = time_series.to_frame(name=key_column)
    return pd.merge(data_frame, date_time_df, how="inner", on=key_column)


def read_data(file_name, key_column):
    """
    This function reads a csv file
    :param file_name: Complete input file path of csv file
    :param key_column: DateTime Column on which sampling is based on
    :return: dataframe
    """
    return pd.read_csv(file_name, parse_dates=[key_column], index_col=0, encoding='utf-8')


def write_csv(final_df, output_file):
    """
    This function write a dataframe to csv file
    :param final_df: Dataframe
    :param output_file: Complete Output file path of csv file
    :return: Nothing
    """
    return final_df.to_csv(output_file, encoding='utf-8', index=False)


def main(properties):
    """
    This is the main function of the program.
    :param properties: Input properties as dictionary
    :return: Boolean Status if run completes, else Error msg if fails.
    """
    try:
        # Iterating through all source files
        for k in range(0, len(properties["source_file_names"])):
            file = properties["working_path"] + properties["source_file_names"][k]
            key_column = properties["key_column_name"][k]
            output_file_name = properties["working_path"] + properties["output_csv_file_names"][k]
            source_data = read_data(file, key_column)
            down_sampled_data = down_sampling(source_data, key_column)
            write_csv(down_sampled_data, output_file_name)

    except Exception as error:
        print("Execution failed with error: {}".format(error))
        raise error


if __name__ == '__main__':
    try:
        print('Process Started')
        # passing all input parameters in dictionary, all Task 1 requirements passed at the same time.
        input_properties = {
            "working_path": "C:/Users/Monika Bisht/Desktop/data_source/",
            "source_file_names": ['detail.csv', 'detailVol.csv', 'detailTemp.csv'],
            "key_column_name": ['Absolute Time', 'Realtime', 'Realtime'],
            "output_csv_file_names": ['detailDownsampled.csv', 'detailVolDownsampled.csv', 'detailTempDownsampled.csv'],
        }
        # Invoking Profiling
        import cProfile

        # Runs the main function and stores the profiling data in output.dat file
        cProfile.run('main(input_properties)', "output.dat")

        import pstats
        from pstats import SortKey

        # Reads the output.dat file and stores the result in readbale format in txt file sorted by time.
        with open("C:/Users/Monika Bisht/Desktop/Nunam_Internship/Task_4/output_task2_time.txt", "w") as f:
            p = pstats.Stats("output.dat", stream=f)
            p.sort_stats("time").print_stats()

        print('Process Completed')
    except Exception as e:
        print("Execution failed with error: {}".format(e))
        raise e
