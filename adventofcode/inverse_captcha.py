def inverse_captcha(digits, step):
  sum = 0
  length = len(digits)

  for i in range(length):
    sum += int(digits[i]) if digits[i] == digits[(i + step) % length] else 0

  return sum

def inverse_captcha_next(digits):
  return inverse_captcha(digits, 1)

def inverse_captcha_halfway(digits):
  return inverse_captcha(digits, len(digits)//2)