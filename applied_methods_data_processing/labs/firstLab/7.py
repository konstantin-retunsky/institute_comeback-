numbers = input('input numbers with space: ').split()
numberX = input("number х: ")
numberWasNotFound = True

for indexNumber, number in enumerate(numbers):
    if number == numberX:
        numberWasNotFound = False
        print(f"number {numberX} found at position {indexNumber}")

if numberWasNotFound:
    print(f'Number {numberX} was not found in {" ".join(numbers)} numbers')
