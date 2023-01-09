def gorenstein_program(n, k):
    # Initialize the generator matrix G
    G = [[0 for _ in range(n)] for _ in range(k)]
    # Initialize the parity check matrix H
    H = [[0 for _ in range(k)] for _ in range(n - k)]

    for i in range(k):
        # Set the i-th row of G to be the i-th standard basis vector
        G[i][i] = 1
    for i in range(k, n):
        # Set the (i - k)-th row of H to be the i-th standard basis vector
        H[i - k][i] = 1

    # Solve the matrix equation G * H^T = 0
    # to obtain additional rows for G and columns for H
    for i in range(k, n):
        for j in range(k):
            # If the (i-k)-th row of H and the j-th column of G have a nonzero entry,
            # add the j-th row of G to the i-th row of G and add the (i-k)-th column of H to the j-th column of H
            if H[i - k][j] != 0:
                for l in range(n):
                    G[i][l] ^= G[j][l]
                    H[l][j] ^= H[l][i - k]

    # Truncate G to the first k columns and H to the last n - k columns
    G = [row[:k] for row in G]
    H = [row[k:] for row in H]

    return G, H
