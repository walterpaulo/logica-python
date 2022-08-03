def simple_generator():
  x = 1
  yield x + 1
  yield x + 2

generator_object = simple_generator()

print(generator_object)
# print(next(generator_object))