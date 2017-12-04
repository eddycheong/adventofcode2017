def inverse_captcha(digits):
  sum = 0
  length = len(digits)

  for i in range(length):
    sum += int(digits[i]) if digits[i] == digits[(i + 1) % length] else 0

  return sum

# Testing

# print(inverse_captcha("1122"))
# print(inverse_captcha("1111"))
# print(inverse_captcha("1234"))
# print(inverse_captcha("91212129"))