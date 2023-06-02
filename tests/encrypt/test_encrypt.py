import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(10, 10)
    assert encrypt_message("Xablau", 3) == "baX_ual"
    assert encrypt_message("Xablau", 2) == "ualb_aX"
    assert encrypt_message("Xablau", 200) == "ualbaX"
