def main():
    line=input('How many Fibonacci numbers do you want? ')
    rivi = int(line)
    edellinen=1
    nykyinen=1
    tuleva = 2
    k=1
    for i in range(rivi):
        print(k,'. ', edellinen,sep='')
        edellinen = nykyinen
        nykyinen = tuleva
        tuleva = edellinen + nykyinen
        k= k+1





main()