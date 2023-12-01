def fibonacci_search(sequence, element):
  fib_numbers = [0, 1]
  while fib_numbers[-1] < len(sequence):
    fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
  lower_bound = 0
  upper_bound = len(fib_numbers) - 1
  while lower_bound <= upper_bound:
    mid_point = (lower_bound + upper_bound) // 2
    if sequence[mid_point] == element:
      return mid_point
    elif sequence[mid_point] < element:
      lower_bound = mid_point + 1
    else:
      upper_bound = mid_point - 1
  return -1
def main():
  sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
  position = fibonacci_search(sequence, 13)
  if position != -1:
    print("The position of 13 in the Fibonacci sequence is", position)
  else:
    print("13 is not in the Fibonacci sequence.")
if __name__ == "__main__":
  main()
