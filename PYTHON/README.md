> # AIML

# Instruction to use this model:

we used cvzone ,mediapipe,opencv,pyautogui for the projects.

So first of all install these things in your machine.




How to use ipynb :
 1. Open a Python file (e.g., my_script.py).
   2. Initialize the Jupyter kernel by pressing <space>mi. You should see a confirmation that the 
      kernel has started.
   3. Define cells in your Python script using #%% as a separator:

    1     #%%
    2     print("Hello from cell 1")
    3 
    4     #%%
    5     import matplotlib.pyplot as plt
    6     import numpy as np
    7 
    8     x = np.linspace(0, 2 * np.pi, 400)
    9     y = np.sin(x**2)
   10 
   11     plt.plot(x, y)
   12     plt.title("A simple plot")
   13     plt.show()

   4. Execute code:
       * Move your cursor into a cell and press <localleader>x to execute it. The output will 
         appear in a split window.
       * To execute the entire script, press <localleader>X.

   5. Manage cells:
       * <localleader>a: Create a new cell above the current one.
       * <localleader>b: Create a new cell below the current one.
       * dd (in normal mode on the #%% line): Delete a cell.

   6. View images: If your code generates plots (like the example above), they will be displayed 
      automatically in a separate window.

   7. Shut down the kernel: Use the :MoltenDeinit command.

  For more advanced usage, you can refer to the molten-nvim documentation.
