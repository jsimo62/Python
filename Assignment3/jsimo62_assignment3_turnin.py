# Import CSV class to work with CSV files
import csv

# initiate list
ls_avg_cm_all, ls_avg_hm_all = [], []
# initiate dictionaries
c_vehicles = {'compact': [],
              '2seater': [],
              'compact': [],
              'midsize': [],
              'minivan': [],
              'pickup': [],
              'subcompact': [],
              'suv': [],}

m_vehicles = {'audi': [],
              'chevrolet': [],
              'dodge': [],
              'ford': [],
              'honda': [],
              'hyundai': [],
              'jeep': [],
              'land rover': [],
              'lincoln': [],
              'mercury': [],
              'nissan': [],
              'pontiac': [],
              'subaru': [],
              'toyota': [],
              'volkswagen': []}

def mpg_calc(v_list):
    # Calculate the average
    calc = sum(v_list)/len(v_list)
    return calc
def print_to_console(ls_avg_cm_all,ls_avg_hm_all,c_vehicles,m_vehicles):
    # Calculate the average for all vehicles
    calc_avg_cm_all = mpg_calc(ls_avg_cm_all)
    calc_avg_hw_all = mpg_calc(ls_avg_hm_all)

    for i in c_vehicles:
        print(i + ' ' + str(round(mpg_calc(c_vehicles[i]),2)))
    for i in m_vehicles:
        print(i + ' ' + str(round(mpg_calc(m_vehicles[i]),2)))

    return

#-----WORK WITH THE FILE---------------------------------------------------------------------------------#
with open('mpg.csv', newline='') as csvfile:
    f_mpg = csv.DictReader(csvfile)

    # Loop through csv
    for row in f_mpg:
        # append to specified list
        ls_avg_cm_all.append(int(row['cty']))
        ls_avg_hm_all.append(int(row['hwy']))

        # group the vehicles by class
        if row['class'] == 'compact':
            c_vehicles['compact'].append(int(row['hwy']))
        elif row['class'] == 'midsize':
            c_vehicles['midsize'].append(int(row['hwy']))
        elif row['class'] == 'suv':
            c_vehicles['suv'].append(int(row['hwy']))
        elif row['class'] == '2seater':
            c_vehicles['2seater'].append(int(row['hwy']))
        elif row['class'] == 'pickup':
            c_vehicles['pickup'].append(int(row['hwy']))
        elif row['class'] == 'minivan':
            c_vehicles['minivan'].append(int(row['hwy']))
        elif row['class'] == 'subcompact':
            c_vehicles['subcompact'].append(int(row['hwy']))

        # Group the vehicles by manufacturer
        if row['manufacturer'] == 'audi':
            m_vehicles['audi'].append(int(row['hwy']))
        elif row['manufacturer'] == 'chevrolet':
            m_vehicles['chevrolet'].append(int(row['hwy']))
        elif row['manufacturer'] == 'dodge':
            m_vehicles['dodge'].append(int(row['hwy']))
        elif row['manufacturer'] == 'ford':
            m_vehicles['ford'].append(int(row['hwy']))
        elif row['manufacturer'] == 'honda':
            m_vehicles['honda'].append(int(row['hwy']))
        elif row['manufacturer'] == 'hyundai':
            m_vehicles['hyundai'].append(int(row['hwy']))
        elif row['manufacturer'] == 'jeep':
            m_vehicles['jeep'].append(int(row['hwy']))
        elif row['manufacturer'] == 'land rover':
            m_vehicles['land rover'].append(int(row['hwy']))
        elif row['manufacturer'] == 'lincoln':
            m_vehicles['lincoln'].append(int(row['hwy']))
        elif row['manufacturer'] == 'mercury':
            m_vehicles['mercury'].append(int(row['hwy']))
        elif row['manufacturer'] == 'nissan':
            m_vehicles['nissan'].append(int(row['hwy']))
        elif row['manufacturer'] == 'pontiac':
            m_vehicles['pontiac'].append(int(row['hwy']))
        elif row['manufacturer'] == 'subaru':
            m_vehicles['subaru'].append(int(row['hwy']))
        elif row['manufacturer'] == 'toyota':
           m_vehicles['toyota'].append(int(row['hwy']))
        elif row['manufacturer'] == 'volkswagen':
           m_vehicles['volkswagen'].append(int(row['hwy']))

    # # Calculate the average for all vehicles
    calc_avg_cm_all = mpg_calc(ls_avg_cm_all)
    calc_avg_hw_all = mpg_calc(ls_avg_hm_all)
    #
    # for i in c_vehicles:
    #     print(i + ' ' + str(round(mpg_calc(c_vehicles[i]),2)))
    # for i in m_vehicles:
    #     print(i + ' ' + str(round(mpg_calc(m_vehicles[i]),2)))
    print_to_console(ls_avg_cm_all,ls_avg_hm_all,c_vehicles,m_vehicles)
    # Make the sentence for all vehicles
    w_avg_cm_all = ('Out of all ' + str(len(ls_avg_cm_all))
        + ' vehicles, the average city mpg is ' + str(round(calc_avg_cm_all,2)) + '\n')
    w_avg_hm_all = ('Out of all ' + str(len(ls_avg_hm_all))
        + ' vehicles, the average highway MPG is ' + str(round(calc_avg_hw_all,2)) + '\n')

    #-----PRINT TO TEXT FILE-----------------------------------------------------------------------------#
    # 1 - Create/Open File
    output = open('jsimo62_assignment3.txt', 'w+')
    # 2 - Write to file
    output.write(w_avg_cm_all + '\n')
    output.write(w_avg_hm_all + '\n')
    # output.write(w_avg_hm_audi + '\n')
    output.close()


    #-----TEST OUTPUTS ----------------------------------------------------------------------------------#
    # Print sets to command line
    #print(s_manuf)
    #print(s_class)
    # Pring grouped by list to command newline
    #print(ls_avg_hm_manuf)
    #print(ls_avg_hm_class)
    # Print the sentences in command line
    print(w_avg_cm_all)
    print(w_avg_hm_all)
    # print(w_avg_hm_audi)
