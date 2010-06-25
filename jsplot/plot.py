data = []

def plot(x, y, format=None, label=None, lw=None):
    d = {
        "data": zip(x, y),
        }
    if label:
        d["label"] = label
    if format:
        options = parse_format(format)
        d.update(options)
    data.append(d)

def parse_format(f):
    assert f is not None
    options = {}
    if len(f) == 2:
        colors = {
                "k": "#000000",
                "r": "#FF0000",
                "g": "#00FF00",
                }
        if f[0] not in colors:
            raise Exception("Unsupported color")
        options["color"] = colors[f[0]]
        if f[1] == "-":
            options["points"] = {"show": False}
            options["lines"] = {"show": True}
        elif f[1] == "o":
            options["points"] = {"show": True}
            options["lines"] = {"show": False}
    return options


def show():
    from plotserver.runserver import main
    main()

def grid(*args, **kwargs):
    pass

def legend(*args, **kwargs):
    pass
