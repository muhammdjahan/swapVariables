firstnumber = int(input("enter first number: "))
secondNumber = int(input("enter second number: "))

# روش ریاضی برای جابجایی بدون متغیر سوم
firstnumber = firstnumber + secondNumber
secondNumber = firstnumber - secondNumber
firstnumber = firstnumber - secondNumber

print(f" firstnumber = {firstnumber}, secondNumber = {secondNumber}")