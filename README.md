# sumchrg_script

SUMCHG_POSTPROCESS2.py takes an input file with data on the charge, or protonation state occupancy, 
of residues on a protein as you increase pH (essentially this is a titration) This data file is 
sumchrg5I6W.out (this specific protein designated by a 4 letter PDB code in this case 5I6W). 
SUMCHG_POSTPROCESS2.py takes in the data and prints out formatted data on the protonation states 
(being the average, stdev, min, max, diff) in a new file called post_sumchrg5I6W.out
