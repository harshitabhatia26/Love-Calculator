
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

string = name1 + name2
t = string.count('t')
r = string.count('r')
u = string.count('u')
e = string.count('e')
l = string.count('l')
o = string.count('o')
v = string.count('v')

true = t + r + u + e
love = l + o + v + e 

true1 = str(true)
love1 = str(love)
score = true1 + love1 
score_no = int(score)

if score_no <10 or score_no >90 : 
  print(f"Your score is {score}, you go together like coke and mentos")
elif score_no >40 and score_no <50 :
    print(f"Your score is {score}, you are alright together")
else : print("Your score is " + score)

input("Press ENTER to exit")
