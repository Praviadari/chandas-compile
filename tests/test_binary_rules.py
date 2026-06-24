from core.binary_rules import analyze_syllable


def test_long_vowel_is_guru() -> None:
	assert analyze_syllable("రా") == 1


def test_short_vowel_is_laghu() -> None:
	assert analyze_syllable("ర") == 0


def test_anusvara_is_guru() -> None:
	assert analyze_syllable("రం") == 1
