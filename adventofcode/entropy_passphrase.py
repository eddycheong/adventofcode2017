def count_valid_passphrase_duplicates(passphrases):
  count = 0
  
  for passphrase in passphrases:
    count += 1 if valid_passphrase_duplicates(passphrase) else 0

  return count

def count_valid_passphrase_anagrams(passphrases):
  count = 0
  
  for passphrase in passphrases:
    count += 1 if valid_passphrase_anagrams(passphrase) else 0

  return count

def valid_passphrase_duplicates(passphrase):
  words = passphrase.split(" ")
  return len(words) == len(set(words))

def valid_passphrase_anagrams(passphrase):
  words = [''.join(sorted(word)) for word in passphrase.split(" ")]
  return len(words) == len(set(words))

# Helper Functions
def parse_input(inputPath):
  passphrases = []
  
  with open(inputPath) as f:
    for line in f:
      passphrases.append(line.rstrip())

  return passphrases