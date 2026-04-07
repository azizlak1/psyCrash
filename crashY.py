from pynput import keyboard
import time 

list0 = [] # this list will hold the inputted characters
list1 = [] # this list will hold the time elapsed between the beginning of the session and the end

start_time = time.perf_counter()
print("**Session started**")
    
def key_logger_helper(key): #this function runs at every keyboard input, 
                            # validating and storing it and its time into the two global lists
    
    try:
        char = key.char
        elapsed = time.perf_counter() - start_time
        
        if char == "1" or char == "2" or char == "3":
            list0.append(char)
            list1.append(round(elapsed,2))
    except:
        print("\n**END**")
    
    return 
        
def code_sorter_helper(number_string): #this function gives the frequency of each code
    coded1 = 0
    coded2 = 0
    coded3 = 0
    
    for num in number_string:
        if num == "1":
            coded1 += 1
        elif num == "2":
            coded2 += 1
        elif num == "3":
            coded3 += 1

    print("===FREQUENCY===")
    print(f"The number of valid characters is {(coded1+coded2+coded3)}.")
            
    print("Number of 1 (Looks at the reward) --->", coded1)
    print("Number of 2 (Looks at self, bell, experimenter, table) --->", coded2)
    print("Number of 3 (Looks away or Head turned or body turned) --->", coded3, "\n")
     

if __name__ == "__main__":
    
    listener = keyboard.Listener(on_press=key_logger_helper)#This calls the function that tracks the characters
    listener.start()
    input()
    
    code_sorter_helper("".join(list0))# This calls the function that gives the frequency
    
    print("===ENTRIES TIME===")
    for i in range(len(list0)): # This will display the character and their times next to each other
        print(f"You entered: {list0[i]} after {list1[i]}s")
        
    
    
    
    
    