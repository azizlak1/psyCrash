from pynput import keyboard
import time 
import pandas as pd

dico={} # global dictionary that holds the ID as an integer and each trial code time as a float
values =[]

def key_logger_helper(key):
    """ 
        This function runs at every keyboard input, storing it in list0 and its time in list1.
        :param key: The key typed
        exits when special non-character keys are used without returning values
    """
    try:
        char = key.char
        elapsed = time.perf_counter() - start_time
        
        if (char == "1" or char == "2" or char == "3" or char == "4" or char == "d" or char == "D") and (len(list0)==0 or list0[-1] != char):#input validation / the next key must be different from the previous
            list0.append(char)
            list1.append(round(elapsed,2))
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
            
    print("Number of 1 (Looks the reward) --->", coded1)
    print("Number of 2 (Looks at self, bell, table) --->", coded2)
    print("Number of 3 (Looks at experimenter (face)) --->", coded3)
    print("Number of 4 (Looks away)--->", coded4, "\n")

def time_interval_helper():
    """ 
        This function populates list2, using list1, with the the duration of each code
        no parameter
        exit without returning values
    """
    for i in range(len(list1)):
        if i != len(list1)-1:
            temp = list1[i+1]-list1[i]
            list2.append(round(temp,2))

     
def total_time_helper():
    """ 
        This function populates list3, using list2, with the total time of each code.
        no parameter
        exit without returning values
    """
    tot1 = 0
    tot2 = 0
    tot3 = 0
    tot4 = 0
    
    for i in range(len(list0)):
        if list0[i] == "1":
            tot1 += list2[i]
        elif list0[i] == "2":
            tot2 += list2[i]
        elif list0[i] == "3":
            tot3 += list2[i]
        elif list0[i] == "4":
            tot4 += list2[i]

    list3.append(round(tot1,2))
    list3.append(round(tot2,2))
    list3.append(round(tot3,2))
    list3.append(round(tot4,2))
            

def display_entries_helper():
    """ 
        This function displays each code entered besides the time it was entered 
            relative to the beginning of the session, using entries_lists and time_lists.
        no parameter
        prints each code and it time
    """
    print("===ENTRIES TIME===")
    
    for i in range(len(list0)-1): # This will display the character and their times next to each other
        print(f"You entered: {list0[i]} after {list1[i]}s")
    

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
            print(f"{key:<7}", end=" ")
        
    print() #line break to start the values at the next line
    
    for key in dic0:
        if(key == "ID #"):
            print(f"{dic0[key]:<5}", end=" ")
        else:
            print(f"{dic0[key]:<7}", end=" ")

def displayer():
    """ 
        This function calls all the other displayers to print out the frequency, the entry times, and the current table
        no parameter
        exit without returning values
    """ 
    code_sorter_helper("".join(list0))# displays frequencies
    print()
    display_entries_helper()# displays entry times
    print()
    display_dico_helper(dico)#  displays current table
    print()
    
def value_join_helper():
    """ 
        This function formats the values of the dictionary so they fit the .csv file format
        no parameter
        returns the formatted string
    """
    for val in dico.values():
        values.append(str(val))
    
    return ",".join(values)
    


if __name__ == "__main__":
    trial_num = 1
    switch = True
    comm = ""
    first_row = "ID #,Tr1Cd1,Tr1Cd2,Tr1Cd3,Tr1Cd4,Tr2Cd1,Tr2Cd2,Tr2Cd3,Tr2Cd4,Tr3Cd1,Tr3Cd2,Tr3Cd3,Tr3Cd4,Tr4Cd1,Tr4Cd2,Tr4Cd3,Tr4Cd4,Comment"
    prompt = "\n1.Start a new trial\n2.Comment on the current code\n3.Display the current trial's stats and the current table of data\n4.Delete the previous trial\n5.Save the data in an excel sheet\n6.Clear the saved data\n7.Stop\n"
    
    ID = int(input("ID number: "))
    dico["ID #"] = ID
    #ID added to the global dictionary
    
    choice = int(input(prompt))

    while choice!=7:
        if choice == 1:
            list0 = [] # this list will hold the inputted characters
            list1 = [] # this list will hold the time elapsed between the beginning of the session and the end
            list2 = [] # this list holds the interval of time a code has been kept
            list3 = [] # this list holds the total time of each code
            
            start_time = time.perf_counter()
            print(f"**Session {trial_num} started**")
        
            listener = keyboard.Listener(on_press=key_logger_helper)#This calls the function that tracks the entries
            listener.start()
            input()
            
            end_time = time.perf_counter()
            
            list1.append(round(end_time - start_time, 2))
            list0.append("f")
            time_interval_helper()
            total_time_helper()
            # list0, list1, list2, and list3 are populated
            
            print(f"Total duration of the session: {list1[-1]}s")
            
            t = "Tr"+str(trial_num)
            t1 = t+ "Cd1"
            t2 = t+ "Cd2"
            t3 = t+ "Cd3"
            t4 = t+ "Cd4"
            
            dico[t1] = list3[0]
            dico[t2] = list3[1]
            dico[t3] = list3[2] 
            dico[t4] = list3[3] 
            
            trial_num +=1
            choice = int(input(prompt))
            
        
        elif choice == 2:
            if not comm:
                comm = input("Insert your comment below.\n")
            else:
                c = input("Insert your comment below.\n")
                comm += " - " + c
                
            print("Comment added")
            
            choice = int(input(prompt))
            
            
        elif choice == 3:
            displayer()   
            choice = int(input(prompt))
            
            
        elif choice == 4:
            trial_num -=1
            
            tn = "Tr"+ str(trial_num)
            for key in dico: #Clears the deleted trial's codes 
                if tn in key:
                    dico[key] = 0
            
            print("**Trial deleted**")
            choice = int(input(prompt))
            
            
        elif choice == 5:
            #Add the current data to the .csv file
            try:
                f = open("data-temp.csv", "x")
            except FileExistsError: # if file already exists,
                with open("data-temp.csv", "a") as f:
                    f.write("\n")
                    f.write(value_join_helper())#just append the new data
            else:
                with open("data-temp.csv", "a") as f:#if file doesn't exist,
                    f.write(first_row)#create the first row,
                    f.write("\n")
                    f.write(value_join_helper())#then append the data
            
            switch=False #prevents from populating the excel file twice
            
            #Populate the excel file
            try:
                f=open("table-temp.xlsx", "x")
            except FileExistsError:
                df = pd.read_csv("data-temp.csv")
                df.to_excel("table-temp.xlsx", sheet_name='Sheet1', index=False)
            else:
                df = pd.read_csv("data-temp.csv")
                df.to_excel("table-temp.xlsx", sheet_name='Sheet1', index=False)
            
            print("The data have been saved in the excel sheet 'table-temp.xlsx'")
            choice = int(input(prompt))
            
            
        elif choice == 6:
            try:
                f = open("data-temp.csv", "x")
            except FileExistsError: # if file already exists,
                with open("data-temp.csv", "w") as f:
                    f.write(first_row)
            else:
                with open("data-temp.csv", "w") as f:
                    f.write(first_row)
                    
                print("You have no data") 
            
            switch = False
            choice = int(input(prompt))
            
        else:
            print("Please delect a number between 1 and 7")
            choice = int(input(prompt))
                    
    print("**END**\n")
    
    if comm: # Adds the comment at the end of the dictionary
        dico["Comment"] = comm
    
    if switch: # If the data were never saved during the run-time, save it now in the .csv file only
        try:
            f = open("data-temp.csv", "x")
        except FileExistsError: # if file already exists,
            with open("data-temp.csv", "a") as f:
                f.write("\n")
                f.write(value_join_helper())#just append the new data
        else:
            with open("data-temp.csv", "a") as f:#if file doesn't exist,
                f.write(first_row)#create the first row,
                f.write("\n")
                f.write(value_join_helper())#then append the data
        
        print("Data saved in 'data-temp.csv'\n")

    display_dico_helper(dico)