def Greeting(name):
    return f"Hello, {name}"
def AverageScore(nums):
    return [len(nums), sum(nums)/len(nums)]
def Evaluate(avgScore):
    if avgScore >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    name = input("What is your name? ")
    print(Greeting(name))
    scores = []
    while True:
        score = int(input("Enter a score (or -1 to finish): "))
        if score == -1:
            break
        scores.append(score)
    avgScore = AverageScore(scores)[1]
    subjects = AverageScore(scores)[0]
    print(f"Subjects: {subjects}")
    print(f"Average Score: {avgScore}")
    print(f"Result: {Evaluate(avgScore)}")