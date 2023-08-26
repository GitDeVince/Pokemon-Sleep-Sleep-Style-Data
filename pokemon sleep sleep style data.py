import numpy as np
import matplotlib.pyplot as plt

#Pokemon Sleep data of Sleep Styles, which pokemon in each stage is not included here
#A pokemon species does not equate one sleep style here since each pokemon species has 3 to 4 sleep styles acrossed different areas and ranks
#data from https://www.serebii.net/pokemonsleep/snorlaxratings.shtml




#all available ranks in the game. From lowest to highest rank: Basic 1 to Ultra 5 then Master 1 to Master 20
basic_to_ultra = ['Basic 1', 'Basic 2', 'Basic 3', 'Basic 4', 'Basic 5', 'Great 1', 'Great 2', 'Great 3', 'Great 4','Great 5', 'Ultra 1', 'Ultra 2', 'Ultra 3', 'Ultra 4', 'Ultra 5']
master_rank = ['Master 1', 'Master 2', 'Master 3', 'Master 4', 'Master 5', 'Master 6', 'Master 7', 'Master 8', 'Master 9', 'Master 10', 'Master 11', 'Master 12', 'Master 13', 'Master 14', 'Master 15', 'Master 16', 'Master 17', 'Master 18', 'Master 19', 'Master 20']

#total amount of sleep style available per rank. arrays are based on basic_to_ultra and master_rank
GI_findablestyle = [20,33,36,40,60,91,111,119,130,134,148,159,169,179,185]
CB_findablestyle = [21,31,38,42,44,67,69,82,94,101,112,116,120,125,125]
TH_findablestyle = [30,35,39,44,48,68,82,90,95,104,112,113,117,118,124]
ST_findablestyle = [30,35,39,44,48,68,82,90,95,104,112,113,117,118,124]

GI_findablestyle_masters = [191,198,199,201,207,210,215,216,221,227,230,231,232,232,233,234,235,235,235,235]
CB_findablestyle_masters = [131,137,139,143,143,147,151,151,152,152,152,156,156,156,156,156,156,156,156,156]
TH_findablestyle_masters = [131,132,134,139,143,143,144,144,147,151,151,151,151,151,151,152,152,152,152,152]
ST_findablestyle_masters = [129,131,132,134,139,143,143,144,144,147,151,151,151,151,151,152,152,152,152,152]

#frequency of additional sleep style of each rank from Basic 1 to Ultra 5 then Master 1 to Master 20 
GI_findablestyle_freq = [20,13,3,4,20,31,20,8,11,4,14,11,10,10,6]
CB_findablestyle_freq = [21,10,7,4,2,23,2,13,12,7,11,4,4,5,0]
TH_findablestyle_freq = [30,5,4,5,4,20,14,8,5,9,8,1,5,6,5]
ST_findablestyle_freq = [30,5,4,5,4,20,14,8,5,9,8,1,4,1,6]

GI_master_findablestyle_freq = [6,7,1,2,6,3,5,1,5,6,3,1,1,0,1,1,1,0,0,0]
CB_master_findablestyle_freq = [6,6,2,4,0,4,4,0,1,0,0,4,0,0,0,0,0,0,0,0]
TH_master_findablestyle_freq = [2,1,2,5,4,0,1,0,3,4,0,0,0,0,0,1,0,0,0,0]
ST_master_findablestyle_freq = [5,2,1,2,5,4,0,1,0,3,4,0,0,0,0,1,0,0,0,0]


def line_basic_ultra():

    plt.style.use('seaborn')

    fig, ax = plt.subplots()

    ax.plot(basic_to_ultra, GI_findablestyle, linewidth = 3, c ='green', label = "Greengrass Isle" )
    ax.plot(basic_to_ultra, CB_findablestyle, linewidth = 3, c ='blue', label = "Cyan Beach")
    ax.plot(basic_to_ultra, TH_findablestyle, linewidth = 3, c ='brown', label = "Taupe Hollow")
    ax.plot(basic_to_ultra, ST_findablestyle, linewidth = 3, c ='purple', label = "Snowdrop Tundra")

    ax.set_title("Basic 1 to Ultra 5 Findable Sleep Style ", fontsize = 24)
    ax.set_xlabel("Ranks", fontsize = 14)
    ax.set_ylabel("Number of Sleep Styles", fontsize = 14)
    leg = ax.legend(loc ="upper left")
    plt.show()

def line_masters():

    plt.style.use('seaborn')

    fig, ax = plt.subplots()
   
    ax.plot(master_rank, GI_findablestyle_masters, linewidth = 3, c ='green', label = "Greengrass Isle" )
    ax.plot(master_rank, CB_findablestyle_masters, linewidth = 3, c ='blue', label = "Cyan Beach")
    ax.plot(master_rank, TH_findablestyle_masters, linewidth = 3, c ='brown', label = "Taupe Hollow")
    ax.plot(master_rank, ST_findablestyle_masters, linewidth = 3, c ='purple', label = "Snowdrop Tundra")

    ax.set_title("Master 1 to Master 20 Findable Sleep Style", fontsize = 24)
    ax.set_xlabel("Ranks", fontsize = 14)
    ax.set_ylabel("Number of Sleep Styles", fontsize = 14)
    leg = ax.legend(loc ="upper left")
    plt.show()

def bar_GI_freq():

    plt.style.use('seaborn')

    plt.title("Basic 1 to Ultra 5 Sleep Style Frequency in Greengrass Isle", fontsize = 24)
    plt.xlabel("Ranks", fontsize = 14)
    plt.ylabel("Frequency of Sleep Styles", fontsize = 14)
    plt.bar(basic_to_ultra, GI_findablestyle_freq, color = 'green')
    plt.show()

def bar_CB_freq():

    plt.style.use('seaborn')

    plt.title("Basic 1 to Ultra 5 Sleep Style Frequency in Cyan Beach", fontsize = 24)
    plt.xlabel("Ranks", fontsize = 14)
    plt.ylabel("Frequency of Sleep Styles", fontsize = 14)
    plt.bar(basic_to_ultra, CB_findablestyle_freq, color = 'blue')
    plt.show()

def bar_TH_freq():

    plt.style.use('seaborn')

    plt.title("Basic 1 to Ultra 5 Sleep Style Frequency in Taupe Hollow", fontsize = 24)
    plt.xlabel("Ranks", fontsize = 14)
    plt.ylabel("Frequency of Sleep Styles", fontsize = 14)
    plt.bar(basic_to_ultra, TH_findablestyle_freq, color = 'brown')
    plt.show()

def bar_ST_freq():

    plt.style.use('seaborn')

    plt.title("Basic 1 to Ultra 5 Sleep Style Frequency in Snowdrop Tundra", fontsize = 24)
    plt.xlabel("Ranks", fontsize = 14)
    plt.ylabel("Frequency of Sleep Styles", fontsize = 14)
    plt.bar(basic_to_ultra, ST_findablestyle_freq, color = 'purple')
    plt.show()

def bar_GI_master_freq():
    plt.style.use('seaborn')

    plt.title("Master 1 to Master 20 Sleep Style Frequency in Greengrass Isle", fontsize = 24)
    plt.xlabel("Ranks", fontsize = 14)
    plt.ylabel("Frequency of Sleep Styles", fontsize = 14)
    plt.bar(master_rank, GI_master_findablestyle_freq, color = 'green')
    plt.show()

def bar_CB_master_freq():
    plt.style.use('seaborn')

    plt.title("Master 1 to Master 20 Sleep Style Frequency in Cyan Beach", fontsize = 24)
    plt.xlabel("Ranks", fontsize = 14)
    plt.ylabel("Frequency of Sleep Styles", fontsize = 14)
    plt.bar(master_rank, CB_master_findablestyle_freq, color = 'blue')
    plt.show()

def bar_TH_master_freq():
    plt.style.use('seaborn')

    plt.title("Master 1 to Master 20 Sleep Style Frequency in Taupe Hollow", fontsize = 24)
    plt.xlabel("Ranks", fontsize = 14)
    plt.ylabel("Frequency of Sleep Styles", fontsize = 14)
    plt.bar(master_rank, TH_master_findablestyle_freq, color = 'brown')
    plt.show()

def bar_ST_master_freq():
    plt.style.use('seaborn')

    plt.title("Master 1 to Master 20 Sleep Style Frequency in Snowdrop Tundra", fontsize = 24)
    plt.xlabel("Ranks", fontsize = 14)
    plt.ylabel("Frequency of Sleep Styles", fontsize = 14)
    plt.bar(master_rank, ST_master_findablestyle_freq, color = 'purple')
    plt.show()

#while loop to cycle the different possible graphs here
while True:
    decision = input("Please choose the letter before the option: '(a) Line Graph Basic 1 to Ultra 5', '(b) Line Master 1 to Master 20', (c) Basic 1 to Ultra 5 Frequency of Sleep Style, (d) Master 1 to Master 20 Frequency of Sleep Style  or (e) Exit' ")
    decision = decision.capitalize()

    if decision == "A":
       line_basic_ultra()

    elif decision == "B":
        line_masters()

    elif decision == "C":
        decision2 = input("Which stage: (a) Greengrass Isle, (b) Cyan Beach, (c) Taupe Hollow, or (d) Snowdrop Tundra, (e) Back ")
        decision2 = decision2.capitalize()

        while True:
            if decision2 == 'A':
                bar_GI_freq()
                break

            elif decision2 == 'B':
                bar_CB_freq()
                break    
            
            elif decision2 == 'C':
                bar_TH_freq()
                break

            elif decision2 == 'D':
                bar_ST_freq()
                break

            elif decision2 == 'E':
                break
    
    elif decision =='D':
        decision2 = input("Which stage: (a) Greengrass Isle, (b) Cyan Beach, (c) Taupe Hollow, or (d) Snowdrop Tundra, (e) Back ")
        decision2 = decision2.capitalize()

        while True:
            if decision2 == 'A':
                bar_GI_master_freq()
                break

            elif decision2 == 'B':
                bar_CB_master_freq()
                break    
            
            elif decision2 == 'C':
                bar_TH_master_freq()
                break

            elif decision2 == 'D':
                bar_ST_master_freq()
                break

            elif decision2 == 'E':
                break

    elif decision == "E":
        print("Goodbye")
        break

    else:
        print("Please only choose the given options.")

