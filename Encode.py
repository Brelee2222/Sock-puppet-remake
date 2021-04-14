def encrint(integer):
  integer_ = hex(int(integer))
  integer = []
  for i in range((len(integer_)-2+(2*(len(integer_) % 2))) // 2):
      try:
        integer.append(int('0x' + integer_[len(integer_)-(2*(i))-2] + integer_[len(integer_)-(2*(i))-1], 0))
      except: 
          integer.append(int('0x' + integer_[2], 0))
  integers = []
  for i in range(len(integer)):
    integers.append(integer[len(integer)-i-1])
  integer = integers
  integers = []
  for i in integer:
    integers.append(chr(i))
  integer = ''.join([str(t) for t in integers])
  return integer
def decrint(string):
  value = '0x'
  for i in range(len(string)):
    if ord(string[i]) >= 16:
      value = value + str(hex(ord(string[i]))).replace('0x', '')
    else: 
      value = value + str(hex(ord(string[i]))).replace('0x', '0')
  value = int(value, 0)
  return value