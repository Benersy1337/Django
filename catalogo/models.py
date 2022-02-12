from statistics import mode
from django.db import models

# Create your models here.

class Genero(models.Model):

    nome = models.CharField(max_length=200, help_text='Entre com um genero de livro. Ex: Ficção cientifica')

    def __str__(self):
        return self.nome


class Linguagem (models.Model):

    nome = models.CharField(max_length=200, help_text="Entre com a linguagem do livro, ex: Inglês, Francês, japonês")



class Autor(models.Model):

    primeiro_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    data_falecimento = models.DateField(null=True, blank=True)
    

    class Meta:
        ordering = ['ultimo_nome' , 'primeiro_nome']


    def __str__(self):
        return f'{self.ultimo_nome} , {self.primeiro_nome}'




class Livro(models.Model):

    titulo = models.CharField(max_length=200)
    # Se o autor for deletado, ele vai ser setado como NULL
    # Relacionamento 1,n utilizar ForeignKey
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    resumo = models.TextField(max_length=1000, help_text='Entre com uma breve descrição do livro')
    isbn = models.CharField('ISBN', max_length=13)
    genero = models.ManyToManyField(Genero, help_text='Selecione um ou mais generos para este livro')
    linguagem = models.ForeignKey(Linguagem, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.titulo


import uuid


class ExemplarLivro(models.Model):

    # UUID gera um id aleatório por exemplo 8cbf0712-1993-472a-8605-d887dd4c7138
    # Cada livro vai ter uma identificação unica um id unico
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identificador unico para este exemplar')
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    editora = models.CharField(max_length=200)
    data_devolucao = models.DateField(null=True, blank=True)


    SITUACAO_EXEMPLAR = (
        ('m', 'Manutenção'),
        ('e', 'Emprestado'),
        ('d', 'Disponível'),
        ('r', 'Reservado'),
    )


    situacao = models.CharField(
        max_length=1,
        choices=SITUACAO_EXEMPLAR,
        blank=True,
        default='m',
        help_text='Situação do exemplar',
    )


    # Quando solicitar todos os exemplares, vao ser pela ordem das datas de devoluções
    class Meta:
        ordering = ['data_devolucao']

    
    def __str__(self):
        return f'{self.id} ({self.livro.titulo})'



