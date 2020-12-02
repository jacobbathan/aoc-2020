def expenseReport():
    report = open('input.txt', 'r')
    report_list = report.read().splitlines()
    cast_report_list = []
    # report_list = report_list.split(',')

    report.close()
    for item in report_list:
        cast_report_list.append(int(item))

    values = []

    values = twoSumExpense(cast_report_list, 2020)

    print(values[0] * values[1])

    three_values = threeSumExpense(cast_report_list, 2020)

    print(three_values[0][0] * three_values[0][1] * three_values[0][2])


def twoSumExpense(array, target):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == target:
                return [array[i], array[j]]


def threeSumExpense(array, target):
    output = []
    array.sort()
    length = len(array)
    for i in range(length):
        left = i + 1
        right = length - 1
        if array[i - 1] == array[i]: continue
        while left < right:
            total = array[i] + array[left] + array[right]
            if total == target:
                output.append([array[i], array[left], array[right]])
                while left < right and array[left] == array[left + 1]:
                    left += 1
                while left < right and array[right] == array[right - 1]:
                    right -= 1
                left, right = left + 1, right - 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return output


        

expenseReport()
