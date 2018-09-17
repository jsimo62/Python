# Import CSV class to work with CSV files
import csv

#-----WORK WITH THE FILE---------------------------------------------------------------------------------#
with open('mpg.csv', newline='') as csvfile:
    f_mpg = csv.DictReader(csvfile)

    # initiate list
    ls_avg_cm_all, ls_avg_hm_all, ls_avg_hm_class, ls_avg_hm_manuf = [], [], [], []
    # initiate sets
    s_manuf, s_class = set(),set()

    # Loop through csv
    for row in f_mpg:
        # Create a set of unique manufacurers and classes
        s_manuf.add(row['manufacturer'])
        s_class.add(row['class'])
        # append to specified list
        ls_avg_cm_all.append(int(row['cty']))
        ls_avg_hm_all.append(int(row['hwy']))


    # Calculate the average for all vehicles
    calc_avg_cm_all = sum(ls_avg_cm_all)/len(ls_avg_cm_all)
    calc_avg_hw_all = sum(ls_avg_hm_all)/len(ls_avg_hm_all)

    # Make the sentence for all vehicles
    w_avg_cm_all = ('Out of all ' + str(len(ls_avg_cm_all))
        + ' vehicles, the average city mpg is ' + str(round(calc_avg_cm_all,2)) + '\n\n')
    w_avg_hm_all = ('Out of all ' + str(len(ls_avg_hm_all))
        + ' vehicles, the average highway MPG is ' + str(round(calc_avg_hw_all,2)) + '\n\n')

    #-----PRINT TO TEXT FILE-----------------------------------------------------------------------------#
    # 1 - Create/Open File
    output = open('jsimo62_assignment3.txt', 'w+')
    # 2 - Write to file
    output.write(w_avg_cm_all)
    output.write(w_avg_hm_all)
    output.close()

    #-----TEST OUTPUTS ----------------------------------------------------------------------------------#
    # Print sets to command line
    print(s_manuf)
    print(s_class)
    # Pring grouped by list to command newline
    #print(ls_avg_hm_manuf)
    #print(ls_avg_hm_class)
    # Print the sentences in command line
    #print(w_avg_cm_all)
    #print(w_avg_hm_all)
