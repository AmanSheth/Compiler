#!/bin/bash
gcc -m64 -c -o main.o main.c
nasm -f macho64 -o output.o output.s
gcc main.o output.o -o output.run