from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from newshackathon.dataloading.data_constructor import construct_data_set


def split_data(data_array):
    x = data_array[:, :-1]
    y = data_array[:, -1]
    return train_test_split(x, y, train_size=0.8, random_state=42)


def train_gnb():
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    return accuracy_score(Y_test, gnb.predict(X_test))


def train_forest():
    rf = RandomForestClassifier(max_features=200, max_depth=300)
    rf.fit(X_train, Y_train)
    return accuracy_score(Y_test, rf.predict(X_test))


def train_svc_poly():
    svc_poly = SVC(kernel="poly").fit(X_train, Y_train)
    return svc_poly.score(X_test, Y_test)


def train_svc_linear():
    svc_linear = SVC(kernel="linear").fit(X_train, Y_train)
    return svc_linear.score(X_test, Y_test)


def train_svc_rbf():
    svc_rbf = SVC(kernel="rbf").fit(X_train, Y_train)
    return svc_rbf.score(X_test, Y_test)

data = construct_data_set()

X_train, X_test, Y_train, Y_test = split_data(data)

train_svc_linear()
