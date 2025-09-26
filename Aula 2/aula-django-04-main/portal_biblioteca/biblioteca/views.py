from django.http import HttpResponse
from django.template import loader
from .models import Livro
from .models import TCC
from .models import QuantitativoMateriais

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def livros(request):
    livros = Livro.objects.all().values()
    template = loader.get_template('livros.html')
    context = {
        'livros': livros,
    }
    return HttpResponse(template.render(context, request))

def tccs(request):
    tccs = TCC.objects.all().values()
    template = loader.get_template('tccs.html')
    context = {
        'tccs': tccs,
    }
    return HttpResponse(template.render(context, request))

def tcc_detalhes(request, id):
    tcc = TCC.objects.get(id=id)
    template = loader.get_template('tcc_detalhes.html')
    context = {
        'tcc': tcc,
    }
    return HttpResponse(template.render(context, request))

def dashboard(request):
    qtd = QuantitativoMateriais.objects.all().values()
    template = loader.get_template('dashboard.html')
    v = qtd[0]
    context = {
        'labels': ['Livros', 'TCCs', 'Dissertações', 'Teses', 'Apostilas', 'Jornais'],
        'data': [v['livros'], v['tccs'], v['dissertacoes'], v['teses'], v['apostilas'], v['jornais']]
    }
    return HttpResponse(template.render(context, request))

