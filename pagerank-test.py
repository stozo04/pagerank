from pagerank import iterate_pagerank, sample_pagerank, transition_model

corpus = {
    "1.html": {"2.html", "3.html"},
    "2.html": {"3.html"},
    "3.html": {"2.html"}
}

# Test transition_model
print(transition_model(corpus, "1.html", 0.85))
# Test sample_pagerank
print(sample_pagerank(corpus, 0.85, 10))
# Test iterate_pagerank
print(iterate_pagerank(corpus, 0.85))