data = []

def plot(x, y, format=None, label=None, lw=None):
    d = {
        "data": zip(x, y),
        }
    if label:
        d["label"] = label
    data.append(d)

def show():
    from plotserver.runserver import main
    main()

def grid(*args, **kwargs):
    pass

def legend(*args, **kwargs):
    pass
