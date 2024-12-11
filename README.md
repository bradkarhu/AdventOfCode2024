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
| 1 | 93% | 0.025 | 93% | 0.021 |
| 2 | 93% | 0.023 | 95% | 0.023 |
| 3 | 93% | 0.022 | 94% | 0.021 |
| 4 | 95% | 0.028 | 94% | 0.021 |
| 5 | 94% | 0.025 | 95% | 0.025 |
| 6 | 56% | 0.128 | --- | --- |
| 7 | 95% | 0.038 | 99% | 0.737 |
| 8 | 88% | 0.024 | 93% | 0.022 |
| 9 | 94% | 0.036 | 99% | 0.537 |
| 10 | 90% | 0.029 | 92% | 0.029 |
| 11 | 93% | 0.025 | 97% | 0.088 |
| Total | 89% | 0.4030 | 95% | 1.5240 |