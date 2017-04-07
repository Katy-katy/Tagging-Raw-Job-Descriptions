import sys
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.neural_network import MLPClassifier

def stopw(w):
    stopwords = ['&', '\uf02d', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']
    return w in stopwords

def create_labels(my_array, str):
    labels = []
    for i in range(len(my_array)):
        my_l = 0
        for l in my_array[i]:
            if str == l:
                my_l = 1
        labels.append(my_l)
    return labels

def work4(test_data, labels):
    my_vector = CountVectorizer(input='content',ngram_range=(1,2))
    X_train_counts = my_vector.fit_transform(train,)
    tf_transformer = TfidfTransformer(use_idf=True,).fit(X_train_counts)
    X_train_tf = tf_transformer.transform(X_train_counts)
    svd = TruncatedSVD(n_components=50, random_state=9)
    X_train = svd.fit_transform(X_train_tf)

    clf3 =  MLPClassifier(max_iter = 400).fit(X_train, labels)

    X_new_counts = my_vector.transform(test_data)
    X_new_tfidf = tf_transformer.transform(X_new_counts)
    X_new = svd.transform(X_new_tfidf)
    return clf3.predict(X_new)

#train
file = open("train.tsv", "rb")
raw_data = file.read().decode()
file.close()

docs = raw_data.split("\n")
docs2 = docs[1: ]

random.seed(0)
random.shuffle(docs2)

train = []
labels = []

for d in docs2:
    d = d.lower()
    d = d.split("\t")
    if len(d) != 0:
        labels.append(d[0].split())
        text = d[1].split()
        train.append(' '.join([i for i in text if not stopw(i)]))

label_1_year = create_labels(labels, '1-year-experience-needed')
label_2_year = create_labels(labels, '2-4-years-experience-needed')
label_5_year = create_labels(labels, '5-plus-years-experience-needed')
label_AS = create_labels(labels, 'associate-needed')
label_BS = create_labels(labels, 'bs-degree-needed')
label_full_time = create_labels(labels, 'full-time-job')
label_hourly = create_labels(labels, 'hourly-wage')
label_1icence = create_labels(labels, 'licence-needed')
label_MS = create_labels(labels, 'ms-or-phd-needed')
label_part_time = create_labels(labels, 'part-time-job')
label_salary = create_labels(labels, 'salary')
label_supervising = create_labels(labels, 'supervising-job')

file = open("test.tsv", "rb")
raw_data = file.read().decode()
file.close()

docs = raw_data.split("\n")
docs2 = docs[1: ]

test = []
for d in docs2:
    d = d.lower()
    if len(d) != 0:
        text = d.split()
        test.append(' '.join([i for i in text if not stopw(i)]))

result = [" "] * len(test)

pr0 = work4(test, label_1_year)
for i in range(len(test)):
    if pr0[i] == 1:
        result[i] +=' 1-year-experience-needed'
print("labels1 are done!")

pr1 = work4(test,label_2_year)
for i in range(len(test)):
    if pr1[i] == 1:
        result[i] += ' 2-4-years-experience-needed'

pr2 = work4(test, label_5_year)
for i in range(len(test)):
    if pr2[i] == 1:
        result[i] += ' 5-plus-years-experience-needed'

pr3 = work4(test, label_AS)
for i in range(len(test)):
    if pr3[i] == 1:
        result[i] += ' associate-needed'

pr4 = work4(test, label_BS)
for i in range(len(test)):
    if pr4[i] == 1:
        result[i] += ' bs-degree-needed'

pr5 = work4(test, label_full_time)
for i in range(len(test)):
    if pr5[i] == 1:
        result[i] += ' full-time-job'

pr6 = work4(test, label_hourly)
for i in range(len(test)):
    if pr6[i] == 1:
        result[i] +=' hourly-wage'

pr7 = work4(test, label_1icence)
for i in range(len(test)):
    if pr7[i] == 1:
        result[i] +=' licence-needed'

print("labels7 are done!")

pr8 = work4(test, label_MS)
for i in range(len(test)):
    if pr8[i] == 1:
        result[i] +=' ms-or-phd-needed'

pr9 = work4(test, label_part_time)
for i in range(len(test)):
    if pr9[i] == 1:
        result[i] +=' part-time-job'

pr10 = work4(test, label_salary)
for i in range(len(test)):
    if pr10[i] == 1:
        result[i] +=' salary'

pr11 = work4(test, label_supervising)
for i in range(len(test)):
    if pr11[i] == 1:
        result[i] +=' supervising-job'


result_l = [2922]
result_l[0] = "tags"
for line in result:
    line = line[2: ]
    line = line.replace(" ", "\t")
    result_l.append(line)


with open("tags.tsv", "w") as record_file:
    for line in result_l:
        record_file.write(line + "\n")
