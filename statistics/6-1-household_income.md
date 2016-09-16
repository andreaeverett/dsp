[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

*Exercise 6.1 -- Compute the median, mean, skewness and Pearson’s skewness of the resulting sample.   
What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?*  

I used Downey's hinc2.py file as directed. Initially I made the mistake of trying to work with the logged sample.  Within the 'main' function I added the following:  

    print('mean', log_sample.mean())  
    print('median', thinkstats2.Median(log_sample))  
    print('skewness', thinkstats2.Skewness(log_sample))  
    print('pearson skewness', thinkstats2.PearsonMedianSkewness(log_sample))  
    print('percent below mean', log_cdf.PercentileRank(log_sample.mean()))  

I ran the file with several different values of log_upper.  The results for 6.0 (top income = $1 million) and 7.0 (top income = $10 million) were as follows:  

*Results when upper_bound = 6.0*  
mean 4.65758573589  
median 4.70949429822  
skewness -0.641354366566  
pearson skewness -0.337920251338  
percent below mean 45.0603472211  

*Results when upper_bound = 7.0*  
mean 4.66947144364  
median 4.70949429822  
skewness 0.0805185357124  
pearson skewness -0.241446679439  
percent below mean 46.1741985007   

These results were confusing since I expected the data to be skewed right. I then looked at Downey's solution and realized I should have unlogged the sample first (duh). Once I did (at that point I just used his code), I got the same results as he did. Close to an additional 20% of the population are below the mean when using the larger upper bound for income.  

*Results when upper_bound = 6.0*  
mean 74278.7075312  
std 93946.9299635  
median 51226.4544789  
skewness 4.94992024443  
pearson skewness 0.736125801914  
cdf[mean] 0.660005879567  

*Results when upper_bound = 7.0*  
mean 124267.397222  
std 559608.501374  
median 51226.4544789  
skewness 11.6036902675  
pearson skewness 0.391564509277  
cdf[mean] 0.856563066521  
