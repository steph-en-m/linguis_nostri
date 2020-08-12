import pandas as pd
import numpy as np

text = pd.read_csv('./Stephen_data_acholi.csv')

acholi = text['acholi_text']
print(f'Dataset shape: {text.shape}')
token_length = [len(x.split(" ")) for x in acholi]
print(f'Max token length: {max(token_length)}')

unique_sentences = len(set(acholi))
print(f'There are {unique_sentences} unique documents in the Acholi corpus')

unique_words = set()
acholi.str.lower().str.split().apply(unique_words.update)
print(f'There are {len(unique_words)} unique words in the Acholi corpus')

