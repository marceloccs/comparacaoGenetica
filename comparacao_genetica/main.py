import service.FileExtractor as fe
import service.HTMLWriter as hw

hw.printHTML( fe.extract("../assert/16s_bacteria.fasta"), "../output/bacteria.html","0,0,0")
hw.printHTML( fe.extract("../assert/18s_humano.fasta"), "../output/humano.html","255,0,0")
