from rank_bm25 import BM25Okapi
from youtube_transcript_api import YouTubeTranscriptApi

def getRankedURLs(query):
    youtube_urls = ["5q87K1WaoFI", "z-EtmaFJieY", "ukzFI9rgwfU", "NWONeJKn6kc", "h0e2HAPTGF4"]

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

    string ranks = ""

    for i in doc_scores:
        ranks = ranks + corpus.index(i)) + " "

    return ranks

 
