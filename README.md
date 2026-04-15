README

    CrashY.py is a Python key-logger program designed to help the entry of data for the Maternal Postpartum Depression Laboratory at UMBC. 

    The program runs by successive "Sessions" storing keyboard inputs and their time, then outputting them as a 2-rows table. The number of sessions is typically 4, but this number does not limit the program, more or less sessions can be coded as long as the user does not exit the program.

    Important Note: Once typed, entries can not be deleted. For this reason, invalid codes (other than 1, 2, or 3) are not recorded nor their time. However, valid codes (1, 2, or 3), even if misplaced, can not be removed afterwards. For example, entering a 4 instead of a 3 will not impact the data collection, as 4 is an invalid entry, so the program will ignore it; but entering a 2 instead of a 3 WILL store the 2 and its time, and take it into acoount for the computations, because 2 is valid. The only way to remove a misplaced valid entry would be to restart the coding. So, be careful!


INSTALL

    The library pynput is used for this project to track the keyboard. It should be installed using, in a terminal, the command:
    pip install pynput 
    
    MacOS users may also need to give the permission to their terminal and IDEs to track the computer's keyboard. For this, they can follow the following steps:
    Settings => Privacy & Security => Accessibilty, then use the + symbol to add the IDE and terminal to the list of apps.
    Then, they should restart both IDE and terminal so the permissions are updated.


