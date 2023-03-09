import fire

def hello(name="mr.D"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)