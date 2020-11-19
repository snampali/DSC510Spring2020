#Name: Harsimar Mangat
#StudentID: 21231935
#Date 9/20/2020

from __future__ import print_function, division
%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import thinkstats2
import thinkplot

import  nsfg



def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


df=nsfg.ReadFemResp()

pmf=thinkstats2.Pmf(df.numkdhh,label='numkdhh')
thinkplot.Pmf(pmf)

thinkplot.Config(xlabel='Number of children', ylabel='PMF')

biased = BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

pmf.Mean()

biased.Mean()




