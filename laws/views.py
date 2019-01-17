from django.shortcuts import render
from .models import LawFile
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def leis(request):
    law_list = LawFile.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(law_list, 10)
    try:
        laws = paginator.page(page)
    except PageNotAnInteger:
        laws = paginator.page(1)
    except EmptyPage:
        laws = paginator.page(paginator.num_pages)
    return render(request, 'laws/leis.html', {'laws': laws})


def decretos(request):
    law_list = LawFile.objects.filter(type_law='Decreto')
    page = request.GET.get('page', 1)
    paginator = Paginator(law_list, 10)
    try:
        laws = paginator.page(page)
    except PageNotAnInteger:
        laws = paginator.page(1)
    except EmptyPage:
        laws = paginator.page(paginator.num_pages)
    return render(request, 'laws/leis.html', {'laws': laws})


def complementar(request):
    law_list = LawFile.objects.filter(type_law='Complementar')
    page = request.GET.get('page', 1)
    paginator = Paginator(law_list, 10)
    try:
        laws = paginator.page(page)
    except PageNotAnInteger:
        laws = paginator.page(1)
    except EmptyPage:
        laws = paginator.page(paginator.num_pages)
    return render(request, 'laws/leis.html', {'laws': laws})


def ordinaria(request):
    law_list = LawFile.objects.filter(type_law='Ordinaria')
    page = request.GET.get('page', 1)
    paginator = Paginator(law_list, 10)
    try:
        laws = paginator.page(page)
    except PageNotAnInteger:
        laws = paginator.page(1)
    except EmptyPage:
        laws = paginator.page(paginator.num_pages)
    return render(request, 'laws/leis.html', {'laws': laws})


def organica(request):
    law_list = LawFile.objects.filter(type_law='Organica')
    page = request.GET.get('page', 1)
    paginator = Paginator(law_list, 10)
    try:
        laws = paginator.page(page)
    except PageNotAnInteger:
        laws = paginator.page(1)
    except EmptyPage:
        laws = paginator.page(paginator.num_pages)
    return render(request, 'laws/leis.html', {'laws': laws})


def pesqlei(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = LawFile.objects.annotate(
                search=SearchVector('desc_law'),
            ).filter(search=query)
    return render(request, 'laws/pesquisa.html', {'form': form, 'query': query, 'results': results})
