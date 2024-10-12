import pytest

from greetings_app.src.greetings_generator import Greetings, MoodTextProvider


@pytest.fixture(scope="module")
def generator():
    return Greetings()


@pytest.fixture(scope="module")
def provider():
    return MoodTextProvider()


class TestGreetingsGeneratorGenerateGreetings:

    def test_generate_for_known_mood(self, generator):
        assert len(generator.generate_greetings("bad")) > 5
        assert len(generator.generate_greetings("good")) > 5

    def test_generate_for_unknown_mood(self, generator):
        with pytest.raises(KeyError):
            generator.generate_greetings("ko")
            generator.generate_greetings("asa")

    def test_init_for_unknown_mood(self):
        with pytest.raises(KeyError):
            Greetings(mood="ko")


class TestMoodTextProviderHasMood:

    def test_has_mood_for_known_mood(self, provider):
        assert provider.has_mood("bad")
        assert provider.has_mood("good")

    def test_has_mood_for_unknown_mood(self, provider):
        assert not provider.has_mood("ko")
