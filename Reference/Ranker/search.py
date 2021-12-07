import metapy

def load_ranker(cfg_file):
    idx = metapy.index.make_inverted_index('youtube-config.toml')
    ranker = metapy.index.OkapiBM25()
    query = metapy.index.Document()
    query.content('OUR SEARCH')
    top_docs = ranker.score(idx, query, num_results=5)
    top_docs  #We are returned a ranked list of (doc_id, score) pairs. The scores are from the ranker, which in this case was Okapi BM25. 
    