# Nunam_Internship
Nunam_Internship

Description:
This repository has been created to store the deliverables of the assignment provided for Nunam Internship Porgramme.

Content:
Repository contains below folders:

Task_1 : Stores the script to combine 2 of the same data source files and create 3 csv files out of them as per the requirement. Script - does following tasks.
      Converts data.xls and data_1.xls into dataframe and process it further to create 3 csvs namely 'detail.csv' , 'detailVol.csv','detailTemp.csv'.  

Task_2 : Stores the script to downsample the data from 1 sample/second to 1 sample/minute from the files created in task_1.

Task_4: Stores output of cProfiling on the functions mentioned in the scripts from task_1 and task_2 in text file.


How to Run:

1. Clone repository to localhost or server where you intended to run these scripts.
      git clone https://github.com/monikabisht59/Nunam_Internship.git
  
2. Install Python and required packages (pandas, openpyxl).

3. To run Task_1_Processing.py:
      Update the "working_path" variable to the location where source files are stored. Line #78
      Update the path where the output of profiling needs to be stored. Line #93

4. After running Task_1_Processing.py, 3 .csv files will be created which is the source for Task_2_Processing.py. Follow below:
      Update the "working_path" variable to the location where source files are stored. Line #70
      Update the path where the output of profiling needs to be stored. Line #85

5. Profiling data for Task1 and Task2 will be stored in 'output_task1_time.txt' and 'output_task2_time.txt' respectively in the location mentioned.

