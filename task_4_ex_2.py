def is_palindrome(test_string: str) -> bool:
    if type(test_string) is not str:
        raise ValueError

    normal=[]
    #spec={'/n', '/t', '/r', '/b', '/f', '\'', "\"", "\\",'`','~',
    #    '!','@','#','$','%','^','&','*','(',')','_','-','+','=',
    #    '{','[','}','}','|',':',';','<',',','>','.','?','/', ' '}

    for it in test_string:
        if it.isalnum():
            normal.append(it.lower())

    for index, char in enumerate(normal):
        #print(char, normal[-index-1])
        if not (char==normal[-index-1]):
            return False
        if index > len(normal)/2-1:
            break
    return True

#print('example', 'ака'[1], 'ака'[-2])
#print("".join([chr(x) for x in range(128)]))
#print(is_palindrome('ака'))
#print(is_palindrome('искать Такси'))