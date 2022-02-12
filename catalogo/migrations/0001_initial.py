# Generated by Django 4.0 on 2022-02-11 22:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=100)),
                ('ultimo_nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('data_falecimento', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['ultimo_nome', 'primeiro_nome'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Entre com um genero de livro. Ex: Ficção cientifica', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Entre com a linguagem do livro, ex: Inglês, Francês, japonês', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resumo', models.TextField(help_text='Entre com uma breve descrição do livro', max_length=1000)),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.autor')),
                ('genero', models.ManyToManyField(help_text='Selecione um ou mais generos para este livro', to='catalogo.Genero')),
                ('linguagem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.linguagem')),
            ],
        ),
        migrations.CreateModel(
            name='ExemplarLivro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador unico para este exemplar', primary_key=True, serialize=False)),
                ('editora', models.CharField(max_length=200)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('situacao', models.CharField(blank=True, choices=[('m', 'Manutenção'), ('e', 'Emprestado'), ('d', 'Disponível'), ('r', 'Reservado')], default='m', help_text='Situação do exemplar', max_length=1)),
                ('livro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.livro')),
            ],
            options={
                'ordering': ['data_devolucao'],
            },
        ),
    ]
