questions = [
  [
    "Which language  is easy?", "Python", "French", "JavaScript",
    "Php", "None", 'a'
  ],
  [
    "What is the capital of india?", "mumbai", "france", "delhi",
    "kolkata", "None", 'c'
  ],
  [
    "Which planet is known as the Red Planet?", "mercury", "jupiter", "mars",
    "neptune", "None", 'c'
  ],
  [
    "What is the capital of France??", "Rome", "France", "berlin",
    "madrid", "None", 'b'
  ],
  [
    "How many days are there in a leap year?", "366", "365", "364",
    "362", "None", 'a'
  ],
  [
    "who invented light bulb?", "einstein", "newton", "edison",
    "gates", "None", 'c'
  ],
  [
    "What is the national animal of india?", "tiger", "lion", "leopard",
    "peacock", "None", 'a'
  ],
  [
    "largest ocean in the world", "pacific", "indian", "atlantic",
    "arctic", "None", 'a'
  ],
  [
    "currency of japan?", "dollars", "euro", "rupees",
    "yen", "None", 'd'
  ],
  [
    "Largest continent in the world?", "europe", "asia", "africa",
    "australia", "None", 'b'
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0,len(questions)):
    question = questions[i]
    
    print(f"\nQuestion for Rs. {levels[i]} ")
    print(f"{question[0]}")
    print(f"a.{question[1]}             b.{question[2]}")
    print(f"c.{question[3]}             d.{question[4]}")
    answer=input("your answer is: ").lower()
    if(answer==question[-1]):
        money=levels[i]
        print(f"correct answer you have won Rs.{levels[i]}")
    else:
        print('wrong answer!!')
        print("better luck next time")
        break
print(f"Your take home money is {money}")
