from radon.raw import analyze
from radon.metrics import mi_visit, mi_parameters
import logging

class CodeAnalysis:
    __code = None
    defs = 0
    blank_before_defs = 0
    comments = 0
    lines = 0
    blank_lines =0
    compl = 0
    maintain = 0
    tabs = False

    def __init__(self, code):
        self.__code = code

    def count_lines(self):
        logging.info("Counting lines with code , comments and blank lines")
        a = analyze(self.__code)
        self.lines=a.loc
        self.blank_lines = a.blank
        self.comments = a.comments

    def complexity_analyze(self):
        logging.info("Complexity analysis")
        try:
            self.compl = mi_parameters(self.__code)[1]
            return self.compl
        except SyntaxError:
            logging.error("Syntax Error in analyzed code")
            print("Syntax Error in analyzed code")

    def maintainability(self):
        logging.info("Maintainability analysis")
        try:
            self.maintain = mi_visit(self.__code,True)
            return self.maintain
        except SyntaxError:
            logging.error("Syntax Error in analyzed code")
            print("Syntax Error in analyzed code")

    def find_tabs(self):
        logging.info("Searching for tabs")
        if '\t' in self.__code:
            self.tabs = True
            return self.tabs
        return self.tabs

    def count_def(self):
        self.defs = self.__code.split().count('def\b')
        return self.defs

    def defs_without_blank(self):
        self.blank_before_defs = self.__code.split().count('\n\ndef\b')
        return self.count_def() - self.blank_before_defs

    def results(self):
        logging.info('Starting analysis')
        self.count_lines()
        print("Total lines of code:", self.lines)
        print("Complexity of the code:", self.complexity_analyze())
        try:
            print("Maintainability of the code:", round(self.maintainability(),2),"%")
            print("Blank lines:", round(100*self.blank_lines/self.lines,2), "% of code")
            print("Comments:", round(100*self.comments/self.lines,2), "% of code")
        except TypeError :
            print("Something gone wrong , probably syntax error in analyzed code.")
            logging.error("something gone wrong. Check the syntax of analyzed code.")

        if self.find_tabs():
            logging.warning("Tabs found")
            print("Tabs used - not recommended")
        if self.defs_without_blank()>0:
            logging.warning("def without blank space before")
            print("Not really PEP8 compatible")
