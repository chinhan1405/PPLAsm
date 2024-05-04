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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0177\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\7\2v\n\2\f\2\16\2y\13\2\3\2\3\2\5\2}\n\2\3\2\3\2")
        buf.write("\3\3\6\3\u0082\n\3\r\3\16\3\u0083\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u00fa\n\30\3\31\3\31\5\31\u00fe")
        buf.write("\n\31\3\31\5\31\u0101\n\31\3\32\6\32\u0104\n\32\r\32\16")
        buf.write("\32\u0105\3\33\3\33\5\33\u010a\n\33\3\34\3\34\5\34\u010e")
        buf.write("\n\34\3\34\3\34\3\35\3\35\7\35\u0114\n\35\f\35\16\35\u0117")
        buf.write("\13\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u0122\n\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\7\65\u0158\n\65")
        buf.write("\f\65\16\65\u015b\13\65\3\66\3\66\7\66\u015f\n\66\f\66")
        buf.write("\16\66\u0162\13\66\3\66\5\66\u0165\n\66\3\66\3\66\3\67")
        buf.write("\3\67\7\67\u016b\n\67\f\67\16\67\u016e\13\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\38\3w\29\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\2\65\2\67\2")
        buf.write("9\33;\2=\2?\2A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*")
        buf.write("_+a,c-e.g/i\60k\61m\62o\63\3\2\n\5\2\13\13\16\17\"\"\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\4\2$$^^\t\2))^^ddhhppttvv\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\2\u0180\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("9\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\3q\3\2\2\2\5\u0081\3\2\2\2\7\u0087\3\2\2\2\t")
        buf.write("\u008e\3\2\2\2\13\u0093\3\2\2\2\r\u009a\3\2\2\2\17\u009e")
        buf.write("\3\2\2\2\21\u00a6\3\2\2\2\23\u00ab\3\2\2\2\25\u00af\3")
        buf.write("\2\2\2\27\u00b5\3\2\2\2\31\u00b8\3\2\2\2\33\u00be\3\2")
        buf.write("\2\2\35\u00c7\3\2\2\2\37\u00ca\3\2\2\2!\u00cf\3\2\2\2")
        buf.write("#\u00d4\3\2\2\2%\u00da\3\2\2\2\'\u00de\3\2\2\2)\u00e5")
        buf.write("\3\2\2\2+\u00e9\3\2\2\2-\u00ed\3\2\2\2/\u00f9\3\2\2\2")
        buf.write("\61\u00fb\3\2\2\2\63\u0103\3\2\2\2\65\u0107\3\2\2\2\67")
        buf.write("\u010b\3\2\2\29\u0111\3\2\2\2;\u011b\3\2\2\2=\u0121\3")
        buf.write("\2\2\2?\u0123\3\2\2\2A\u0126\3\2\2\2C\u0128\3\2\2\2E\u012a")
        buf.write("\3\2\2\2G\u012c\3\2\2\2I\u012e\3\2\2\2K\u0130\3\2\2\2")
        buf.write("M\u0132\3\2\2\2O\u0135\3\2\2\2Q\u0139\3\2\2\2S\u013c\3")
        buf.write("\2\2\2U\u013f\3\2\2\2W\u0141\3\2\2\2Y\u0143\3\2\2\2[\u0146")
        buf.write("\3\2\2\2]\u0149\3\2\2\2_\u014b\3\2\2\2a\u014d\3\2\2\2")
        buf.write("c\u014f\3\2\2\2e\u0151\3\2\2\2g\u0153\3\2\2\2i\u0155\3")
        buf.write("\2\2\2k\u015c\3\2\2\2m\u0168\3\2\2\2o\u0174\3\2\2\2qr")
        buf.write("\7%\2\2rs\7%\2\2sw\3\2\2\2tv\13\2\2\2ut\3\2\2\2vy\3\2")
        buf.write("\2\2wx\3\2\2\2wu\3\2\2\2x|\3\2\2\2yw\3\2\2\2z}\5g\64\2")
        buf.write("{}\7\2\2\3|z\3\2\2\2|{\3\2\2\2}~\3\2\2\2~\177\b\2\2\2")
        buf.write("\177\4\3\2\2\2\u0080\u0082\t\2\2\2\u0081\u0080\3\2\2\2")
        buf.write("\u0082\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3")
        buf.write("\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\b\3\2\2\u0086\6")
        buf.write("\3\2\2\2\u0087\u0088\7p\2\2\u0088\u0089\7w\2\2\u0089\u008a")
        buf.write("\7o\2\2\u008a\u008b\7d\2\2\u008b\u008c\7g\2\2\u008c\u008d")
        buf.write("\7t\2\2\u008d\b\3\2\2\2\u008e\u008f\7d\2\2\u008f\u0090")
        buf.write("\7q\2\2\u0090\u0091\7q\2\2\u0091\u0092\7n\2\2\u0092\n")
        buf.write("\3\2\2\2\u0093\u0094\7u\2\2\u0094\u0095\7v\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7k\2\2\u0097\u0098\7p\2\2\u0098\u0099")
        buf.write("\7i\2\2\u0099\f\3\2\2\2\u009a\u009b\7x\2\2\u009b\u009c")
        buf.write("\7c\2\2\u009c\u009d\7t\2\2\u009d\16\3\2\2\2\u009e\u009f")
        buf.write("\7f\2\2\u009f\u00a0\7{\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2")
        buf.write("\7c\2\2\u00a2\u00a3\7o\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7e\2\2\u00a5\20\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8")
        buf.write("\7w\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7e\2\2\u00aa\22")
        buf.write("\3\2\2\2\u00ab\u00ac\7h\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\24\3\2\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1")
        buf.write("\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\26\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7")
        buf.write("\7{\2\2\u00b7\30\3\2\2\2\u00b8\u00b9\7d\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd")
        buf.write("\7m\2\2\u00bd\32\3\2\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\34\3\2\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\36\3\2\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc")
        buf.write("\7n\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7g\2\2\u00ce \3")
        buf.write("\2\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7h\2\2\u00d3\"\3\2\2\2\u00d4\u00d5")
        buf.write("\7d\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7i\2\2\u00d7\u00d8")
        buf.write("\7k\2\2\u00d8\u00d9\7p\2\2\u00d9$\3\2\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7f\2\2\u00dd&\3")
        buf.write("\2\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4(\3\2\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7v\2\2\u00e8*\3\2\2\2\u00e9\u00ea")
        buf.write("\7c\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7f\2\2\u00ec,\3")
        buf.write("\2\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7t\2\2\u00ef.\3")
        buf.write("\2\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7w\2\2\u00f3\u00fa\7g\2\2\u00f4\u00f5\7h\2\2\u00f5\u00f6")
        buf.write("\7c\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8\7u\2\2\u00f8\u00fa")
        buf.write("\7g\2\2\u00f9\u00f0\3\2\2\2\u00f9\u00f4\3\2\2\2\u00fa")
        buf.write("\60\3\2\2\2\u00fb\u00fd\5\63\32\2\u00fc\u00fe\5\65\33")
        buf.write("\2\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0100")
        buf.write("\3\2\2\2\u00ff\u0101\5\67\34\2\u0100\u00ff\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0101\62\3\2\2\2\u0102\u0104\t\3\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106\64\3\2\2\2\u0107\u0109\7\60")
        buf.write("\2\2\u0108\u010a\5\63\32\2\u0109\u0108\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\66\3\2\2\2\u010b\u010d\t\4\2\2\u010c\u010e")
        buf.write("\t\5\2\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0110\5\63\32\2\u01108\3\2\2\2\u0111")
        buf.write("\u0115\5;\36\2\u0112\u0114\5=\37\2\u0113\u0112\3\2\2\2")
        buf.write("\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3")
        buf.write("\2\2\2\u0116\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119")
        buf.write("\5;\36\2\u0119\u011a\b\35\3\2\u011a:\3\2\2\2\u011b\u011c")
        buf.write("\7$\2\2\u011c<\3\2\2\2\u011d\u0122\n\6\2\2\u011e\u0122")
        buf.write("\5? \2\u011f\u0120\7)\2\2\u0120\u0122\7$\2\2\u0121\u011d")
        buf.write("\3\2\2\2\u0121\u011e\3\2\2\2\u0121\u011f\3\2\2\2\u0122")
        buf.write(">\3\2\2\2\u0123\u0124\7^\2\2\u0124\u0125\t\7\2\2\u0125")
        buf.write("@\3\2\2\2\u0126\u0127\7-\2\2\u0127B\3\2\2\2\u0128\u0129")
        buf.write("\7/\2\2\u0129D\3\2\2\2\u012a\u012b\7,\2\2\u012bF\3\2\2")
        buf.write("\2\u012c\u012d\7\61\2\2\u012dH\3\2\2\2\u012e\u012f\7\'")
        buf.write("\2\2\u012fJ\3\2\2\2\u0130\u0131\7?\2\2\u0131L\3\2\2\2")
        buf.write("\u0132\u0133\7>\2\2\u0133\u0134\7/\2\2\u0134N\3\2\2\2")
        buf.write("\u0135\u0136\7\60\2\2\u0136\u0137\7\60\2\2\u0137\u0138")
        buf.write("\7\60\2\2\u0138P\3\2\2\2\u0139\u013a\7?\2\2\u013a\u013b")
        buf.write("\7?\2\2\u013bR\3\2\2\2\u013c\u013d\7#\2\2\u013d\u013e")
        buf.write("\7?\2\2\u013eT\3\2\2\2\u013f\u0140\7>\2\2\u0140V\3\2\2")
        buf.write("\2\u0141\u0142\7@\2\2\u0142X\3\2\2\2\u0143\u0144\7>\2")
        buf.write("\2\u0144\u0145\7?\2\2\u0145Z\3\2\2\2\u0146\u0147\7@\2")
        buf.write("\2\u0147\u0148\7?\2\2\u0148\\\3\2\2\2\u0149\u014a\7*\2")
        buf.write("\2\u014a^\3\2\2\2\u014b\u014c\7+\2\2\u014c`\3\2\2\2\u014d")
        buf.write("\u014e\7]\2\2\u014eb\3\2\2\2\u014f\u0150\7_\2\2\u0150")
        buf.write("d\3\2\2\2\u0151\u0152\7.\2\2\u0152f\3\2\2\2\u0153\u0154")
        buf.write("\7\f\2\2\u0154h\3\2\2\2\u0155\u0159\t\b\2\2\u0156\u0158")
        buf.write("\t\t\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015aj\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015c\u0160\5;\36\2\u015d\u015f\5=\37\2")
        buf.write("\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3")
        buf.write("\2\2\2\u0160\u0161\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0163\u0165\7\2\2\3\u0164\u0163\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\b\66\4")
        buf.write("\2\u0167l\3\2\2\2\u0168\u016c\5;\36\2\u0169\u016b\5=\37")
        buf.write("\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016f\u0170\7^\2\2\u0170\u0171\n\7\2\2")
        buf.write("\u0171\u0172\3\2\2\2\u0172\u0173\b\67\5\2\u0173n\3\2\2")
        buf.write("\2\u0174\u0175\13\2\2\2\u0175\u0176\b8\6\2\u0176p\3\2")
        buf.write("\2\2\22\2w|\u0083\u00f9\u00fd\u0100\u0105\u0109\u010d")
        buf.write("\u0115\u0121\u0159\u0160\u0164\u016c\7\b\2\2\3\35\2\3")
        buf.write("\66\3\3\67\4\38\5")
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
    FUNC = 8
    FOR = 9
    UNTIL = 10
    BY = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSE = 15
    ELIF = 16
    BEGIN = 17
    END = 18
    RETURN = 19
    NOT = 20
    AND = 21
    OR = 22
    BOOLLIT = 23
    NUMBERLIT = 24
    STRINGLIT = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    EQUAL = 31
    ASSIGN = 32
    CONCAT = 33
    STRINGCOMPARE = 34
    NOTEQ = 35
    LT = 36
    MT = 37
    LOEQ = 38
    MOEQ = 39
    LP = 40
    RP = 41
    LS = 42
    RS = 43
    COMMA = 44
    NEWLINE = 45
    IDENTIFIER = 46
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'var'", "'dynamic'", "'func'", 
            "'for'", "'until'", "'by'", "'break'", "'continue'", "'if'", 
            "'else'", "'elif'", "'begin'", "'end'", "'return'", "'not'", 
            "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", 
            "'...'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'('", 
            "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "WS", "NUMBERTYPE", "BOOLTYPE", "STRINGTYPE", "VARTYPE", 
            "DYNAMICTYPE", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "RETURN", "NOT", "AND", 
            "OR", "BOOLLIT", "NUMBERLIT", "STRINGLIT", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "ASSIGN", "CONCAT", "STRINGCOMPARE", 
            "NOTEQ", "LT", "MT", "LOEQ", "MOEQ", "LP", "RP", "LS", "RS", 
            "COMMA", "NEWLINE", "IDENTIFIER", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "WS", "NUMBERTYPE", "BOOLTYPE", "STRINGTYPE", 
                  "VARTYPE", "DYNAMICTYPE", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "RETURN", "NOT", "AND", "OR", "BOOLLIT", "NUMBERLIT", 
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
            actions[27] = self.STRINGLIT_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1].replace("'\"", '"').replace("\\b", "\b").replace("\\t", "\t").replace("\\n", "\n").replace("\\f", "\f").replace("\\r", "\r").replace("\\\\", "\\");
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


