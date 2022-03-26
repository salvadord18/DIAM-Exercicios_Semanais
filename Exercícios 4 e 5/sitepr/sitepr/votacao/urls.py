from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)

app_name = 'votacao'

urlpatterns = [ path("", views.index, name="index"),
                path("<int:questao_id>", views.detalhe, name="detalhe"),
                path("<int:questao_id>/resultados", views.resultados, name="resultados"),
                path("<int:questao_id>/voto", views.voto, name="voto"),
                path("criarquestao", views.criarquestao, name="criarquestao"),
                path("submeter_questao", views.submeter_questao, name="submeter_questao"),]