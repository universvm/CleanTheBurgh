from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from newshackathon.dataloading.data_constructor import DataConstructor


def split_data(data_array):
    x = data_array[:, :-1]
    y = data_array[:, -1]
    return train_test_split(x, y, train_size=0.8, random_state=42)


def train_gnb():
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    return accuracy_score(Y_test, gnb.predict(X_test)), accuracy_score(Y_train, gnb.predict(X_train))


def train_forest():
    rf = RandomForestClassifier(max_features=100, max_depth=100)
    rf.fit(X_train, Y_train)
    return accuracy_score(Y_test, rf.predict(X_test)), accuracy_score(Y_train, rf.predict(X_train))


def train_svc_poly():
    svc_poly = SVC(kernel="poly")
    svc_poly.fit(X_train, Y_train)
    return accuracy_score(Y_test, svc_poly.predict(X_test)), accuracy_score(Y_train, svc_poly.predict(X_train))


def train_svc_linear():
    svc_linear = SVC(kernel="linear")
    svc_linear.fit(X_train, Y_train)
    return accuracy_score(Y_test, svc_linear.predict(X_test)), accuracy_score(Y_train, svc_linear.predict(X_train))


def train_svc_rbf():
    svc_rbf = SVC(kernel="rbf")
    svc_rbf.fit(X_train, Y_train)
    return accuracy_score(Y_test, svc_rbf.predict(X_test)), accuracy_score(Y_train, svc_rbf.predict(X_train))

data_constructor = DataConstructor()
trainset = data_constructor.get_trainset()
print('dataset size: {}'.format(len(trainset)))

X_train, X_test, Y_train, Y_test = split_data(trainset)

print('Gaussian NB accuracy (test, train): ' + str(train_gnb()))
print('Random Forest accuracy (test, train): ' + str(train_forest()))
print('SVM Polly accuracy (test, train): ' + str(train_svc_poly()))
print('SVM Linear accuracy (test, train): ' + str(train_svc_linear()))
print('SVM RBF accuracy (test, train): ' + str(train_svc_rbf()))
