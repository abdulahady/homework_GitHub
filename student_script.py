#!/usr/bin/env python3
"""
student_script.py — Version 1
PyROOT homework: create, fill, and print histogram entries
"""
import ROOT
# Create a 1D histogram: 50 bins from -5 to 5
h = ROOT.TH1F("h", "Random Uniform;x;Entries", 100, -5, 5)
# Fill with 1000 uniform random numbers
for i in range(5000):
    h.Fill(ROOT.gRandom.Uniform(-5, 5))
# Print number of entries
print("Histogram name:", h.GetName())
print("Number of bins:", h.GetNbinsX())
print("Number of entries:", h.GetEntries())
