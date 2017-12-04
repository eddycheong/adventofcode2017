def inverse_captcha(digits):
  sum = 0
  length = len(digits)

  for i in range(length):
    sum += int(digits[i]) if digits[i] == digits[(i + 1) % length] else 0

  return sum