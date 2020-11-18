#!/usr/bin/perl
use Tk;
#use strict;
#use warnings;
use feature ":5.10";
use File::Copy;
use List::Util qw( min );
use List::Util qw( max );
use List::Util qw(min max);
use Statistics::Descriptive();

# initialize
$refID = "1rex";
$alnID = "1rex_align";
$outdir = "pdb_mutants";
$chainID = "a";
$start = 1;
$finish = 130;
#$chainTYPE = "DNA";  # "DNA" or "AA"
$chimera_path = "~/.local/UCSF-Chimera64-1.14/bin/";

#### This creates a GUI to write the control files needed for the GPU accelerated pmemd.cuda pipeline ####

#### Declare variables ####
my $fileID = $refID;
my $dirID = $outdir;
my $pathID = $chimera_path;
my $startID = $start;
my $endID = $finish;

my $AA = 1;
my $DNA = 0;
my $ALL = 0;
my $ALN = 1;

#### Create GUI ####
my $mw = MainWindow -> new; # Creates a new main window
$mw -> title("PDB mutator script for UCSF Chimera"); # Titles the main window

# chain type Frame
my $typeFrame = $mw->Frame(	-label => "CHAIN TYPE",
				-relief => "groove",
				-borderwidth => 2
				);
	my $dnaCheck = $typeFrame->Checkbutton( -text => "DNA",
						-variable=>\$DNA
						);
	my $aaCheck = $typeFrame->Checkbutton( -text => "amino acid",
						-variable=>\$AA
						);
# data type Frame
my $inputFrame = $mw->Frame(	-label => "DATA INPUT - variants",
				-relief => "groove",
				-borderwidth => 2
				);
	my $allCheck = $inputFrame->Checkbutton( -text => "create all possible variants (not available)",
						-variable=>\$ALL
						);
	my $alnCheck = $inputFrame->Checkbutton( -text => "create all variants from protein CLUSTAL .aln file",
						-variable=>\$ALN
						);

    my $alnFrame = $inputFrame->Frame();
		my $alnLabel = $alnFrame->Label(-text=>"file (e.g. 1rex_align) : ");
		my $alnEntry = $alnFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$alnID
					);
        my $listButton = $alnFrame -> Button(-text => "process variants in alignment", 
				-command => \&list
				); # Creates a program close button    



# PDB ID Frame				
my $pdbFrame = $mw->Frame();
	my $fileFrame = $pdbFrame->Frame();
		my $fileLabel = $fileFrame->Label(-text=>"pdb ID (e.g. 1rex) : ");
		my $fileEntry = $fileFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$fileID
					);
	my $dirFrame = $pdbFrame->Frame();
		my $dirLabel = $dirFrame->Label(-text=>"create name of output directory :");
		my $dirEntry = $dirFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$dirID
					);
     my $pathFrame = $pdbFrame->Frame();
		my $pathLabel = $pathFrame->Label(-text=>"path to chimera exe directory :");
		my $pathEntry = $pathFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$pathID
					);     
	my $chainFrame = $pdbFrame->Frame();
		my $chainLabel = $chainFrame->Label(-text=>"chain ID (e.g. a, b, c, etc): ");
		my $chainEntry = $chainFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$chainID
					);
	my $startFrame = $pdbFrame->Frame();
		my $startLabel = $startFrame->Label(-text=>"start position on chain: ");
		my $startEntry = $startFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$startID
					);
      my $endFrame = $pdbFrame->Frame();
		my $endLabel = $endFrame->Label(-text=>"stop position on chain: ");
		my $endEntry = $endFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$endID
					);
       my $chainrFrame = $pdbFrame->Frame();
		my $chainrLabel = $chainrFrame->Label(-text=>"reverse chain ID (DNA only): ");
		my $chainrEntry = $chainrFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$chainrID
					);
       my $startrFrame = $pdbFrame->Frame();
		my $startrLabel = $startrFrame->Label(-text=>"start position on reverse chain (DNA only): ");
		my $startrEntry = $startrFrame->Entry(-borderwidth => 2,
					-relief => "groove",
					-textvariable=>\$startrID
					);
      
# Buttons
my $execButton = $mw -> Button(-text => "execute AA replacements and deletions", 
				-command => \&execute
				); # Creates a main execute button
my $sealButton = $mw -> Button(-text => "seal deletions and finalize", 
				-command => \&seal
				); # Creates a main execute button
my $closeButton = $mw -> Button(-text => "close program", 
				-command => \&close
				); # Creates a program close button



#### Organize GUI Layout ####
$closeButton->pack(-side=>"bottom",
			-anchor=>"s"
			);
$sealButton->pack(-side=>"bottom",
			-anchor=>"s"
			);
$execButton->pack(-side=>"bottom",
			-anchor=>"s"
			);

$fileLabel->pack(-side=>"left");
$fileEntry->pack(-side=>"left");
$dirLabel->pack(-side=>"left");
$dirEntry->pack(-side=>"left");
$pathLabel->pack(-side=>"left");
$pathEntry->pack(-side=>"left");
$chainLabel->pack(-side=>"left");
$chainEntry->pack(-side=>"left");
$startLabel->pack(-side=>"left");
$startEntry->pack(-side=>"left");
$endLabel->pack(-side=>"left");
$endEntry->pack(-side=>"left");
#$chainrLabel->pack(-side=>"left");
#$chainrEntry->pack(-side=>"left");
#$startrLabel->pack(-side=>"left");
#$startrEntry->pack(-side=>"left");



$dirFrame->pack(-side=>"top",
		-anchor=>"e");
$fileFrame->pack(-side=>"top",
		-anchor=>"e");
$pathFrame->pack(-side=>"top",
		-anchor=>"e");
$chainFrame->pack(-side=>"top",
		-anchor=>"e");
$startFrame->pack(-side=>"top",
		-anchor=>"e");
$endFrame->pack(-side=>"top",
		-anchor=>"e");
$chainrFrame->pack(-side=>"top",
		-anchor=>"e");
$startrFrame->pack(-side=>"top",
		-anchor=>"e");
$pdbFrame->pack(-side=>"top",
		-anchor=>"n");


$dnaCheck->pack();
$aaCheck->pack();
$typeFrame->pack(-side=>"top",
		-anchor=>"n"
		);

$alnLabel->pack(-side=>"left");
$alnEntry->pack(-side=>"left");
$allCheck->pack();
$alnCheck->pack();
$alnFrame->pack(-side=>"top",
		-anchor=>"e");
$listButton->pack(-side=>"bottom",
			-anchor=>"s"
			);
$inputFrame->pack(-side=>"top",
		-anchor=>"n"
		);



MainLoop; # Allows Window to Pop Up


print "path to Chimera .exe\t"."$pathID\n";


########################################################################################
######################    SUBROUTINES   #############################################
########################################################################################

sub execute{
mkdir($outdir);
print("\nrunning mutator.pl script\n");
print("number of variants = "."$Vnum\n");
print("\nclose Chimera window when processing is complete\n\n");
if($DNA == 1 && $ALL == 1){system("$pathID"."chimera --script \"DNAmutator_all.py --rID=$fileID --outdir=$dirID --chain=$chainID --start=$startID --end=$endID --chainR=$chainrID --startR=$startrID\"\n");}
if($AA == 1 && $ALL == 1){system("$pathID"."chimera --script \"AAmutator_all.py --rID=$fileID --outdir=$dirID --chain=$chainID --start=$startID --end=$endID\"\n");}
if($DNA == 1 && $ALN == 1){print "\n\n THE ALIGNMENT FILE MUST CONSIST OF PROTEIN SEQUENCES\n\n";}
if($AA == 1 && $ALN == 1){system("$pathID"."chimera --script \"AAmutator_aln.py --rID=$fileID --outdir=$dirID --chain=$chainID --start=$startID --end=$endID --alnID=$alnID --Vnum=$Vnum\"\n");}

}

###################################################################
sub list{
print("\nprocessing .ctl files for variants from .aln file\n");   
sleep(1);
mkdir($outdir.'_ctl');
mkdir($outdir.'_temp');
print "NOTE: reference sequence assumed in first row and variant sequences underneath\n";
print "NOTE: reference sequence MAY NOT have gap symbols (i.e. insertions)\n";
print "NOTE: variant sequences MAY have gap symbols (i.e. deletions)\n";
print "NOTE: the example file (1rex_align.aln) has 8 variants (lysozyme paralogs)\n\n";
print "\nENTER THE NUMBER OF VARIANTS IN YOUR .aln FILE (i.e. number of rows minus one)\n\n";
$varnum = <STDIN>;
chop($varnum);
sleep(1);
$Vnum = $varnum;
# collect array of headers
open(IN, "<"."$alnID".".aln");
@IN = <IN>;
@headers = ();
for (my $i = 0; $i < $varnum+3; $i++){
	 if ($i<=2){next;}
	 my $INrow = $IN[$i];
     my @INrow = split (/\s+/, $INrow);
	 my $header = $INrow[0];
     push(@headers, $header);
	 }
     #print @headers;
	 #print"\n";
	 #exit;


for(my $v = 0; $v <= $varnum; $v++){
    if ($v == 0){next;}
    my $headlabel = $headers[$v-1];
open(OUT, ">"."$outdir"."_ctl/variant$v.com");
#open(OUT, ">"."$outdir"."_ctl/variant$v.com");
#print OUT "mol = chimera.openModels.open($fileID)[0]\n";


print "\nprocessing variant $v"."_$headlabel\n\n";
sleep(2);
$postrack = $startID; # init position
# write swap commands to .ctl file for each variant
for (my $i = 0; $i < scalar @IN; $i++){
	 my $INrow = $IN[$i+$v];
     my $refINrow = $IN[$i];
	 my @INrow = split (/\s+/, $INrow);
	 my @refINrow = split (/\s+/, $refINrow);
     my $header = $INrow[0];
     my $ref_header = $refINrow[0];
     my $sequence = $INrow[1];
     my $ref_sequence = $refINrow[1];
	 #print "my sequence\t"."$sequence\n";
	 #print "my ref sequence\t"."$ref_sequence\n";
     # compare residues
     if ($ref_header =~ m/$fileID/){print "\nREF $ref_header\t"."$ref_sequence\n"."SEQ $header\t"."$sequence\n";
         my @refSEQ = split (//, $ref_sequence);my @SEQ = split (//, $sequence);
         for(my $s = 0; $s < 50; $s++){
            $ref_letter = $refSEQ[$s];
            $seq_letter = $SEQ[$s];
            #print "$ref_letter\t"."$seq_letter\n";
            if($ref_letter ne $seq_letter && $seq_letter ne "-"){
                print "mismatch found\t"; print "$ref_letter\t"."$seq_letter\t"."$postrack\n";
                # convert single letter code to 3 letter code
                if($seq_letter eq 'A'){$three_letter = "ALA"} #1
                if($seq_letter eq 'R'){$three_letter = "ARG"} #2
                if($seq_letter eq 'N'){$three_letter = "ASN"} #3
                if($seq_letter eq 'D'){$three_letter = "ASP"} #4
                if($seq_letter eq 'C'){$three_letter = "CYS"} #5
                if($seq_letter eq 'E'){$three_letter = "GLU"} #6
                if($seq_letter eq 'Q'){$three_letter = "GLN"} #7
                if($seq_letter eq 'G'){$three_letter = "GLY"} #8
                if($seq_letter eq 'H'){$three_letter = "HIS"} #9
                if($seq_letter eq 'I'){$three_letter = "ILE"} #10
                if($seq_letter eq 'L'){$three_letter = "LEU"} #11
                if($seq_letter eq 'K'){$three_letter = "LYS"} #12
                if($seq_letter eq 'M'){$three_letter = "MET"} #13
                if($seq_letter eq 'F'){$three_letter = "PHE"} #14
                if($seq_letter eq 'P'){$three_letter = "PRO"} #15
                if($seq_letter eq 'S'){$three_letter = "SER"} #16
                if($seq_letter eq 'T'){$three_letter = "THR"} #17
                if($seq_letter eq 'W'){$three_letter = "TRP"} #18
                if($seq_letter eq 'Y'){$three_letter = "TYR"} #19
                if($seq_letter eq 'V'){$three_letter = "VAL"} #20
                print OUT "swapaa $three_letter :$postrack.$chainID\n";
                }
			if($ref_letter ne $seq_letter && $seq_letter eq "-"){
			    print "deletion found\t"; print "$ref_letter\t"."$seq_letter\t"."$postrack\n";
				print OUT "select :$postrack.$chainID\n";
				print OUT "delete selected\n"; 
				}
             $postrack= $postrack+1;
			 }
           }
         }
close IN;
print OUT "write 0 $outdir"."_temp/$fileID"."_temp$v"."_chain$chainID.pdb\n";
print OUT "close 0\n";
close OUT;
}
sleep(2);
print("\nprocessing from .aln file is complete\n");   
}
####################################################################
sub seal{
sleep(1);
print("\nIMPORTANT: remove TER lines created by your deletions in each PDB file\n");
print("\...then resave the file and close\n\n");
sleep(1);
for(my $v = 0; $v <= $varnum; $v++){
    if ($v == 0){next;}
	system "gedit $outdir"."_temp/$fileID"."_temp$v"."_chain$chainID.pdb";
	system "pdb4amber -i $outdir"."_temp/$fileID"."_temp$v"."_chain$chainID.pdb -o $outdir/$fileID"."_variant$v"."_chain$chainID.pdb --dry";
    sleep(1);
	}
for(my $v = 0; $v <= $varnum; $v++){
    if ($v == 0){next;}
unlink("$outdir"."_temp/$fileID"."_temp$v"."_chain$chainID.pdb") or die "Can't unlink $outdir"."_temp/$fileID"."_temp$v"."_chain$chainID.pdb\n";
}
rmdir($outdir.'_temp');

print("\n PDBmutator.pl is now complete\n\n");

}

####################################################################
sub close{
 print "IMPORTANT NOTE:structures should now be reduced and energy minimized\n";	
 print "This can be done manually in Chimera with addH and minimize commands\n";
 print "if you are taking these PDB structures to our DROIDS MD program,\n";
 print "these procedures will be done automatically for you during file preparation\n";
 sleep(1);	
 print "\nclosing PDBmutator\n";
 exit;
}
####################################################################
