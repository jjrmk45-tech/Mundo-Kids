from django.test import TestCase
from django.urls import reverse

from .models import Brinquedo


class CatalogoBrinquedosTests(TestCase):
    def setUp(self):
        self.brinquedo = Brinquedo.objects.create(
            nome='Carrinho Veloz',
            descricao='Carrinho com controle remoto',
            preco='89.90',
            estoque=5,
            faixa_etaria='A partir de 9 anos',
            categoria=Brinquedo.CATEGORIA_MENINOS,
            imagem='carro-controle-remoto.png',
        )

    def test_pagina_inicial_exibe_brinquedos_do_banco_em_cartoes(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.brinquedo.nome)
        self.assertContains(response, 'R$ 89,90')
        self.assertContains(response, 'carro-controle-remoto.png')
        self.assertContains(response, 'Ver brinquedo')
        self.assertContains(response, reverse('catalogo'))

    def test_busca_na_pagina_inicial_filtra_brinquedos(self):
        response = self.client.get(reverse('index'), {'q': 'carrinho veloz'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.brinquedo.nome)
        self.assertContains(response, 'Resultados para "carrinho veloz"')
        self.assertNotContains(response, 'Carrinho de Controle Remoto')

    def test_filtro_de_categoria_na_pagina_inicial(self):
        Brinquedo.objects.create(
            nome='Jogo de memória',
            preco='29.90',
            estoque=3,
            categoria=Brinquedo.CATEGORIA_JOGOS,
        )

        response = self.client.get(
            reverse('index'),
            {'categoria': Brinquedo.CATEGORIA_MENINOS},
        )

        self.assertContains(response, self.brinquedo.nome)
        self.assertNotContains(response, 'Jogo de memória')

    def test_busca_filtra_nome_sem_distinguir_maiusculas(self):
        response = self.client.get(reverse('catalogo'), {'q': 'cARRINHO vELOZ'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.brinquedo.nome)
        self.assertNotContains(response, 'Carrinho de Controle Remoto')
        self.assertContains(response, 'Resultados para "cARRINHO vELOZ"')

    def test_busca_encontra_descricao_e_faixa_etaria(self):
        por_descricao = self.client.get(reverse('catalogo'), {'q': 'controle remoto'})
        por_faixa_etaria = self.client.get(reverse('catalogo'), {'q': '9 anos'})

        self.assertContains(por_descricao, self.brinquedo.nome)
        self.assertContains(por_faixa_etaria, self.brinquedo.nome)

    def test_busca_sem_resultados_exibe_mensagem(self):
        response = self.client.get(reverse('catalogo'), {'q': 'inexistente'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Não encontramos brinquedos com esses filtros.')
        self.assertContains(response, '0 brinquedo(s) encontrado(s).')

    def test_catalogo_lista_brinquedos_sem_busca(self):
        response = self.client.get(reverse('catalogo'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.brinquedo.nome)
        self.assertContains(response, 'A partir de 9 anos')
        self.assertContains(response, 'R$ 89,90')

    def test_detalhe_exibe_brinquedo(self):
        brinquedo = Brinquedo.objects.get(nome='Carrinho de Controle Remoto')

        response = self.client.get(reverse('detalhe', args=[brinquedo.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, brinquedo.nome)
        self.assertContains(response, brinquedo.faixa_etaria)

    def test_detalhe_inexistente_retorna_404(self):
        response = self.client.get(reverse('detalhe', args=[9999]))

        self.assertEqual(response.status_code, 404)
