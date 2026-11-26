def main():
    print("this is a function that checks if a number is even or odd")
    even_odd_checker()

def even_odd_checker():
    num = int(input("Enter the number you want to check: "))




    # Check  if the numbers are neggative or zero
    if num <= 0:
        print("Please enter a positive number greater than zero.")

    #2 perform calculation to check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")


main()