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
                path("<int:questao_id>/view_questao_otimizada", views.view_questao_otimizada, name="view_questao_otimizada"),
                path("registar", views.registar, name="registar"),
                path("logoutview", views.logoutview, name="logoutview"),
                path("iniciarsessao", views.iniciarsessao, name="iniciarsessao"),
                path("perfil", views.perfil, name="perfil"),
                path("<int:questao_id>/view_opcao_otimizada", views.view_opcao_otimizada, name="view_opcao_otimizada"),
                path("<int:questao_id>/apagarquestao", views.apagarquestao, name="apagarquestao"),
                path("<int:questao_id>/apagaropcao", views.apagaropcao, name="apagaropcao"),
                path("fazer_upload", views.fazer_upload, name="fazer_upload"),
                ]

