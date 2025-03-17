#supabase password:bDUc47hKFQIr7yz5
#AIzaSyCMX8pHuzKUlp5AgkBtp3SD12MBhvGuc_g
#Pg$!7uJ3kX8&zT2#qVwR
import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

import torch as pt
import flask as fl
from importlib.metadata import version

class Ai:
    def __init__(self):
        print("PyTorch version:", version('torch'))
        print("Flask version:", version('flask'))
        # Test PyTorch functionality
        x = pt.randn(3, 3)
        print("\nTest tensor:\n", x)

if __name__ == "__main__":
    ai = Ai()