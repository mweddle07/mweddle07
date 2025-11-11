def main():
    n = 0
    n = int(input('How many lines to display? '))
    if n > 1: 
         print(n) 
    for i in range(n): 
         print('*' * n)
print()
main()