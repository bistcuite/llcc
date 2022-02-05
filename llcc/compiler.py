from .lex import CLexer
from .parse import CParser

import llvmlite.ir as ir
import llvmlite.binding as llvm

class CCompiler(object):
    ... # todo