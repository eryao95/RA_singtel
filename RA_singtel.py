import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

data = pd.read_csv(r"C:\Users\lite0\OneDrive\Desktop\Re__Application_for_RA_position_with_NUS-Singtel_Cybersecurity_Lab\dataset.csv")

TYPE = data.Type

FEATURES = data.drop(["Type", "URL", "WHOIS_REGDATE", "WHOIS_UPDATED_DATE", "CHARSET", "SERVER", "WHOIS_COUNTRY", "WHOIS_STATEPRO",
                   "CONTENT_LENGTH", "URL_LENGTH", "NUMBER_SPECIAL_CHARACTERS", "SOURCE_APP_PACKETS"], axis = 1)

from sklearn import tree

x_train,x_test,y_train,y_test = train_test_split(FEATURES,TYPE,test_size=0.01,random_state=1)
x_train['DNS_QUERY_TIMES'] = x_train['DNS_QUERY_TIMES'].fillna(0)
Tree = tree.DecisionTreeClassifier()
Tree.fit(x_train, y_train)

scores = cross_val_score(Tree, x_train, y_train, cv = 10)
print("DecisionTree: ")
print(scores)
print(Tree.score(x_test, y_test))