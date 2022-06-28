
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
dict=unpickle("C:\\Users\\WIN10\\Documents\\שיעורי בית ועבודות הכל המקצועות\\bootcamp\\שיעורים באפלייד\\cifar-10-batches-py\\data_batch_1")
import pandas as pd
import numpy as np
import glob, os
df=pd.DataFrame()
os.chdir("C:\\Users\\WIN10\\Documents\\שיעורי בית ועבודות הכל המקצועות\\bootcamp\\שיעורים באפלייד\\cifar-10-batches-py\\")
for file in glob.glob("*"):
    d=file
    df.append(file)
print("jj")