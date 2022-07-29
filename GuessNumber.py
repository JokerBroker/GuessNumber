import random
def guess(x):
    random_number=random.randint(1,x)
    num=0
    print(random_number)
    while num!=random_number:
       num=int(input(f"Enter your guess between 1 and {x}: "))
       if num<random_number:
        print("Number is too low")
       elif num>random_number:
        print("Number is too high")
      
    print("Number correct :)")
guess(10)