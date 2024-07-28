from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Nao comer carne por um mes",
    "february": "Correr 3 vezes na semana",
    "march": "Ler um livro",
    "april": "Meditar todos os dias",
    "may": "Aprender uma nova habilidade",
    "june": "Fazer trabalho voluntario",
    "july": "Evitar redes sociais",
    "august": "Beber 2 litros de agua por dia",
    "september": "Escrever um diario",
    "october": "Fazer uma caminhada diaria",
    "november": "Aprender a cozinhar uma nova receita",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", { "months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('mes invalido')
    redirect_month = months[month - 1]
    redirect_url = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", { "month_name": month.capitalize(), "challenge_text" : challenge_text })
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
