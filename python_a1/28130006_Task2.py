# This python program has been developed by Arushi Tejpal with student ID:28130006.
# This program is for Task 2 Assignment 1 for the unit: FIT9132
# The start date of this python program is on the 12th of April 2020.
# The of aim this assignment is to stimulate the stocking level of one product, the Cantilever Umbrellas based on the information
# provided with in assignment for algorithm used.
# Furthermore, the aim of the task 2 is to get start of a year data for stock and revenue from
# a file AU_INV_START.txt and create a file AU_INV_END.txt for stock and revenue for end of the year.
# This program will calculate total stock remaining and total revenue of default value of three year cycle.
# This program will also account for global financial crisis, defective items and inflation increase.
#version 0.1 : 10/april/2020 program started
#verion 0.4 : 14/4/2020 updated main menu with error checking and read and write files
#updated with proper checks 28/4/2020
#updated 1st May- removed main function and fixed bugs.
#This program used pycharm 2019 3.3
#Task 2 completed on the 29th of April 2020
#Reference:
#stackoverflow.com
#udemmy.com
#FIT9136 lecture notes week 1 to week 4
#docs.python.org

############### Any Import ###########
import math
######## Global Value ################
base_year =  2000 # year start of the company
last_year=2040 # Upper year limit for the program as per the assignment

NO_YEAR_SIM = 3 #3 year simulation

CRIS_RECUR_FREQUENCY = 9 #if every 9 years Crisis frequency
CRIS_years=2 # if Crisis stays for 2 years
PER_DEF = 0.05 #5% defective item each month

####Base Values####
base_RRP=587.5 #$705 was 20% increased peak vlaue i.e 705/1.2
quantity=26.6 #36 was 35% increased value of Peak i.e 36/1.35
low_stock=400   # stock low level
stock_uplift=600    # stock uplift if stock reaches at low level
input_file = "AU_INV_START.txt"
output_file = "AU_INV_END.txt"

###############  Reading Writting data Functions##########


#####################create some DateTime Functions############

def is_leap(year):
    """check if year is leap"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_before_year(year):
    """Convert year -> number of days before January 1st of year."""
    y = year - 1
    return y*365 + y//4 - y//100 + y//400

def days_in_month(year, month):
    """Convert year, month -> number of days in that month in that year."""
    _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert 1 <= month <= 12, month
    if month == 2 and is_leap(year):
        return 29
    return _DAYS_IN_MONTH[month]

def days_before_month(year, month):
    """Convert year, month ->  number of days in year preceding first day of month."""
    _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _DAYS_BEFORE_MONTH = [-1]  # -1 is a placeholder for indexing purposes.
    dbm = 0
    for dim in _DAYS_IN_MONTH[1:]:
        _DAYS_BEFORE_MONTH.append(dbm)
        dbm += dim
    del dbm, dim
    assert 1 <= month <= 12, 'month must be in 1..12'
    return _DAYS_BEFORE_MONTH[month] + (month > 2 and is_leap(year))

def ymd2num(year, month, day):
    """Convert year, month, day -> to a Number"""
    assert 1 <= month <= 12, 'month must be in 1..12'
    dim = days_in_month(year, month)
    assert 1 <= day <= dim, (f"day must be in 1..{dim}")
    return (days_before_year(year) +
            days_before_month(year, month) +
            day)


def _check_int_field(value):
    """checks values is Int"""
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        raise TypeError('integer argument expected, got float')
    if isinstance(value,str):
        raise TypeError('integer argument expected, got string')

def _check_float_int_field(value):
    """check Value is Float & Int for Rev or Stock"""
    if isinstance(value, float):
        return value
    if isinstance(value, int):
        raise value
    if isinstance(value,str):
        raise TypeError('integer argument expected, got string')

def check_year_limit(value):
        """check year Limit is correct"""
        global base_year, last_year
        value=_check_int_field(value)
        if value in range(base_year, last_year):
            return (value)
        else:
            raise TypeError("Error it should be between base and last year e.g. 2000 to 2040")


def check_stock_limit(message):
    """check stock value is correct"""
    message1 = _check_float_int_field(message)
    if message1 > 0:
        return (message1)
    else:
        raise TypeError("Error it should be more than zero")


def check_revenue_limit(message):
    """check revenue Value is correct"""
    message1 = _check_float_int_field(message)
    if message1 >= 1:
        message1 = round(message1, 2)
        return (message1)
    else:
        raise TypeError("Error it should be more than 1 min value of Revenue")


def read_data():
    """read data from file"""
    global input_file
    start_dic = {
        "start_date": 0,
        "start_stock": 0,
        "start_revenue": 0
    }
    try:
        with open(input_file, "r") as rf:

            for item in start_dic:
                line = rf.readline()
                line = line.strip()
                start_dic[item] = line
            #####Some Error Checking to the input######
            key_lists = list(start_dic.values())
            s_date = (key_lists[0])
            s_stock = float((key_lists[1]))
            s_revenue = float((key_lists[2]))
            assert len(s_date) >= 8, "date format should be more than 8 char"
            yy = int(s_date[0:4])
            mm = int(s_date[4:6])
            dd = int(s_date[6:8])

            _ = check_year_limit(yy) # only checking the value is correct
            assert 1 <= mm <= 12, 'month must be in 1..12'
            dim = days_in_month(yy, mm)
            assert 1 <= dd <= dim, (f"day must be in 1..{dim}")
            s_stock = check_stock_limit(s_stock)
            s_revenue = check_revenue_limit(s_revenue)
            data_dic = {}   # setting dict for output
            data_dic.update({'start_year': yy})
            data_dic.update({'start_stock': s_stock})
            data_dic.update({'start_revenue': s_revenue})
            data_dic.update({'start_month': mm})
            data_dic.update({'start_date': dd})
            return (data_dic)
    except IOError:
        print("file does not exist")
        print("Please ensure input file 'AU_INV_START.txt' file exist in the same directory as Python script")

def write_data(data_dic):
    """write data to file back after simulation"""
    global output_file
    values = data_dic.values()
    values_list = list(values)
    try:
        with open(output_file, "w+") as wf:
            wf.writelines(f"{values_list[0]:02}{values_list[3]:02}{values_list[4]:02}\n")
            wf.writelines(f"{values_list[1]}\n")
            wf.writelines(f"{values_list[2]}\n")
    except IOError:
            print("file does not exist")
            print("Please ensure AU_INV_END.txt file exist in the same directory as Python script")

############################

def num2ymd(n):
    """Convert a Day Nummber to -> (year, month, day).
        This will only be used to check date during simulation"""
    _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _DAYS_BEFORE_MONTH = [-1]  # -1 is a placeholder for indexing purposes.
    dbm = 0
    for dim in _DAYS_IN_MONTH[1:]:
        _DAYS_BEFORE_MONTH.append(dbm)
        dbm += dim
    del dbm, dim

    _DI400Y = days_before_year(401)  # number of days in 400 years
    _DI100Y = days_before_year(101)  # "    "   "   " 100   "
    _DI4Y = days_before_year(5)  # "    "   "   "   4   "
    # A 4-year cycle has an extra leap day over what we'd get from pasting
    assert _DI4Y == 4 * 365 + 1
    assert _DI400Y == 4 * _DI100Y + 1
    assert _DI100Y == 25 * _DI4Y - 1
    n -= 1
    n400, n = divmod(n, _DI400Y)
    year = n400 * 400 + 1   # ..., -399, 1, 401, ...
    n100, n = divmod(n, _DI100Y)
    # Now compute how many 4-year cycles precede it.
    n4, n = divmod(n, _DI4Y)
    n1, n = divmod(n, 365)
    year += n100 * 100 + n4 * 4 + n1
    if n1 == 4 or n100 == 4:
        assert n == 0
        return year-1, 12, 31
    # Now the year is correct, and n is the offset from January 1.  We find
    leapyear = n1 == 3 and (n4 != 24 or n100 == 3)
    assert leapyear == is_leap(year)
    month = (n + 50) >> 5
    preceding = _DAYS_BEFORE_MONTH[month] + (month > 2 and leapyear)
    if preceding > n:  # estimate is too large
        month -= 1
        preceding -= _DAYS_IN_MONTH[month] + (month == 2 and leapyear)
    n -= preceding
    assert 0 <= n < days_in_month(year, month)
    # Now the year and month are correct, and n is the offset from the
    return year, month, n+1

def _check_date_fields(year, month, day):
    """checking date is correct"""
    global base_year,last_year
    year = _check_int_field(year)
    month = _check_int_field(month)
    day = _check_int_field(day)
    if not base_year <= year <= last_year:
        raise ValueError(f"year must be in {base_year} and {last_year}, {year}")
    if not 1 <= month <= 12:
        raise ValueError(f"month must be in 1..12, {month}")
    dim = days_in_month(year, month)
    if not 1 <= day <= dim:
        raise ValueError(f"day must be in 1..{dim}, {day}")
    return year, month, day


def _add_years(year,month,day,num):
    """add years of simulation require and provide the end date"""
    new_year=year+num
    if month==2 and day==28 and is_leap(year) and is_leap(new_year):
        day=day
    elif month==2 and day==29 and is_leap(year) and is_leap(new_year)==False:
        day=28
    elif month ==2 and day==28 and is_leap(year)==False and is_leap(new_year)==True:
        day=29
    elif month==2 and day >=29 and is_leap(year)==False:
        print("invalid date")
        raise TypeError('Feb date should be valid')
    elif  day > 31 or day <1 :
        raise TypeError("date is not valid")
    elif month >12 or month<1 :
        raise TypeError("month is not valid")
    _check_date_fields(new_year,month,day)
    return new_year,month,day


def create_day_list(start_year,smonth,sday,num,year):
    """this will create the days list of each month depending upon the year for simluation"""
    assert start_year<=year <= start_year+num, 'year must be in between the year range'
    newyear, emonth, eday = _add_years(start_year, smonth, sday, num)

    if start_year == year:
        daylist = [days_in_month(start_year, j) for j in range(1, 13)]
        daylist = daylist[smonth - 1:]
        daylist[0] = (days_in_month(start_year, smonth) - (sday-1))
        return daylist
    elif year == start_year + num:
        endlist = [days_in_month(newyear, j) for j in range(1, emonth)]
        endlist.append(eday)
        return endlist
    else:
        otherlist = [days_in_month(year, j) for j in range(1, 13)]
        return otherlist


##############################Create GFC impact list########################################

def update_with_gfc(year):
    """this provide value for a particular year based on GFC impact
    Return  with no GFC impact =0,for 1 year impact= 1,
    for 2nd year impact =2 for 3rd year impact =3"""
    global CRIS_RECUR_FREQUENCY,CRIS_years,base_year
    gfc_rem = ((year) - (base_year-CRIS_years)) % (CRIS_RECUR_FREQUENCY+CRIS_years)
    if gfc_rem == 0:
        return 1
    elif gfc_rem == 1:
        return 2
    elif gfc_rem == 2 and year==base_year:
        return 0
    elif gfc_rem == 2:
        return 3
    else:
        return 0



def create_list_years (start_year):
    """This will be used for calculating the base RRP and Q"""
    years=[]
    for i in range(base_year,start_year+1):
        years.append(i)
    return(years)

def base_RRP_Q_with_gfc(start_year):
    """This will provide base RRP for the year based on GFC impact"""
    global base_RRP, quantity,CRIS_RECUR_FREQUENCY, CRIS_years, base_year
    list_of_list=[]
    base_RRP_list=[]
    base_Q_list=[]
    years = create_list_years(start_year)
    Y_RRP=base_RRP
    Y_quantity=quantity

    for year in years:
        gfc_rem = ((year) - (base_year - CRIS_years)) % (CRIS_RECUR_FREQUENCY + CRIS_years)
        if gfc_rem == 0: #no GFC year
            Y_RRP=int(round(Y_RRP*1.15))
            base_RRP_list.append(Y_RRP)
            Y_quantity=int(round(Y_quantity*0.9))
            base_Q_list.append(Y_quantity)
            list_of_list.append(1)
        elif gfc_rem == 1: #GFC year 1
            Y_RRP=int(round(Y_RRP*1.1)) #10% increase in RRP
            base_RRP_list.append(Y_RRP)
            Y_quantity = int(round(Y_quantity))
            base_Q_list.append(Y_quantity)
            list_of_list.append(2)
        elif gfc_rem == 2 and year==base_year:
            Y_RRP=int(round(Y_RRP*1.05)) #GFC year 2: 5% increase RRP
            base_RRP_list.append(Y_RRP)
            Y_quantity = int(round(Y_quantity * 1.1))
            base_Q_list.append(Y_quantity)
            list_of_list.append(0)
        elif gfc_rem == 2:
            Y_RRP = int(round(Y_RRP * 1.08))
            base_RRP_list.append(Y_RRP)
            Y_quantity = int(round(Y_quantity * 1.05))
            base_Q_list.append(Y_quantity)
            list_of_list.append(3)
        else:
            Y_RRP = int(round(Y_RRP * 1.05))
            base_RRP_list.append(Y_RRP)
            Y_quantity = int(round(Y_quantity * 1.1))
            base_Q_list.append(Y_quantity)
            list_of_list.append(0)
    full_list = list(zip(years,list_of_list,base_RRP_list,base_Q_list))
    for i, y, r, q in full_list:
        if i == start_year - 1:
            return r, q
        elif i == base_year:
            return base_RRP,quantity
        else:
            print("Error in getting the base RRP & Quantity")



def provide_RRP(year):
    """This will provide RRP of a Year with FirstPeaak, FirstOffpeak
        SecondOffPeak and SecondPeak information"""
    global base_RRP,base_year
    gfc_status=update_with_gfc(year) # checking the GFC status
    year_RRP, _ = base_RRP_Q_with_gfc(year)
    if gfc_status == 0:  #NO GFC EFFECT
        jan_value = int(round(year_RRP * 1.2)) #increase in january peak by 20% RRP peak season
        march_value = int(round(year_RRP))   # base value RRP no increase - no peak season
        july_value= int(round(year_RRP * 1.05)) #increase RRP by 5% inflation period starts 1st July
        nov_value= int(round(year_RRP * 1.25)) #increase by 25% because of inflation and peak season
    elif gfc_status == 1:   #GFC YEAR 1: 10% increase
        jan_value= int(round(year_RRP * 1.3))  #GFC EFFECT by 10% and peak season by 20% will increase RRP by 30#
        march_value=int(round(year_RRP * 1.1)) #increase march RRP value by 10% by effect of GFC year 1
        july_value= int(round(year_RRP * 1.15)) #increase july RRP by 15% as GFC year 1 and inflation 5% increase
        nov_value= int(round(year_RRP * 1.35)) #increase RRP 35%  due to inflation, peak and GFP increase effect.
    elif gfc_status == 2: # GFC YEAR 2: 5% increase
        jan_value= int(round(year_RRP * 1.25))  #GFC effect by 5% and peak season effect by 20% increase
        march_value= int(round(year_RRP * 1.05)) #GFC effect by 5% no peak season
        july_value=int(round(year_RRP * 1.1)) #GFC increase by 5% and inflation effect by 5%
        nov_value= int(round(year_RRP * 1.3)) #GFC increase 5%, peak season by 20% and inflation increase by 5%
    elif gfc_status == 3: #GFC YEAR 3: 3% increase
        jan_value= int(round(year_RRP * 1.23))  #effect of peak season 20% and GFC increase 3%
        march_value= int(round(year_RRP * 1.03)) # base price effect GFC by 3%
        july_value= int(round(year_RRP * 1.08)) #base price effect GFC by 3% and inflation by 5%
        nov_value= int(round(year_RRP * 1.28)) #base price effect GFC by 3%, inflation by 5% and peak season by 20%
    return jan_value,march_value,july_value,nov_value

def provide_quantity(year):
    """This will provide quantity of a Year with FirstPeaak, FirstOffpeak
        SecondOffPeak and SecondPeak information"""
    global base_year,quantity
    gfc_quantstatus=update_with_gfc(year)
    _, year_quantity = base_RRP_Q_with_gfc(year)
    if gfc_quantstatus == 0:
        jan_value= int(round(year_quantity * 1.35))
        march_value= int(round(year_quantity))
        july_value = int(round(year_quantity * 1.1))  # inflation
        nov_value = int(round(year_quantity * 1.45))  # peak and inflation
    elif gfc_quantstatus == 1:
        jan_value= int(round(year_quantity * 1.15))  # peak and year 1 gfc infation so .35 - .20 = 1.15
        march_value= int(round(year_quantity * 0.8))  # 20% decrease in GF non peak . base price
        july_value = int(round(year_quantity * 1.1)) # GFC influence 20% decreae and 10% increase in inflation so 20% - 10%
        nov_value = int(round(year_quantity * 1.25)) # GFC decrease 20% and 10%inflation increase, 35% increase so 45% - 20% = 1.25
    elif gfc_quantstatus == 2:
        jan_value = int(round(year_quantity * 1.25))  # peak quantity year 2 gfc inflation so 35% - 10%
        march_value = int(round(year_quantity * 0.9))  # GFC decrease  10% decrease = 0.9
        july_value = int(round(year_quantity))  # 10% inflation and 10# decrease in year 2 GFC
        nov_value= int(round(year_quantity * 1.35)) # 35% peak season, 10% increase inflation but, decrease 10% GFC = 35%
    elif gfc_quantstatus == 3:
        jan_value= int(round(year_quantity * 1.3))  # 35% peak and GFC year 3 decrease 5% = 30%
        march_value = int(round(year_quantity * 0.95)) # quantity decrease 5% GFC
        july_value= int(round(year_quantity * 1.05))  # 5% decrease GFC, 10% increase inflation
        nov_value = int(round(year_quantity * 1.4))  # peak increase, inflation increase, GFC decrease: 35%+10% - 5% = 40%

    return jan_value, march_value, july_value, nov_value


########################## Main start Calculation and Simulation #########################

def cal_stock_revenue(data_dic):
    """This will calculate and simulate the stock and revenue"""
    global NO_YEAR_SIM,PER_DEF,low_stock,stock_uplift
    ######checking the data in#########
    try:
        start_year = int(data_dic['start_year'])
        start_stock = float(data_dic['start_stock'])
        start_revenue = float(data_dic['start_revenue'])
        smonth=int(data_dic['start_month'])
        sday=int(data_dic['start_date'])
    except IOError:
        print("Please check the file or input as we have Wrong Data")
    #####Setting some Counters######
    num = NO_YEAR_SIM
    newyear, emonth, eday = _add_years(start_year, smonth, sday, num)
    year = start_year   #Setting a variaable to start of the year
    #setting Total recieved from file
    TotalRev=start_revenue
    TotalStock=start_stock
    #settiing counter for While Loop
    count =ymd2num(start_year,smonth,sday)
    while count <= (ymd2num(newyear, emonth, eday)):
        if year == start_year:  #if the year is same as start year
            monthcount = smonth
            #day_range = sday
        elif year==start_year+num:  # if the year is last year of Simulation
            monthcount=1
            #day_range=1
        else:
            monthcount = 1
            #day_range = 1
        days_list = create_day_list(start_year, smonth, sday, num, year)
        # getting RRP and Q for the current Year based on GFC impact
        FPeak_R, _, _, _ = provide_RRP(year)
        _, FOPeak_R, _, _ = provide_RRP(year)
        _, _, SOPeak_R, _ = provide_RRP(year)
        _, _, _, SPeak_R = provide_RRP(year)

        FPeak_Q, _, _, _ = provide_quantity(year)
        _, FOPeak_Q, _, _ = provide_quantity(year)
        _, _, SOPeak_Q, _ = provide_quantity(year)
        _, _, _, SPeak_Q = provide_quantity(year)

        #setting some more counters
        #start_ord = ymd2num(year, monthcount, day_range)
        DEF_Items = 0  ######to start setting defective items to 0
        for months in days_list:
            for j in range(1,months+1):
                if ymd2num(year,1,1) <= count < ymd2num(year,1,1)+days_before_month(year,month=3):
                    #print(num2ymd(count))
                    #########Fixing up total Rev at the start of month######
                    if j==1:
                        TotalRev=TotalRev-round(DEF_Items*FPeak_R*0.08)
                        DEF_Items=0
                    TotalRev=TotalRev+FPeak_R*FPeak_Q
                    TotalStock=TotalStock-FPeak_Q
                    ##########Calculating Defective Items#########
                    DEF_Items=round((DEF_Items+FPeak_Q)*PER_DEF) ##5% of items are defective that come back
                    if TotalStock <= low_stock:
                        TotalStock = TotalStock + stock_uplift
                    else:
                        TotalStock=TotalStock
                     ############# Impact on the stock of Dective Items##########
                    if j==months:
                        TotalStock=TotalStock-DEF_Items
                        monthcount+=1
                    count+=1
                elif ymd2num(year,7,1) <= count and count <= ymd2num(year,10,31):
                    #print(num2ymd(count))
                    #########Fixing up total Rev at the start of month######
                    if j==1:
                        TotalRev=TotalRev-round(DEF_Items*SOPeak_R*0.08)
                        DEF_Items=0
                    TotalRev = TotalRev + SOPeak_R * SOPeak_Q
                    TotalStock = TotalStock - SOPeak_Q
                    ##########Calculating Defective Items#########
                    DEF_Items=round((DEF_Items+SOPeak_Q)*PER_DEF)##5% of items are defective that come back
                    if TotalStock <= low_stock:
                        TotalStock = TotalStock + stock_uplift
                    else:
                        TotalStock=TotalStock

                    if j == months:
                        TotalStock = TotalStock - DEF_Items
                        monthcount+=1
                    count+=1
                elif count >= ymd2num(year,11,1) and count < ymd2num(year+1,1,1):
                    #print(num2ymd(count))
                    #########Fixing up total Rev at the start of month#
                    if j==1:
                        TotalRev=TotalRev-round(DEF_Items*SPeak_R*0.08)
                        DEF_Items=0
                    TotalRev = TotalRev + SPeak_R * SPeak_Q
                    TotalStock = TotalStock - SPeak_Q
                    ##########Calculating Defective Items#########
                    DEF_Items=round((DEF_Items+SPeak_Q)*PER_DEF)##5% of items are defective that come back
                    if TotalStock <= low_stock:
                        TotalStock = TotalStock + stock_uplift
                    else:
                        TotalStock=TotalStock

                    if j == months:
                        TotalStock = TotalStock - DEF_Items
                        monthcount+=1
                    count+=1
                else:
                    #########Fixing up total Rev at the start of month######
                    #print(num2ymd(count))
                    if j==1:
                        TotalRev=TotalRev-round(DEF_Items*FOPeak_R*0.08)
                        DEF_Items=0
                    TotalRev = TotalRev + FOPeak_R * FOPeak_Q
                    TotalStock = TotalStock - FOPeak_Q
                    ##########Calculating Defective Items#########
                    DEF_Items=round((DEF_Items+FOPeak_Q)*PER_DEF)##5% of items are defective that come back
                    if TotalStock <= low_stock:
                        TotalStock = TotalStock + stock_uplift
                    else:
                        TotalStock=TotalStock
                    if j == months:
                        TotalStock = TotalStock - DEF_Items
                        monthcount+=1
                    count+=1

            if monthcount == 13:
                year += 1
            elif monthcount==13 and year==newyear:
                year +=1

        if count >= (ymd2num(newyear, emonth, eday)):
            end_year = newyear  # for last year
            end_data_dic = {}
            end_data_dic.update({'end_year': end_year})
            end_data_dic.update({'end_stock': round(TotalStock)})
            end_data_dic.update({'end_revenue': round(TotalRev)})
            end_data_dic.update({'end_month':emonth})
            end_data_dic.update({'end_date':eday})
            return end_data_dic
            break

############ Main Progran Readfile, calculate and write data###########


data_dic=read_data()
print(data_dic)
end_of_year_dic = cal_stock_revenue(data_dic)
print(end_of_year_dic)
write_data(end_of_year_dic)




