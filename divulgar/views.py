from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pet, Tag, Raca
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def novo_pet(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})
    elif request.method == "POST":
        pet = Pet()
        pet.usuario = request.user
        pet.foto = request.FILES['foto']
        pet.nome = request.POST['nome']
        pet.descricao = request.POST['descricao']
        pet.estado = request.POST['estado']
        pet.cidade = request.POST['cidade']
        pet.telefone = request.POST['telefone']
        pet.raca = Raca.objects.get(id=request.POST['raca'])
        pet.status = 'P'
        pet.save()
        for tag_id in request.POST.getlist('tags'):
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)
        messages.add_message(request, messages.SUCCESS, 'Pet cadastrado com sucesso')

        tags = Tag.objects.all()
        racas = Raca.objects.all()
        return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})

@login_required
def seus_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(usuario=request.user)
        return render(request, 'seus_pets.html', {'pets': pets})

@login_required
def remover_pet(request, id):
    pet = Pet.objects.get(id=id)
    if request.user != pet.usuario:
        messages.add_message(request, messages.ERROR, 'Você não pode remover este pet')
        return redirect('/divulgar/seus_pets')
    pet.delete()
    messages.add_message(request, messages.SUCCESS, 'Pet removido com sucesso')
    return redirect('/divulgar/seus_pets')