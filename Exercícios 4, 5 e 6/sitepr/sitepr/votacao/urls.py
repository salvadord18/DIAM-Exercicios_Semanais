from django.urls import include, path
from . import views
from django.utils import timezone
import datetime
# (. significa que importa views da mesma directoria)

app_name = 'votacao'

urlpatterns = [ path("", views.index, name="index"),
                path("<int:questao_id>", views.detalhe, name="detalhe"),
                path("<int:questao_id>/resultados", views.resultados, name="resultados"),
                path("<int:questao_id>/voto", views.voto, name="voto"),
                path("criarquestao", views.criarquestao, name="criarquestao"),
                path("registar", views.registar, name="registar"),
                path("profile", views.profile, name="profile"),
                path("<gravarquestao>", views.gravarquestao, name="gravarquestao"),
                path("<int:questao_id>/novaopcao", views.novaopcao, name="novaopcao"),
                path("<int:questao_id>/gravaropcao", views.gravaropcao, name="gravaropcao"),

                ]

