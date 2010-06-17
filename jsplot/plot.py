from numpy import array, concatenate

data = []

def plot(x, y, label=None):
    d = {
        "data": zip(x, y),
        }
    if label:
        d["label"] = label
    data.append(d)

def show():
    print data
