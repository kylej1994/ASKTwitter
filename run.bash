#!/bin/bash
python dp.py Kyle/file.txt $1 > song.txt
cat song.txt | espeak --stdout > tmp.wav && sox -m out2.wav tmp.wav mix.wav
sleep 2
cat song.txt
