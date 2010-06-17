data = []

def plot(x, y, label=None):
    d = {
        "data": zip(x, y),
        }
    if label:
        d["label"] = label
    data.append(d)

def show():
    from plotserver.runserver import main
    main()
