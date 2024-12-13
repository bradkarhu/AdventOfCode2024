# Advent of Code 2024 - Python

## Setup

Install required dependencies
``` sh
brew install scarvalhojr/tap/aoc-cli
pip3 install -r requirements.txt
```

Save AOC session cookie to `~/.adventofcode.session` (see [instructions](https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#session-cookie-))

Download AOC files (input.txt, puzzle.md) into each day's folder by running:
``` sh
python3 download.py
```

## Benchmarking
``` sh
python3 time_all.py
```

MacBook Pro M1 Max using Python 3.13.1

| Day | p1 cpu | p1 sec | p2 cpu | p2 sec |
| --- | --- | --- | --- | --- |
| 1 | 92% | 0.024 | 92% | 0.021 |
| 2 | 92% | 0.024 | 94% | 0.024 |
| 3 | 91% | 0.024 | 92% | 0.024 |
| 4 | 76% | 0.042 | 93% | 0.023 |
| 5 | 93% | 0.025 | 94% | 0.025 |
| 6 | 58% | 0.126 | --- | --- |
| 7 | 95% | 0.038 | 99% | 0.745 |
| 8 | 88% | 0.024 | 92% | 0.022 |
| 9 | 94% | 0.036 | 99% | 0.53 |
| 10 | 90% | 0.028 | 93% | 0.026 |
| 11 | 91% | 0.026 | 98% | 0.084 |
| 12 | 95% | 0.036 | 97% | 0.045 |
| Total | 87% | 0.4530 | 94% | 1.5690 |