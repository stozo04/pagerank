import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.

    corpus: A dictionary where keys are page names, and values are sets of pages they link to.
    page: The current page the random surfer is on.
    damping_factor: A floating-point number like 0.85.
    """
    total_pages = len(corpus)
    prob_distribution = {}

    if corpus[page]:  # Case: Page has outgoing links
        linked_pages = corpus[page]
        num_links = len(linked_pages)

        # Step 1: Assign probabilities for linked pages
        for linked_page in linked_pages:
            prob_distribution[linked_page] = damping_factor / num_links

        # Step 2: Add random jump factor to all pages
        for p in corpus:
            prob_distribution[p] = prob_distribution.get(p, 0) + (1 - damping_factor) / total_pages

    else:  # Case: Page has no outgoing links
        # Treat it as linking to all pages equally
        for p in corpus:
            prob_distribution[p] = 1 / total_pages
    
    # Return the computed probability distribution
    return prob_distribution



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    corpus: A dictionary mapping pages to sets of linked pages.
    damping_factor: Probability of following a link vs. jumping randomly.
    n: Number of samples to generate.
    """
    # Step 1: Start with a random page

    # Pick a random page using random.choice
    current_page = random.choice(list(corpus.keys()))
    # Initialize a dictionary to track the visit counts
    visit_counts = {page: 0 for page in corpus}
    # Increment the visit count for the initial page
    visit_counts[current_page] += 1

    # Step 2: Loop through n samples
    for _ in range(n - 1):  # n-1 because the first sample is already chosen
        probabilities = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(
            population=list(probabilities.keys()),
            weights=list(probabilities.values())
        )[0]
        visit_counts[current_page] += 1

    # Step 3: Normalize the visit counts
    total_samples = sum(visit_counts.values())
    return {page: count / total_samples for page, count in visit_counts.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N = len(corpus)
    pagerank = {page: 1 / N for page in corpus}  # Step 1: Initialize

    while True:
        new_pagerank = {}

        for page in corpus:
            # Step 2.1: Random jump component
            rank = (1 - damping_factor) / N

            # Step 2.2: Contributions from all pages linking to `page`
            for linking_page in corpus:
                if corpus[linking_page]:  # Normal case: `linking_page` has outgoing links
                    if page in corpus[linking_page]:
                        rank += damping_factor * (pagerank[linking_page] / len(corpus[linking_page]))
                else:  # Special case: `linking_page` has no links
                    rank += damping_factor * (pagerank[linking_page] / N)

            new_pagerank[page] = rank

        # Step 3: Check for convergence
        if all(abs(new_pagerank[page] - pagerank[page]) < 0.001 for page in corpus):
            break

        pagerank = new_pagerank

    # Step 4: Normalize
    total_rank = sum(new_pagerank.values())
    return {page: rank / total_rank for page, rank in new_pagerank.items()}


if __name__ == "__main__":
    main()
