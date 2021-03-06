#!/user/bin/python3
# -*- coding: utf-8 -*-

"""
This module contains a set of methods for obtaining a minimal cover
from a set of functional dependencies


 Disclaimer:
 This module does not claim to give an optimal minimal cover.
 For cases where the size, complexity or other distinguishing
 characteristics of an attribute or attributes may largely affect
 performance it is recommend you manually inspect the produced
 results at each stage of the formation
"""

import copy
import pprint

__all__ = ["find_closures", "split_rhs", "mincover"]


def sizeof(attr_list):
    """Return the number of attributes in the given sequence"""
    return len(attr_list)

def remove(attr_list, attr):
    """Remove the specified attribute from the sequence of attributes"""
    return attr_list.replace(attr, "")

def contains(attr_list, attrs):
    """Return whether the sequence contains the specified attribute"""
    for each in attrs:
        if each not in attr_list:
            return False
    return True


def split_rhs (DEPS):
    """Splits FDs with multiple attributes on the RHS to multiple FDs with a
    single attribute on the RHS"""
    FDS = []
    for dep in DEPS:
        for let in dep[1]:
            if not [dep[0],let] in FDS:
                FDS.append([dep[0],let])                    
    return FDS


def find(x1, x2):
    """Return whether x2 is a superset of x1"""
    for i in x1:
        if i not in x2:
            return False
    return True


def find_closures(dependencies):
    """Given a list of dependencies, finds the closure"""
    closures = []

    #For each dependency
    for i in range(len(dependencies)): 

        #We are finding the closure of the LHS
        lhs = dependencies[i][0]

        # True when LHS has been covered already
        if lhs in [s[0] for s in closures]:
            continue
        
        while (True):
            temp = lhs

            #For each dependency x -> y
            for x, y in dependencies:

                # If lhs is a superset of x
                # and y is not part of closure yet add y to the lhs
                if find(x, lhs):
                    if y not in lhs:
                        lhs += y            

            # If no new dependencies are added then finished
            if temp == lhs and lhs != []:
                closures.append((''.join(sorted(dependencies[i][0])), ''.join(sorted(lhs))))                
                break
        
    return closures


def remove_redundant (FDS, closures):
    """Removes redunant functional dependencies by computing and testing closures"""
    i = 0

    while i < len(FDS):
        current = FDS[i]
        deps = copy.deepcopy(FDS)
        deps.remove(FDS[i])
        
        if current[0] not in [fcd[0] for fcd in deps]:        
            deps.insert(i, [current[0], ''])
            removed = True
        new_closure = find_closures(deps)
        
        if closures == new_closure:       
            FDS.remove(FDS[i])
            if removed == True:
                deps.remove(deps[i])
                closures = find_closures(FDS)
                removed = False
        else:
            i += 1
            removed = False

    return FDS


def minimize_lhs (FDS):
    """Minimizes the LHS of FDs by computing closures"""
    for dependency in FDS:
        lhs = dependency[0].replace(',','')
        x = dependency[0].replace(',','')
        y = dependency[1]        

        if sizeof(x) == 1:
            continue
        
        redundant = False    
        for attr in x:
            dependency[0] = remove(x, attr)
            redundant = False
            for dep in FDS:
                if dep == dependency:
                    continue
                if contains(dependency[0], dep[0]) and contains(dep[1], attr):             
                    x = remove(x, attr)
                    lhs = remove(x, attr)
                    redundant = True
                    break
            if redundant == False:
                dependency[0] = lhs
        dependency[0] = ','.join(list(dependency[0]))
    return FDS


def mincover(dependencies):
    """Computes and returns a minimal cover made from the set of FDs"""
    fds = split_rhs(dependencies)
    closures = find_closures(fds)
    fds = remove_redundant(fds, closures)
    fds = minimize_lhs(fds)
    return fds

# Example minimal cover construction
if __name__ == "__main__":
    import pprint
    
    # Original Set of Functional Dependencies
    DEPS = [['A','B'],['ABD','FGH'],['AEH','BD'],
           ['BC','EH'],['C','ACG'],['C','AFH'],
           ['DE','HB'],['DF','AC'],['E','F'],
           ['H','EA']]


    # Functional Dependencies w RHS Split
    NEW = [['A','B'],
    ['ABD','F'],
    ['ABD','G'],
    ['ABD','H'],
    ['AEH','B'],
    ['AEH','D'],
    ['BC','E'],
    ['BC','H'],
    ['C','A'],
    ['C','C'],
    ['C','G'],
    #['C','A'],
    ['C','F'],
    ['C','H'],
    ['DE','H'],
    ['DE','B'],
    ['DF','A'],
    ['DF','C'],
    ['E','F'],
    ['H','E'],
    ['H','A']]


    # One example of a minimal cover
    COVER = [['A', 'B'], ['AD', 'GH'], ['AH', 'D'],
           ['C', 'H'], ['DF', 'C'], ['E', 'F'],
           ['H', 'AE']]

    FDS = split_rhs(DEPS)

    # Testing RHS attributes were split properly
    assert FDS == NEW

    print("Functional Dependencies")
    pprint.pprint(FDS)

    print("-"*60)

    closures = find_closures(FDS)
    pprint.pprint(closures)


    print("-"*60)
    print("Finding Minimal Cover")
    print("-"*60)


    print("_"*60)
    print("")
    print("Removing Redundant FDs")
    print("_"*60)
    print("")

    print("")
    print("-"*60)

    FDS = remove_redundant(FDS, closures)

    print("")
    print("_"*60)
    print("")
    print("Minimizing the RHS")
    print("_"*60)
    print("")

    pprint.pprint(FDS)

    print('-'*60)
    print('-'*60)

    FDS = minimize_lhs(FDS)

    print('-'*60)
    print("")
    print("Minimal Cover")
    print("")
    print('-'*60)

    pprint.pprint(FDS)
