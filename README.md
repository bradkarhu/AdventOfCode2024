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
| 1 | 91% | 0.023 | 93% | 0.021 |
| 2 | 92% | 0.024 | 94% | 0.023 |
| 3 | 92% | 0.023 | 93% | 0.021 |
| 4 | 94% | 0.029 | 94% | 0.021 |
| 5 | 93% | 0.025 | 95% | 0.025 |
| 6 | 71% | 0.087 | --- | --- |
| 7 | 95% | 0.038 | 99% | 0.745 |
| 8 | 89% | 0.024 | 93% | 0.021 |
| 9 | 93% | 0.036 | 99% | 0.539 |
| 10 | 90% | 0.028 | 92% | 0.026 |
| 11 | 90% | 0.025 | 98% | 0.085 |
| 12 | 92% | 0.037 | 96% | 0.045 |
| 13 | 88% | 0.025 | 94% | 0.021 |
| Total | 90% | 0.4240 | 95% | 1.5930 |