"Coin"

# Readme: https://www.zhihu.com/question/315108379?

import numpy as np

def coin(tot):
    "Definition of coins"
    toc      = tot + 1
    category = [1, 5, 10, 20, 50, 100]
    count    = np.zeros(toc, dtype=int)
    count[0] = 1
    for i in category:
        for j in range(1,toc):      # 1 to tot
            if j >= i:
                count[j] = count[j] + count[j-i]
    return count[tot]

print(coin(500))
