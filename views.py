# Create your views here.
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from meta_gen import meta_keywords, meta_description

this_template = "index.html"

def index(request):
	return render_to_response(this_template, {'keys' : meta_keywords(render_to_string(this_template)),
	'description' : meta_description(render_to_string(this_template)) })