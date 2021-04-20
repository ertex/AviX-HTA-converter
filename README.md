# AviX-HTA-converter
A script to generate a HTA graph in LaTeX Tikiz from a AviX savefile
The script only generates the layout and name of the blocks and not the look/format of the blocks all is generated as basic as possible.
See Example files for clarification

# Issues
Names containing special LaTeX characters cause problems, eg. \%_$]()& etc 
Using Multiple unconnected lines can cause them to overlap, they are sepperated by a sepperatior in output though.
Operations with identical names cause trouble for the Tikz builder as the ID of the block is generated the same as the name.

# Usage

if you are running linux run ./converter FILENAME.avx4 and the output should be in output.txt

if running Windows create a folder named tmp in the root directory
	Unzip the FILENAME.avx4 (it is a compressed folder) rename the output to "avix_out.xml"
	place the file in your tmp directory and run parser.py
 
Please Note, This script is not very robust and intended for a one time usage
