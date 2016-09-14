[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

*Question 4 -- Exercise 5.1: In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters mean = 178 cm and std dev = 7.7 cm for men, and mean = 163 cm and std dev = 7.3 cm for women. In order to join Blue Man Group, you have to be male between 5'10" and 6'1". What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.*  

*STEP 1: Import necessary modules*  
from scipy.stats import norm

*STEP 2: Transform minimum & maximum heights to centimeters*  
minheight = (5*12 + 10)  
maxheight = (6*12 + 1)  
minheight = minheight*2.54  
maxheight = maxheight*2.54    

*STEP 3: Set mean and variance*  
mean = 178  
variance = 7.7**2  

*STEP 4: Get the % of the normal distribution with mean 178 and std dev 7.7 for minheight and maxheight*  
pct_below_min = norm.cdf(minheight, mean, variance)  
pct_below_max = norm.cdf(maxheight, mean, variance)  

*STEP 5: Get % of the male population within this range*  
print pct_below_max - pct_below_min

**The result returned is 0.0511423714411, or just over 5% of the U.S. male population.**
