# PageRank Implementation

This project implements the PageRank algorithm to rank web pages based on their importance using both sampling (Random Surfer Model) and iterative methods.

## Folder Structure

```
project-folder/
├── corpus0/          # Sample test folder 0
│   ├── 1.html
│   ├── 2.html
│   ├── 3.html
│   └── 4.html
├── corpus1/          # Sample test folder 1
│   ├── bfs.html
│   ├── dfs.html
│   ├── games.html
│   ├── minesweeper.html
│   ├── minimax.html
│   ├── search.html
│   └── tictactoe.html
├── corpus2/          # Sample test folder 2
│   ├── ai.html
│   ├── algorithms.html
│   ├── c.html
│   ├── inference.html
│   ├── logic.html
│   ├── programming.html
│   ├── python.html
│   └── recursion.html
├── pagerank.py       # Main implementation
├── pagerank-test.py  # Test suite
└── README.md
```

## Usage

1. Ensure Python 3 is installed
2. Run: `python pagerank.py corpus0`
 - Replace corpus0 with any sample corpus folder (e.g., corpus1, corpus2)

Example output:
```
PageRank Results from Sampling (n = 10000)
  1.html: 0.2200
  2.html: 0.3800
  3.html: 0.2600
  4.html: 0.1400

PageRank Results from Iteration
  1.html: 0.2205
  2.html: 0.3802
  3.html: 0.2597
  4.html: 0.1396
```

## Implementation Details

### Sampling Method
- Starts at random page
- Selects next page based on transition probabilities
- Tracks visit frequency over n samples
- Returns visit proportions as PageRanks

### Iterative Method
- Initializes equal PageRank values
- Updates using recursive formula
- Converges at < 0.001 change
- Returns final PageRanks

## Test Corpora

### corpus0
- 4 basic pages for testing
- Simple link structure

### corpus1
- Search algorithm topics
- BFS, DFS, Minimax, etc.

### corpus2
- Programming concepts
- AI, recursion, Python, etc.

## Notes
- Pages without outgoing links treated as linking to all pages
- Both methods should produce similar results
- All PageRank values sum to 1

## Troubleshooting
- Verify correct folder structure and HTML formatting
- Check damping factor if results don't converge
- Ensure PageRank values are normalized

## Support
For issues or questions, please use the project forums.
