#!python3
# -*- coding:utf-8 -*-

def concat_str(a="",b=""):
    '''
      this code is sample that how to use of doctest package.
      example of test by doctest ::
      >>> concat_str("a","b") == "ab"
      True
      >>> concat_str("","") == "" and len(concat_str("","")) == 0
      True
    '''
    
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()