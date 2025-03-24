<<<<<<< HEAD
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
=======
#AIzaSyCMX8pHuzKUlp5AgkBtp3SD12MBhvGuc_g
# #supabase password:bDUc47hKFQIr7yz5
#Pg$!7uJ3kX8&zT2#qVwR
import tensorflow as tf
import pandas as pd
import numpy as np
import requests as rq

class Ai:
    def __init__(self):
        pass

print(tf.__version__)
>>>>>>> adde195a48fc3487f95cceb18db0a6b03169c8e7
