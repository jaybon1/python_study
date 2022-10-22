def solution(numbers: list):
    sum = 0

    for item in numbers:
        sum = sum + item

    answer = sum / len(numbers)
    return answer
    
def solution(numbers: list):
    return sum(numbers) / len(numbers)
    
solution = lambda numbers : sum(numbers) / len(numbers)


