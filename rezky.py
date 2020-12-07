# No 1 Hashtag

def hashtag(x):
    if len(x) > 140:
        return False
    elif x == '':
        return False
    else:
        capital = x.title()
        ilang = capital.replace(' ', '')
        tambah = str('#')+ilang 
        return tambah
        
x = str(input('Masukkan Kalimat: '))
print(hashtag(x))
print(hashtag('Hello there how are you doing'))
print(hashtag('  Hello World '))
print(hashtag(''))


# No 2 Phone Number

def phonenumber():
    x = list(map(int,input('Input Angka: ').split())) # Input 1 2 3 4 5 6 7 8 9 0
    kurung = x[:3]
    garis = x[3:6]
    akhir = x[6:]
    return (f'({kurung}),{garis}-,{akhir}') 
print(phonenumber())


# No 3 Odd Even

def sortoddeven(x):
    y = sorted(x)
    x = y
    ganjil = []
    genap = []
    for i in x:
        if i%2 == 0:
            genap.append(i)
        else:
            ganjil.append(i)
    genap.reverse()
    ganjil.insert(2, genap[0])
    ganjil.insert(3, genap[1])
    ganjil.insert(5, genap[2])
    print (ganjil)
sortoddeven([5,3,2,8,1,4])

# No 4 Hollow Triange

def hollowtriangle(x):
    r = ''
    for i in range (x):
        if i == 0 :
            r += ' '*(x)
            r += '*'
        elif 0<i<x-1 :
            r += '_'*(x-i)
            r += "*"
            r += '_'*(2*i-1)
            r += '*'
        elif i == (x-1) :
            r += '_'
            r +='*'*(2*x)
        r += '\n'
    return r

x = int(input('Length: '))
print(hollowtriangle(x))
