import numpy as np
from fastapi import FastAPI, Request

app = FastAPI()


def create_corpus():
    text = open('342870791.txt', encoding='utf-8').read()
    corpus = text.lower().split()
    return corpus

def make_pairs(corpus:list):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

def prepare_dict():
    corpus = create_corpus()
    pairs = make_pairs(corpus)
    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1]=[word_2]
    return word_dict

def generate_text(word: str, n_words: int = 100)-> str:
    word_dict = prepare_dict()
    chain = [word]
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
    return ' '.join(chain)

# print(generate_text('привет', 25))

@app.get('/text/{word}')
def get_text(word: str, size: int = 100):
    responce = generate_text(wprd, size)
    return {'text': response, 'status': 'ok'}



