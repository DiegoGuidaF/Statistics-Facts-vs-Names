# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:13:37 2016

@author: DiegoFG
"""

import numpy as np
import pandas
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
from statsmodels.stats.anova import anova_lm
import numpy as np
from scipy.stats import ttest_ind, ttest_ind_from_stats
from scipy.special import stdtr

#We import the data files for the two studies and insert a code for each Study
DataS = pandas.read_csv('./datas.csv')    
DataS = DataS[DataS["QuestionsNumber"] < 3]
DataS.insert(0,'Study',0)

DataG = pandas.read_csv('./datag.csv')    
DataG = DataG[DataG["QuestionsNumber"] < 3]
DataG.insert(0,'Study',1)


#We collapse the data form the two different studies in one variable.
DataSum = DataS.append(DataG)

#Isolate the responses for names and for facts.
DataSumN = DataSum[DataSum["QuestionType"] == 'Name']
DataSumF = DataSum[DataSum["QuestionType"] == 'Fact']

#We select the responses for the 2nd session and isolate it in a variable.
DataS2 = DataSum[DataSum["Session"] == 2]

#Isolate the responses for names and for facts in the second session.
DataS2N = DataS2[DataS2["QuestionType"] == 'Name']
DataS2F = DataS2[DataS2["QuestionType"] == 'Fact']

#We group the data in Datasum by session, condition and questiontype.
Session = DataSum.groupby(['Session', 'Condition','QuestionType'])
#Calculate the mean answers
Hist = Session["Value"].mean()

#we group the data in Datasum by subject, and then calculate the mean for each subject
Rendimiento = DataSum.groupby(['Subject'])
SubjMean = Rendimiento["Value"].mean()

print ('')
print ('Average performance')
#Calculate the average performance
print (SubjMean.mean())
print ('')
#report subjects with a mean higher than average
print ('-------Subjects with a mean higher than average')
print (SubjMean[SubjMean >= 0.75])

print ('')

#report subjects with a mean lower than average
print ('-------Subjects with a mean lower than average')
print (SubjMean[SubjMean <= 0.25])

#One way ANOVA to compare both studies
formula1 = 'DataSum.Study ~ C(DataSum.Value)'


model1 = ols(formula1, DataSum).fit()
aov_table1 = anova_lm(model1,typ=2)
print ('--------------')
print('One- Way ANOVA comparing both studies')
print(aov_table1)
print ('')
print ('--------------')
#T-test between the two sample data groups 
t, p = ttest_ind(DataS['Value'], DataG['Value'], equal_var=False)
print('T-Test comparing both studies')
print("ttest_ind:            t = %g  p = %g" % (t, p))
print ('--------------')
print ('')

# Three-way ANOVAs over the collapsed data from both studies
formula2 = 'DataSum.Value ~ C(DataSum.Session)*C(DataSum.QuestionType)*C(DataSum.Condition)'

model2 = ols(formula2, DataSum).fit()
aov_table2 = anova_lm(model2,typ=2)

print ('Three-Way ANOVAs over the collapsed data')
print (aov_table2)

#T-Tests in order to asses performance against chance level
print('')
print('---------------------')
print('T-test to evaluate results obtained vs. chance over the collapsed data.')
print('---------------------')

SG_ttest_NAMEOst = stats.ttest_1samp(DataSumN[DataSumN['Condition'] == 'Ostensive']["Value"],1/6)
SG_ttest_NAMENOst = stats.ttest_1samp(DataSumN[DataSumN['Condition'] == 'No-Ostensive']["Value"],1/6)

SG_ttest_FACTOst = stats.ttest_1samp(DataSumF[DataSumF['Condition'] == 'Ostensive']["Value"],1/10)
SG_ttest_FACTNOst = stats.ttest_1samp(DataSumF[DataSumF['Condition'] == 'No-Ostensive']["Value"],1/10)

print('NAME: t-test considering a 1/6 change of getting the right answer')
print('p Ost= ',SG_ttest_NAMEOst[1])
print('p Nost = ',SG_ttest_NAMENOst[1])
print('------')
print('FACT: t-test considering a 1/10 change of getting the right answer')
print('p ost= ',SG_ttest_FACTOst[1])
print('p Nost= ',SG_ttest_FACTNOst[1])
print ('--------------')
print ('')



#Two-Way Anova over the data of the second session isolateed.
formula3 = 'DataS2.Value ~ C(DataS2.QuestionType)*C(DataS2.Condition)'


model3 = ols(formula3, DataS2).fit()
aov_table3 = anova_lm(model3,typ=2)

print ('Two-Way ANOVA over the data of session 2')
print (aov_table3)

#T-Tests in order to asses performance against chance level
print('')
print('---------------------')
print('T-test to evaluate results obtained vs. chance just over the data of the second session')
print('---------------------')

SG2_ttest_NAMEOst = stats.ttest_1samp(DataS2N[DataS2N['Condition'] == 'Ostensive']["Value"],1/6)
SG2_ttest_NAMENOst = stats.ttest_1samp(DataS2N[DataS2N['Condition'] == 'No-Ostensive']["Value"],1/6)

SG2_ttest_FACTOst = stats.ttest_1samp(DataS2F[DataS2F['Condition'] == 'Ostensive']["Value"],1/10)
SG2_ttest_FACTNOst = stats.ttest_1samp(DataS2F[DataS2F['Condition'] == 'No-Ostensive']["Value"],1/10)

print('NAME: t-test considering a 1/6 change of getting the right answer')
print('p Ost= ',SG_ttest_NAMEOst[1])
print('p Nost = ',SG_ttest_NAMENOst[1])
print('------')
print('FACT: t-test considering a 1/10 change of getting the right answer')
print('p ost= ',SG_ttest_FACTOst[1])
print('p Nost= ',SG_ttest_FACTNOst[1])
print('------')
print('')


#Anova over data of the second session, just considering names
formula4 = 'DataS2N.Value ~ C(DataS2N.Condition)'


model4 = ols(formula4, DataS2N).fit()
aov_table4 = anova_lm(model4,typ=2)

print ('One-Way ANOVA just over names in the second session')
print (aov_table4)
print('---------------------')
print('')


#Figure corresponding to the Ostensive & Non-Ostensive Bar plots for
#sessions 1 & 2.
N=2 # Number of histograms per figure.
ind = np.arange(N)
width=0.35 # Width of the bars
fig, (ax1,ax2) = plt.subplots(1, 2, sharey=True)

#Bars 1-2 and 3-4 with their corresponding figure.
rects1=ax1.bar(ind,[Hist[1]['Ostensive']['Fact'],Hist[1]['No-Ostensive']['Fact']],width,color='r',yerr=[Session["Value"].std()[1]['Ostensive']['Fact'],Session["Value"].std()[1]['No-Ostensive']['Fact']])

rects2=ax1.bar(ind+width,[Hist[1]['Ostensive']['Name'],Hist[1]['No-Ostensive']['Name']],width,color='b',yerr=[Session["Value"].std()[1]['Ostensive']['Name'],Session["Value"].std()[1]['No-Ostensive']['Name']])

rects3=ax2.bar(ind,[Hist[2]['Ostensive']['Fact'],Hist[2]['No-Ostensive']['Fact']],width,color='r',yerr=[Session["Value"].std()[2]['Ostensive']['Fact'],Session["Value"].std()[2]['No-Ostensive']['Fact']])

rects4=ax2.bar(ind+width,[Hist[2]['Ostensive']['Name'],Hist[2]['No-Ostensive']['Name']],width,color='b',yerr=[Session["Value"].std()[2]['Ostensive']['Name'],Session["Value"].std()[2]['No-Ostensive']['Name']])#,yerr=menStd)

ax1.set_xticks(ind+width)
ax1.set_xticklabels(('Ostensive','Non-Ostensive'))
ax1.set_ylabel('Mean correct answer')
ax1.set_ylim([0,1.3])
ax1.set_title("Session 1")
#The following function attaches the column height number to the top of it.
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        Num='{0:.2g}'.format(height)
        ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % (Num),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
ax2.set_xticks(ind+width)
ax2.set_xticklabels(('Ostensive','Non-Ostensive'))
ax2.set_title("Session 2")
ax2.legend((rects3[0], rects4[0]), ('Fact', 'Name'))

#The following function attaches the column height number to the top of it.
def autolabel(rects):
    # attach some text labelsº
    for rect in rects:
        height = rect.get_height()
        Num='{0:.2g}'.format(height)
        ax2.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % (Num),
                ha='center', va='bottom')

autolabel(rects3)
autolabel(rects4)









