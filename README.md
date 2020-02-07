# sqir2circ

This repository provides the script sqir2pdf, which converts programs output by [VOQC](https://github.com/inQWIRE/SQIR) to circuit diagrams using Isaac Chuang's quantum circuit viewer (qasm2circ). qasm2circ is documented and available for download [here](https://www.media.mit.edu/quanta/qasm2circ/). The version in this repository is slightly modified from the original to support visualizing larger circuits.

**Usage**: `./sqir2circ f.qasm` will produce f.pdf. 

Kudos to Isaac Chuang for the original tool! It was useful for debugging VOQC transformations.