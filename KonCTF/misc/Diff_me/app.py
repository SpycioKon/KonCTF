import random
secret_value = random.randint(1,10000) 
input2 = input("Input(): Guess the secret number: ") 

if input2 == secret_value: 
    print "Zlick3rCTF{H0w_c0ulD_y0u_d0??}"
else: 
    print "wrong answer"
