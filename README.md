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
| 1 | 89% | 0.026 | 93% | 0.022 |
| 2 | 93% | 0.024 | 94% | 0.025 |
| 3 | 89% | 0.024 | 92% | 0.021 |
| 4 | 93% | 0.029 | 94% | 0.022 |
| 5 | 93% | 0.025 | 94% | 0.025 |
| 6 | 72% | 0.084 | --- | --- |
| 7 | 95% | 0.039 | 99% | 0.764 |
| 8 | 89% | 0.026 | 94% | 0.025 |
| 9 | 93% | 0.039 | 99% | 0.544 |
| Total | 89% | 0.3160 | 94% | 1.4480 |