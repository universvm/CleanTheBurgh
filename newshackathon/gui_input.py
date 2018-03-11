from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from newshackathon.dataloading.data_constructor import DataConstructor
from tkinter import *
from PIL import ImageTk, Image
from newshackathon.dataloading.webscraper import scrap_data
from newshackathon.bsdetector import bs_detect
import numpy as np


def split_data(data_array):
    x = data_array[:, :-1]
    y = data_array[:, -1]
    return x,y


def train_gnb():
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    # return accuracy_score(Y_test, gnb.predict(X_test)), accuracy_score(Y_train, gnb.predict(X_train))
    return gnb


def train_forest():
    rf = RandomForestClassifier(max_features=200, max_depth=300)
    rf.fit(X_train, Y_train)
    # return accuracy_score(Y_test, rf.predict(X_test)), accuracy_score(Y_train, rf.predict(X_train))
    return rf


def train_svc_poly():
    svc_poly = SVC(kernel="poly")
    svc_poly.fit(X_train, Y_train)
    # return accuracy_score(Y_test, svc_poly.predict(X_test)), accuracy_score(Y_train, svc_poly.predict(X_train))
    return svc_poly


def train_svc_linear():
    svc_linear = SVC(kernel="linear")
    svc_linear.fit(X_train, Y_train)
    # return accuracy_score(Y_test, svc_linear.predict(X_test)), accuracy_score(Y_train, svc_linear.predict(X_train))
    return svc_linear


def train_svc_rbf(stringfrominput):
    svc_rbf = SVC(kernel="rbf")
    svc_rbf.fit(X_train, Y_train)
    # return accuracy_score(Y_test, svc_rbf.predict(X_test)), accuracy_score(Y_train, svc_rbf.predict(X_train))
    return svc_rbf


def printer(string):
    string = string + 'HELLO'

    text.insert(INSERT, string)


def get_gui_input():
    # global e
    text.delete('1.0', END)
    url_domain = e.get()

    domain, title, body = scrap_data(url_domain)

    print(domain)

    domain_list = bs_detect.create_bs_dict()
    if domain in domain_list:
        result = 0
    else:
        X_test = data_constructor.calculate_feature_vector(body)
        print(X_test)

        X_test = np.array(X_test)
        print(X_test)
        X_test = X_test.reshape(1, -1)
        print('reshaped')
        print(X_test)

        result = forest_model.predict_proba(np.array(X_test))[0][0]

    text.insert(INSERT, "Clean probabilty:\n" + str(result*100)[0:5] + "%\n")


def draw_gui():
    window = Tk()

    window.title('CleanTheBurgh')
    window.geometry("300x450")
    window.configure()
    global path
    path = "logo.png"
    global img

    global panel
    image_logo = Image.open(path)
    image_logo = image_logo.resize((206,247))
    img = ImageTk.PhotoImage(image_logo)


    panel = Label(window, image=img)
    panel.configure(image=img)
    panel.image = img

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

data_constructor = DataConstructor()
trainset = data_constructor.get_trainset()
print('dataset size: {}'.format(len(trainset)))

X_train, Y_train = split_data(trainset)

forest_model = train_forest()

draw_gui()