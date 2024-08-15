# Databricks notebook source
def fibonacci_sum(n):
    if n <= 0:
        return 0
    fibo = [0, 1]
    sum = fibo[0] + fibo[1]
    
    while True:
        next_fibo = fibo[-1] + fibo[-2]
        if next_fibo > n:
            break
        fibo.append(next_fibo)
        sum += next_fibo
    
    return sum

# Example usage
n = 10
result = fibonacci_sum(n)
display(result)
