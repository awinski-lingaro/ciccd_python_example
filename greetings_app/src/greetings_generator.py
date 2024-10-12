import random


class MoodTextProvider:
    def __init__(self):
        self._moods = {
            "good": ["Hello! What a beautiful day", "Welcome back sweetheart!"],
            "bad": ["Hello! Another stupid day", "Bad morning as usual"],
        }

    def has_mood(self, mood):
        return mood in self._moods

    def provide(self, mood):
        ls = self._moods[mood]
        return random.choice(ls)


class Greetings:
    def __init__(self, mood_text_provider=None, mood="bad"):
        self.mood_text_provider = mood_text_provider or MoodTextProvider()
        if not self.mood_text_provider.has_mood(mood):
            raise KeyError("Mood is not valid")
        self.mood = mood

    def generate_greetings(self, mood=None):
        mood = mood or self.mood
        return self.mood_text_provider.provide(mood)
