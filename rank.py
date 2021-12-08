from rank_bm25 import BM25Okapi
from youtube_transcript_api import YouTubeTranscriptApi

youtube_urls = ["5q87K1WaoFI", "z-EtmaFJieY", "ukzFI9rgwfU", "NWONeJKn6kc", "h0e2HAPTGF4"]
# youtube_urls = ["z-EtmaFJieY"]

corpus = []

for url in youtube_urls:
    # srt = YouTubeTranscriptApi.get_transcript(url)
    transcript_list = YouTubeTranscriptApi.list_transcripts(url)
    transcript = transcript_list.find_generated_transcript(['en'])
    text = transcript.fetch()
    # print(type(srt))
    # text = transcript.fetch()
    # print(text[0]['text'])

    phrases = ""

    for i in range(len(text)):
        phrases = phrases + ' ' + text[i]['text']

    # print(phrases)
    corpus.append(phrases)

# print(corpus)

# corpus = [
#     "Hello there good man!",
#     "London bridge is falling down",
#     "Chicago is more windy than London",
#     "It is quite windy in London",
#     "How is the weather today?"
# ]

tokenized_corpus = [doc.split(" ") for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)

query = "machine learning"
tokenized_query = query.split(" ")

# doc_scores = bm25.get_scores(tokenized_query)

doc_scores2 = bm25.get_top_n(tokenized_query, corpus, n=len(corpus))

for i in doc_scores2:
    print(corpus.index(i))

# print(doc_scores)
# print(doc_scores2)