import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib.pyplot as plt
import time
from sklearn.metrics import accuracy_score


# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
#for dirname, _, filenames in os.walk('/content/drive/My Drive/Colab Notebooks/kshield_project/dataset'):
#    for filename in filenames:
#        print(filename)
        #print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.

#/content/drive/My Drive/Colab Notebooks/kshield_project/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
pd.set_option('display.float_format', '{:.5f}'.format)
df1=pd.read_csv("C:/Users/songj/Desktop/케쉴/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")
df2=pd.read_csv("C:/Users/songj/Desktop/케쉴/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv")
df3=pd.read_csv("C:/Users/songj/Desktop/케쉴/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Friday-WorkingHours-Morning.pcap_ISCX.csv")
df4=pd.read_csv("C:/Users/songj/Desktop/케쉴/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Monday-WorkingHours.pcap_ISCX.csv")
df5=pd.read_csv("C:/Users/songj/Desktop/케쉴/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv")
df6=pd.read_csv("C:/Users/songj/Desktop/케쉴/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv")
df7=pd.read_csv("C:/Users/songj/Desktop/케쉴/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv")
df8=pd.read_csv("C:/Users/songj/Desktop/케쉴/dataset/cicids2017/MachineLearningCSV/MachineLearningCVE/Wednesday-workingHours.pcap_ISCX.csv")
df1.head()

df=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])
del df1,df2,df3,df4,df5,df6,df7,df8
#df2=df[df.columns[6:-1]]
#df=df2
#df2=[]
#del df2
print(df)
df=df.dropna( axis=0, how='any')

label_list = df[df.columns[-1]]
label_type = list(set(label_list))
for i in label_type:
    print(i)

#df=df.replace(',,', np.nan, inplace=False)

df=df.drop(columns=[' Fwd Header Length.1'], axis=1, inplace=False)

df.replace("Infinity", 0, inplace=True)
'''
df['Flow Bytes/s'].replace("Infinity", 0,inplace=True)
df[" Flow Packets/s"].replace("Infinity", 0, inplace=True)
df[" Flow Packets/s"].replace(np.nan, 0, inplace=True)
df['Flow Bytes/s'].replace(np.nan, 0,inplace=True)


df["Bwd Avg Bulk Rate"].replace("Infinity", 0, inplace=True)
df["Bwd Avg Bulk Rate"].replace(",,", 0, inplace=True)
df["Bwd Avg Bulk Rate"].replace(np.nan, 0, inplace=True)

df[" Bwd Avg Packets/Bulk"].replace("Infinity", 0, inplace=True)
df[" Bwd Avg Packets/Bulk"].replace(",,", 0, inplace=True)
df[" Bwd Avg Packets/Bulk"].replace(np.nan, 0, inplace=True)


df[" Bwd Avg Bytes/Bulk"].replace("Infinity", 0, inplace=True)
df[" Bwd Avg Bytes/Bulk"].replace(",,", 0, inplace=True)
df[" Bwd Avg Bytes/Bulk"].replace(np.nan, 0, inplace=True)


df[" Fwd Avg Bulk Rate"].replace("Infinity", 0, inplace=True)
df[" Fwd Avg Bulk Rate"].replace(",,", 0, inplace=True)
df[" Fwd Avg Bulk Rate"].replace(np.nan, 0, inplace=True)


df[" Fwd Avg Packets/Bulk"].replace("Infinity", 0, inplace=True)
df[" Fwd Avg Packets/Bulk"].replace(",,", 0, inplace=True)
df[" Fwd Avg Packets/Bulk"].replace(np.nan, 0, inplace=True)


df["Fwd Avg Bytes/Bulk"].replace("Infinity", 0, inplace=True)
df["Fwd Avg Bytes/Bulk"].replace(",,", 0, inplace=True)
df["Fwd Avg Bytes/Bulk"].replace(np.nan, 0, inplace=True)


df[" CWE Flag Count"].replace("Infinity", 0, inplace=True)
df[" CWE Flag Count"].replace(",,", 0, inplace=True)
df[" CWE Flag Count"].replace(np.nan, 0, inplace=True)

df[" Bwd URG Flags"].replace("Infinity", 0, inplace=True)
df[" Bwd URG Flags"].replace(",,", 0, inplace=True)
df[" Bwd URG Flags"].replace(np.nan, 0, inplace=True)

df[" Bwd PSH Flags"].replace("Infinity", 0, inplace=True)
df[" Bwd PSH Flags"].replace(",,", 0, inplace=True)
df[" Bwd PSH Flags"].replace(np.nan, 0, inplace=True)

df[" Fwd URG Flags"].replace("Infinity", 0, inplace=True)
df[" Fwd URG Flags"].replace(",,", 0, inplace=True)
df[" Fwd URG Flags"].replace(np.nan, 0, inplace=True)

df["Flow Bytes/s"]=df["Flow Bytes/s"].astype("float64")
df[' Flow Packets/s']=df[" Flow Packets/s"].astype("float64")

df['Bwd Avg Bulk Rate']=df["Bwd Avg Bulk Rate"].astype("float64")
df[' Bwd Avg Packets/Bulk']=df[" Bwd Avg Packets/Bulk"].astype("float64")
df[' Bwd Avg Bytes/Bulk']=df[" Bwd Avg Bytes/Bulk"].astype("float64")
df[' Fwd Avg Bulk Rate']=df[" Fwd Avg Bulk Rate"].astype("float64")
df[' Fwd Avg Packets/Bulk']=df[" Fwd Avg Packets/Bulk"].astype("float64")
df['Fwd Avg Bytes/Bulk']=df["Fwd Avg Bytes/Bulk"].astype("float64")
df[' CWE Flag Count']=df[" CWE Flag Count"].astype("float64")
df[' Bwd URG Flags']=df[" Bwd URG Flags"].astype("float64")
df[' Bwd PSH Flags']=df[" Bwd PSH Flags"].astype("float64")
df[' Fwd URG Flags']=df[" Fwd URG Flags"].astype("float64")
'''
df.replace('Infinity', 0.0, inplace=True)
df.replace('NaN', 0.0, inplace=True)
df.head()

X=df[df.columns[0:-1]]
y=df[df.columns[-1]]
del df

from scipy import stats

cols = list(X.columns)
for col in cols:
    X[col] = stats.zscore(X[col])

features=X.columns
#features=[" Fwd Packet Length Max"," Flow IAT Std"," Fwd Packet Length Std" ,"Fwd IAT Total",' Flow Packets/s', " Fwd Packet Length Mean",  "Flow Bytes/s",  " Flow IAT Mean", " Bwd Packet Length Mean",  " Flow IAT Max", " Bwd Packet Length Std", ]
X=X[features].copy()
X.dropna(axis=1, inplace=True)
X.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=10)
y_test_arr=y_test.to_numpy()   #as_matrix()


def calculate_metrics(true, false, not_detected):
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    if 'BENIGN' in true:
        true_positive = sum(true.values()) - true['BENIGN']
        true_negative = true['BENIGN']
    if 'BENIGN' in false:
        false_negative = false['BENIGN']
    if 'BENIGN' in not_detected:
        false_positive = not_detected['BENIGN']

    if true_positive + false_positive == 0:
        precision = "undefined"
    else:
        precision = (true_positive / (true_positive + false_positive)) * 100
    if true_positive + false_negative == 0:
        recall = "undefined"
    else:
        recall = (true_positive / (true_positive + false_negative)) * 100
    accuracy = ((true_positive + true_negative) / (
                true_positive + true_negative + false_positive + false_negative)) * 100
    print("========================================")
    print(" True positives :: ", true_positive)
    print(" True negatives :: ", true_negative)
    print(" False positive :: ", false_positive)
    print(" False negative :: ", false_negative)
    print(" Accuracy :: ", accuracy)
    print(" Recall :: ", recall)
    print(" Precision :: ", precision)
    print("========================================")


def calculate_confusion_matrix(y_test_arr, yhat):
    true = {}
    false = {}
    not_detected = {}

    for x in range(len(y_test_arr)):
        if y_test_arr[x] == yhat[x]:
            if y_test_arr[x] in true:
                true[y_test_arr[x]] = true[y_test_arr[x]] + 1
            else:
                true[y_test_arr[x]] = 1
        elif y_test_arr[x] != yhat[x]:
            if yhat[x] in false:
                false[yhat[x]] = false[yhat[x]] + 1

                if y_test_arr[x] in not_detected:
                    not_detected[y_test_arr[x]] = not_detected[y_test_arr[x]] + 1
                else:
                    not_detected[y_test_arr[x]] = 1

            else:
                false[yhat[x]] = 1

                if y_test_arr[x] in not_detected:
                    not_detected[y_test_arr[x]] = not_detected[y_test_arr[x]] + 1
                else:
                    not_detected[y_test_arr[x]] = 1

    calculate_metrics(true, false, not_detected)

from sklearn.neighbors import KNeighborsClassifier


#knn
t1=time.time()
knn=KNeighborsClassifier()
model_knn=knn.fit(X_train,y_train)
yhat=model_knn.predict(X_test)
print("knn accuracy is : ", accuracy_score(y_test, yhat))
calculate_confusion_matrix(y_test_arr,yhat)
t2=time.time()
print(" time for knn :: ", (t2-t1)/60 , " minutes")


#xgboost
from xgboost import XGBClassifier
t1=time.time()
xgb=XGBClassifier()
model_xgb=xgb.fit(X_train, y_train)
yhat=model_xgb.predict(X_test)
print("xgb accuracy is : ", accuracy_score(y_test, yhat))
calculate_confusion_matrix(y_test_arr,yhat)
t2=time.time()
print(" time for xgb :: ", (t2-t1)/60 , " minutes")

#randomforest
from sklearn.ensemble import RandomForestClassifier
t1=time.time()
randromforest=RandomForestClassifier()
model_randromforest=randromforest.fit(X_train, y_train)
yhat=model_randromforest.predict(X_test)
print("randromforest accuracy is : ", accuracy_score(y_test, yhat))
calculate_confusion_matrix(y_test_arr,yhat)
t2=time.time()
print(" time for randromforest :: ", (t2-t1)/60 , " minutes")


#for i in count:
#for i in range(1,len(X_train.columns)+1):
    #knn=KNeighborsClassifier(n_neighbors=i)
    #model_knn=knn.fit(X_train,y_train)
    #yhat=model_knn.predict(X_test)
    #print("for " , i,  " as K, accuracy is : ", accuracy_score(y_test, yhat))
#t2=time.time()
#print(" time for ", i ," k's :: ", (t2-t1)/60 , " minutes")

#calculate_confusion_matrix(y_test_arr,yhat)



