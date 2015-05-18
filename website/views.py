from django.shortcuts import render
from django.template.response import TemplateResponse
from website.models import *


# Create your views here.

def index(request):
	slider_list = Slider.objects.filter(active = '1').order_by('id')
	context = {'slider_list': slider_list}
	return render(request, 'index.html', context)


def chisiamo(request):
	imgchisiamo = ImmaginiChiSiamo.objects.order_by('pub_date').first()
	context = {'imgchisiamo': imgchisiamo}
	return render(request, 'chisiamo.html', context)

def ilte(request):
	return TemplateResponse(request, 'ilte.html')


def classificazionete(request):
	return TemplateResponse(request, 'classificazionete.html')


def ipaesidelte(request):
	return TemplateResponse(request, 'ipaesidelte.html')

def inostrite(request):
	categorie_te = CategorieTe.objects.order_by('id')
	inostri_te = UnnostroTe.objects.order_by('id')
	context = {'categorie_te': categorie_te,
			   'inostri_te': inostri_te}

	return render(request, 'inostrite.html', context)


def categoriate(request):
	return TemplateResponse(request, 'categoriate.html')

def unnostrote(request):
	return TemplateResponse(request, 'unnostrote.html')


def ritodelte(request):
	return TemplateResponse(request, 'ritodelte.html')


def dovesiamo(request):
	return TemplateResponse(request, 'dovesiamo.html')


def contatti(request):
	return TemplateResponse(request, 'contatti.html')

