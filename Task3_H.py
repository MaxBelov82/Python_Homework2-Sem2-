# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково:
#     "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе 
# стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они 
# складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

word = str(input())
x = len(word)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if word[x - i] == word[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("не палиндром")
else:
  print("палиндром")