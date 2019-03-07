import pandas as pd
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt
import math


np.random.seed(1)

#age beta distribution for males
data_beta_male = beta.rvs(3.55,1.91, size=594)

#age beta distribution for females
data_beta_female = beta.rvs(3.55,2.76, size = 594)

#calculates a probability for each gender and age of showing up in the simulation
maleHist = np.histogram(data_beta_male)[1]*10 +8
maleHistProb = .5*np.histogram(data_beta_male)[0]/sum(np.histogram(data_beta_male)[0])
femaleHist = np.histogram(data_beta_female)[1]*10+8
femaleHistProb = .5*np.histogram(data_beta_female)[0]/sum(np.histogram(data_beta_female)[0])

#creating initial dataframe
db = pd.DataFrame({'Males':data_beta_male,'Females':data_beta_female})
db = db.reindex(columns = ["Males","Females","Gender","Age","Q1","Q3a","Q3b","Q3c","Q3d","Q3e","Q5","Q6","Q7","Q8","Q9","Q11","Q13","Q15","Q17","Q20","Q21","Q22","Q24","Q25","Q27","Q28","Q29","Q30","Q31","Q33","Q34","Q36","Q40","Q41","Q43","Q45","Q47a","Q47b","Q47c","Q47d","Q48","Q49","Q50","Q51","Q54","Q55","Q58","Q60","Q61a","Q61b","Q61c","Q62","Q63a","Q63b","Q63c","Q64a","Q64b","Q64c","Q64d","Q64e","Q65","Q66a","Q66b","Q66c","Q66d","Q66e","Q66f","Q66g","Q67a","Q67b","Q67c","Q67d","Q68","Q70","Q75","Q76a","Q76b","Q76c","Q76d","Q76e","Q76f","Q81","Q83","Q84","Q86","Q88","Q90","Q92","Q93","Q95","Q98","Q99","Q100","Q101","Q102","Q103","Q104","Q105","Q106","Q107","Q108","Q109","Q110","Q111","Q112","Q113","Q114","Q115","Q116","Q117","Q118","Q119","Q121","Q122","Q123","Q124","Q125","Q126","Q128","Q129","Q130","Q131","Q134","Q135","Q136","Q137a","Q137b","Q137c","Q138a","Q138b","Q138c","Q138d","Q139a","Q139b","Q139c","Q139d","Q140","Q141","Q142","Q143","Q144","Q145a","Q145b","Q145c","Q146d","Q146a","Q146b","Q146c","Q148","Q149","Q152a1","Q152a2","Q152b1","Q152b2","Q152c1","Q152c2","Q152d1","Q152d2","Q152e1","Q152e2","Q152f1","Q152f2","Q152g1","Q152g2","Q152h1","Q152h2","Q152i1","Q152i2","Q152j1","Q152j2","Q152k1","Q152k2","Q152l1","Q152l2","Q152m1","Q152m2","Q152n1","Q152n2","Q152o1","Q152o2","Q152q1","Q152q2","Q152r1","Q152r2","Q152s1","Q152s2","Q153","Q154","Q155","Q156","Q157","Q158","Q159","Q160","Q161","Q162","Q163","Q164","Q165","Q166","Q167","Q168","Q169","Q170","Q171a1","Q171a2","Q171a3","Q171b1","Q171b2","Q171b3","Q171c1","Q171c2","Q171c3","Q171d1","Q171d2","Q171d3","Q171e1","Q171e2","Q171e3","Q171f1","Q171f2","Q171f3","Q171g1","Q171g2","Q171g3","Q171h1","Q171h2","Q171h3","Q172","Q173","Q174","Q175","Q176","Q177","Q178","Q179","Q180","Q181","Q182","Q183","Q184","Q185","Q186","Q187","Q189","Q190","Q191","Q192","Q193","Q194","Q195","Q196","Q197","Q198","Q199","Q200","Q201","Q202","Q203","Q204","Q205","Q206",'RA','TopCharacteristic'])

#question characteristic type
questReps = ["JJH","VBA","VBA","VBA","VBA","VBA","JJH","JJH","JJH","JJH","JJH","JJH","JJH","JJH","SAMHP","JJH/VBA","JJH/VBA","JJH/VBA","JJH/VBA","JJH","VBA","VBA","VBA","VBA","PSS","PSS","PSS","FLA","EE","EE","EE","EE","EE","EE","EE","EE","EE","PSSN","EE","EE","FLA","PSSN","FLA/JJH","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","EE","EE","EE","EE","EE","EE","EE","EE","EE","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","SAMHP","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","PSS","VBA","VBA","VBA","VBA","VBA","VBA","VBA","VBA","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","PSSN","FLA/VBA","PSSN/VBA","PSSN/VBA","VBA","VBA","PSSN","FLA","FLA","VBA","EE","EE","EE","EE","VBA/EE","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","FLA","EE","EE","EE","EE/VBA","EE","EE","PSSN","FLA","VBA","VBA","VBA","VBA","VBA","VBA","VBA","VBA","VBA","VBA","VBA","SAMHP","SAMHP","SAMHP","FLA","PSSN","VBA","VBA","FLA","FLA"]

#listing whether a question has two or three possible answers - indicated by 1 for two possible answers and 2 for three possible answers
questNums = [2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,2,2,1,1,1,2,2,1,1,2,2,2,2,1,2,2,2,1,1,2,2,2,1,1,1,1,2,2,2,2,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,2,2,2,2,1,2,2,2,2,2,2,2,2,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,2,2,2,2,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

#determines if certain questions should be answered based on a child's previous answer. For example, Q6 will only be answered if Q5's answer is a "1"
priorQ = [["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q5"],["0","0"],["0","0"],["0","0"],["1","Q9"],["0","0"],["1","Q13"],["0","0"],["0","0"],["1","Q20"],["0","0"],["0","0"],["1","Q24"],["0","0"],["0","0"],["0","0"],["1","Q29"],["0","0"],["0","0"],["1","Q33"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q48"],["1","Q48"],["1","Q50"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q62"],["1","Q62"],["1","Q62"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q65"],["1","Q65"],["1","Q65"],["1","Q65"],["1","Q65"],["1","Q65"],["1","Q65"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q68"],["1","Q68"],["1","Q68"],["1","Q68"],["1","Q68"],["1","Q68"],["1","Q68"],["1","Q68"],["0","0"],["1","Q81"],["1","Q81"],["1","Q81"],["1","Q86"],["1","Q86"],["1","Q86"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q110"],["0","0"],["0","0"],["1","Q113"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q130"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q152a1"],["0","0"],["1","Q152b1"],["0","0"],["1","Q152c1"],["0","0"],["1","Q152d1"],["0","0"],["1","Q152e1"],["0","0"],["1","Q152f1"],["0","0"],["1","Q152g1"],["0","0"],["1","Q152h1"],["0","0"],["1","Q152i1"],["0","0"],["1","Q152j1"],["0","0"],["1","Q152k1"],["0","0"],["1","Q152l1"],["0","0"],["1","Q152m1"],["0","0"],["1","Q152n1"],["0","0"],["1","Q152o1"],["0","0"],["1","Q152q1"],["0","0"],["1","Q152r1"],["0","0"],["1","Q152s1"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["1","Q48"],["1","Q48"],["1","Q48"],["1","Q48"],["1","Q48"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"]]

#every child begins at a neutral state - .5 for each category
buckets = {'JJH':.5,'SAMHP':.5,'PSSN':.5,'VBA':.5,'PSS':.5, 'FLA':.5,'EE':.5}
bucketListMale = []
bucketListFemale = []

#keeps track of childs answers based on characteristic 
questionsTwoScore = {'JJH_0':0,'SAMHP_0':0,'PSSN_0':0,'VBA_0':0,'PSS_0':0, 'FLA_0':0,'EE_0':0, 'JJH_1':0,'SAMHP_1':0,'PSSN_1':0,'VBA_1':0,'PSS_1':0, 'FLA_1':0,'EE_1':0, 'JJH_2':0,'SAMHP_2':0,'PSSN_2':0,'VBA_2':0,'PSS_2':0, 'FLA_2':0,'EE_2':0}
questionsOneScore = {'JJH_0':0,'SAMHP_0':0,'PSSN_0':0,'VBA_0':0,'PSS_0':0, 'FLA_0':0,'EE_0':0, 'JJH_1':0,'SAMHP_1':0,'PSSN_1':0,'VBA_1':0,'PSS_1':0, 'FLA_1':0,'EE_1':0}

#final values multiplied by the "buckets" list. These values were ranked to show that some characterisitics play a higher role in determining rearrest.
finalEvalBucket = {'JJH':.21,'SAMHP':.157,'PSSN':.157,'VBA':.133,'PSS':.133, 'FLA':.105,'EE':.105}

#changes all NA to 0
db[np.isnan(db)] = 0

#determines, based on amount of characteristics, what characterisitc in "buckets" to increment per child, what the answer to the question is, and increments "questionsOneScore". Returns answer to question.
def one_q(num,strg,gender,age):
    if(isinstance(strg,list)):

        cat1 = strg[0]
        cat2 = strg[1]

        if(gender ==0):
            prob = buckets[cat1] + .05
            prob = addAgeProb(prob,gender,age)
        else:
            prob = buckets[cat1]
            prob = addAgeProb(prob,gender,age)

        psdval = np.random.choice([0,1],p=[(1-prob),prob])

        addProb(cat1,psdval,1,False)
        addProb(cat2,psdval,1,True)

        addQuestsOne(cat1,psdval)
        addQuestsOne(cat2,psdval)
    else:
        cat1 = strg

        if(gender ==0):
            prob = buckets[cat1] + .05
            prob = addAgeProb(prob,gender,age)
        else:
            prob = buckets[cat1]
            prob = addAgeProb(prob,gender,age)

        psdval = np.random.choice([0,1],p=[(1-prob),prob])
        addProb(cat1,psdval,1,False)
        addQuestsOne(cat1,psdval)

    return psdval

#adds values to "buckets"
def addProb(strg,num, type, half):
    if(buckets[strg]>.8):
        buckets[strg] = .8
    elif(buckets[strg]<.2):
        buckets[strg] = .2
    else:
        if(type==1 and half):
            buckets[strg] = buckets[strg] + one_q_ans_half(num)
        else:
            buckets[strg] = buckets[strg] + one_q_ans(num)
        if(type ==2 and half):
            buckets[strg] = buckets[strg] + two_q_ans_half(num)
        else:
            buckets[strg] = buckets[strg] + two_q_ans(num)

#adds a higher probability to children whose age and gender make them more susceptible to rearrest
def addAgeProb(prob,gen,age):
    if(gen ==0):
        for i in maleHist:
            if(age>i):
                prob = prob + maleHistProb[i]
            break
    else:
        for i in femaleHist:
            if(age>i):
                prob = prob + femaleHistProb[i]
            break
    return prob

#increments "questionsOneScore"
def addQuestsOne(word,num):
    if(num ==0):
        questionsOneScore[word+'_0']+=1
    else:
        questionsOneScore[word+'_1']+=1

#increments "questionsTwoScore"
def addQuestsTwo(word,num):
    if(num ==0):
        questionsTwoScore[word+'_0']+=1
    elif(num==1):
        questionsTwoScore[word+'_1']+=1
    else:
        questionsTwoScore[word+'_2']+=1

#determines, based on amount of characteristics, what characterisitc in "buckets" to increment per child, what the answer to the question is, and increments "questionsOneScore". Returns answer to question.
def two_q(num,strg,gender,age):
    if(isinstance(strg,list)):

        cat1 = strg[0]
        cat2 = strg[1]

        if(gender ==0):
            prob = buckets[cat1] + .05
            prob = addAgeProb(prob,gender,age)
        else:
            prob = buckets[cat1]
            prob = addAgeProb(prob,gender,age)

        psdval = np.random.choice([0,1,2],p=[(1-prob)*(1/3),(1-prob)*(2/3),prob])

        addProb(cat1,psdval,2,False)
        addProb(cat2,psdval,2,True)

        addQuestsTwo(cat1,psdval)
        addQuestsTwo(cat2,psdval)
    else:
        cat1 = strg

        if(gender ==0):
            prob = buckets[cat1] + .05
            prob = addAgeProb(prob,gender,age)
        else:
            prob = buckets[cat1]
            prob = addAgeProb(prob,gender,age)

        psdval = np.random.choice([0,1,2],p=[(1-prob)*(1/3),(1-prob)*(2/3),prob])
        addProb(cat1,psdval,2,False)
        addQuestsTwo(cat1,psdval)

    return psdval

#calculates amount to be added to "buckets" for two possible answer questions
def one_q_ans(num):
    if(num ==1):
        return .05
    else:
        return -.05

#calculates amount to be added to "buckets" for two possible answer questions and split characteristic questions
def one_q_ans_half(num):
    if(num ==1):
        return .005
    else:
        return -.005

#calculates amount to be added to "buckets" for three possible answer questions
def two_q_ans(num):
    if(num ==2):
        return .01
    elif(num==1):
        return 0.0
    else:
        return -.01

#calculates amount to be added to "buckets" for three possible answer questions and split characteristic questions
def two_q_ans_half(num):
    if(num ==2):
        return .005
    elif(num ==1):
        return 0.0
    else:
        return -.005

#determines whether a question had a previous requirement
def priorQuest(arr1):
    if(arr1[0]=="1"):
        return arr1[1]
    else:
        return "0"

#given values in "buckets", determines whether child should be rearrested
def evalBuckets(buck):
    catList = ['JJH','SAMHP','PSSN','VBA','PSS','FLA','EE']
    num = 0
    for i in range(0,len(catList)):
        num += buck[catList[i]]*finalEvalBucket[catList[i]]

    if(num>=.4):
        return 1
    else:
        return 0

#returns question characterisitic type that has been answered most 
def getLargestChar(buck):
    values = list(buck.values())
    index = 0
    for i in range(0,len(values)):
        if(values[i] >= values[index]):
            index = i
    return list(buck.keys())[index]

#for all children in the sample
for i in range(0,len(db)):
    #for all questions
    for j in range(0,len(questNums)):
        #get question number and characteristic
        questRepType = questReps[j]
        questNumType = questNums[j]
        #Return the previous requirement, or 0 for no requirement
        pQ = priorQuest(priorQ[j]) 
        #choose male or female
        db.iloc[i,2] = np.random.choice([0,1],p=[.6,.4])
        #calculate an age based on gender selection and beta distribution
        if(db.iloc[i,2]==0):
            db.iloc[i,3] = (db.iloc[i,0]*10) +8
        else:
            db.iloc[i,3] = (db.iloc[i,1]*10) +8

        #if the question does have a prior requirement..
        if(pQ != "0"):
            #if the prior requirement question is not a 0 (the question was answered in a way that suggests rearrest)
            if(db.loc[i,pQ] != 0):
                #if the question has two characteristics assigned to it
                if('/' in questRepType):
                    #split the two characteristic categories
                    words = questRepType.split('/')
                    #if the question type only has two possible responses, evaluate the question
                    if(questNumType==1):
                        psdval = one_q(questNumType,words,db.iloc[i,2],db.iloc[i,1]) 
                    #if the question type has three possible repsonses, evaluate the question
                    elif(questNumType==2):
                        psdval = two_q(questNumType, words,db.iloc[i,2],db.iloc[i,1])
                    else:
                        print('nan')
                #if the question does not have two characteristics
                else:
                    #if the question type only has two possible responses, evaluate the question
                    if(questNumType==1):
                        psdval = one_q(questNumType,questRepType,db.iloc[i,2],db.iloc[i,1])
                        #if the question type has three possible repsonses, evaluate the question
                    elif(questNumType==2):
                        psdval = two_q(questNumType,questRepType,db.iloc[i,2],db.iloc[i,1])
                    else:
                        print('nan')
            else:
                psdval = np.nan
        #if the question does have a prior requirement..
        else:
            #if the prior requirement question is not a 0 (the question was answered in a way that suggests rearrest)
            if('/' in questRepType):
                #split the two characteristic categories
                words = questRepType.split('/')
                #if the question type only has two possible responses, evaluate the question
                if(questNumType==1):
                    psdval = one_q(questNumType,words,db.iloc[i,2],db.iloc[i,1])
                #if the question type has three possible repsonses, evaluate the question 
                elif(questNumType==2):
                    psdval = two_q(questNumType, words,db.iloc[i,2],db.iloc[i,1])
                else:
                    print('nan')
            #if the question does not have two characteristics
            else:
                #if the question type only has two possible responses, evaluate the question
                if(questNumType==1):
                    psdval = one_q(questNumType,questRepType,db.iloc[i,2],db.iloc[i,1])
                #if the question type has three possible repsonses, evaluate the question
                elif(questNumType==2):
                    psdval = two_q(questNumType,questRepType,db.iloc[i,2],db.iloc[i,1])
                else:
                    print('nan')
        #place answer in dataset
        db.iloc[i,j+4] = psdval

    #given values in "buckets", determines whether child should be rearrested, and adds it to the data set
    finalVal = evalBuckets(buckets)
    db.iloc[i,len(db.columns)-2] = finalVal

    #returns question characterisitic type that has been answered most, and adds it to the data set
    topChar = getLargestChar(buckets)
    db.iloc[i,len(db.columns)-1] = topChar

    print(i)

    #resets "buckets" for next child
    buckets = {'JJH':.5,'SAMHP':.5,'PSSN':.5,'VBA':.5,'PSS':.5, 'FLA':.5,'EE':.5}


print('Done!')

db.to_csv("Capstone.csv")
