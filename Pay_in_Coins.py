import sys

def is_prime(num):
    if num < 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes_up_to(n):
    return [i for i in range(1, n+1) if is_prime(i)]

def get_combinations1(primes,money_owed,n,):
    dp = [[0 for _ in range(money_owed + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(money_owed + 1):
            if dp[i][j-primes[i-1]] >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j-primes[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][money_owed]

def get_combinations2(primes,money_owed,num_coins):
    dp = [[0 for _ in range(money_owed + 1)] for _ in range(num_coins + 1)]
    dp[0][0] = 1
    for coin in primes:
        for i in range(1, num_coins + 1):
            for j in range(coin,money_owed + 1):
                    dp[i][j] = dp[i][j] + dp[i-1][j-coin]
    return dp[num_coins][money_owed]

def get_combinations3(primes,money_owed,num_coins,range_coins):
    dp = [[0 for _ in range(money_owed + 1)] for _ in range(range_coins + 1)]
    dp[0][0] = 1
    for coin in primes:
        for i in range(1, range_coins  + 1):
            for j in range(coin,money_owed + 1):
                    dp[i][j] = dp[i][j] + dp[i-1][j-coin]
    sum = 0
    for i in range(num_coins,range_coins+1):
            sum = sum + dp[i][money_owed]
    return sum

def main():
    if len(sys.argv) != 2:
        return

input_file_path = sys.argv[1]

with open(input_file_path, 'r') as f_in:
    stored = []
    for line in f_in:
        line = line.strip().split()
        stored.append(line)

for line in stored:
    if len(line) == 1:
        money_owed = int(line[0])
        primes = get_primes_up_to(money_owed)
        if money_owed not in primes:
            primes.append(money_owed)
        n = len(primes)
        number_of_combos = get_combinations1(primes,money_owed,n)
        print(number_of_combos)
    
    if len(line) == 2:
        money_owed = int(line[0])
        num_coins = int(line[1])  
        primes = get_primes_up_to(money_owed)
        if money_owed not in primes:
            primes.append(money_owed)
        n = len(primes)
        number_of_combos = get_combinations2(primes,money_owed,num_coins)
        print(number_of_combos)

    if len(line) == 3:
        money_owed = int(line[0])
        num_coins = int(line[1])
        range_coins = int(line[2])
        primes = get_primes_up_to(money_owed)
        if money_owed not in primes:
            primes.append(money_owed)
        number_of_combos = get_combinations3(primes,money_owed,num_coins,range_coins)
        print(number_of_combos)