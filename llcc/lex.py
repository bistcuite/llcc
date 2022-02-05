from sly import Lexer

class CLexer(Lexer):
    tokens = {
        NAME,
        NUMBER,STRING,
        PLUS,MINUS,MUL,DIV,MOD,
        EQ,NEQ,LT,GT,LE,GE,
        ASSIGN,
        SEMICOLON,
        LPAREN,RPAREN,
        LBRACE,RBRACE,
        LBRACKET,RBRACKET,
        IF,ELSE,
        WHILE,
        FOR,
        RETURN,
        COMMA,
        EOF,
        INT,CHAR,VOID,BOOL,
        TRUE,FALSE,
        NOT,AND,OR,
        COMMENT,HASHTAG,
        INCLUDE,
    }

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    STRING = r'\"([^\\\n]|(\\.))*?\"'
    PLUS = r'\+'
    MINUS = r'-'
    MUL = r'\*'
    DIV = r'/'
    MOD = r'%'
    EQ = r'=='
    NEQ = r'!='
    LT = r'<'
    GT = r'>'
    LE = r'<='
    GE = r'>='
    ASSIGN = r'='
    SEMICOLON = r';'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'
    LBRACKET = r'\['
    RBRACKET = r'\]'
    NOT = r'!'
    AND = r'&&'
    OR = r'\|\|'
    HASHTAG = r'\#'

    NAME['if'] = IF
    NAME['else'] = ELSE
    NAME['while'] = WHILE 
    NAME['for'] = FOR
    NAME['return'] = RETURN
    NAME['int'] = INT
    NAME['char'] = CHAR
    NAME['void'] = VOID
    NAME['bool'] = BOOL
    NAME['true'] = TRUE
    NAME['false'] = FALSE
    NAME['include'] = INCLUDE
    
    @_(r'\n+')
    def ignore_newline(self,t):
        self.lineno += t.value.count('\n')
    
    @_(r'//.*')
    def ignore_comment(self,t):
        pass