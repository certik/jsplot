from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response("index.html",
        context_instance=RequestContext(request)
        )

def raphael(request):
    return render_to_response("raphael.html",
        context_instance=RequestContext(request)
        )

def flotr(request):
    return render_to_response("flotr.html",
        context_instance=RequestContext(request)
        )
