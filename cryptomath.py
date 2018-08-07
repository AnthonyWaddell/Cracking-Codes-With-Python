''' Python module that includes functions for finding the greatest common 
	divisor of two ints (Euclid's) and finding the modular inverse of two
	ints.'''

# Greatest common divisor using Euclid's algorthm
def gcd(a, b):
	while a!= 0:
		a, b = b % a, a
	return b

# Return the modulus inverse of a % m, which is the number
# x such that A * x % m = 1 (relative prime)
def findModInverse(a, m):

	# If a and m are not relatively prime, no mod inverse
	if gcd(a, m) != 1:
		return None

	# Calculate using the extended Euclidean algorithm
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, m
	while v3 != 0:
		# Integer division
		q = u3 // v3
		v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2),
		(u3 - q * v3), v1, v2, v3
	return u1 % m