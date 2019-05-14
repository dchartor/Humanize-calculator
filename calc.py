operations = {
    '*': 'multiplied by ',
    '/': 'divided by ',
    '+': 'plus ',
    '-': 'minus ',
    '=': 'equals '
}

numWords = ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]
tens = ['twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']
thousands = ['hundred ', 'thousand ','million ', 'billion ', 'trillion ']


def up_to_3_chars(num:int) -> str :
    ''' 
    Convert number only up to 3 chars to words representation
    '''
    first = num // 100
    second = num // 10 % 10
    third = num % 10
    
    converted = ''

    if first != 0:
        converted += numWords[first] + thousands[0]
    
    if second <= 1:
        converted += numWords[num % 100]
    
    elif second > 1:
        converted += tens[second - 2] + numWords[third] 
    
    return converted


def num2word(num:str) -> str:
    start = 3
    flag = True
    counter = 1
    fin = ''

    while flag:
        part = num[-start:]
        num = num[:-start]
        
        if num == '':
            flag = False 
        
        if num != '':
            fin = thousands[counter]+ up_to_3_chars(int(part)) + fin
        else:
            fin = up_to_3_chars(int(part)) + fin
            
        counter += 1
   
    return fin


def converter(mathExpr:str) -> str:
    
    mathExpr = mathExpr.strip().rstrip().split(' ')
    result = ''
    
    try:
        for char in mathExpr:
            if char.isdigit():
                result += num2word(char)
            else:
                result += operations.get(char)
    except:
        return 'Invalid input'

    return result


if __name__ == '__main__':
    string = input('Enter a string with whitespace between each char: ')
    result = converter(string)
    print(result)