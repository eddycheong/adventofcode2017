def spreadsheet_checksum(spreadsheet):
  checksum = 0

  for row in spreadsheet:
    checksum += max(row) - min(row)

  return checksum

def evenly_divisble_checksum(spreadsheet):
  checksum = 0

  for row in spreadsheet:
    row.sort()
    for pos, smaller in enumerate(row):
      for larger in row[pos+1:]:
        if larger % smaller == 0:
          checksum += larger//smaller
          break

  return checksum

# Helper Functions
def parse_input(inputPath):
  spreadsheet = []
  
  with open(inputPath) as f:
    for line in f:
      spreadsheet.append([int(x) for x in line.split()])

  return spreadsheet
