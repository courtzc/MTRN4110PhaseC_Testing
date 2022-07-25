# MTRN4110PhaseC_Testing
Testing and test photos for MTRN4110 Phase C


# Adding the contents of this test repo to your project

To update your current project git repo with these latest files, add this repo as an upstream friend. In your terminal in your project's root directory, run:

`git remote add upstream https://github.com/courtzc/MTRN4110PhaseC_Testing.git`

Then, to pull latest changes from that upstream into your project, go to your **project's** root directory and run:

`git pull upstream main --allow-unrelated-histories`


# Using the autotester

Export your ipynb notebook into a python script (it's an option in vscode command palette). Copy the content into the file `project_function_code.py`, which looks like this:


```
def my_project(maze_pic, bug_pic, robot_pic):


  < all your code >
  
  
  return <output text in the form of 37x11 array of chars>
```

Change your paths for the three pictures to be the three input variables.

*note: we maybe should return the image as well? that way it can show it if the output isn't correct.*

## Keeping it valid
The project_function_code.py function should return a str which is the maze. I did it like this (for each row that I put together)

```
actual_output = ""
# for each row (obvs str('') content will vary)
  actual_output += str(' --- --- --- --- --- --- --- --- --- \n')
return actual_output
```

## Recommendations
Comment out most of your print statements if you're doing lots of tests at once, it gets messy

Comment out your `plt.show()` statements if you're doing lots - they pause the execution until you close them

# Adding to the test repo

All changes to the test things (pictures, the autotester, expected output maps) **should be committed and pushed to this test repo** (not your project repo, even though it will have the files). This is because the testing repo isn't watching your project, and won't update automatically.

It's just your normal clone procedure to have this repo on your computer and contribute directly to it.

# Syntax for contributing to the test repo

## World
These go in the worlds/ folder.

Let's put the number of the world (001 - 999) somewhere in the world name so we can keep track and make more photos later if we need to. 


## Outputs

Put these bad boys in the tests/ directory.

### Output text file (the known map):

Just `001.txt` is great (ensures it's first in the list of files returned by the 001 search)

## Photo sets

These also go in the tests/ directory.

Each set of photos of the world (bug, maze, robot) have this syntax:

### bug:
world(001-999)_photoset(a-z)_bug

i.e. for world one, 2nd photoset, it would be

`001_b_bug`

### maze:
maze(001-999)_photo(a-z)_maze_inversion('inv' or 'nor')_robotpos(rowcolumn)_robotheading(N S E or W)_realtargetpos(rowcolumn)_faketargetpos(rowcolumn)

i.e. for world one, 2nd photoset, which has the maze inverted, it would be

`001_b_maze_inv_00_S_24_16`

(not sure if we need all this info, but it might be useful for say giving an output like "you said it was north, but it's actually south". Also, the 'inv' or 'nor' need to be 3 characters each so I can continue to hack at the substrings)

### robot:
world(001-999)_photoset(a-z)_robot

i.e. for world one, 2nd photoset, it would be

`001_b_robot`


Let's get testin!
