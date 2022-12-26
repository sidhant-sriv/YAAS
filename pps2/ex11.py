import math


def allocate_room(marks):

    if marks < 50:

        start = 1
        end = 400 + marks

        for i in range(start, end + 1):
            if is_perfect(i):
                return i
        return "No room available"

    else:

        start = 500 + marks
        end = 1000

        for i in range(start, end + 1):
            if is_ramanujan(i):
                return i

        for i in range(start, end + 1):
            if is_perfect_square(i):
                return i
        return "No room available"


def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num


def is_ramanujan(num):

    nums = [1, 9, 16, 28, 35, 54, 65, 72, 91, 126, 128, 133, 152, 189, 217, 224, 243, 250, 280, 341, 344, 351, 370, 407, 432, 468, 513, 520, 539, 559, 576, 637, 686, 728, 730, 737, 756, 793, 854, 855, 945, 1001, 1008, 1024, 1027, 1064, 1072, 1125, 1216, 1241, 1332, 1339, 1343]
    return num in nums


def is_perfect_square(num):
    sqrt = int(math.sqrt(num))
    return sqrt**2 == num
