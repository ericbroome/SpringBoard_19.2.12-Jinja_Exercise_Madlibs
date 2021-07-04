"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""
        labels = []
        for label in words:
            labels.append(label.replace('_', ' ').title())
        # Let's make a dict of prompts and labels
        self.prompts = dict(zip(words, labels))
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


stories = []

stories.append(Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a/n {adjective} {noun}. It loved to {verb} {plural_noun}."""
))

stories.append(Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "gender_pronoun"],
    """
        The time to {adjective}ly {verb} has arrived. If {gender_pronoun} decides not to {verb} then so be it but when the
        {noun} decides to confront the {plural_noun} at the {place} there will be no time to {verb} so the time is NOW I say.
    """
))

stories.append(Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """
        Release the {noun}s, the director cried. There aren't nearly enough {noun}s in this {place}. And those {noun}s over there
        aren't even {verb}ing as {adjective}ly as they could or should be. What we really need is more {plural_noun}. 
    """
))

stories.append(Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "gender_pronoun"],
    """
        One day a/n {adjective} {noun} decided to {verb} for some {plural_noun}, not because {gender_pronoun} really wanted to
        but because {gender_pronoun} thought it would be a good idea. So {gender_pronoun} went about {verb}ing and eventually
        ended up {adective}ly {verb}ing every day for ever and ever.
    """
))

