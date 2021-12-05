#!python3
'''
  sample code about annotation.
   function annotation
     Type annotation is after args identifire (this case is x,y) , semicolon and expression string .
     Return annotation is writed code that "-> 'description-return'"
'''


def func_annotations_default(x: 'description-x', y: 'description-y' = 3) -> 'description_return':
    return x * y
