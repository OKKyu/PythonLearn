#!python3
'''
  sample code about annotation.
'''

# function annotation
#  after args identifire (this case is x,y) , semicolon and expression string .
#  It is return annotation that writed code "-> 'description-return'" 
def func_annotations_default(x: 'description-x', y: 'description-y' = 3) -> 'description-return':
    return x * y