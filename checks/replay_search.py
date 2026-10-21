"""Replay both rankings offline from saved corpus, queries and normalized vectors.

No LLM/API/model download. BM25 formula and tokenizer are the course implementation;
vector scores are recomputed independently as dot products of the saved embeddings.
This checks reproducibility of scores, not the relevance of a scientific paper.
"""
import json, math, re, sys
from collections import Counter,defaultdict
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
STOP=set('a an and are as at be by for from has have in is it its of on or that the this to was were which with we our can'.split())
def tokenize(text):
    return [w for w in re.findall(r'[a-zа-яё0-9]+',text.lower()) if w not in STOP and len(w)>1]
def replay(root=ROOT):
    """Данные: library/corpus.jsonl, library/rankings.json и сохранённые library/*_vectors.npy.
    Проверка: размеры, нормы, оценки и порядок BM25/cosine проверяются сравнением с сохранёнными результатами; расхождение даёт ValueError.
    Используется в: checks/replay_search.py::__main__ и CHECK.cmd для независимого пересчёта без сети.
    """
    docs=[json.loads(x) for x in (root/'library/corpus.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
    rankings=json.loads((root/'library/rankings.json').read_text(encoding='utf-8'))
    dv=np.load(root/'library/document_vectors.npy',allow_pickle=False)
    qv=np.load(root/'library/query_vectors.npy',allow_pickle=False)
    if dv.shape!=(len(docs),384) or qv.shape!=(5,384):raise ValueError('Wrong embedding dimensions')
    if not np.allclose(np.linalg.norm(dv,axis=1),1,atol=1e-5) or not np.allclose(np.linalg.norm(qv,axis=1),1,atol=1e-5):
        raise ValueError('Embeddings are not normalized')
    index=defaultdict(dict);lengths=[]
    for i,d in enumerate(docs):
        tokens=tokenize(d['title']+'. '+d['abstract']);lengths.append(len(tokens))
        for word,tf in Counter(tokens).items():index[word][i]=tf
    average=sum(lengths)/len(lengths)
    for qi,r in enumerate(rankings):
        scores=np.zeros(len(docs))
        for word in tokenize(r['query']):
            posting=index.get(word,{})
            idf=math.log(1+(len(docs)-len(posting)+0.5)/(len(posting)+0.5))
            for i,tf in posting.items():scores[i]+=idf*tf*2.2/(tf+1.2*(0.25+0.75*lengths[i]/average))
        vector=dv@qv[qi]
        if not np.allclose(scores,r['bm25_scores'],atol=1e-8):raise ValueError(f'BM25 scores differ: query {qi+1}')
        if not np.allclose(vector,r['vector_scores'],atol=2e-6):raise ValueError(f'Vector scores differ: query {qi+1}')
        for key,values in [('bm25',scores),('vector',vector)]:
            actual=[docs[int(i)]['id'] for i in np.argsort(-values)]
            if actual!=r[key+'_order']:raise ValueError(f'{key} order differs: query {qi+1}')
    return {'status':'PASS','documents':len(docs),'queries':len(rankings),'methods':['BM25','dense cosine'],'network_used':False}
if __name__=='__main__':
    try:print(json.dumps(replay(),ensure_ascii=False));raise SystemExit(0)
    except Exception as exc:print('FAIL:',type(exc).__name__,str(exc));raise SystemExit(1)
