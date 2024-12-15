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
| 1 | 91% | 0.021 | 93% | 0.017 |
| 2 | 91% | 0.021 | 93% | 0.021 |
| 3 | 90% | 0.019 | 93% | 0.017 |
| 4 | 93% | 0.025 | 93% | 0.018 |
| 5 | 88% | 0.023 | 94% | 0.021 |
| 6 | 56% | 0.118 | --- | --- |
| 7 | 94% | 0.035 | 99% | 0.746 |
| 8 | 89% | 0.022 | 93% | 0.02 |
| 9 | 76% | 0.057 | 99% | 0.528 |
| 10 | 89% | 0.025 | 94% | 0.021 |
| 11 | 87% | 0.022 | 98% | 0.089 |
| 12 | 91% | 0.035 | 96% | 0.044 |
| 13 | 86% | 0.022 | 92% | 0.019 |
| 14 | 93% | 0.021 | 99% | 0.182 |
| Total | 86% | 0.4660 | 95% | 1.7430 |