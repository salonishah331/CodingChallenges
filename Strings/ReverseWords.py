# Reverse Words
# Write a function that takes in a message as a list of characters and reverses the order of the words in place 

# Input: message ['c', 'a', 'k', 'e', '',
#                 'p','o','u','n','d','',
#                 's','t','e','a','l' ] 

# Output: 'steal pound cake' 


def ReverseWords(message):
    word = ''
    arr = []
    for i in range(len(message)):
        word += message[i]
        if message[i] == '' or i == len(message) - 1:
            arr.append(word)
            word = ''

    arr = arr[::-1]
    return arr



# How to define a main function
def main():
    message = ['c', 'a', 'k', 'e', '',
                'p','o','u','n','d','',
                's','t','e','a','l' ] 
    print(ReverseWords(message))

# How to call a main function
main()