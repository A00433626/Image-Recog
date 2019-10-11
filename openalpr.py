# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:34:02 2018

@author: DELL
"""
from openalpr import Alpr
import sys
alpr = Alpr("us", "/path/to/openalpr.conf", "/path/to/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
 else 
     alpr.set_top_n(20)
     alpr.set_default_region("md")

results = alpr.recognize_file("/path/to/image.jpg")

i = 0
for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

# Call when completely done to release memory
alpr.unload()