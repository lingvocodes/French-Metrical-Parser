Program for automated metrical markup of French verse.

What it does

The program provides French verses with metrical markup. It gives information about their metre (the number of syllables in each line), type of rhyme (masculine or feminine) and position of caesura (or about its absence). It processes txt-files and creates xml-documents. Each line gets a tag <l>, whose attributes contain the necessary metrical information (id – the line’s number; m – its metre; rh – the type of rhyme in it; caes – the position of caesura (or «no caesura» in case of its absence; the modification of caesura in this line is printed in the square brackets, the alternative variants are placed in the round ones)), and tag <caes/>, which marks up the place of caesura if it has been found.

How to use it

First make sure that the program file and the txt-document with the verse are in the same directory of your computer. Open the software code in «IDLE (Python GUI)» and launch it with F5. Then put the name of the document with the verse in and press Enter. Find an xml-file in the same directory.

Code starter: 
Anastasiya Khromalenkova - 