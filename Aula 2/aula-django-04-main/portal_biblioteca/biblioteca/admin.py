from django.contrib import admin
from .models import Livro
from .models import TCC
from .models import QuantitativoMateriais

class LivroAdmin(admin.ModelAdmin):
    list_display = ("nome", "autor", "ano")

class TCCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "orientador", "ano")

class QuantitativoMateriaisAdmin(admin.ModelAdmin):
    list_display = ("id", "livros", "tccs", "dissertacoes", "teses", "apostilas", "jornais")

admin.site.register(Livro, LivroAdmin)
admin.site.register(TCC, TCCAdmin)
admin.site.register(QuantitativoMateriais, QuantitativoMateriaisAdmin)