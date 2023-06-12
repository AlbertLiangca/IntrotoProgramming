class AWordGame:
    def outcome(self, wordList):
        words = set()
        for wordsString in wordList:
            wordArray = wordsString.split()
            words.update(wordArray)

        return self.playGame(words, "", 1)

    def playGame(self, wordList, currentWord, currentPlayer):
        if currentPlayer == 1:
            if currentWord in wordList:
                return currentWord

            for c in range(ord('a'), ord('z') + 1):
                nextWord = currentWord + chr(c)
                result = self.playGame(wordList, nextWord, 2)
                if not result:
                    return nextWord
        else:
            if currentWord in wordList:
                return currentWord

            for c in range(ord('a'), ord('z') + 1):
                nextWord = currentWord + chr(c)
                result = self.playGame(wordList, nextWord, 1)
                if result:
                    return nextWord

        return ""

case1 = ['f','pi']


AWordGame().outcome(case1)


# change 1