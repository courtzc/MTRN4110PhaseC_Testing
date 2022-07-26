from ntpath import join
import os
import numpy as np
import os.path
from project_function_code import project_function

# ---
# note: use the command palette to set the interpreter as python 3.7.10
# ---

# -----------------------------------------------------------------------------

### CHANGE THESE INPUTS ###

# what is the path to your tests folder?
path = 'C:\\Users\\leap.staff\\Desktop\\Other\\Term 2 2022\\4110_ROBOTIC_DESIGN\\z1234567_MTRN4110_PhaseC\\tests'

# how many worlds are you testing?
x = 2

# -----------------------------------------------------------------------------

# Summary code
total_tests = 0
passed = 0
failed = 0


### CODE ###
t = x + 1

# for each world
for j in range(1,t):

    h = str(j).zfill(3)
    print("=================================")
    print("Beginning tests for world", h, ".")
    
    files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and i.startswith(h)]

    # read in expected output .txt
    map_file_temp = ["tests/", files[0]]
    map_file = ''.join(map_file_temp)
    
    map_ex = ""
    with open(map_file, 'r') as f:
        line = f.readline()
        while line:
            map_ex+=str(line)
            line = f.readline()

    # for each test set
    k = 1
    while k < len(files):
     
        # take the three files
        bugfile =  ["tests/", files[k]]
        mazefile =  ["tests/", files[k+1]]
        robotfile =  ["tests/", files[k+2]]
        bug_photo = ''.join(bugfile)
        maze_photo = ''.join(mazefile)
        robot_photo = ''.join(robotfile)
        
        set_letter = bug_photo[9:12]
        print("-----------------------")
        print("Beginning test set", set_letter)
        
        # feed them into the project as inputs
        map_generated = project_function(bug_photo, maze_photo, robot_photo)
        
        # compare output to the output text file
        # if identical, yay!
        if (map_generated == map_ex):
            print("success! in set ", set_letter)
            total_tests += 1
            passed += 1
            
        # if not identical, sad.
        else:
            print("failure in set ", set_letter)
            print("you generated: ")
            print(map_generated)
            print("but the expected output was: ")
            print(map_ex)
            total_tests += 1
            failed += 1
        
        print("End of set", set_letter, "tests.")
        print("---------------------")
        
        k += 3;
        
    print("End of world", h, "tests.")
    print("==========================")


print("\n\n================SUMMMARY=================")
#print("Conducted " + str(total_tests) + " total tests")
print("Passed: " + str(passed) + " / " + str(total_tests))
#print("Failed: " + str(failed) + " / " + str(total_tests))
print("================SUMMMARY=================")

