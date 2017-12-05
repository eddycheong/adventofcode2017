import math

def spiral_memory(location):
  
  # Edge case to check if the location is at the port
  if location == 1:
    return 0

  # The square root pivot point of the "outer" spiral square at the bottom right.
  # The bottom-right pivot is always the square of an odd number
  pivot = math.ceil(math.sqrt(location)) + (location + 1) % 2

  # The first part determines the minimum distance from the outer square to the port.
  # I refer the locations that takes the minimum distance from the outer square as anchor points
  
  # The second part determines the distance of the actual location from any of the four possible anchor points.
  result = pivot//2 + math.fabs(pivot//2 - (pivot**2 - location) % (pivot -1 ))

  # Convert the result into an integer
  return int(result)