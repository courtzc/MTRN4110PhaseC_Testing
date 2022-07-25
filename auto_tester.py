import os
import numpy as np

# -----------------------------------------------------------------------------

### CHANGE THESE INPUTS ###

# what is the path to your test folder?
path_test = 'C:\\Users\\Court\\OneDrive\\Documents\\AAUNSW\\2022 T2\\MTRN4110\\MTRN4110PhaseC\\testing'

# what is the path to your project folder?
path_project = 'C:\\Users\\Court\\OneDrive\\Documents\\AAUNSW\\2022 T2\\MTRN4110\\MTRN4110PhaseC\\programs'

# how many worlds are you testing?
x = 1

# -----------------------------------------------------------------------------




### CODE ###
t = x + 1

# for each world
for j in range(1,t):
    
    h = str(j).zfill(3)
    
    files = [i for i in os.listdir(path_test) if os.path_test.isfile(os.path_test.join(path_test,i)) and i.startswith(h)]

    num_tests_for_maze = np.floor((len(files) - 1) / 3).astype(int)

    Map_Expected = files[0]

    # for each test set
    k = 1
    while k < len(files):
        # take the three files
        bug_photo = files[k]
        maze_photo = files[k + 1]
        robot_photo = files[k + 2]
        
        # feed them into your program as inputs
        
        # compare output to the output text file
        
        # if identical, yay!
        
        # if not identical, show error.
        
        k += 1;