from django.core import mail
from django.test.testcases import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
                    email='henrique@bastos.net', phone='21-99618-6180')
        self.client.post('/inscricao/', data)
        self.mail = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.mail.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.mail.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']

        self.assertEqual(expect, self.mail.to)

    def test_subscription_email_body(self):
        contents = [
            'Henrique Bastos',
            '12345678901',
            'henrique@bastos.net',
            'Henrique Bastos',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.mail.body)
