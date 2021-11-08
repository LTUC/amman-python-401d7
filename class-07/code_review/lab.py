# Counters
from collections import Counter

dice = (5,3,6,6,6,3)

ctr = Counter(dice)
print(ctr)
print(type(ctr))

most_comm = ctr.most_common()
print(most_comm)

# [(6, 3), (3, 2), (5, 1)]

# Calculate score
# 6 dice, most common one is (dice, 1)
# 1500

