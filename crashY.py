from pynput import keyboard
import time 

dico={} # global dictionary that holds the ID as an integer and each trial code time as a float

def key_logger_helper(key):
    """ 
        This function runs at every keyboard input, storing it in entries_lists and its time in time_lists.
        :param key: The key typed
        exits when special non-character keys are used without returning values
    """
    try:
        char = key.char
        elapsed = time.perf_counter() - start_time
        
        if (char == "1" or char == "2" or char == "3" or char == "4") and (len(entries_list)==0 or entries_list[-1] != char):#input validation / the next key must be different from the previous
            entries_list.append(char)
            times_list.append(round(elapsed,2))
    except:
        return
        
    return 
            
def code_sorter_helper(number_string): 
    """ 
        This function sorts the code types, and displays the frequency of each code.
        :param number_string: The string of number typed
        prints the frequency of each code
    """
    coded1 = 0
    coded2 = 0
    coded3 = 0
    coded4 = 0
    
    for num in number_string:
        if num == "1":
            coded1 += 1
        elif num == "2":
            coded2 += 1
        elif num == "3":
            coded3 += 1
        elif num == "4":
            coded4 +=1

    print("===FREQUENCY===")
    print(f"The number of valid characters is {(coded1+coded2+coded3+coded4)}.")
            
    print("Number of 1 --->", coded1)
    print("Number of 2 --->", coded2)
    print("Number of 3 --->", coded3)
    print("Number of 4 --->", coded4, "\n")

def time_interval_helper():
    """ 
        This function populates duration_lists, using time_lists, with the the duration of each code
        no parameter
        exit without returning values
    """
    for i in range(len(times_list)):
        if i != len(times_list)-1:
            temp = times_list[i+1]-times_list[i]
            duration_list.append(round(temp,2))

     
def total_time_helper():
    """ 
        This function populates total_duration_lists, using duration_lists, with the total time of each code.
        no parameter
        exit without returning values
    """
    tot1 = 0
    tot2 = 0
    tot3 = 0
    tot4 = 0
    
    for i in range(len(entries_list)):
        if entries_list[i] == "1":
            tot1 += duration_list[i]
        elif entries_list[i] == "2":
            tot2 += duration_list[i]
        elif entries_list[i] == "3":
            tot3 += duration_list[i]
        elif entries_list[i] == "4":
            tot4 += duration_list[i]

    total_duration_list.append(round(tot1,2))
    total_duration_list.append(round(tot2,2))
    total_duration_list.append(round(tot3,2))
    total_duration_list.append(round(tot4,2))
            

def display_entries_helper():
    """ 
        This function displays each code entered besides the time it was entered 
            relative to the beginning of the session, using entries_lists and time_lists.
        no parameter
        prints each code and it time
    """
    print("===ENTRIES TIME===")
    
    for i in range(len(entries_list)-1): # This will display the character and their times next to each other
        print(f"You entered: {entries_list[i]} after {times_list[i]}s")
    

def display_dico_helper(dic0):
    """ 
        This function displays the ID and each trialcode with its value as a table
        :param dic0: The dictionary which content is displayed
        prints a table
    """
    for key in dic0:
        if(key == "ID #"): #Displays the ID in a smaller width for space 
            print(f"{key:<5}", end=" ")
        else:
            print(f"{key:<12}", end=" ")
        
    print() #line break to start the values at the next line
    
    for key in dic0:
        if(key == "ID #"):
            print(f"{dic0[key]:<5}", end=" ")
        else:
            print(f"{dic0[key]:<12}", end=" ")

def displayer():
    """ 
        This function calls all the other displayers to print out the frequency, the entry times, and the current table
        no parameter
        exit without returning values
    """
    
    code_sorter_helper("".join(entries_list))# displays frequencies
    print()
    display_entries_helper()# displays entry times
    print()
    display_dico_helper(dico)#  displays current table
    print()
    


if __name__ == "__main__":
    
    
    ID = int(input("ID number: "))
    trial_num = 1
    dico["ID #"] = ID
    #ID added to the global dictionary
    
    new_code = input("Would you like to start a code (yes/no)? ").lower()
    print()
    while new_code == "yes":
        entries_list = [] # this list will hold the inputted characters
        times_list = [] # this list will hold the time elapsed between the beginning of the session and the end
        duration_list = [] # this list holds the interval of time a code has been kept
        total_duration_list = [] # this list holds the total time of each code
        
        start_time = time.perf_counter()
        print(f"**Session {trial_num} started**")
    
        listener = keyboard.Listener(on_press=key_logger_helper)#This calls the function that tracks the characters
        listener.start()
        input()
        
        end_time = time.perf_counter()
        
        times_list.append(round(end_time - start_time, 2))
        entries_list.append("f")
        time_interval_helper()
        total_time_helper()
        # entries_lists, time_lists, duration_lists, and total_duration_lists are populated
        
        print(f"Total duration of the session: {times_list[-1]}s\n")
        
        t = "Trial"+str(trial_num) # will give the smth like "Trial1" or "Trial2" etc...
        t1 = t+ "Code1"
        t2 = t+ "Code2"
        t3 = t+ "Code3"
        t4 = t+ "Code4"
        
        dico[t1] = total_duration_list[0]
        dico[t2] = total_duration_list[1]
        dico[t3] = total_duration_list[2] 
        dico[t4] = total_duration_list[3] 
        
        trial_num +=1
        new_code = input("Type 'yes' to continue coding or 'display' to display the current trial's stats: ").lower()
        print()
        if new_code == "display":
            displayer()   
            new_code = input("\nType 'yes' to continue coding: ").lower()
            print()
            
            
    print("**END**\n")

    display_dico_helper(dico)