class String(str):
    def __init__(self, value):
        super().__init__()
        self.value = str(value)

    def __add__(self, other):
        return String(self.value + str(other))

    def __sub__(self, other):
        other_str = str(other)
        index = self.value.find(other_str)
        if index != -1:
            new_value = self.value[:index] + self.value[index + len(other_str):]
            return String(new_value)
        else:
            return self



result1 = String('New') + String(890)
result2 = String(1234) + 5678
result3 = String('New') + 'castle'
result4 = String('New') + 77
result5 = String('New') + True
result6 = String('New') + ['s', ' ', 23]

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
# print(type(result1))
result7 = String('New bala7nce') - 7
result8 = String('New balance') - 'bal'
result9 = String('New balance') - 'Bal'
result10 = String('pineapple apple pine') - 'apple'
result11 = String('New balance') - 'apple'
result12 = String('NoneType') - None
result13 = String(55678345672) - 7

print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)
print(result13)
# print(type(result7))
