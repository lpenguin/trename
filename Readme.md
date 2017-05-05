# trename - utility for renaming files

## Examples
```bash
>  ls -1
16043_ACAGTG_R1_boston.txt
16045_ACTTGA_R1_boston.txt
16046_ATTCCT_R1_boston.txt
16047_ATGTCA_R1_boston.txt
16048_ATTCCT_R2_boston.txt
16050_GTGGCC_R2_texas.txt
16051_ACTGAT_R2_texas.txt
16052_ACAGTG_R2_texas.txt


> trename '{sample}_{readno}_{subid}.txt' '{sample}_{subid}_{readno}.txt' *.txt
> ls -1
16043_ACAGTG_boston_R1.txt
16045_ACTTGA_boston_R1.txt
16046_ATTCCT_boston_R1.txt
16047_ATGTCA_boston_R1.txt
16048_ATTCCT_boston_R2.txt
16050_GTGGCC_boston_R2.txt
16051_ACTGAT_boston_R2.txt
16052_ACAGTG_boston_R2.txt

```
## Installation
```bash
pip install https://github.com/lpenguin/trename/archive/master.zip
# or
git clone https://github.com/lpenguin/trename
cd trename
python setup.py install
```
## Getting help
```bash
> trename -h
usage: trename [-h] [-v] [-n] [-D] from_tpl to_tpl [files [files ...]]

positional arguments:
  from_tpl       template for old file name
  to_tpl         template for new file name
  files          files that will be renamed

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print old name and new name for each file
  -n, --dry-run  print names, do not actually rename
  -D, --debug    print debug information
```
