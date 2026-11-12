from validacao import email_valido

def test_email_correto_e_aceito():
    resultado = email_valido("ana@senac.br")
    assert resultado is True


def test_email_sem_arroba_e_rejeitado():
    assert False, "complete este teste"


def test_email_vazio_e_rejeitado():
    assert False, "complete este teste"
