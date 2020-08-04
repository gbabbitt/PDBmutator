#!/usr/bin/env python

# Imports
import getopt, sys # Allows for command line arguments
import os
import chimera
from chimera import runCommand as rc

############################################
def make_mutants():

    try:
    	opts, args = getopt.getopt(sys.argv[1:], '', ['rID=', 'outdir=', 'chain=', 'start=', 'end='])
    except getopt.error as message:
        raise chimera.NonChimeraError("%s: %s" % (__name__, message)) # Prints error if present
    
    # initialize
    rID = ''
    outdir = ''
    chain = ''
    start = ''
    end = ''

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
        
     # Ensures that all variables have been assigned and ends script if any are missing
    assert(len(rID) != 0)
    assert(len(outdir) != 0)
    assert(len(chain) != 0)
    assert(len(start) != 0)
    assert(len(end) != 0)
    # open PDB
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

    for x in range(start,end):
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa ALA :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutALA%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutALA%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa ARG :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutARG%s_chain%s.pdb\n" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutARG%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa ASN :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutASN%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutASN%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa ASP :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutASP%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutASP%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa CYS :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutCYS%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutCYS%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa GLU :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutGLU%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutGLU%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa GLN :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutGLN%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutGLN%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa GLY :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutGLY%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutGLY%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa HIS :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutHIS%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutHIS%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa ILE :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutILE%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutILE%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa LEU :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutLEU%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutLEU%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa LYS :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutLYS%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutLYS%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa MET :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutMET%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutMET%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa PHE :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutPHE%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutPHE%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa PRO :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutPRO%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutPRO%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa SER :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutSER%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutSER%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa THR :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutTHR%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutTHR%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa TRP :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutTRP%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutTRP%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa TYR :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutTYR%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutTYR%s_chain%s\n' % (rID, x, chain))
        mol = chimera.openModels.open(pdb_file)[0] # Opens molecule
        rc("swapaa VAL :%s.%s" % (x, chain))
        rc("write 0 %s/%s_mutVAL%s_chain%s.pdb" % (outdir, rID, x, chain))
        rc("close 0")
        file_out.write('%s_mutVAL%s_chain%s\n' % (rID, x, chain))

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