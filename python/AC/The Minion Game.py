def minion_game(string):
    # your code goes here
    aeiou_sub_sum,qwer_sub_sum=0,0
    for i in range(len(string)):
        if string[i] in list("AEIOU"):
            aeiou_sub_sum+=len(string)-i
        else:
            qwer_sub_sum+=len(string)-i


    if aeiou_sub_sum==qwer_sub_sum:
        print("Draw")
    elif aeiou_sub_sum>qwer_sub_sum:
        print("Kevin",aeiou_sub_sum)
    else:
        print("Stuart",qwer_sub_sum)
if __name__ == '__main__':
    s = input()
    minion_game(s)