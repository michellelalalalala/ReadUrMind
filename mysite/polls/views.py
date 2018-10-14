# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import Template, Context, loader

# Create your views here.
from django.http import HttpResponse


def index(request):
	fp = open("polls/index.html")
	template = Template(fp.read())
	fp.close()
	return HttpResponse(template.render(Context({})))

def upload_file(request):
    if request.method == 'POST':
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
        # return HttpResponseRedirect('polls/success/')
        fp = open("polls/index.html")
		template = Template(fp.read())
		fp.close()
		return HttpResponse(template.render(Context({})))
    else:
    	return index(request)
    	# print("FUCK")
    # else:
    #     form = UploadFileForm()
    # return render(request, 'upload.html', {'form': form})