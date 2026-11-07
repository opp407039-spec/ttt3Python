class WordLengthIterator:
    def __init__(self, words):
        self.words = words
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.words):
            raise StopIteration
        word = self.words[self.i]
        self.i += 1
        return word, len(word)


words = ["яблуко", "python", "ітератор", "код", "програмування"]
iterator = WordLengthIterator(words)

for word, length in iterator:
    print(f"{word}: {length}")

# Повторный обход работает, потому что __iter__ сбрасывает self.i
for word, length in iterator:
    print(f"{word}: {length}")