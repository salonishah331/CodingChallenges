# Parentheses Matching 
# Given the index of the opening parentheses, give the index of the closing parentheses
# sentence = "((()((()))", index = 4, output = 9

def closing_parentheses(sentence, opening):
    stack = [] #create a list
    for i in range(opening,len(sentence)): #start at index and iterate through end
        if sentence[i] == '(': 
            stack.append(sentence[i]) #if an opening parentheses add to stack
        else:
            stack.pop() #if a close parentheses remove last element of stack
            if stack == []: #if the stack is empty return the index
                return i



def main():
    sentence = "((()((()))"
    index = 4
    print(closing_parentheses(sentence,index))

main()
        


