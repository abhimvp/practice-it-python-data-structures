from collections import deque
def main():
    #add code here
    foods = deque(maxlen=5)
    foods.append("food1")
    print(foods)
    ordered_foods=["food2","food3","food4","food5"]
    foods.extend(ordered_foods)
    print(foods) #1,2,3,4,5
    foods.append("food6")
    print(foods) # gives us the latest foods ordered 6,5,4,3,2
    foods.appendleft("food0")
    print(foods)
    # return

if __name__ == "__main__":
    main()