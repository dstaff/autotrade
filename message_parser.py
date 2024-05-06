import re

text = """
GOLD SELL 2328.3-2331.8

TP=2326.3
TP=2324.3
TP=2318.3

SL=2334.3
"""

# Extract GOLD/SELL or GOLD/CALL and range
pattern_header = re.compile(r'GOLD (SELL|CALL) (\d+\.\d+)-(\d+\.\d+)')
match_header = pattern_header.search(text)
if match_header:
    direction = match_header.group(1)
    low_range = match_header.group(2)
    high_range = match_header.group(3)
    print(f"Direction: {direction}")
    print(f"Low Range: {low_range}")
    print(f"High Range: {high_range}")

# Extract target prices (TP)
pattern_tp = re.compile(r'TP=(\d+\.\d+)')
matches_tp = pattern_tp.findall(text)
if matches_tp:
    print("\nTarget Prices:")
    for tp in matches_tp:
        print(tp)

# Extract stop loss (SL)
pattern_sl = re.compile(r'SL=(\d+\.\d+)')
match_sl = pattern_sl.search(text)
if match_sl:
    sl = match_sl.group(1)
    print(f"\nStop Loss: {sl}")
