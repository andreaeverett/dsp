[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

*Question 7 -- Exercise 7.1 : Using data from the NSFG, make a scatter plot of birth weight versus mother's age. Plot percentiles of birth weight versus mother's age. Compute Pearson's and Spearman's correlations. How would you characterize the relationship between these variables?*  

*STEP 1: Import necessary modules*  

import numpy as np  
import sys  
import nsfg  
import thinkstats2  
import thinkplot  
import first  

*STEP 2: Generate dataframes for live births, first births, and others.  Will be using data on live births here.*  

live, firsts, others = first.MakeFrames()  
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])  

*STEP 3: Plot birth weight vs. mother's age*  
thinkplot.Scatter(live.agepreg, live.totalwgt_lb)  
thinkplot.Show(xlabel='Mother Age', ylabel='Birth Weight (lbs)', axis=[10, 45, 0, 15])  

*STEP 4: Plot percentiles of birth weight vs. mother's age*  
bins = np.arange(10, 45, 5)  
indices = np.digitize(live.agepreg, bins)  
groups = live.groupby(indices)  

ages = [group.agepreg.mean() for i, group in groups]  
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]  

thinkplot.PrePlot(3)  
for percent in [75, 50, 25]:  
    birth_weights = [cdf.Percentile(percent) for cdf in cdfs]  
    label = '%dth' % percent  
    thinkplot.Plot(ages, birth_weights, label=label)  

thinkplot.Show(xlabel='Mother Age', ylabel='Birth Weight (lbs)', axis=[10, 45, 0, 15])  

*STEP 5: Compute Pearson's and Spearman's correlations*  
print ("Pearson's Correlation", thinkstats2.Corr(live.agepreg, live.totalwgt_lb))  
print ("Spearman's Correlation", thinkstats2.SpearmanCorr(live.agepreg, live.totalwgt_lb))  

*STEP 6: Describe the relationship between these variables*  

*There doesn't appear to be any meaningful relationship between mother's age and birthweight. In neither the scatterplot nor the binned percentile plot is there a visible trend. What is more, both correlation measures are close to 0: Pearson's Correlation = 0.0688339703541 and Spearman's Correlation = 0.0946100410966. One thing I found interesting was that in the scatterplot you can clearly see horizonal lines at specific #s of pounds that indicate people were rounding when they reported their babies' birthweights.*
