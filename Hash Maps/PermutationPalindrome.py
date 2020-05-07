'''
Permutation Palindrome:
    Write an efficient function that checks whether any permutation of an input string is a palindrome.
    Ex: "ivicc" should return True
        "civil" should return False
'''

def PermutationPalindrome(word):
    perm = {}
    for i in range(len(word)):
        if word[i] not in perm:
            # add to dict 
            perm[word[i]] = 1
        else:
            # increment value
            perm[word[i]] += 1
    vals = list(perm.values())
    odd_count = 0
    for elem in vals:
        if elem % 2 != 0:
            odd_count += 1
    return odd_count <= 1
    
def ver2(word):
    perms = set()
    for char in word:
        if char in perms:
            perms.remove(char)
        else:
            perms.add(char)
    return len(perms) <= 1

def main():
    word = 'salas'
    print(PermutationPalindrome(word))
    print(ver2(word))

main()




