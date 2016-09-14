[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

*Question 2 -- Exercise 3.1 : Something like the class size paradox appears if you survey children and ask how many children are
in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample. Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household. Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household. Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.*  

*STEP 1: Import necessary modules*  
import thinkstats2  
import chap01soln  
import thinkplot  

*STEP 2: Get the 'correct' number of kids by respondent from Downey's chap01soln*  
resp = chap01soln.ReadFemResp()  
numkids = resp['numkdhh']  

*STEP 3: Construct the 'correct' PMF, find the mean, and display the PMF*  
pmf_kids = thinkstats2.Pmf(numkids)  
print('mean', pmf_kids.Mean())  

thinkplot.Pmf(pmf_kids, label = 'Actual')  
thinkplot.Show(block = True)  

**The resulting mean returned is 1.0242051550438309. I was also confused about something: I haven't learned iPython yet, and when I first tried the command above it froze my terminal window until I added the 'block = True' to thinkplot.Show. I googled around to come up with this solution, but I don't really understand why it works.**    

*STEP 4: Reproduce Downey's BiasPmf function.  Again sorry about lack of indenting.*  

def BiasPmf(pmf, label=''):  
    """Returns the Pmf with oversampling proportional to value.  

    If pmf is the distribution of true values, the result is the  
    distribution that would be seen if values are oversampled in  
    proportion to their values; for example, if you ask students  
    how big their classes are, large classes are oversampled in  
    proportion to their size.  

    Args:  
      pmf: Pmf object.  
      label: string label for the new Pmf.  

     Returns:  
       Pmf object  
    """  
    new_pmf = pmf.Copy(label=label)  

    for x, p in pmf.Items():  
        new_pmf.Mult(x, x)  

    new_pmf.Normalize()  
    return new_pmf  

*STEP 5: Call BiasPmf on pmf_kids and find the mean*  
biasedpmf_kids = BiasPmf(pmf_kids, label = 'Reported by kids')  
print('mean', biasedpmf_kids.Mean())  

**The resulting mean returned is 2.4036791006642821. So if we were to make inferences about family size from asking kids, we would over-state the true number of kids per household by almost 1.4**  

*STEP 6: Display the two PMFs together*  
thinkplot.PrePlot(2)  
thinkplot.Pmfs([pmf_kids, biasedpmf_kids])  
thinkplot.Show(block = True, xlabel = 'Number of Children in Household', ylabel = 'PMF')  
