from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)

app_name = 'votacao'

urlpatterns = [ path("", views.index, name="index"),
                path("<int:questao_id>", views.detalhe, name="detalhe"),
                path("<int:questao_id>", views.resultados, name="resultados"),]
                path("<int:questao_id>", views.voto, name="voto"),