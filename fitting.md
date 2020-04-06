---
description: >-
  After picking an mpt file and pressing "Load MPT," we can go ahead and start
  the fitting process.
---

# Fitting

Selecting a file will show us a dataframe of the mpt file as well as a graph of the Nvyquist Impedance Graph.

![I selected DE\_49\_8\_30.mpt](.gitbook/assets/image%20%2811%29.png)

## Masking Choices

There are 4 choices for the mask limits. The first three are pre-built masking functions where one of them worked for all of the testing files. There is also a no mask choice, where you can just fit the entire function.

For this example, I'll pick masker 3 and fit the function by pressing the FIT button. It may take a while depending on the inputs and masking choice. A black screen running python will pop up while running and disappear when finished. You can exit out this box if you deem it's taking too long or just don't like the choice.

There will also be a notification box telling you how many values were fitted and a display graph with a new, red set of fitted dots will present itself.

![We can see the graph is updated, with a fitted set of data below the data frame](.gitbook/assets/image%20%286%29.png)

The fitted coefficients are updated underneath, and if you notice, the blue box has been updated to say "FITTED" next to the file you just fit.

## Window Masking

Lets say that we don't like any of the masks are satisfactory to us, or they're just taking too long. We can custom create a mask, either by scrolling up and down, or just creating your own window by dragging the mouse across the desired area.

![Create a window, and it&apos;ll update the screen](.gitbook/assets/image%20%284%29.png)

![Updated window, and now we can press Window Masker, and then FIT](.gitbook/assets/image%20%283%29.png)

Pressing Window Masker button and then FIT will automatically update the chart to fit within these dimensions only. You can also scroll down to get the original dimensions of the graph.

![](.gitbook/assets/image%20%281%29.png)

![As we can see, the graph only fit the selected area.](.gitbook/assets/image%20%2814%29.png)

