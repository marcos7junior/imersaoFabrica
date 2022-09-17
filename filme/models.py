from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.categoria
    
class Titulo(models.Model):
    nome = models.CharField(max_length=100)
    classificacao = models.IntegerField(null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
    