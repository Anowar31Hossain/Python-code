#FIFO=first in first out
from collections import deque
banks=deque(["Anis","Karim","Bijoy"])
print(banks)
banks.popleft()
banks.append("Sathi")
print(banks)
banks.popleft()
print(banks)
banks.popleft()

print(banks)
if not banks:
    print("No person left.")