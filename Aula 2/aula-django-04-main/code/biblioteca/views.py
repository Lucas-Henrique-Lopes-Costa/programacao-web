from django.http import HttpResponse
from django.template import loader
from .models import Livro
from .models import TCC
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required


def principal(request):
    template = loader.get_template("principal.html")
    return HttpResponse(template.render({}, request))


def livros(request):  # atualize esta função
    livros = Livro.objects.all().values()
    context = {"livros": livros}
    template = loader.get_template("livros.html")
    return HttpResponse(template.render(context, request))


def tccs(request):  # atualize esta função
    tccs = TCC.objects.all().values()
    context = {
        "tccs": tccs,
    }
    template = loader.get_template("tccs.html")
    return HttpResponse(template.render(context, request))


def tcc_detalhes(request, id):  # atualize esta função
    tcc = TCC.objects.get(id=id)
    context = {
        "tcc": tcc,
    }
    template = loader.get_template("tcc_detalhes.html")
    return HttpResponse(template.render(context, request))


def dashboard(request):
    qtdLivros = Livro.objects.count()
    qtdTCCs = TCC.objects.count()
    context = {"labels": ["Livros", "TCCs"], "data": [qtdLivros, qtdTCCs]}
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render(context, request))


def logout(request):
    logout_django(request)
    return render(request, "login.html")


def dashboard(request):
    if request.user.is_authenticated:
        qtdLivros = Livro.objects.count()
        qtdTCCs = TCC.objects.count()
        context = {"labels": ["Livros", "TCCs"], "data": [qtdLivros, qtdTCCs]}
        template = loader.get_template("dashboard.html")
        return HttpResponse(template.render(context, request))
    return HttpResponse("Você precisa estar logado!")


@login_required(login_url="/auth/login")
def dashboard(request):
    qtdLivros = Livro.objects.count()
    qtdTCCs = TCC.objects.count()
    context = {"labels": ["Livros", "TCCs"], "data": [qtdLivros, qtdTCCs]}
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render(context, request))
