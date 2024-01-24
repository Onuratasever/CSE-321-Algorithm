def minimum_edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D array to store the minimum costs
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    #print("dp1: ", dp)

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    #print("dp2: ", dp)

    # Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Check if the current characters are the same
            # print("i: ", i)
            # print("j: ", j)
            # print("str1: ", str1[i - 1])
            # print("str2: ", str2[j - 1])
            # print("--------------------")

            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Calculate the cost of insertion, deletion, and substitution
                insert_cost = dp[i][j - 1] + 1
                delete_cost = dp[i - 1][j] + 1
                substitute_cost = dp[i - 1][j - 1] + 3  # Substitution cost is three times higher

                # Choose the minimum cost
                dp[i][j] = min(insert_cost, delete_cost, substitute_cost)

    # The minimum cost is stored in the bottom-right cell of the matrix
    return dp[m][n]

# Example usage:
dna1 = "ATGCA"
dna2 = "ATGT"
cost = minimum_edit_distance(dna1, dna2)
print(f"The minimum cost to transform '{dna1}' to '{dna2}' is: {cost}")
