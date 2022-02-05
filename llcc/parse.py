from .lex import CLexer
from sly import Parser

class CParser(Parser):
	tokens = CLexer.tokens

	@_('')
    def block(self, p):
        return ('block', )
    @_('statement block')
    def block(self, p):
        return ('block', p.statement, *p.block[1:])
      
    @_('')
    def in_block(self, p):
        return ('in_block', )
    @_('in_statement in_block')
    def in_block(self, p):
        return ('in_block', p.in_statement, *p.in_block[1:])

    @_('INT')
    def return_type(self, p):
        return ('return_type','int',p.lineno)
    @_('CHAR')
    def return_type(self, p):
        return ('return_type','char',p.lineno)
    @_('BOOL')
    def return_type(self, p):
        return ('return_type','bool',p.lineno)
    @_('FLOAT')
    def return_type(self, p):
        return ('return_type','float',p.lineno)
    @_('VOID')
    def return_type(self, p):
        return ('return_type','void',p.lineno)
	
	@_('return_type ID SEMICOLON')
	def var_declare(self, p):
		return ('var_declare', p.return_type, p.ID,(), p.lineno)
	@_('return_type NAME ASSIGN expr SEMICOLON')
	def var_declare(self, p):
		return ('var_declare', p.return_type, p.NAME, (p.expr,), p.lineno)