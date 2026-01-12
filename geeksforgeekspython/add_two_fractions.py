def addFraction(num1, den1, num2, den2):
    # Calculate numerator and denominator
    num = num1 * den2 + num2 * den1
    den = den1 * den2

    # Find GCD to reduce the fraction
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    g = gcd(num, den)

    # Print reduced fraction
    print(f"{num//g}/{den//g}")
