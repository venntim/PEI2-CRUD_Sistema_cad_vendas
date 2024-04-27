from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vendas

def adicionar_vendas(request):
    if request.method == "GET":
        return render(request, "adicionar_vendas.html")
    elif request.method == "POST":
        nome_cliente = request.POST.get('nome_cliente')
        cpf_cliente = request.POST.get('cpf')
        telefone_cliente = request.POST.get('telefone')
        nome_produto = request.POST.get('nome_produto')
        preco_produto = request.POST.get('preco_produto')
        situação_produto = request.POST.get('situacao')
        observacao = request.POST.get('observacao')

        dados_vendas = Vendas(
            nome_cliente = nome_cliente,
            cpf_cliente = cpf_cliente,
            telefone_cliente = telefone_cliente,
            nome_produto = nome_produto,
            preco_produto = preco_produto,
            situação_produto = situação_produto,
            observacao = observacao,
        )
       
        dados_vendas.save()

    return redirect("/vendas/adicionar")


def listar_vendas(request):
    if request.method == "GET":
        return render(request, "listar_vendas.html")