def print_rangoli(size):
    
    row = ((size-1)*4)+1
    col = ((size-1)*2)+1
    alphabets = ['x']
    for i in range(97, 97+size):
        letter = chr(i)
        alphabets.append(letter)

    left = ''
    center = alphabets[size]
    right = ''
    for i in range(size, 0, -1):
        print(left.rjust(col, '-'), end="")
        print(center.center(3, '-'), end="")
        print(right.ljust(col, '-'))
        left = left + '-' + center
        right = center + '-' + right
        center = alphabets[i-1]

    left = list(left)
    left.pop()
    left.pop()
    temp = "".join(left)
    left = temp
 
    right = list(right)
    right.reverse()
    right.pop()
    right.pop()
    right.pop()
    right.reverse()
    temp = "".join(right)
    right = temp

    for i in range(2, size):#+1):
        print(left.rjust(col+2, '-'), end="")
        print(right.ljust(col+2, '-'))
        
        left = list(left)
        left.pop()
        left.pop()
        temp = "".join(left)
        left = temp

        right = list(right)
        right.reverse()
        right.pop()
        right.pop()
        right.reverse()
        temp = "".join(right)
        right = temp
    
    left = list(left)
    left.reverse()
    left.pop()
    left.reverse()
    temp = "".join(left)
    left = temp      
    print(left.center((col*2)+4, '-'))

if __name__ == '__main__':
    n = 5#int(input())
    print_rangoli(n)