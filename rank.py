from rank_bm25 import BM25Okapi
from youtube_transcript_api import YouTubeTranscriptApi

def getRankedURLs(query):
    youtube_url_dict = {"5q87K1WaoFI":"Computer Scientist Explains Machine Learning in 5 Levels of Difficulty | WIRED", "z-EtmaFJieY":"Machine Learning & Artificial Intelligence: Crash Course Computer Science #34", "ukzFI9rgwfU":"Machine Learning Basics | What Is Machine Learning? | Introduction To Machine Learning | Simplilearn", "NWONeJKn6kc":"Machine Learning Course for Beginners", "h0e2HAPTGF4":"11. Introduction to Machine Learning"}

    youtube_urls = list(youtube_url_dict.keys())

    corpus = []

    for url in youtube_urls:
        transcript_list = YouTubeTranscriptApi.list_transcripts(url)
        transcript = transcript_list.find_generated_transcript(['en'])
        text = transcript.fetch()

        phrases = ""

        for i in range(len(text)):
            phrases = phrases + ' ' + text[i]['text']

        corpus.append(phrases)

    tokenized_corpus = [doc.split(" ") for doc in corpus]

    bm25 = BM25Okapi(tokenized_corpus)

    tokenized_query = query.split(" ")

    doc_scores = bm25.get_top_n(tokenized_query, corpus, n=len(corpus))

    ranks = []

    for i in range(len(doc_scores)):
        url = youtube_urls[corpus.index(doc_scores[i])]
        ranks.append(youtube_url_dict[url])

    return ranks

 
