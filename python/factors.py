def factors(num):
    answer = set()
    for i in xrange(1, int(num ** 0.5)):
        if num % i == 0:
            answer.add(i)
            answer.add(num / i)
    return list(answer)

print(factors(100))
print(factors(813217))
print(factors(123194))

