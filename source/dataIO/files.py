#from pprint import pprint
import numpy as np
import os

import warnings
warnings.filterwarnings("error", category=np.VisibleDeprecationWarning) 

def read_blocks(filename,delimiter = '\n\n', comment = None,*args,**kwargs):
    """Read a file containing blocks of numerical data separated by a white line.
    
    Return a list, each element of which is a list of the lines in the block.  
    2022/06/29 converted result from dictionary to list.    
    """
    
    f = open(filename, 'r')
    content = f.read()
    f.close()
    pList=[]
    for block in content.split(delimiter):
        if (block.strip() != ''):
            """build a dic with a set of points, first line is used as key"""
            lines=block.split('\n')
            goodlines = [dd for dd in lines if (comment is None) or not(dd.startswith(comment))] 
            goodlines = [gl for gl in goodlines if len(gl.strip())!=0] #il caso di commento e' gia' escluso
            try:
                l = np.array([dd.split() for dd in goodlines],*args,**kwargs)
                l = np.array([dd.split() for dd in goodlines],*args,**kwargs)
            except np.VisibleDeprecationWarning:
                print ('Triying to convert splitted strings with unknown dtype results'+
                       ' in non corresponding lengths. Return array of strings.')
                l = goodlines
            except ValueError:
                print('Data type not corresponding to user-provided dtype. Return array of strings.')
                l = goodlines
                
            pList.append(np.array(l))

    return pList
    
def test_read_blocks(filename=None):

    def print_results(a, title):
        '''pass result and descriptive title for a test.'''
        
        print('\n======',title)
        print('%i blocks read'%len(a))
        print('block shapes: ',[aa.shape for aa in a])
        print('block contents: ')
        for i,aa in enumerate(a):
            print('%i)\n'%(i+1),'[%s\n..\n..\n%s]'%(','.join(map(str,aa[:3])),','.join(map(str,aa[-2:]))))
        return a
    
    filename = r'C:\Users\kovor\Documents\python\pyXTel\source\pyProfile\test\input_data\data_blocks_spaced.dat'
    
    print('read "%s", contains three white-line-separated blocks with initial 3-line # comment followed by 94 couples of data. First block has 6-line comment.'%os.path.join(os.path.basename(os.path.dirname(filename)),os.path.basename(filename)))
    
    a = print_results(read_blocks(filename, comment = '#'),"comment = '#', ignore commented lines, lines are splitted. Return 2xN string array.") #array of strings 2 x N
    
    a = print_results(read_blocks(filename, comment = '#', dtype = float),"comment = '#' with float dtype, Return 2xN float array.") #array of floats 2 x N
    
    a = print_results(read_blocks(filename),"no comment or dtype, lines are splitted but they are inconsistent length. Return string vector with lines.")  # da warning in quanto lo split funziona creando liste. Se queste sono di lunghezze diversa,
                         # la conversione in array restituiscce un array monodimensionale (vettore) di oggetti (lista)

    a = print_results(read_blocks(filename, dtype = float),"dtype, but no comment character, comment lines break consistency. Return string vector with lines.") #lista di array
    
    
    
    
def head(fn,N=10):
    """return first n lines of file `fn`, without reading the other lines.
    
    from https://stackoverflow.com/questions/1767513/read-first-n-lines-of-a-file-in-python"""
    with open(fn) as myfile:
        return [next(myfile) for x in range(N)]
    

def program_path0():
    """first version. Both are from 
    https://stackoverflow.com/questions/51487645/get-path-of-script-containing-the-calling-function
    this one is not working on case 2 of test.
    See also:
    https://note.nkmk.me/en/python-script-file-path/#:~:text=In%20Python%2C%20you%20can%20get,python%20(or%20python3%20)%20command.
    """
    import inspect
    stack = inspect.stack()
    calling_context = next(context for context in stack if context.filename != __file__)
    return calling_context.filename
    #return stack


def program_path():
    """return the path
    
    to the calling file. """
    import sys

    namespace = sys._getframe(1).f_globals  # caller's globals
    #pprint(namespace)
    return namespace['__file__']


def test_program_path():
    """cases:
        1. called from input (VScode python file): 
            <ipython-input-11-0fddf82ac4ab>     
            
        if 2. called from ipython shell running this file:
            %run .../pyXTel/dataIO/files.py
            
        or 3. importing from this function from here with:
            from dataIO.files import test_program_path
            test_program_path()
        
        gives correct result:            
            caller's path: ...\pyXTel\dataIO\files.py
            

       if 4. called from a  .py file containing a copy of 
            this function.
            
            %run .../dataIO/test/test_program_path.py
            
            caller's path: ...\dataIO\test\test_program_path.py
            
        N.B. program_path0 gives incorrect results on case 2. only.
    """ 
    p = program_path0()  
    print("caller's path: ", p )
    return  p
    
    
        
if __name__ == "__main__":
    a = test_program_path()