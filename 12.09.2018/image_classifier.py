import numpy as np
from PIL import Image
import time
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize 

x_train = [];
x_test = [];
y_train = [];
y_test = [];
y_pred = [];

def reshape(mat):
    matsize = len(mat)*len(mat[0])*len(mat[0][0]);
    new_mat = np.reshape(mat, matsize);
    return new_mat;
    
def open_images(file_path, x, y, f_size):
    for i in range(1, f_size+1):
        img = Image.open(file_path+'/'+str(i)+'.jpg');
        mat = np.array(img);
        #print(len(mat[0]), len(mat[0][0]));
        new_mat = reshape(mat);
        #print(np.shape(new_mat));
        x.append(new_mat);
        if f_size == 20:
            y.append((i+1)//2);
        else:
            y.append(i);
        #print(y);

def test_dataset(mlp, x_test, y_test):
    y_pred = mlp.predict(x_test);
    file_path = "TestDataset";
    print("Predicted classes:");
    images = [];
    for pred in y_pred:
        #img = mpimg.imread(file_path+'/'+str(pred)+'.jpg');
        img = Image.open(file_path+'/'+str(pred)+'.jpg');
        images.append(img);
        
    for i in range(len(images)):
        img = images[i];
        pred = y_pred[i];
        print("Class "+str(pred)+":");
        plt.imshow(img);
        plt.show();
        time.sleep(0.01);
        
    acc = accuracy_score(y_test, y_pred, normalize=False)/len(y_test);
    print("Test accuracy: ", acc);
    return y_pred;
    
def train_dataset(x_train, y_train):
    maxacc = 0.0;
    res = None;
    for i in range(0, 10):
        activation = 'logistic';
        #nepoch = 200;
        #mlp = MLPClassifier(solver='lbfgs', alpha=0.0001, activation=activation, hidden_layer_sizes=(5, 5), max_iter=nepoch, random_state=None);
        mlp = MLPClassifier(solver='lbfgs', alpha=0.0001, activation=activation, hidden_layer_sizes=(5, 5), random_state=None);
        mlp.fit(x_train, y_train);
        y_t_pred = mlp.predict(x_train);
        acc = accuracy_score(y_train, y_t_pred, normalize=False)/len(y_train);
        if acc>maxacc:
            res = mlp;
            maxacc=acc;
        print("Training accuracy: ", acc);
        #y_pred = test_dataset(mlp, x_test, y_test);
        #print(y_pred);
    print(maxacc);
    return res;

def normalize_fun(x):
    normalized_x = normalize(x, axis=0);
    return normalized_x;
    
#input processing
ip1 = "F:/115cs0237/Fwd todays assignment/12sept18/TrainDataset";
open_images(ip1, x_train, y_train, 20);
x_train = normalize_fun(x_train);
print(y_train);
ip2 = "F:/115cs0237/Fwd todays assignment/12sept18//TestDataset";
open_images(ip2, x_test, y_test, 10);
x_test = normalize_fun(x_test);
print(y_test);
mlp = train_dataset(x_train, y_train);
y_pred = test_dataset(mlp, x_test, y_test);
#print(x_train);
print(y_pred);