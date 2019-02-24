from konlpy.tag import Okt; t = Okt()
from konlpy.tag import Mecab
t = Mecab(dicpath="C:/mecab/mecab-ko-dic")
pos = lambda d: ['/'.join(p) for p in t.morphs(d)]
texts_ko = [pos(doc) for doc in docs_ko]

from gensim.models import word2vec
wv_model_ko = word2vec.Word2Vec(texts_ko)
wv_model_ko.init_sims(replace=True)
wv_model_ko.save('ko_word2vec_e.model')

print(wv_model_ko.most_similar(pos('기가지니')))