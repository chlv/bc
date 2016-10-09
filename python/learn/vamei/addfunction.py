class SampleMore(object):
#    def __init__(self , value):
#       self.value = value
    def __call__(self , value):
        print value + 5

add = SampleMore()
print(add(4))
map(add,[4,5,6])