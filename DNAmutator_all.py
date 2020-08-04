#!/usr/bin/env python

# Imports
import getopt, sys # Allows for command line arguments
import os
import chimera
from chimera import runCommand as rc

############################################
def make_mutants():
    try:
    	opts, args = getopt.getopt(sys.argv[1:], '', ['rID=', 'outdir=', 'chain=', 'start=', 'end=', 'chainR=', 'startR='])
    except getopt.error as message:
        raise chimera.NonChimeraError("%s: %s" % (__name__, message)) # Prints error if present
    # initialize
    rID = ''
    outdir = ''
    chain = ''
    start = ''
    end = ''
    chainR = ''
    startR = ''

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
        if o == '--chainR':
            chainR = a	
        if o == '--startR':
            startR = a
    

    # Ensures that all variables have been assigned and ends script if any are missing
    assert(len(rID) != 0)
    assert(len(outdir) != 0)
    assert(len(chain) != 0)
    assert(len(start) != 0)
    assert(len(end) != 0)
    assert(len(chainR) != 0)
    assert(len(startR) != 0)
    
    # open PDB file
    file_out = open('%s/mutants_chain%s.txt' % (outdir, chain), 'a' )
    model = "1"
    pdb_file = "%s.pdb" % (rID)
    #out_dir = "%s" % (outdir)
    #pdb_file = "1zbb_bound.pdb"
    print(outdir)
    print(pdb_file)
    # redefine as integer
    start = int(start)
    end = int(end)+1
    startR = int(startR)

    for x in range(start,end):
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapna A :%s.%s" % (x, chain))
        y = startR - x + 1
        rc("swapna T :%s.%s" % (y, chainR))
        rc("write 0 %s/%s_mutA%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutA%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapna T :%s.%s" % (x, chain))
        y = startR - x + 1
        rc("swapna A :%s.%s" % (y, chainR))
        rc("write 0 %s/%s_mutT%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutT%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapna C :%s.%s" % (x, chain))
        y = startR - x + 1
        rc("swapna G :%s.%s" % (y, chainR))
        rc("write 0 %s/%s_mutC%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutC%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapna G :%s.%s" % (x, chain))
        y = startR - x + 1
        rc("swapna C :%s.%s" % (y, chainR))
        rc("write 0 %s/%s_mutG%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutG%s_chain%s\n' % (rID, x, chain))

    file_out.close()
    return rID, outdir, startR, chainR, chain, start, end

############################################
def main():
    print('running DNAmutator')
    make_mutants()
    print('mutations completed')
############################################
#run main program
main()
	
	