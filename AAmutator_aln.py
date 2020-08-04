#!/usr/bin/env python

# Imports
import getopt, sys # Allows for command line arguments
import os
import chimera
from chimera import runCommand as rc

############################################
def make_mutants():

    try:
    	opts, args = getopt.getopt(sys.argv[1:], '', ['rID=', 'outdir=', 'chain=', 'start=', 'end=', 'alnID=', 'Vnum='])
    except getopt.error as message:
        raise chimera.NonChimeraError("%s: %s" % (__name__, message)) # Prints error if present
    
    # initialize
    rID = ''
    outdir = ''
    chain = ''
    start = ''
    end = ''
    alnID = ''
    Vnum = ''
    
    # Assigns option values to variables
    for o,a  in opts:
        if o == '--rID':
            rID = a
        if o == '--outdir':
            outdir = a
        if o == '--chain':
            chain = a
        if o == '--start':
            start = a
        if o == '--end':
            end = a
        if o == '--alnID':
            alnID = a
        if o == '--Vnum':
            Vnum = a

    # Ensures that all variables have been assigned and ends script if any are missing
    assert(len(rID) != 0)
    assert(len(outdir) != 0)
    assert(len(chain) != 0)
    assert(len(start) != 0)
    assert(len(end) != 0)
    assert(len(alnID) != 0)
    assert(len(Vnum) != 0)

    # ctl directory
    indir = "%s_ctl" % (outdir)   
    # open PDB
    file_out = open('%s/mutants_chain%s.txt' % (outdir, chain), 'a' )
    model = "1"
    pdb_file = "%s.pdb" % (rID)
    #out_dir = "%s" % (outdir)
    #pdb_file = "1zbb_bound.pdb"
    aln_file = "%s.aln" % (alnID)
    print(outdir)
    print(pdb_file)
    print(aln_file)
    # redefine as integer
    start = int(start)
    end = int(end)+1
    Vnum = int(Vnum)

    for x in range(1,Vnum+1):
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc('read ~/Desktop/%s/variant%s.com' % (indir, x))
        file_out.write('%s_variant%s_chain%s\n' % (rID, x, chain))
    # Close the file
    file_out.close()
    return rID, outdir, chain, start, end

############################################
def main():
    print('running AAmutator')
    make_mutants()
    print('mutations completed')
############################################
#run main program
main()