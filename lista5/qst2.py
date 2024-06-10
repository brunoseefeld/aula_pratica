def Roman(number):

    #tabela de conversões para romanos.
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    conversao=''
     
    while number:
        div = number // num[i]
        number %= num[i]
 
        while div:
            conversao+=str(sym[i])
            div -= 1
        i -= 1
    return conversao
 
# Driver code
if __name__ == "__main__":
    number = 3001
    print("Roman value is:", end = " ")
    print(Roman(number))