import pdb;

def exponent(base, power):
    if power <= 0: return 1

    return base * exponent(base, power - 1)

def main():
    print "2^0: %d" % (exponent(2, 0))
    print "2^1: %d" % (exponent(2, 1))
    print "2^2: %d" % (exponent(2, 2))
    print "2^3: %d" % (exponent(2, 3))
    print "3^1: %d" % (exponent(3, 1))
    print "3^3: %d" % (exponent(3, 3))
    print "3^4: %d" % (exponent(3, 4))
    print "5^3: %d" % (exponent(5, 3))

    return 1

if __name__ == '__main__':
  main()
