"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    strItems = [str(j) for j in items]

    for i in strItems:
        if i in frequencies: 
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies
