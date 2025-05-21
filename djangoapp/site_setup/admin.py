from django.contrib import admin
from site_setup.models import MenuLink

# Register your models here.
@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path'
    list_display_links = 'id', 'text', 'url_or_path' # Local onde podemos adicionar link para acessar as informação da postagem
    search_fields = 'id', 'text', 'url_or_path' # Forma de pesquisa