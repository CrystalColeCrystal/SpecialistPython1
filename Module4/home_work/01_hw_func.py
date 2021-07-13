# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых трех и последних трех цифр равны.

def lucky_ticket(ticket_number):
   a = ticket_number % 100
   ticket_number = int(str(ticket_number)[::-1])
   b = ticket_number % 100
   if (a % 10 + a // 10) == (b % 10 + b // 10):
      return 'YES'
   else:
      return 'NO'


print(lucky_ticket(123003))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
