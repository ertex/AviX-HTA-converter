#!/bin/bash

mkdir tmp
cp $1 tmp/filecopy.zip
cd tmp
unzip filecopy.zip
rm -rf filecopy.zip
mv base* avix_out.xml
cd ..
python3 parser.py > out.txt
rm -rf tmp
echo "==================================="
echo "Done conversion"
echo "==================================="
