from SemanticAnalysis.SemanticParse import SemanticParse


class Main:
    def __init__(self):
        self._semantic_parse = SemanticParse()

    @property
    def semantic_parse(self):
        return self._semantic_parse

    def output_result(self, sentences):
        for sentence in sentences:
            print(sentence)

    def translate(self, file_path):
        with open(file_path) as f:
            str = f.read()
            words_list = str.split('\n')
            result = self._semantic_parse.syntax_analysis(words_list)
        result = [res for res in result if res != '']
        self.output_result(result)
        # Mainly for unit testing invoke
        return result


if __name__ == '__main__':
    main = Main()
    main.translate('UnitTests/TestInput/test.txt')
