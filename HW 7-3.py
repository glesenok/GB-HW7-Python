def make_order(rows, nums):
    return '\n'.join(['*' * rows for _ in range (nums // rows)]) + '\n'

print(make_order(6, 45))
