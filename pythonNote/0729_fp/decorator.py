
# ======= 1 ========
def decorator(func):
  def wrapper(param):
    print 'start'
    func(param)
    print 'end'
  return wrapper

@decorator
def test(param):
  print "run with param %s"%(param)

# test = decorator(test)
test('test ....')


# ======= 2 ========
def decoratorPrint(fn):
  def a():
    param = fn()
    print('params....', param)
  return a

@decoratorPrint
def test1():
  return range(1, 6)

test1()