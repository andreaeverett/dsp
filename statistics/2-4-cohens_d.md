[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

*Question 1 -- Exercise 2.4: Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?*  

*Import necessary modules*  

from __future__ import print_function  
import numpy as np  
import sys  
import nsfg  
import thinkstats2  
import first  

*Generate dataframes for live births, first births, and others. Then calculate Cohen's d for firsts vs. others.*  
def main(script):  
    live, firsts, others = first.MakeFrames()   
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)   
    print('Cohen d', d)  

if __name__ == '__main__':  
    main(*sys.argv)  


*Running this, Python returns -0.0886729270726 as Cohen's d. This is about 3 times bigger in absolute value than the .029 figure returned for pregnancy length as described in the book. Another key difference is the opposite sign, which indicates that first babies are on average smaller than later babies, even though they arrive a bit later.*
