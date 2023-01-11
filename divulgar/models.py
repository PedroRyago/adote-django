from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Raca(models.Model):
    raca = models.CharField(max_length=50)

    def __str__(self):
        return self.raca

    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Pet(models.Model):
    choices_status = (('P', 'Para adoção'),
                      ('A', 'Adotado'))
    
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="fotos_pets")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default='P')
    
    def __str__(self):
        return f'{self.nome} - {self.raca} - {self.usuario}'

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'