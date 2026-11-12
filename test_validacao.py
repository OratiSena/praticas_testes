from validacao import email_valido


def test_email_correto_e_aceito():
    resultado = email_valido("ana@senac.br")
    assert resultado is True


def test_email_sem_arroba_e_rejeitado():
    resultado = email_valido("anasenac.br")
    assert resultado is False


def test_email_vazio_e_rejeitado():
    resultado = email_valido("")
    assert resultado is False
