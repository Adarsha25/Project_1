def search(pat, txt):
    M=len(pat)
    N=len(txt)

    # looping through the String
    for i in range(N-M+1):
        j = 0

        # searching the match with index i
        while (j < M):
            if (txt[i+j] != pat[j]):
                break
            j+=1

            if (j==M):
                print('The pattern is found at ',i)


# Driver code
txt = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
pat = 'wood'

# function calling
search(pat, txt)

