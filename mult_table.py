
def find_primes(num):
    """ square the number to use a large limit with seive, works for small solutions"""
    limit = num * num
    if num == 1:
        return [2]
    result_arr = []
    """ Find Primes within a range using seive of Eratosthenes"""
    primes = seive_of_eratosthenes(limit)
    """ parse the primes list for index values """
    for idx, item in enumerate(primes[2:]):
        if item:
            result_arr.append(idx + 2)
        if len(result_arr) == num:
            return result_arr
    return result_arr

def seive_of_eratosthenes(limit):
    primes = [True for i in xrange(limit + 1)]
    check = 2
    while check * check <= limit:
        """ if number is prime, it will be True """
        if primes[check] == True:
            """ if number is prime, set all multiples of it to be false """
            for item in range(check * 2, limit + 1, check):
                primes[item] = False
        check += 1
    return primes

def create_mult_table(num):
    primes = find_primes(num)
    table = []
    header = '\t{}'.format('\t'.join(map(str, primes)))
    rows = []
    for i in primes:
        row = '\t'.join(map(str, (i*q for q in primes)))
        rows.append('{}\t{}'.format(i,row))
    print(header +'\n' + '\n'.join(rows))
    return [header] + rows

if __name__ == "__main__":
    create_mult_table(10)
