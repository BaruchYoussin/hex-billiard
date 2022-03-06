# hex-billiard
 Code for the paper *Numerical non-integrability of Hexagonal string billiard* 

This repository contains the code that calculates the orbits and creats the plots for the paper 
*Numerical non-integrability of Hexagonal string billiard* by Misha Byaly and Baruch Youssin.

The orbits and figures are not included as they take too much space.

First, orbits need to be created; to this end, run the scripts `orbits...py` and `periodic...py`.  The scripts `orbits...py` take hours to run.  
The scripts `orbit...val.py` create the orbits used for validation of the precision (the *control calculations* mentioned in the paper).
If you are interested in the figures only, run only `orbits_30.py` and `orbits_other.py`.

Figures are created by the scripts `plot...py` and the control calculations are performed by `validation...py`.

Enjoy!
