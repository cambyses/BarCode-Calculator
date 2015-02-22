import time

def main():

    barcode = str(input("Enter an 11 Digit Barcode Number: "))
    if len(barcode)<1:
        print ("Not a Natural Number")
    elif len(barcode) != 11:
        print ("Barecode is not an 11 Digit Number")
    else:
        barcode=list(barcode)
        barcode = [int(num) for num in barcode]
        barcode.reverse()
        odd_sum = 0
        i = 0
        while (i<len(barcode)):
            odd_sum = odd_sum + barcode[i]
            i += 2
        odd_sum=odd_sum*3

        even_sum=0
        i=1
        while (i<len(barcode)):
            even_sum = even_sum + barcode[i]
            i += 2

        total = odd_sum + even_sum
        time.sleep(1)
        print("The Total is: ", total)

        time.sleep(1)

        remainder = total % 10
        if remainder == 0:
            print("Answer is 0")
        else:
            print ("The 12th Number is: ", 10-remainder)

main()
