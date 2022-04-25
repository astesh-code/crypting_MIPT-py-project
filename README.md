# Overview
**CodeIt** is a small python module/utility performs different algorithms of ciphering or deciphering of _.txt_ files.
# Features
 - [Ceasar ciphering and hacking with frequency analysis](https://en.wikipedia.org/wiki/Caesar_cipher);
 - [Vigenere ciphering](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher);
 - [Vernam ciphering](https://en.wikipedia.org/wiki/Vernam_cipher);
 - Auto key generating;
 - Console and module usage
# Requirements
 - Python 3.6 and above;
 
# Usage
### As a console uitlity
```
 CodeIt_console.py <arguments>
 Required arguments:
    -h, --help                : show help message and exit
    -m, --mode                : Mode : {c, d ,h} : for ciphering, deciphering and hacking for caesar only
    -t, --type                : Way of ciphering : {caesar, vigenere, vernam} 
    -i, --input               : Input txt file
    -o, --output              : Output txt file
 Optional arguments:
  -k KEY, --key KEY           : File with a key. Optional argument for coding, obligatory for decoding
 ```

## Usage examples
Cipher with Caesar method. Original text in _in.txt_, key in _key.txt_, output will be in _out.txt_ :
 ```
 python3 main.py -m c -type caesar -i in.txt -o out.txt -k key.txt
 ```
Use Vernam method to cipher _input.txt_ file to _outplut.txt_. Key will be generated automatically and written to _key.txt_:
 ```
 python3 main.py --mode c --type vernam --input input.txt --output output.txt
 ```
Decipher Vigenere-coding file with _key.txt_ key:
 ```
 python3 main.py -m d -type Vigenere -i in.txt -o out.txt -k key.txt
 ```
Attemplt to hack Caesar-ciphering file. Found key will be written to _key.txt_, text to _out.txt_:
 ```
 python3 main.py -m h -type caesar -i in.txt -o out.txt
 ```

