import random
colors = ["red","blue","orange "]
result = random.choices(colors, weights=[5,3,1] ,k=10)  
print(result)