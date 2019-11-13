from ObjectClasses.RomanBaseList import RomanBaseList
from SemanticAnalysis.InfoCollection import InfoCollection
from SemanticAnalysis.QuizHandler import QuizHandler
from ObjectClasses.MetalList import MetalList
from Except.UnrecognizedSentence import UnrecognizedSentence
from Except.UnrecognizedRomanForm import UnrecognizedRomanForm
import re

class SemanticParse:
    def __init__(self):
        self._roman_base_list = RomanBaseList()
        self._metal_list = MetalList()
        self._info_collection = InfoCollection(self._roman_base_list, self._metal_list)
        self._quiz_handler = QuizHandler(self._roman_base_list, self._metal_list)

    def syntax_analysis(self, sentences):
        """
        Syntax analysis entrance
        :param sentences:
        :return: output
        """
        result_sentences = []
        for sentence in sentences:
            try:
                res_sent = self.syntax_analysis_by_catagories(sentence)
            except UnrecognizedRomanForm as e:
                result_sentences.append(e)
                return result_sentences
            except SyntaxError as e:
                res_sent = str(e)
            result_sentences.append(res_sent)
        return result_sentences

    def syntax_analysis_by_catagories(self, sentence):
        """
        classification of sentence based on regex
        :param sentence:
        :return: sentence result
        """
        result = ''
        if re.search(r'is [IVXLCDM]', sentence):
            self._info_collection.assignment_syntax_handle(sentence)
        elif re.match(r'([a-z ]+[a-z]) ([A-Z][a-z]+) is (\d+) Credits', sentence):
            self._info_collection.metal_syntax_handle(sentence)
        elif re.match(r'how much is ([a-z ]+[a-z]) ?', sentence):
            result = self._quiz_handler.how_much_quiz_handle(sentence)
        elif re.match(r'how many Credits is (([a-z ]+[a-z]) ([A-Z][a-z]+)) ?', sentence):
            result = self._quiz_handler.how_many_quiz_handle(sentence)
        else:
            raise UnrecognizedSentence()
        return result
