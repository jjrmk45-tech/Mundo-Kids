from django.db import models


class Brinquedo(models.Model):
    CATEGORIA_MENINOS = 'meninos'
    CATEGORIA_MENINAS = 'meninas'
    CATEGORIA_BEBES = 'bebes'
    CATEGORIA_EDUCACAO = 'educacao'
    CATEGORIA_JOGOS = 'jogos'
    CATEGORIA_AR_LIVRE = 'ao_ar_livre'
    CATEGORIA_CRIATIVOS = 'criativos'

    CATEGORIAS = [
        (CATEGORIA_MENINOS, 'Meninos'),
        (CATEGORIA_MENINAS, 'Meninas'),
        (CATEGORIA_BEBES, 'Bebês'),
        (CATEGORIA_EDUCACAO, 'Educação'),
        (CATEGORIA_JOGOS, 'Jogos'),
        (CATEGORIA_AR_LIVRE, 'Ao ar livre'),
        (CATEGORIA_CRIATIVOS, 'Criativos'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    faixa_etaria = models.CharField(max_length=50, default='')
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default=CATEGORIA_CRIATIVOS,
    )
    imagem = models.CharField(
        max_length=100,
        blank=True,
        help_text='Caminho relativo em static/images, por exemplo: robo-roxo.png',
    )

    def __str__(self):
        return self.nome