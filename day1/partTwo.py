if __name__ == '__main__':
    with open("input.txt") as file:
        number = 50
        numberOfZeros = 0
        for line in file:
            value = int(line.rstrip()[1:])
            numberOfZeros += (value // 100)
            value = (value % 100)
            direction = line.rstrip()[0:1]
            rotates = False
            if 'L' == direction:
                if (number - value) > 0:
                    rotates = False
                    number = number - value
                elif (number - value) == 0:
                    rotates = True
                    number = number - value
                else:
                    rotates = number != 0
                    number = 100 - (value - number)
            else:
                if (number + value) <= 99:
                    rotates = False
                    number = number + value
                else:
                    rotates = number != 0
                    number = (number + value) - 100

            if rotates:
                numberOfZeros += 1
        print(numberOfZeros)