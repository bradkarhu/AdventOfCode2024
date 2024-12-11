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
| 1 | 93% | 0.024 | 94% | 0.021 |
| 2 | 94% | 0.023 | 95% | 0.023 |
| 3 | 94% | 0.023 | 93% | 0.022 |
| 4 | 95% | 0.029 | 94% | 0.021 |
| 5 | 94% | 0.025 | 95% | 0.025 |
| 6 | 97% | 0.06 | --- | --- |
| 7 | 95% | 0.038 | 99% | 0.741 |
| 8 | 92% | 0.024 | 94% | 0.023 |
| 9 | 95% | 0.035 | 99% | 0.538 |
| 10 | 94% | 0.027 | 95% | 0.025 |
| Total | 94% | 0.3080 | 95% | 1.4390 |