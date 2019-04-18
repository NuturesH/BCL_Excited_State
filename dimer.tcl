mol new 3A_protein.pdb
#loading new molecule
set pro [atomselect top "resname BCL"]
#select same residue that designation
set number [lsort -unique -integer [$pro get resid]]
#echo $number
#get the resid of designation residue
foreach i $number {
    #echo $i
    set sourr_residue [atomselect top "{same residue as within 3 of resid $i}"]
 #   echo $i
    #select sourrding residues that it with the center residues distance in 5 A. 
    set sourr_resid [lsort -unique -integer [$sourr_residue get residue]]
  #  echo $sourr_resid
    foreach j $sourr_resid {
	#echo BCL$i\_$name_two$j
        set name_two [lsort -unique [[atomselect top "residue $j"] get resname]]
        mkdir BCL$i\_$name_two$j
        set BCL [atomselect top "resid $i"]
        set BCL_AA [atomselect top "{resid $i} or {residue $j}"]
        #$BCL writepdb BCL$i\_$name_two$j\/BCL$i.pdb
        $BCL_AA writepdb BCL$i\_$name_two$j\/BCL$i\_$name_two$j.pdb
	$BCL delete
	$BCL_AA delete
        }
    unset sourr_resid
    $sourr_residue delete
}
mol delete top
