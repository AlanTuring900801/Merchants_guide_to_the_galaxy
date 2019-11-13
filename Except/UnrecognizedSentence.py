class UnrecognizedSentence(SyntaxError):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return "I have no idea what you are talking about"
