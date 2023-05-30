"""
Multiplying two polynomials means that we need their coefficients. We are gonna keep the coefficients in the arrays
"""


# NAIVE APPROACH (double loop)
def multiply_poly_1(A, B):
    m = len(A)
    n = len(B)
    # create a product array with a length of (m + n -1)
    # since the multiplication of polynomials have distributive property. Initialize it with zeros
    product = [0] * (m + n - 1)

    # multiply two polynomials term by term

    # take every term of the first polynomial
    for i in range(m):
        # multiply the current term with every term of the second polynomial
        for j in range(n):
            product[i + j] += A[i] * B[j]

    return product
