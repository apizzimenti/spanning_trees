# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 12:21:16 2018

@author: MGGG
"""

'''
The sampler class:
    
    variables: graph, num_partitions, num_blocks, list of trees
    
    functions: random_sample_wilson (import from tree sample)
     divide and consquer
     
    Walk tools ... takes a tree in the list of trees and walks until it meets the criterion... clean up walk tools, and import from there...
    
    
    projections (import from projection tools)
    
The tree class: 
    extends graph
    
    variables: root, topological_ordering'''

class Sampler:
    ''' blah '''
    
    def __init__(self, graph, num_partitions, num_blocks, trees, sampling_function):
        ''' blah '''
        # TODO
        self.graph = graph
        self.num_partitions = num_partitions
        self.num_blocks = num_blocks
        self.trees = trees
        self.sampling_function = sampling_function


class Tree:
    ''' blah '''

    def __init__(self, root, topological_ordering):
        ''' blah '''
        # TODO
