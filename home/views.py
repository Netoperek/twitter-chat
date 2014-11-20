from django.shortcuts import render, render_to_response, RequestContext

def home(request):
    return render_to_response("home.html",
                                locals(),
                                context_instance=RequestContext(request))
