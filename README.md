# Tagging-Raw-Job-Descriptions
Multi labels text classification.  One day project. 

The project was written for a contest at hackerrank.com: 

https://www.hackerrank.com/contests/indeed-ml-codesprint-2017/challenges/tagging-raw-job-descriptions

Indeed.com provides the world's largest job search engine. They want to give the users the best possible experience  enhancing the job searching process by automatically extracting interesting properties (tags) from job descriptions. These tags allow users to filter and find jobs more easily. For example, given the full job description, our program should accurately extract information like the number of required years of experience.

### Goal:
to assign tags given the job description. 
I was interested in only these twelve tags:

part-time-job,
full-time-job,
hourly-wage,
salary,
associate-needed,
bs-degree-needed,
ms-or-phd-needed,
licence-needed,
1-year-experience-needed,
2-4-years-experience-needed,
5-plus-years-experience-needed,
supervising-job.

#### train.tsv 
is the training dataset providing tags and  job descriptions. The header row has the following two columns:
tags: A space-separated list of tags.
description: A job description.

#### test.tsv 
is the testing dataset providing the raw job descriptions of  jobs. The header row has only column: description containing job descriptions.

#### tags.tsv 
is the output file. It contains a space-separated list of tags -- the order of the tags does not matter -- for each of the job descriptions from the file test.tsv in that same order. For some descriptions it has an empty list of tags.


Working of this project I found some errors  in training data. For example:
4290 "... Preferred bachelors degree from a four-year college or university …"
1317 "... -College Degree preferred …"

for 4290 we do not have “bs-degree-needed”, but for 1317 we have this tag

### Data preprocessing:
I converted the data to lowercase and removed “stopwords” including ‘&' and ‘\uf02d'

### Model Selection:
My main idea was to create a different model for every label class. I tried some combinations of KNeighborsClassifier, RandomForestClassifier, and MLPClassifier for VotingClassifier. Finally I got the best result using MLPClassifier with increased the number of iteration (I used 400) for all labels.

I had only some hours for this project. I think, I could get a better result if I had more time (I would try more different models with different parameters). 



