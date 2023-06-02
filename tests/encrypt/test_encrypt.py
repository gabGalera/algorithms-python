import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_if_not_string_throws_an_error():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(10, 10)


def test_if_not_int_throws_an_error():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("10", "10")


def test_if_key_not_in_range():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Xablau", -10)


def test_if_it_is_odd():
    assert encrypt_message("Xablau", 3) == "baX_ual"


def test_if_it_is_pair():
    assert encrypt_message("Xablau", 2) == "ualb_aX"
