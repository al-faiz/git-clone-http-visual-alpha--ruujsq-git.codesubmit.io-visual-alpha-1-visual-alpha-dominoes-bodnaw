def find_domino_chain(dominoes):
    def backtrack(chain):
        if len(chain) == len(dominoes):
            if chain[0][0] == chain[-1][1]:
                return chain
            else:
                return None
        
        for i in range(len(dominoes)):
            if not used[i]:
                if len(chain) == 0 or chain[-1][1] == dominoes[i][0]:
                    chain.append(dominoes[i])
                    used[i] = True
                    result = backtrack(chain)
                    if result:
                        return result
                    used[i] = False
                    chain.pop()
        
        return None
    
    used = [False] * len(dominoes)
    chain = []
    return backtrack(chain)

# Example usage:
dominoes1 = [(2, 1), (2, 3), (1, 3)]
chain1 = find_domino_chain(dominoes1)
if chain1:
    print("Valid Domino Chain:", chain1)
else:
    print("No valid chain found for dominoes1")

dominoes2 = [(1, 2), (4, 1), (2, 3)]
chain2 = find_domino_chain(dominoes2)
if chain2:
    print("Valid Domino Chain:", chain2)
else:
    print("No valid chain found for dominoes2")
