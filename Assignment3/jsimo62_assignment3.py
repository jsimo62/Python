# Import CSV class to work with CSV files
import csv

# VARIABLES LIST
ls_avg_cm_all, ls_avg_hm_all = [], []
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
file = 'mpg.csv'

# FUNCTION LIST
def group_by_class(row):
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
    return
def group_by_manuf(row):
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
    return
def mpg_calc(v_list):
    # Calculate the average
    calc = sum(v_list)/len(v_list)
    return calc
def build_the_string(ls_avg_cm_all,ls_avg_hm_all):
    # # Calculate the average for all vehicles
    calc_avg_cm_all = mpg_calc(ls_avg_cm_all)
    calc_avg_hw_all = mpg_calc(ls_avg_hm_all)
    # Make the sentence for all vehicles
    w_avg_cm_all = ('Out of all ' + str(len(ls_avg_cm_all))
        + ' vehicles, the average city mpg is ' + str(round(calc_avg_cm_all,2)) + '\n')
    w_avg_hm_all = ('Out of all ' + str(len(ls_avg_hm_all))
        + ' vehicles, the average highway MPG is ' + str(round(calc_avg_hw_all,2)) + '\n')
    return w_avg_cm_all,w_avg_hm_all
def print_to_console(w_avg_cm_all, w_avg_hm_all, c_vehicles, m_vehicles):
    print('\n***AVERAGE MPG PER CLASS***')
    for i in c_vehicles:
        print(i + ' ' + str(round(mpg_calc(c_vehicles[i]),2)))
    print('\n***AVERAGE MPG PER MANUFACTURER***')
    for i in m_vehicles:
        print(i + ' ' + str(round(mpg_calc(m_vehicles[i]),2)))
    print('\n***AVERAGE MPG FOR ALL***')
    print(w_avg_cm_all)
    print(w_avg_hm_all)
    return
def output_to_file(w_avg_cm_all, w_avg_hm_all, c_vehicles, m_vehicles):
    #-----PRINT TO TEXT FILE-----------------------------------------------------------------------------#
    # 1 - Create/Open File
    with open('jsimo62_assignment3.txt', 'w') as output:
        # 2 - Write to file
        output.write('\n\n***AVERAGE MPG PER CLASS***\n')
        for i in c_vehicles:
            output.write(i + ' ' + str(round(mpg_calc(c_vehicles[i]),2)) + '\n')
        output.write('\n\n***AVERAGE MPG PER MANUFACTURER***\n')
        for i in m_vehicles:
            output.write(i + ' ' + str(round(mpg_calc(m_vehicles[i]),2)) + '\n')
        output.write('\n\n***AVERAGE MPG FOR ALL***\n')
        output.write(w_avg_cm_all + '\n')
        output.write(w_avg_hm_all + '\n')
        return
def scan_file(file):
    with open(file, newline='') as csvfile:
        f_mpg = csv.DictReader(csvfile)
        # Loop through csv
        for row in f_mpg:
            # append to specified list
            ls_avg_cm_all.append(int(row['cty']))
            ls_avg_hm_all.append(int(row['hwy']))
            group_by_class(row)
            group_by_manuf(row)
    return

# DO THE WORK
scan_file(file)
w_avg_cm_all,w_avg_hm_all = build_the_string(ls_avg_cm_all,ls_avg_hm_all)
# SHOW ME THE RESULTS
print_to_console(w_avg_cm_all,w_avg_hm_all,c_vehicles,m_vehicles)
output_to_file(w_avg_cm_all,w_avg_hm_all,c_vehicles,m_vehicles)
