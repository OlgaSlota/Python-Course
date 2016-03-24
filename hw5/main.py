import requests
import CodeCheck
import logging
import argparse

logging.basicConfig(filename='main.log', level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()
link = getattr(args,"url")

if not link:
    link = "https://raw.githubusercontent.com/joeyajames/Python/master/SortingAlgorithms.py"
    logging.warning("Something went wrong with parsing argument")

page = requests.get(link)

logging.info('Before analysis')

code_check = CodeCheck.CodeAnalysis(page.text)
code_check.results()

logging.info('Finished')
