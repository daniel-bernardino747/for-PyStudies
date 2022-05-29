import random
from time import sleep
list = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
for a in range(10, 0, -1):
    print(random.choice(list), a)
    sleep(1)
print('\033[1:92mBUM!', '\033[93mBUMM!!', '\033[95mPOOW!')