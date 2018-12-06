# Avería Libre

Avería means "breakdown" or "mechanical damage" in Spanish - and is related to the root of the English word "average." Averia Libre is based on the average of 725 fonts in the Google Fonts collection, and both glyph outlines and metrics are the result of the averaging process described at iotic.com/averia

## Variable Font Specimen 
![Averia](https://github.com/eliheuer/averia-libre-vf/raw/vf-mastering/docs/images/animated-specimen.gif)

## Building From Source
Note: A few dependencies are required for this to work, please see the source documentation [here](https://github.com/eliheuer/orbitron-vf/tree/master/sources).

To build the fonts; clone this repo, then navigate to its root directory in a terminal and run:
```
python3 sources/BUILD.py --ttfautohint "-I -W --increase-x-height=0 --stem-width-mode=sss --default-script=latn"
```
This will build new fonts in the `fonts` directory and apply autohinting.

Additional options are available by adding flags to the build script, for example, if you wanted to update the DrawBot specimen, prepare the font for a PR to Google Fonts and test with FontBakery, we could run:
```
python3 sources/BUILD.py --googlefonts ~/Google/fonts/ofl/orbitron --fontbakery --drawbot --ttfautohint "-I -W --increase-x-height=0 --stem-width-mode=sss --default-script=latn"
```
For more help, run:
```
python3 sources/BUILD.py --help
```

## License
Averia Libre VF is licensed under the SIL Open Font License v1.1 (<http://scripts.sil.org/OFL>). 
To view the copyright and specific terms and conditions please refer to [OFL.txt](https://github.com/eliheuer/averia-libre-vf/blob/master/OFL.txt)

## Downloading Font Files (TTF)
Find binary releases in the `fonts` directory of this repo. 

## Installation Instructions
- [GNU+Linux](https://wiki.archlinux.org/index.php/fonts#Manual_installation)
- [MacOS](https://support.apple.com/en-us/HT201749)
- [Windows](https://support.microsoft.com/en-us/help/314960/how-to-install-or-remove-a-font-in-windows)

## Getting Involved
Would you like to contribute to the development of this font? Here is how **you** can help:

1. Tell us about any bugs you find, or enhancements you would like to see on the issue tracker: [https://github.com/eliheuer/averia-libre-vf/issues](https://github.com/eliheuer/averia-libre-vf/issues)

2. Contribute directly to the fonts. This repository contains a complete set of source files and build documentation. Make changes and submit a pull request. Make changes and submit a pull request.
