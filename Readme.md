# trename - utility for renaming files

## Examples
```bash
>  ls -1                                                                                                                                                                        18:01:47
16043_ACAGTG_R1_boston.txt
16045_ACTTGA_R1_boston.txt
16046_ATTCCT_R1_boston.txt
16047_ATGTCA_R1_boston.txt
16048_ATTCCT_R1_boston.txt
16050_GTGGCC_R1_texas.txt
16051_ACTGAT_R1_texas.txt
16052_ACAGTG_R1_texas.txt


> trename '{sample}_{readno}_{subid}.txt' '{sample}_{subid}_{readno}.txt' *.txt
> ls -1
16043_ACAGTG_boston_R1.txt
16045_ACTTGA_boston_R1.txt
16046_ATTCCT_boston_R1.txt
16047_ATGTCA_boston_R1.txt
16048_ATTCCT_boston_R1.txt
16050_GTGGCC_boston_R1.txt
16051_ACTGAT_boston_R1.txt
16052_ACAGTG_boston_R1.txt

```
## Installation
```bash
python setup.py install
# or
pip install https://github.com/lpenguin/trename/archive/master.zip
```
## Getting help
```bash
> trename -h
usage: trename [-h] [-v] [-n] [-D] from_tpl to_tpl [files [files ...]]

positional arguments:
  from_tpl       Template for old file name
  to_tpl         Template for new file name
  files          Files that will be renamed

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Print old name and new name for each file
  -n, --dry-run  Print names, do not actually rename
  -D, --debug    Print debug information
```