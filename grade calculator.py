# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sc

def year_average(credits_20, credits_10):
    
    earned_marks = sum(credits_10) + 2*sum(credits_20)
    total_marks = 100*(len(credits_10) + 2*len(credits_20))
    
    return earned_marks / total_marks

def grading(weighted):
    final_grade = ""
    if weighted >= 0.7: 
        final_grade = "1st"
    if weighted > 0.6 and weighted < 0.7: 
        final_grade = "2.1"
    if weighted > 0.5 and weighted < 0.6:
        final_grade = "2.2"
    if weighted < 0.5:
        final_grade = "Fail"
    return final_grade

# BSC programme
# {20 credit},{10 credit}
y1 = year_average({46,40},{72,63,42,40,59,54,58,55})
y2 = year_average({46,51},{49,49,64,47,72,65,64})
y3 = year_average({63,86,67},{46,47,40,88,72,65})

BSC_weighted = (0.4*y2 + 0.6*y3)
BSC_classificaiton = grading(BSC_weighted)

# MSC programme
#y4 = year_average({},{})
#MSC_weighted = (0.2*y2 + 0.3*y3 + 0.5*y4)
#MSC_classification = grading(MSC_weighted)


    