# making a game that displays the question and if the answer is right sum and give the money the person is winning

l = [["Q1. Formula of water? ", "1. H2O", "2. O2", "3. H1O", "4. H2E"],
     ["Q2. Which political party won 2014 elctions in India? ", "1. BJP", "2. RJD", "3. AAP", "4. CNG"],
     ["Q3. What is the national song of India?", "1. Jan Gan Man", "2. Vande mataram", "3. Sare jaha se acha", "4. Ekla chlo re"],
     ["Q4. Pea is what? ", "1. Fruit", "2. Dry fruit", "3. Vegetable", "4. Snack"],
     ["Q5. Who owns reliance?", "1. Ambani", "2. Tata", "3. Birla", "4. Malya"]]
l_answers = [1, 1, 2, 2, 1]
count = 0
money = 0
f=1
for i in l:
    for j in i:
        print(j, end="\n")
    ch = int(input("Choose one option: "))
    if ch == l_answers[count]:
        print("Correct")
        money = money+10000*f
        f = f+1
        count = count+1
    else:
        print("Incorrect")


print("You won: Rs ",money)

