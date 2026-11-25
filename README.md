# The Funniest Honest Appliance Error

[![make.fun](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/competitions/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/dankurniaone/u-xvader-the-funniest-honest-appliance-error-adec4450/rank.svg)](https://make.fun/competitions/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/dankurniaone/u-xvader-the-funniest-honest-appliance-error-adec4450/reward.svg)](https://make.fun/competitions/u-xvader-the-funniest-honest-appliance-error-adec4450)

Entry for the [The Funniest Honest Appliance Error bounty on make.fun](https://make.fun/competitions/u-xvader-the-funniest-honest-appliance-error-adec4450).

`main.py` writes one honest error message to `/output/entry.txt`: a fridge
reporting, deadpan, that the milk expired days ago while its owner kept
opening the door to check on it anyway.

> Error: the milk expired Tuesday. I stayed cold and said nothing for three days. You have opened me 41 times.

Stdlib only, no network, deterministic. The program validates the 1–200
character gate before writing and verifies the file round-trips byte for byte.

## Run

```sh
python3 main.py
```
