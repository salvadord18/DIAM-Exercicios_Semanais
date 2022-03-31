from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Questao, Opcao, Aluno

def index(request):
    latest_question_list = Questao.objects.all()
    return render(request, 'votacao/index.html', {'latest_question_list': latest_question_list})

def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})

def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
    # Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html', {'questao': questao, 'error_message': "Não escolheu uma opção",})
    else:
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
 # Retorne sempre HttpResponseRedirect depois de
 # tratar os dados POST de um form
 # pois isso impede os dados de serem tratados
 # repetidamente se o utilizador
 # voltar para a página web anterior.
        return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))

def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})

def criarquestao(request):
    return render(request, 'votacao/criarquestao.html')

def gravarquestao(request):
    questao_texto = request.POST['questao']
    pub_data = timezone.now()
    q = Questao(questao_texto=questao_texto, pub_data=pub_data)
    q.save()
    return HttpResponseRedirect(reverse('votacao:index'))

def novaopcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/novaopcao.html', {'questao': questao})

def gravaropcao(request, questao_id):
    questao = Questao.objects.get(pk=questao_id)
    questao.opcao_set.create(opcao_texto=request.POST['opcao'], votos=0)
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))

def apagarquestao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.delete()
    return HttpResponseRedirect(reverse('votacao:index'))

def removeropcao(request, questao_id):
    #opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    #del opcao_seleccionada
    print("fgrr")

def registar(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        course = request.POST['course']
        u = User.objects.create_user(username, password=password, email=email)
        a = Aluno(user=u, course=course)
        a.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'votacao/index.html')

        else:
            return render(request, 'votacao/registar.html')
    except MultiValueDictKeyError:
        return render(request, 'votacao/registar.html')

def profile(request):
    return render(request, 'votacao/profile.html')

def logout(request):
    logout(request)
    return redirect('votacao/index.html')

def apagaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'votacao/detalhe.html', {'questao': questao, 'error_message': "Não escolheu uma opção",})
    else:
        opcao_seleccionada.delete()
        return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))




