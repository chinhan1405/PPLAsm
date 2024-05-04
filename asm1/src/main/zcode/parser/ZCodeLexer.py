# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
# 2111898 Hoang Chi Nhan



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u017e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\7\2x\n\2\f\2\16\2{\13\2\3\2\3\2\5\2\177\n\2")
        buf.write("\3\2\3\2\3\3\6\3\u0084\n\3\r\3\16\3\u0085\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0101\n\31\3\32\3\32\5\32\u0105\n\32\3\32\5\32\u0108")
        buf.write("\n\32\3\33\6\33\u010b\n\33\r\33\16\33\u010c\3\34\3\34")
        buf.write("\5\34\u0111\n\34\3\35\3\35\5\35\u0115\n\35\3\35\3\35\3")
        buf.write("\36\3\36\7\36\u011b\n\36\f\36\16\36\u011e\13\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3 \3 \3 \3 \5 \u0129\n \3!\3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)")
        buf.write("\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\7\66\u015f\n\66\f\66\16\66\u0162\13")
        buf.write("\66\3\67\3\67\7\67\u0166\n\67\f\67\16\67\u0169\13\67\3")
        buf.write("\67\5\67\u016c\n\67\3\67\3\67\38\38\78\u0172\n8\f8\16")
        buf.write("8\u0175\138\38\38\38\38\38\39\39\39\3y\2:\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\2\67\29\2;\34=\2?\2A\2C\35E\36G\37I K!M\"O#Q$S%U&")
        buf.write("W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63q\64\3\2\n\5\2\13\13")
        buf.write("\16\17\"\"\3\2\62;\4\2GGgg\4\2--//\4\2$$^^\t\2))^^ddh")
        buf.write("hppttvv\5\2C\\aac|\6\2\62;C\\aac|\2\u0187\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2;\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3s\3\2\2\2\5\u0083\3")
        buf.write("\2\2\2\7\u0089\3\2\2\2\t\u0090\3\2\2\2\13\u0095\3\2\2")
        buf.write("\2\r\u009c\3\2\2\2\17\u00a0\3\2\2\2\21\u00a8\3\2\2\2\23")
        buf.write("\u00ad\3\2\2\2\25\u00b2\3\2\2\2\27\u00b6\3\2\2\2\31\u00bc")
        buf.write("\3\2\2\2\33\u00bf\3\2\2\2\35\u00c5\3\2\2\2\37\u00ce\3")
        buf.write("\2\2\2!\u00d1\3\2\2\2#\u00d6\3\2\2\2%\u00db\3\2\2\2\'")
        buf.write("\u00e1\3\2\2\2)\u00e5\3\2\2\2+\u00ec\3\2\2\2-\u00f0\3")
        buf.write("\2\2\2/\u00f4\3\2\2\2\61\u0100\3\2\2\2\63\u0102\3\2\2")
        buf.write("\2\65\u010a\3\2\2\2\67\u010e\3\2\2\29\u0112\3\2\2\2;\u0118")
        buf.write("\3\2\2\2=\u0122\3\2\2\2?\u0128\3\2\2\2A\u012a\3\2\2\2")
        buf.write("C\u012d\3\2\2\2E\u012f\3\2\2\2G\u0131\3\2\2\2I\u0133\3")
        buf.write("\2\2\2K\u0135\3\2\2\2M\u0137\3\2\2\2O\u0139\3\2\2\2Q\u013c")
        buf.write("\3\2\2\2S\u0140\3\2\2\2U\u0143\3\2\2\2W\u0146\3\2\2\2")
        buf.write("Y\u0148\3\2\2\2[\u014a\3\2\2\2]\u014d\3\2\2\2_\u0150\3")
        buf.write("\2\2\2a\u0152\3\2\2\2c\u0154\3\2\2\2e\u0156\3\2\2\2g\u0158")
        buf.write("\3\2\2\2i\u015a\3\2\2\2k\u015c\3\2\2\2m\u0163\3\2\2\2")
        buf.write("o\u016f\3\2\2\2q\u017b\3\2\2\2st\7%\2\2tu\7%\2\2uy\3\2")
        buf.write("\2\2vx\13\2\2\2wv\3\2\2\2x{\3\2\2\2yz\3\2\2\2yw\3\2\2")
        buf.write("\2z~\3\2\2\2{y\3\2\2\2|\177\5i\65\2}\177\7\2\2\3~|\3\2")
        buf.write("\2\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\b\2\2\2\u0081")
        buf.write("\4\3\2\2\2\u0082\u0084\t\2\2\2\u0083\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0088\b\3\2\2\u0088\6\3\2\2")
        buf.write("\2\u0089\u008a\7p\2\2\u008a\u008b\7w\2\2\u008b\u008c\7")
        buf.write("o\2\2\u008c\u008d\7d\2\2\u008d\u008e\7g\2\2\u008e\u008f")
        buf.write("\7t\2\2\u008f\b\3\2\2\2\u0090\u0091\7d\2\2\u0091\u0092")
        buf.write("\7q\2\2\u0092\u0093\7q\2\2\u0093\u0094\7n\2\2\u0094\n")
        buf.write("\3\2\2\2\u0095\u0096\7u\2\2\u0096\u0097\7v\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\u0099\7k\2\2\u0099\u009a\7p\2\2\u009a\u009b")
        buf.write("\7i\2\2\u009b\f\3\2\2\2\u009c\u009d\7x\2\2\u009d\u009e")
        buf.write("\7c\2\2\u009e\u009f\7t\2\2\u009f\16\3\2\2\2\u00a0\u00a1")
        buf.write("\7f\2\2\u00a1\u00a2\7{\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4")
        buf.write("\7c\2\2\u00a4\u00a5\7o\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7e\2\2\u00a7\20\3\2\2\2\u00a8\u00a9\7o\2\2\u00a9\u00aa")
        buf.write("\7c\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7p\2\2\u00ac\22")
        buf.write("\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7w\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7e\2\2\u00b1\24\3\2\2\2\u00b2\u00b3")
        buf.write("\7h\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7t\2\2\u00b5\26")
        buf.write("\3\2\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7n\2\2\u00bb\30")
        buf.write("\3\2\2\2\u00bc\u00bd\7d\2\2\u00bd\u00be\7{\2\2\u00be\32")
        buf.write("\3\2\2\2\u00bf\u00c0\7d\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7m\2\2\u00c4\34")
        buf.write("\3\2\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7g\2\2\u00cd\36")
        buf.write("\3\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7h\2\2\u00d0 ")
        buf.write("\3\2\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7u\2\2\u00d4\u00d5\7g\2\2\u00d5\"\3\2\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7h\2\2\u00da$\3\2\2\2\u00db\u00dc\7d\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7i\2\2\u00de\u00df\7k\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0&\3\2\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3\u00e4\7f\2\2\u00e4(\3\2\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9")
        buf.write("\7w\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7p\2\2\u00eb*\3")
        buf.write("\2\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef,\3\2\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7f\2\2\u00f3.\3\2\2\2\u00f4\u00f5")
        buf.write("\7q\2\2\u00f5\u00f6\7t\2\2\u00f6\60\3\2\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7w\2\2\u00fa\u0101")
        buf.write("\7g\2\2\u00fb\u00fc\7h\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe\u00ff\7u\2\2\u00ff\u0101\7g\2\2\u0100\u00f7")
        buf.write("\3\2\2\2\u0100\u00fb\3\2\2\2\u0101\62\3\2\2\2\u0102\u0104")
        buf.write("\5\65\33\2\u0103\u0105\5\67\34\2\u0104\u0103\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0107\3\2\2\2\u0106\u0108\59\35\2")
        buf.write("\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2\u0108\64\3\2")
        buf.write("\2\2\u0109\u010b\t\3\2\2\u010a\u0109\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\66\3\2\2\2\u010e\u0110\7\60\2\2\u010f\u0111\5\65\33\2")
        buf.write("\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u01118\3\2\2")
        buf.write("\2\u0112\u0114\t\4\2\2\u0113\u0115\t\5\2\2\u0114\u0113")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0117\5\65\33\2\u0117:\3\2\2\2\u0118\u011c\5=\37\2\u0119")
        buf.write("\u011b\5? \2\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011f\u0120\5=\37\2\u0120\u0121\b")
        buf.write("\36\3\2\u0121<\3\2\2\2\u0122\u0123\7$\2\2\u0123>\3\2\2")
        buf.write("\2\u0124\u0129\n\6\2\2\u0125\u0129\5A!\2\u0126\u0127\7")
        buf.write(")\2\2\u0127\u0129\7$\2\2\u0128\u0124\3\2\2\2\u0128\u0125")
        buf.write("\3\2\2\2\u0128\u0126\3\2\2\2\u0129@\3\2\2\2\u012a\u012b")
        buf.write("\7^\2\2\u012b\u012c\t\7\2\2\u012cB\3\2\2\2\u012d\u012e")
        buf.write("\7-\2\2\u012eD\3\2\2\2\u012f\u0130\7/\2\2\u0130F\3\2\2")
        buf.write("\2\u0131\u0132\7,\2\2\u0132H\3\2\2\2\u0133\u0134\7\61")
        buf.write("\2\2\u0134J\3\2\2\2\u0135\u0136\7\'\2\2\u0136L\3\2\2\2")
        buf.write("\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139\u013a\7>\2\2")
        buf.write("\u013a\u013b\7/\2\2\u013bP\3\2\2\2\u013c\u013d\7\60\2")
        buf.write("\2\u013d\u013e\7\60\2\2\u013e\u013f\7\60\2\2\u013fR\3")
        buf.write("\2\2\2\u0140\u0141\7?\2\2\u0141\u0142\7?\2\2\u0142T\3")
        buf.write("\2\2\2\u0143\u0144\7#\2\2\u0144\u0145\7?\2\2\u0145V\3")
        buf.write("\2\2\2\u0146\u0147\7>\2\2\u0147X\3\2\2\2\u0148\u0149\7")
        buf.write("@\2\2\u0149Z\3\2\2\2\u014a\u014b\7>\2\2\u014b\u014c\7")
        buf.write("?\2\2\u014c\\\3\2\2\2\u014d\u014e\7@\2\2\u014e\u014f\7")
        buf.write("?\2\2\u014f^\3\2\2\2\u0150\u0151\7*\2\2\u0151`\3\2\2\2")
        buf.write("\u0152\u0153\7+\2\2\u0153b\3\2\2\2\u0154\u0155\7]\2\2")
        buf.write("\u0155d\3\2\2\2\u0156\u0157\7_\2\2\u0157f\3\2\2\2\u0158")
        buf.write("\u0159\7.\2\2\u0159h\3\2\2\2\u015a\u015b\7\f\2\2\u015b")
        buf.write("j\3\2\2\2\u015c\u0160\t\b\2\2\u015d\u015f\t\t\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161l\3\2\2\2\u0162\u0160\3\2\2")
        buf.write("\2\u0163\u0167\5=\37\2\u0164\u0166\5? \2\u0165\u0164\3")
        buf.write("\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u016a")
        buf.write("\u016c\7\2\2\3\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\u016e\b\67\4\2\u016en\3\2\2")
        buf.write("\2\u016f\u0173\5=\37\2\u0170\u0172\5? \2\u0171\u0170\3")
        buf.write("\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0173\3\2\2\2\u0176")
        buf.write("\u0177\7^\2\2\u0177\u0178\n\7\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u017a\b8\5\2\u017ap\3\2\2\2\u017b\u017c\13\2\2")
        buf.write("\2\u017c\u017d\b9\6\2\u017dr\3\2\2\2\22\2y~\u0085\u0100")
        buf.write("\u0104\u0107\u010c\u0110\u0114\u011c\u0128\u0160\u0167")
        buf.write("\u016b\u0173\7\b\2\2\3\36\2\3\67\3\38\4\39\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    WS = 2
    NUMBERTYPE = 3
    BOOLTYPE = 4
    STRINGTYPE = 5
    VARTYPE = 6
    DYNAMICTYPE = 7
    MAIN = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    RETURN = 20
    NOT = 21
    AND = 22
    OR = 23
    BOOLLIT = 24
    NUMBERLIT = 25
    STRINGLIT = 26
    ADD = 27
    SUB = 28
    MUL = 29
    DIV = 30
    MOD = 31
    EQUAL = 32
    ASSIGN = 33
    CONCAT = 34
    STRINGCOMPARE = 35
    NOTEQ = 36
    LT = 37
    MT = 38
    LOEQ = 39
    MOEQ = 40
    LP = 41
    RP = 42
    LS = 43
    RS = 44
    COMMA = 45
    NEWLINE = 46
    IDENTIFIER = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'var'", "'dynamic'", "'main'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'return'", 
            "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'='", "'<-'", "'...'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "WS", "NUMBERTYPE", "BOOLTYPE", "STRINGTYPE", "VARTYPE", 
            "DYNAMICTYPE", "MAIN", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "RETURN", 
            "NOT", "AND", "OR", "BOOLLIT", "NUMBERLIT", "STRINGLIT", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "ASSIGN", "CONCAT", "STRINGCOMPARE", 
            "NOTEQ", "LT", "MT", "LOEQ", "MOEQ", "LP", "RP", "LS", "RS", 
            "COMMA", "NEWLINE", "IDENTIFIER", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "WS", "NUMBERTYPE", "BOOLTYPE", "STRINGTYPE", 
                  "VARTYPE", "DYNAMICTYPE", "MAIN", "FUNC", "FOR", "UNTIL", 
                  "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                  "END", "RETURN", "NOT", "AND", "OR", "BOOLLIT", "NUMBERLIT", 
                  "INTEGER", "DECIMAL", "EXPONENT", "STRINGLIT", "DQ", "CHAR", 
                  "ESCAPE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "ASSIGN", "CONCAT", "STRINGCOMPARE", "NOTEQ", "LT", "MT", 
                  "LOEQ", "MOEQ", "LP", "RP", "LS", "RS", "COMMA", "NEWLINE", 
                  "IDENTIFIER", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[28] = self.STRINGLIT_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


