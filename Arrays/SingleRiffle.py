# Single Riffle:
#     write a function to tell us if a full deck of cardsshuffled_deck is a single riffle of two other halves half1 and half2.
#     Input: Half1: [1, 4, 5] Half2: [2, 3, 6] Deck: [1, 2, 3, 4, 5, 6]
#     Output: True

# def SingleRiffle(half1, half2, deck):
#     ptr1 = 0 
#     ptr2 = 0
#     comparedeck = []
#     for i in range(len(deck)):
#         if half1[ptr1] < half2[ptr2]: 
#             comparedeck.append(half1[ptr1])
#             # half1.remove(half1[ptr1])
#             if ptr1 != len(half1) -1:
#                 ptr1 += 1
#         elif half2[ptr2] < half1[ptr1]:
#             comparedeck.append(half2[ptr2])
#             # half2.remove(half2[ptr2])
#             if ptr2 != len(half2) -1 :
#                 ptr2 += 1
#     print(comparedeck)
#     print(ptr1)
#     print(ptr2)
#     if comparedeck == deck:
#         return True
#     else:
#         return False 

def SingleRiffle(half1, half2, deck):
    

def main():
    half1 = [1, 4, 5]
    half2 = [2, 3, 6]
    deck = [1, 2, 3, 4, 5, 6]
    print(SingleRiffle(half1,half2,deck))

main()