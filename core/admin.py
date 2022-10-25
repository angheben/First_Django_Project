from django.contrib import admin
from .models import Produto, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    pass


class ClienteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

