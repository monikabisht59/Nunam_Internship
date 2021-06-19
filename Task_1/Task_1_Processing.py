#!/usr/bin/env python
# coding: utf-8

__author__ = 'monika_bisht'

# importing pandas package for usage
import pandas as pd


def read_data(file):
    """
    This function reads an excel file with any number of sheets and convert it to a dataframe.
    :param file: complete path of source data file (excel) to be read
    :return: pandas dataframe having data from all sheets from the excel
    """
    return pd.read_excel(file, sheet_name=None)


def write_csv(data, pattern, output_file):
    """
    This function filters out required sheets from the dataframe based on specific patterns in sheet names and stores
    all that in respective csv files.
    :param data: dataframe that needs to be converted to csv file
    :param pattern: Pattern refers to the similar pattern in sheet names.
    :param output_file: Complete csv file path that needs to be created
    :return: Nothing
    """
    try:
        list_df = []
        for i in data.keys():
            if i.startswith(pattern):
                list_df.append(data[i])
        pd.concat(list_df).to_csv(output_file, encoding='utf-8', index=False)
        print("{0} file generated from data sourced from sheet name like {1}".format(output_file, pattern))

    except Exception as error:
        print("Execution failed with error: {}".format(error))
        raise error


def main(properties):
    """
    This is the main function of the program.
    :param properties: Input properties as dictionary
    :return: Boolean Status if run completes, else Error msg if fails.
    """
    try:
        # Iterating through all source files
        for k in range(0, len(properties['source_file_names'])):
            file = properties['working_path'] + properties['source_file_names'][k]
            dataframe = read_data(file)  # Reading the source file and storing the dataframe in a variable
            print('Successfully read file {0}'.format(file))
            # If else block is checking for iteration as post 1st iteration data read from source files get combined
            # into 1 single dataframe
            if k == 0:
                overall_data = dataframe
            else:
                overall_data = {**data, **dataframe}
            data = overall_data

        # Once all the source files are read, selective data is written back to csv files as per the pattern found in
        # sheet names
        for i in range(0, len(properties['sheet_name_patterns'])):
            write_csv(overall_data, properties['sheet_name_patterns'][i],
                      properties['working_path'] + properties['output_csv_file_names'][i])
        return True

    except Exception as error:
        print('Execution failed with error: {}'.format(error))
        raise error


if __name__ == '__main__':
    try:
        print('Process Started')
        # passing all input parameters in dictionary, all Task 1 requirements passed at the same time.
        input_properties = {
            "working_path": "C:/Users/Monika Bisht/Desktop/data_source/",
            "source_file_names": ['data.xlsx', 'data_1.xlsx'],
            "sheet_name_patterns": ['Detail_67_', 'DetailVol_67_', 'DetailTemp_67_'],
            "output_csv_file_names": ['detail.csv', 'detailVol.csv', 'detailTemp.csv'],
        }
        # Invoking Profiling
        import cProfile

        # Runs the main function and stores the profiling data in output.dat file
        cProfile.run('main(input_properties)', "output.dat")

        import pstats
        from pstats import SortKey

        # Reads the output.dat file and stores the result in readbale format in txt file sorted by time.
        with open("C:/Users/Monika Bisht/Desktop/Nunam_Internship/Task_4/output_task1_time.txt", "w") as f:
            p = pstats.Stats("output.dat", stream=f)
            p.sort_stats("time").print_stats()

        print('Process Completed')
    except Exception as e:
        print("Execution failed with error: {}".format(e))
        raise e
