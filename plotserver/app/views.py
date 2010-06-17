from math import sin, pi

from django.shortcuts import render_to_response
from django.template import RequestContext

import json

def index(request):
    try:
        from jsplot.plot import data
        jsplot_import_ok = True
    except ImportError:
        jsplot_import_ok = False
    if jsplot_import_ok and data == []:
        jsplot_import_ok = False
    if not jsplot_import_ok:
        # use some demo data for debugging/testing purposes
        from numpy import arange, pi, sin
        x = arange(0, 3*pi, 0.1)
        y1 = sin(x)
        y2 = sin(x*sin(x))
        data = [
                {"data": zip(x, y1), "label": "sin(x)",
                                    "points": {"show": True}},
                {"data": zip(x, y2), "label": "sin(x*sin(x))"},
                ]
    graphs = json.dumps(data)
    return render_to_response("index.html", {
        "graphs": graphs,
        "show_import_warning": not jsplot_import_ok,
        }, context_instance=RequestContext(request))

def raphael(request):
    return render_to_response("raphael.html",
        context_instance=RequestContext(request)
        )

def flotr1(request):
    return render_to_response("flotr1.html",
        context_instance=RequestContext(request)
        )

def flotr2(request):
    x1 = 0
    x2 = 3*pi
    d = []
    for i in range(101):
        x = x1 + i * (x2 - x1) / 100.
        d.append([x, sin(x * sin(x))])
    graphs = json.dumps([
        {"data": ([0, 0], [2, -1], [3, 1]), "label": "data1"},
        {"data": ([0, 0], [5, -0.5]), "label": "data2"},
        {"data": d, "label": "sin(x*sin(x))"},
        ])
    return render_to_response("flotr2.html", {
        "graphs": graphs,
        }, context_instance=RequestContext(request))
