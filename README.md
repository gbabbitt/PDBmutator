# PDBmutator

PDBmutator is a GUI enabled script to batch run swapna or swapaa commands in chimera on a PDB file. It is tested on UCSF Chimera 1.14 installed Linux Mint 19.3

Within a selected range of a given chain, mutator will create all possible base substitutions (for DNA chain) or all possible 
amino acid replacements (protein chain) and deposit all possible mutant PDB files in a directory. PDBmutator can also model all amino acid replacements present in 1 or more genetic variants aligned to a reference sequence of a CLUSTAL (.aln) file.

You must install perl, python and UCSF Chimera.  Type 'perl PDBmutator.pl' at terminal or command line to launch the GUI. Add information regarding PDB file, directory name, path to chimera executable, chain ID, start and end position on chain.  Select DNA or AA. Select data input, and run 'process variants in alignment' if a CLUSTAL file is being used.  Then push 'execute mutations'. 

NOTE: make sure path to chimera executable is correct for your machine on the GUI

NOTE: To model all AA replacements between position 155 and 157, simply open GUI, select chain type = amino acid and data input to create all possible mutants and then execute mutations. 

NOTE; To model all the AA replacements in the CLUSTAL alignment given (1cdw_align.aln), enter the file name (without the .aln extension), click 'process variants in alignment' and enter 5 when prompted to enter the number of variants at the terminal, then click 'execute mutations'. 

NOTE: For DNA mode, script assumes numbering of nucleotides on forward chain increases (e.g. 1cdw chain b) while numbering on the reverse chain decreases (e.g.1cdw chain c).  To model all DNA substitutions at all 16 sites on the DNA segment in this file, select start position = 1, stop position = 16 and start position on reverse chain = 116

ALSO NOTE: at a given position, script creates all 4 variants for a DNA substitution and all 20 variants an amino acid replacement. Thus when compared to sequence, 1 in 4 DNA subs are silent and 1 in 20 replacements are silent and do not represent any change. KEEP THEM IF YOU ARE ANALYZING ALL SEQUENCE VARIANTS. REMOVE THEM MANUALLY IF YOU ARE ANALYZING MUTANTS FROM A REFERENCE SEQUENCE. 
