def total_divisor(num):
    return len([j for j in range(1, int(num/2+1)) if num % j == 0])

i = 0
triangular_number = 0
while True:
    print(f'triangular_number= {triangular_number} i={i}')
    if total_divisor(triangular_number) > 500:
        print('Found ', triangular_number)
        break
    triangular_number += i
    i += 1
print(triangular_number)
# Answer 76576500