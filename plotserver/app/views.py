from math import sin

from django.shortcuts import render_to_response
from django.template import RequestContext

import json

def index(request):
    x1 = 0
    x2 = 8
    d = []
    for i in range(100):
        x = x1 + i * (x2 - x1) / 100.
        d.append([x, sin(x * sin(x))])
    graphs = json.dumps([
        {"data": ([0, 0], [2, -1], [3, 1]), "label": "data1"},
        {"data": ([0, 0], [5, -0.5]), "label": "data2"},
        {"data": d, "label": "sin(x*sin(x))"},
        ])
    return render_to_response("index.html", {
        "graphs": graphs,
        }, context_instance=RequestContext(request))

def raphael(request):
    return render_to_response("raphael.html",
        context_instance=RequestContext(request)
        )

def flotr(request):
    return render_to_response("flotr.html",
        context_instance=RequestContext(request)
        )
