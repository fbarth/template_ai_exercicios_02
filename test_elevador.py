import pytest
from Elevador import main

def test_2_bl(capsys):
    main(0,2,'BL')
    captured = capsys.readouterr()
    assert captured.out == 'Solução:  ; subir 2 andares\n'

def test_3_bl(capsys):
    main(0,3,'BL')
    captured = capsys.readouterr()
    assert captured.out == 'Solução:  ; subir 2 andares ; subir 1 andar\n'

def test_10_bl(capsys):
    main(0,10,'BL')
    captured = capsys.readouterr()
    assert captured.out == 'Solução:  ; subir 2 andares ; subir 2 andares ; subir 2 andares ; subir 2 andares ; subir 2 andares\n'

def test_2_bp(capsys):
    main(0,2,'BP')
    captured = capsys.readouterr()
    assert captured.out == 'Solução:  ; subir 1 andar ; subir 1 andar\n'

def test_3_bp(capsys):
    main(0,3,'BP')
    captured = capsys.readouterr()
    assert captured.out == 'Solução:  ; subir 1 andar ; subir 1 andar ; subir 1 andar\n'

def test_10_bp(capsys):
    main(0,10,'BP')
    captured = capsys.readouterr()
    assert captured.out == 'Solução:  ; subir 1 andar ; subir 1 andar ; subir 1 andar ; subir 1 andar ; subir 1 andar ; subir 1 andar ; subir 1 andar ; subir 1 andar ; subir 1 andar ; subir 1 andar\n'