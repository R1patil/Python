import random 
print(random.random())

print(random.randint(1, 10))
print(random.uniform(1.5, 10.5)) 

choices = ['run in one place', 'laugh loudly', 'jump outside the window'] 
print(random.choice(choices)) 

numbers = [1, 2, 3, 4, 5] 
random.shuffle(numbers) 
print(numbers) 