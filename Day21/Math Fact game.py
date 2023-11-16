print("Welcome to Math Facts Game")
print()
print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")
print()

fact_family = int(input("Name your multiples: "))
print()

counter = 0
for i in range(1, 11):
  correct_answer = i*fact_family
  print(i, "x", fact_family)
  answer = int(input("> "))
  if answer == correct_answer:
    print("You got it right!")
    counter += 1
  else:
    print("That's not correct. It should have been", correct_answer)

if counter == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", counter, "out of 10 correct.")
