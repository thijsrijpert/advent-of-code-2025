if __name__ == '__main__':
    with open("day1/input.txt") as file:
        number = 50
        numberOfZeros = 0
        for line in file:
            value = int(line.rstrip()[1:]) % 100
            direction = line.rstrip()[0:1]
            if 'L' == direction:
                if (number - value) >= 0:
                    number = number - value
                else:
                    number = 100 - (value - number)
            elif 'R' == direction:
                if (number + value) <= 99:
                    number = number + value
                else:
                    number = (number + value) - 100

            if number == 0:
                numberOfZeros += 1
        print(numberOfZeros)