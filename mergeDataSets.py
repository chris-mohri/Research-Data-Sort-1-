import csv
from collections import OrderedDict
 
#opens csv files
youthSurvey = open('Youth Survey.csv')
youthSurveyReader = csv.reader(youthSurvey)
hcvParent = open('HCV Tech - Parent Survey 1-15-21.csv')
hcvParentReader = csv.reader(hcvParent)
hcvSelf = open('HCV Tech - Youth Self Survey 1-15-21.csv')
hcvSelfReader = csv.reader(hcvSelf)
 
q1,q2,q3=[],[],[]
rows = []
rows2 = []
rows3 = []
count=0
prompts=[]
rowCopy=[]
for row in youthSurveyReader:
        rowCopy=row
        if (count==0):
                #prompts=row
                rowCopy.insert(0, "Source")
        else:
                rowCopy.insert(0, "Youth Survey")
        rows.append(rowCopy)
        count+=1
youthSurvey.close()







#Reads all rows of hcv Parent survey
count=0
for row in hcvParentReader:
        rowCopy=row
        #if count>2:
                #print(row)
        if (count==0):
                #prompts=row
                rowCopy.insert(0, "Source")
        else:
                rowCopy.insert(0, "HCV Parent Survey")
        rows2.append(rowCopy)
        count+=1
hcvParent.close()





#Reads all rows of hcv self survey
count=0
#print('row3 stuff')
for row in hcvSelfReader:
        rowCopy=row
        #print('hi')
        if (count==0):
                #prompts=row
                rowCopy.insert(0, "Source")
        else:
                rowCopy.insert(0, "HCV Self Survey")
        rows3.append(rowCopy)
        count+=1
hcvSelf.close()

#ex



#question List per survey
q1=rows[0]
q2=rows2[0]
q3=rows3[0]

masterQuestionList=[]

dict1=OrderedDict()
for i in range(len(q1)):
        question=q1[i]
        dict1[question]=[]
        for answer in rows[1:]:
                dict1[question].append(answer[i])


dict2=OrderedDict()
for i in range(len(q2)):
        question=q2[i]
        dict2[question]=[]
        for answer in rows2[1:]:
                dict2[question].append(answer[i])

dict3=OrderedDict()
for i in range(len(q3)):
        question=q3[i]
        dict3[question]=[]
        for answer in rows3[1:]:
                dict3[question].append(answer[i])

for q in q1:
        if q not in masterQuestionList:
                masterQuestionList.append(q)
for q in q2:
        if q not in masterQuestionList:
                masterQuestionList.append(q)
for q in q3:
        if q not in masterQuestionList:
                masterQuestionList.append(q)

final = OrderedDict()
dicts=[dict1]
count=0 #counter for each person
count2=0
count3=0
len1=(len(dict1["Gender"]))
len2=(len(dict2["Gender"]))
len3=(len(dict3["Gender"]))
for q in masterQuestionList:
        final[q]=[]

        if q in dict1:
                final[q].extend(dict1[q])
        else:
                final[q].extend([""]*len1)
for q in masterQuestionList:

        if q in dict2:
                final[q].extend(dict2[q])
        else:
                final[q].extend([""]*len2)

for q in masterQuestionList:

        if q in dict3:
                final[q].extend(dict3[q])
        else:
                final[q].extend([""]*len3)

finalLength=(len(final["Gender"]))

with open('results.csv', mode='w') as results:
        writer = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(masterQuestionList)
        for i in range(finalLength):
                qList=[]
                for q in final:
                        qList.append(final[q][i])
                
                writer.writerow(qList)

        


dict6={1:[0,2]}
#print(1 in dict6)









def isSame(q1,q2, threshold=6):
        return 42




#["Time", "Gender", "Role", "Neighborhood", "School", "Grade", "Race", ]        
 
#print(prompts)
#print('hi')
 
        
 

