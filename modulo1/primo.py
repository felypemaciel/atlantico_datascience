def prime(number):
    if number > 1:
        for i in range(2, int(number/2) + 1):
            if (number % i == 0):
                print("Não é primo.")
                break
            else:
                print("É primo.")
                break
    else:
        print("Não é primo.")