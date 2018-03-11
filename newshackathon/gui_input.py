from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from newshackathon.dataloading.data_constructor import construct_data_set
from tkinter import *
from PIL import ImageTk, Image
from newshackathon.dataloading.webscraper import scrap_data


def split_data(data_array):
    x = data_array[:, :-1]
    y = data_array[:, -1]
    return x,y


def train_gnb():
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    return accuracy_score(Y_test, gnb.predict(X_test)), accuracy_score(Y_train, gnb.predict(X_train))


def train_forest():
    rf = RandomForestClassifier(max_features=200, max_depth=300)
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


def train_svc_rbf(stringfrominput):
    svc_rbf = SVC(kernel="rbf")
    svc_rbf.fit(X_train, Y_train)
    return accuracy_score(Y_test, svc_rbf.predict(X_test)), accuracy_score(Y_train, svc_rbf.predict(X_train))


def printer(string):
    string = string + 'HELLO'

    text.insert(INSERT, string)


def get_gui_input():
    global e
    text.delete('1.0', END)
    url_domain = e.get()

    domain, title, body = scrap_data(url_domain)

    # text.insert(INSERT, string)


def draw_gui():
    window = Tk()

    window.title('CleanTheBurgh')
    window.geometry("300x450")
    window.configure()
    path = "logo.png"

    img = ImageTk.PhotoImage(Image.open(path))

    panel = Label(window, image=img)

    panel.pack(side="top")

    global text
    global e

    text = Text(window, width=20, height=7)
    e = Entry(window)
    e.pack()
    e.focus_set()

    b = Button(window, text='Clean!', command=get_gui_input)

    text.pack(side='top')

    b.pack(side='bottom')
    window.mainloop()

data = construct_data_set()
print('dataset size: {}'.format(len(data)))

X_train, Y_train = split_data(data)



print('Gaussian NB accuracy (test, train): ' + str(train_forest()))
print('Random Forest accuracy (test, train): ' + str(train_forest()))
print('SVM Polly accuracy (test, train): ' + str(train_svc_poly()))
print('SVM Linear accuracy (test, train): ' + str(train_svc_linear()))
print('SVM RBF accuracy (test, train): ' + str(train_svc_rbf()))
