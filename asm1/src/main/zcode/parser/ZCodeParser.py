# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u0190\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4k\n\4\3\5\3\5\5\5o\n\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6y\n\6\3\7\3\7\5\7}\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u0084\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u008d")
        buf.write("\n\t\3\n\3\n\3\n\3\n\5\n\u0093\n\n\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a0\n\f\3\r\3\r\5\r\u00a4")
        buf.write("\n\r\3\r\3\r\3\r\3\r\5\r\u00aa\n\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00b4\n\r\3\r\3\r\3\r\3\r\5\r\u00ba\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c2\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\7\17\u00ca\n\17\f\17\16\17\u00cd")
        buf.write("\13\17\3\20\3\20\5\20\u00d1\n\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00d9\n\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00e3\n\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f0\n\23\3\24\3\24")
        buf.write("\5\24\u00f4\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\5\32\u0110\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\5\34\u0119\n\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u0120\n\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u012c\n\37")
        buf.write("\3 \3 \3 \3 \3 \5 \u0133\n \3!\3!\3!\3!\3!\5!\u013a\n")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0142\n\"\f\"\16\"\u0145")
        buf.write("\13\"\3#\3#\3#\3#\3#\3#\7#\u014d\n#\f#\16#\u0150\13#\3")
        buf.write("$\3$\3$\3$\3$\3$\7$\u0158\n$\f$\16$\u015b\13$\3%\3%\3")
        buf.write("%\5%\u0160\n%\3&\3&\3&\5&\u0165\n&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\5\'\u0171\n\'\3(\3(\5(\u0175\n(\3")
        buf.write("(\3(\3(\3(\3)\3)\3)\3)\3)\3)\7)\u0181\n)\f)\16)\u0184")
        buf.write("\13)\3*\3*\3*\5*\u0189\n*\3+\3+\3+\5+\u018e\n+\3+\2\7")
        buf.write("\34BDFP,\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRT\2\7\3\2\5\7\4\2\"\"%*\3")
        buf.write("\2\30\31\3\2\35\36\3\2\37!\2\u0195\2V\3\2\2\2\4^\3\2\2")
        buf.write("\2\6j\3\2\2\2\bn\3\2\2\2\np\3\2\2\2\f|\3\2\2\2\16\u0083")
        buf.write("\3\2\2\2\20\u0085\3\2\2\2\22\u0092\3\2\2\2\24\u0094\3")
        buf.write("\2\2\2\26\u009f\3\2\2\2\30\u00b9\3\2\2\2\32\u00c1\3\2")
        buf.write("\2\2\34\u00c3\3\2\2\2\36\u00d0\3\2\2\2 \u00d2\3\2\2\2")
        buf.write("\"\u00e2\3\2\2\2$\u00e4\3\2\2\2&\u00f3\3\2\2\2(\u00f5")
        buf.write("\3\2\2\2*\u00fc\3\2\2\2,\u00ff\3\2\2\2.\u0108\3\2\2\2")
        buf.write("\60\u010a\3\2\2\2\62\u010f\3\2\2\2\64\u0111\3\2\2\2\66")
        buf.write("\u0118\3\2\2\28\u011f\3\2\2\2:\u0121\3\2\2\2<\u012b\3")
        buf.write("\2\2\2>\u0132\3\2\2\2@\u0139\3\2\2\2B\u013b\3\2\2\2D\u0146")
        buf.write("\3\2\2\2F\u0151\3\2\2\2H\u015f\3\2\2\2J\u0164\3\2\2\2")
        buf.write("L\u0170\3\2\2\2N\u0174\3\2\2\2P\u017a\3\2\2\2R\u0188\3")
        buf.write("\2\2\2T\u018d\3\2\2\2VW\5R*\2WX\5\6\4\2XY\5\4\3\2YZ\5")
        buf.write("T+\2Z[\3\2\2\2[\\\5\6\4\2\\]\7\2\2\3]\3\3\2\2\2^_\7\13")
        buf.write("\2\2_`\7\n\2\2`a\7+\2\2ab\7,\2\2bc\5R*\2cd\5\26\f\2d\5")
        buf.write("\3\2\2\2ef\5\b\5\2fg\5T+\2gh\5\6\4\2hk\3\2\2\2ik\3\2\2")
        buf.write("\2je\3\2\2\2ji\3\2\2\2k\7\3\2\2\2lo\5\n\6\2mo\5\30\r\2")
        buf.write("nl\3\2\2\2nm\3\2\2\2o\t\3\2\2\2pq\7\13\2\2qr\7\61\2\2")
        buf.write("rs\7+\2\2st\5\f\7\2tu\7,\2\2ux\5R*\2vy\5\26\f\2wy\3\2")
        buf.write("\2\2xv\3\2\2\2xw\3\2\2\2y\13\3\2\2\2z}\5\16\b\2{}\3\2")
        buf.write("\2\2|z\3\2\2\2|{\3\2\2\2}\r\3\2\2\2~\177\5\20\t\2\177")
        buf.write("\u0080\7/\2\2\u0080\u0081\5\16\b\2\u0081\u0084\3\2\2\2")
        buf.write("\u0082\u0084\5\20\t\2\u0083~\3\2\2\2\u0083\u0082\3\2\2")
        buf.write("\2\u0084\17\3\2\2\2\u0085\u0086\5\24\13\2\u0086\u008c")
        buf.write("\7\61\2\2\u0087\u0088\7-\2\2\u0088\u0089\5\22\n\2\u0089")
        buf.write("\u008a\7.\2\2\u008a\u008d\3\2\2\2\u008b\u008d\3\2\2\2")
        buf.write("\u008c\u0087\3\2\2\2\u008c\u008b\3\2\2\2\u008d\21\3\2")
        buf.write("\2\2\u008e\u008f\7\33\2\2\u008f\u0090\7/\2\2\u0090\u0093")
        buf.write("\7\33\2\2\u0091\u0093\7\33\2\2\u0092\u008e\3\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\23\3\2\2\2\u0094\u0095\t\2\2\2\u0095")
        buf.write("\25\3\2\2\2\u0096\u00a0\5\30\r\2\u0097\u00a0\5 \21\2\u0098")
        buf.write("\u00a0\5$\23\2\u0099\u00a0\5,\27\2\u009a\u00a0\5.\30\2")
        buf.write("\u009b\u00a0\5\60\31\2\u009c\u00a0\5\62\32\2\u009d\u00a0")
        buf.write("\5\64\33\2\u009e\u00a0\5:\36\2\u009f\u0096\3\2\2\2\u009f")
        buf.write("\u0097\3\2\2\2\u009f\u0098\3\2\2\2\u009f\u0099\3\2\2\2")
        buf.write("\u009f\u009a\3\2\2\2\u009f\u009b\3\2\2\2\u009f\u009c\3")
        buf.write("\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\27")
        buf.write("\3\2\2\2\u00a1\u00a4\5\24\13\2\u00a2\u00a4\7\t\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a9\7\61\2\2\u00a6\u00a7\7#\2\2\u00a7\u00aa\5")
        buf.write("> \2\u00a8\u00aa\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00aa\u00ba\3\2\2\2\u00ab\u00ac\5\24\13\2\u00ac")
        buf.write("\u00ad\7\61\2\2\u00ad\u00ae\7-\2\2\u00ae\u00af\5\22\n")
        buf.write("\2\u00af\u00b3\7.\2\2\u00b0\u00b1\7#\2\2\u00b1\u00b4\5")
        buf.write("\32\16\2\u00b2\u00b4\3\2\2\2\u00b3\u00b0\3\2\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\u00ba\3\2\2\2\u00b5\u00b6\7\b\2\2")
        buf.write("\u00b6\u00b7\7\61\2\2\u00b7\u00b8\7#\2\2\u00b8\u00ba\5")
        buf.write("> \2\u00b9\u00a3\3\2\2\2\u00b9\u00ab\3\2\2\2\u00b9\u00b5")
        buf.write("\3\2\2\2\u00ba\31\3\2\2\2\u00bb\u00bc\7-\2\2\u00bc\u00bd")
        buf.write("\5\34\17\2\u00bd\u00be\7.\2\2\u00be\u00c2\3\2\2\2\u00bf")
        buf.write("\u00c0\7-\2\2\u00c0\u00c2\7.\2\2\u00c1\u00bb\3\2\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c2\33\3\2\2\2\u00c3\u00c4\b\17\1\2\u00c4")
        buf.write("\u00c5\5\36\20\2\u00c5\u00cb\3\2\2\2\u00c6\u00c7\f\4\2")
        buf.write("\2\u00c7\u00c8\7/\2\2\u00c8\u00ca\5\36\20\2\u00c9\u00c6")
        buf.write("\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\35\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce")
        buf.write("\u00d1\5> \2\u00cf\u00d1\5\32\16\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d0\u00cf\3\2\2\2\u00d1\37\3\2\2\2\u00d2\u00d8\7\61")
        buf.write("\2\2\u00d3\u00d4\7-\2\2\u00d4\u00d5\5\"\22\2\u00d5\u00d6")
        buf.write("\7.\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8")
        buf.write("\u00d3\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00db\7#\2\2\u00db\u00dc\5> \2\u00dc!\3\2\2\2\u00dd")
        buf.write("\u00de\5> \2\u00de\u00df\7/\2\2\u00df\u00e0\5\"\22\2\u00e0")
        buf.write("\u00e3\3\2\2\2\u00e1\u00e3\5> \2\u00e2\u00dd\3\2\2\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3#\3\2\2\2\u00e4\u00e5\7\21\2\2\u00e5")
        buf.write("\u00e6\7+\2\2\u00e6\u00e7\5> \2\u00e7\u00e8\7,\2\2\u00e8")
        buf.write("\u00e9\5R*\2\u00e9\u00ea\5\26\f\2\u00ea\u00eb\5R*\2\u00eb")
        buf.write("\u00ec\5&\24\2\u00ec\u00ef\5R*\2\u00ed\u00f0\5*\26\2\u00ee")
        buf.write("\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f0%\3\2\2\2\u00f1\u00f4\5(\25\2\u00f2\u00f4\3\2\2")
        buf.write("\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\'\3\2")
        buf.write("\2\2\u00f5\u00f6\7\23\2\2\u00f6\u00f7\7+\2\2\u00f7\u00f8")
        buf.write("\5> \2\u00f8\u00f9\7,\2\2\u00f9\u00fa\5R*\2\u00fa\u00fb")
        buf.write("\5\26\f\2\u00fb)\3\2\2\2\u00fc\u00fd\7\22\2\2\u00fd\u00fe")
        buf.write("\5\26\f\2\u00fe+\3\2\2\2\u00ff\u0100\7\f\2\2\u0100\u0101")
        buf.write("\7\61\2\2\u0101\u0102\7\r\2\2\u0102\u0103\5> \2\u0103")
        buf.write("\u0104\7\16\2\2\u0104\u0105\5> \2\u0105\u0106\5R*\2\u0106")
        buf.write("\u0107\5\26\f\2\u0107-\3\2\2\2\u0108\u0109\7\17\2\2\u0109")
        buf.write("/\3\2\2\2\u010a\u010b\7\20\2\2\u010b\61\3\2\2\2\u010c")
        buf.write("\u010d\7\26\2\2\u010d\u0110\5> \2\u010e\u0110\7\26\2\2")
        buf.write("\u010f\u010c\3\2\2\2\u010f\u010e\3\2\2\2\u0110\63\3\2")
        buf.write("\2\2\u0111\u0112\7\61\2\2\u0112\u0113\7+\2\2\u0113\u0114")
        buf.write("\5\66\34\2\u0114\u0115\7,\2\2\u0115\65\3\2\2\2\u0116\u0119")
        buf.write("\58\35\2\u0117\u0119\3\2\2\2\u0118\u0116\3\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\67\3\2\2\2\u011a\u011b\5> \2\u011b")
        buf.write("\u011c\7/\2\2\u011c\u011d\58\35\2\u011d\u0120\3\2\2\2")
        buf.write("\u011e\u0120\5> \2\u011f\u011a\3\2\2\2\u011f\u011e\3\2")
        buf.write("\2\2\u01209\3\2\2\2\u0121\u0122\7\24\2\2\u0122\u0123\5")
        buf.write("T+\2\u0123\u0124\5<\37\2\u0124\u0125\7\25\2\2\u0125;\3")
        buf.write("\2\2\2\u0126\u0127\5\26\f\2\u0127\u0128\5T+\2\u0128\u0129")
        buf.write("\5<\37\2\u0129\u012c\3\2\2\2\u012a\u012c\3\2\2\2\u012b")
        buf.write("\u0126\3\2\2\2\u012b\u012a\3\2\2\2\u012c=\3\2\2\2\u012d")
        buf.write("\u012e\5@!\2\u012e\u012f\7$\2\2\u012f\u0130\5@!\2\u0130")
        buf.write("\u0133\3\2\2\2\u0131\u0133\5@!\2\u0132\u012d\3\2\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133?\3\2\2\2\u0134\u0135\5B\"\2\u0135")
        buf.write("\u0136\t\3\2\2\u0136\u0137\5B\"\2\u0137\u013a\3\2\2\2")
        buf.write("\u0138\u013a\5B\"\2\u0139\u0134\3\2\2\2\u0139\u0138\3")
        buf.write("\2\2\2\u013aA\3\2\2\2\u013b\u013c\b\"\1\2\u013c\u013d")
        buf.write("\5D#\2\u013d\u0143\3\2\2\2\u013e\u013f\f\4\2\2\u013f\u0140")
        buf.write("\t\4\2\2\u0140\u0142\5D#\2\u0141\u013e\3\2\2\2\u0142\u0145")
        buf.write("\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("C\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\b#\1\2\u0147")
        buf.write("\u0148\5F$\2\u0148\u014e\3\2\2\2\u0149\u014a\f\4\2\2\u014a")
        buf.write("\u014b\t\5\2\2\u014b\u014d\5F$\2\u014c\u0149\3\2\2\2\u014d")
        buf.write("\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014fE\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152\b$\1\2")
        buf.write("\u0152\u0153\5H%\2\u0153\u0159\3\2\2\2\u0154\u0155\f\4")
        buf.write("\2\2\u0155\u0156\t\6\2\2\u0156\u0158\5H%\2\u0157\u0154")
        buf.write("\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u015a\3\2\2\2\u015aG\3\2\2\2\u015b\u0159\3\2\2\2\u015c")
        buf.write("\u015d\7\27\2\2\u015d\u0160\5H%\2\u015e\u0160\5J&\2\u015f")
        buf.write("\u015c\3\2\2\2\u015f\u015e\3\2\2\2\u0160I\3\2\2\2\u0161")
        buf.write("\u0162\7\36\2\2\u0162\u0165\5J&\2\u0163\u0165\5L\'\2\u0164")
        buf.write("\u0161\3\2\2\2\u0164\u0163\3\2\2\2\u0165K\3\2\2\2\u0166")
        buf.write("\u0171\7\61\2\2\u0167\u0171\7\33\2\2\u0168\u0171\7\32")
        buf.write("\2\2\u0169\u0171\7\34\2\2\u016a\u0171\5\64\33\2\u016b")
        buf.write("\u0171\5N(\2\u016c\u016d\7+\2\2\u016d\u016e\5> \2\u016e")
        buf.write("\u016f\7,\2\2\u016f\u0171\3\2\2\2\u0170\u0166\3\2\2\2")
        buf.write("\u0170\u0167\3\2\2\2\u0170\u0168\3\2\2\2\u0170\u0169\3")
        buf.write("\2\2\2\u0170\u016a\3\2\2\2\u0170\u016b\3\2\2\2\u0170\u016c")
        buf.write("\3\2\2\2\u0171M\3\2\2\2\u0172\u0175\7\61\2\2\u0173\u0175")
        buf.write("\5\64\33\2\u0174\u0172\3\2\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0177\7-\2\2\u0177\u0178\5P)\2\u0178")
        buf.write("\u0179\7.\2\2\u0179O\3\2\2\2\u017a\u017b\b)\1\2\u017b")
        buf.write("\u017c\5> \2\u017c\u0182\3\2\2\2\u017d\u017e\f\4\2\2\u017e")
        buf.write("\u017f\7/\2\2\u017f\u0181\5> \2\u0180\u017d\3\2\2\2\u0181")
        buf.write("\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183Q\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\7\60\2")
        buf.write("\2\u0186\u0189\5R*\2\u0187\u0189\3\2\2\2\u0188\u0185\3")
        buf.write("\2\2\2\u0188\u0187\3\2\2\2\u0189S\3\2\2\2\u018a\u018b")
        buf.write("\7\60\2\2\u018b\u018e\5T+\2\u018c\u018e\7\60\2\2\u018d")
        buf.write("\u018a\3\2\2\2\u018d\u018c\3\2\2\2\u018eU\3\2\2\2%jnx")
        buf.write("|\u0083\u008c\u0092\u009f\u00a3\u00a9\u00b3\u00b9\u00c1")
        buf.write("\u00cb\u00d0\u00d8\u00e2\u00ef\u00f3\u010f\u0118\u011f")
        buf.write("\u012b\u0132\u0139\u0143\u014e\u0159\u015f\u0164\u0170")
        buf.write("\u0174\u0182\u0188\u018d")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'number'", 
                     "'bool'", "'string'", "'var'", "'dynamic'", "'main'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'return'", 
                     "'not'", "'and'", "'or'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'<-'", "'...'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "WS", "NUMBERTYPE", "BOOLTYPE", 
                      "STRINGTYPE", "VARTYPE", "DYNAMICTYPE", "MAIN", "FUNC", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "RETURN", "NOT", "AND", "OR", 
                      "BOOLLIT", "NUMBERLIT", "STRINGLIT", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "EQUAL", "ASSIGN", "CONCAT", 
                      "STRINGCOMPARE", "NOTEQ", "LT", "MT", "LOEQ", "MOEQ", 
                      "LP", "RP", "LS", "RS", "COMMA", "NEWLINE", "IDENTIFIER", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_mainfunc = 1
    RULE_decllist = 2
    RULE_decl = 3
    RULE_funcdecl = 4
    RULE_paramlist = 5
    RULE_paramprime = 6
    RULE_param = 7
    RULE_numlist = 8
    RULE_primetype = 9
    RULE_stmt = 10
    RULE_vardeclstmt = 11
    RULE_array = 12
    RULE_arrayprime = 13
    RULE_arrayelem = 14
    RULE_assignstmt = 15
    RULE_exprlist = 16
    RULE_ifstmt = 17
    RULE_elifstmtlist = 18
    RULE_elifstmt = 19
    RULE_elsestmt = 20
    RULE_forstmt = 21
    RULE_breakstmt = 22
    RULE_continuestmt = 23
    RULE_returnstmt = 24
    RULE_funccallstmt = 25
    RULE_n_exprlist = 26
    RULE_exprprime = 27
    RULE_blockstmt = 28
    RULE_stmtlist = 29
    RULE_expr = 30
    RULE_expr1 = 31
    RULE_expr2 = 32
    RULE_expr3 = 33
    RULE_expr4 = 34
    RULE_expr5 = 35
    RULE_expr6 = 36
    RULE_operand = 37
    RULE_elemexpr = 38
    RULE_indexop = 39
    RULE_nnls = 40
    RULE_nls = 41

    ruleNames =  [ "program", "mainfunc", "decllist", "decl", "funcdecl", 
                   "paramlist", "paramprime", "param", "numlist", "primetype", 
                   "stmt", "vardeclstmt", "array", "arrayprime", "arrayelem", 
                   "assignstmt", "exprlist", "ifstmt", "elifstmtlist", "elifstmt", 
                   "elsestmt", "forstmt", "breakstmt", "continuestmt", "returnstmt", 
                   "funccallstmt", "n_exprlist", "exprprime", "blockstmt", 
                   "stmtlist", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "operand", "elemexpr", "indexop", "nnls", 
                   "nls" ]

    EOF = Token.EOF
    COMMENT=1
    WS=2
    NUMBERTYPE=3
    BOOLTYPE=4
    STRINGTYPE=5
    VARTYPE=6
    DYNAMICTYPE=7
    MAIN=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    RETURN=20
    NOT=21
    AND=22
    OR=23
    BOOLLIT=24
    NUMBERLIT=25
    STRINGLIT=26
    ADD=27
    SUB=28
    MUL=29
    DIV=30
    MOD=31
    EQUAL=32
    ASSIGN=33
    CONCAT=34
    STRINGCOMPARE=35
    NOTEQ=36
    LT=37
    MT=38
    LOEQ=39
    MOEQ=40
    LP=41
    RP=42
    LS=43
    RS=44
    COMMA=45
    NEWLINE=46
    IDENTIFIER=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    ERROR_CHAR=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nnls(self):
            return self.getTypedRuleContext(ZCodeParser.NnlsContext,0)


        def decllist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DecllistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DecllistContext,i)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def mainfunc(self):
            return self.getTypedRuleContext(ZCodeParser.MainfuncContext,0)


        def nls(self):
            return self.getTypedRuleContext(ZCodeParser.NlsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.nnls()
            self.state = 85
            self.decllist()

            self.state = 86
            self.mainfunc()
            self.state = 87
            self.nls()
            self.state = 89
            self.decllist()
            self.state = 90
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def MAIN(self):
            return self.getToken(ZCodeParser.MAIN, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def nnls(self):
            return self.getTypedRuleContext(ZCodeParser.NnlsContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_mainfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainfunc" ):
                return visitor.visitMainfunc(self)
            else:
                return visitor.visitChildren(self)




    def mainfunc(self):

        localctx = ZCodeParser.MainfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(ZCodeParser.FUNC)
            self.state = 93
            self.match(ZCodeParser.MAIN)
            self.state = 94
            self.match(ZCodeParser.LP)
            self.state = 95
            self.match(ZCodeParser.RP)
            self.state = 96
            self.nnls()
            self.state = 97
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def nls(self):
            return self.getTypedRuleContext(ZCodeParser.NlsContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decllist)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.decl()
                self.state = 100
                self.nls()
                self.state = 101
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def vardeclstmt(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.funcdecl()
                pass
            elif token in [ZCodeParser.NUMBERTYPE, ZCodeParser.BOOLTYPE, ZCodeParser.STRINGTYPE, ZCodeParser.VARTYPE, ZCodeParser.DYNAMICTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.vardeclstmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def nnls(self):
            return self.getTypedRuleContext(ZCodeParser.NnlsContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ZCodeParser.FUNC)
            self.state = 111
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 112
            self.match(ZCodeParser.LP)
            self.state = 113
            self.paramlist()
            self.state = 114
            self.match(ZCodeParser.RP)
            self.state = 115
            self.nnls()
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERTYPE, ZCodeParser.BOOLTYPE, ZCodeParser.STRINGTYPE, ZCodeParser.VARTYPE, ZCodeParser.DYNAMICTYPE, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.RETURN, ZCodeParser.IDENTIFIER]:
                self.state = 116
                self.stmt()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramlist)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERTYPE, ZCodeParser.BOOLTYPE, ZCodeParser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.paramprime()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramprime)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.param()
                self.state = 125
                self.match(ZCodeParser.COMMA)
                self.state = 126
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primetype(self):
            return self.getTypedRuleContext(ZCodeParser.PrimetypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def numlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumlistContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.primetype()
            self.state = 132
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LS]:
                self.state = 133
                self.match(ZCodeParser.LS)
                self.state = 134
                self.numlist()
                self.state = 135
                self.match(ZCodeParser.RS)
                pass
            elif token in [ZCodeParser.RP, ZCodeParser.COMMA]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NUMBERLIT)
            else:
                return self.getToken(ZCodeParser.NUMBERLIT, i)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_numlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlist" ):
                return visitor.visitNumlist(self)
            else:
                return visitor.visitChildren(self)




    def numlist(self):

        localctx = ZCodeParser.NumlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_numlist)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 141
                self.match(ZCodeParser.COMMA)
                self.state = 142
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(ZCodeParser.NUMBERLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERTYPE(self):
            return self.getToken(ZCodeParser.NUMBERTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(ZCodeParser.BOOLTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(ZCodeParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primetype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimetype" ):
                return visitor.visitPrimetype(self)
            else:
                return visitor.visitChildren(self)




    def primetype(self):

        localctx = ZCodeParser.PrimetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primetype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBERTYPE) | (1 << ZCodeParser.BOOLTYPE) | (1 << ZCodeParser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclstmt(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def funccallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.vardeclstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 153
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 154
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 155
                self.funccallstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 156
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def primetype(self):
            return self.getTypedRuleContext(ZCodeParser.PrimetypeContext,0)


        def DYNAMICTYPE(self):
            return self.getToken(ZCodeParser.DYNAMICTYPE, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def numlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumlistContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def VARTYPE(self):
            return self.getToken(ZCodeParser.VARTYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardeclstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclstmt" ):
                return visitor.visitVardeclstmt(self)
            else:
                return visitor.visitChildren(self)




    def vardeclstmt(self):

        localctx = ZCodeParser.VardeclstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vardeclstmt)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBERTYPE, ZCodeParser.BOOLTYPE, ZCodeParser.STRINGTYPE]:
                    self.state = 159
                    self.primetype()
                    pass
                elif token in [ZCodeParser.DYNAMICTYPE]:
                    self.state = 160
                    self.match(ZCodeParser.DYNAMICTYPE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 163
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 167
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGN]:
                    self.state = 164
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 165
                    self.expr()
                    pass
                elif token in [ZCodeParser.ELSE, ZCodeParser.ELIF, ZCodeParser.NEWLINE]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.primetype()
                self.state = 170
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 171
                self.match(ZCodeParser.LS)
                self.state = 172
                self.numlist()
                self.state = 173
                self.match(ZCodeParser.RS)
                self.state = 177
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGN]:
                    self.state = 174
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 175
                    self.array()
                    pass
                elif token in [ZCodeParser.ELSE, ZCodeParser.ELIF, ZCodeParser.NEWLINE]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(ZCodeParser.VARTYPE)
                self.state = 180
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 181
                self.match(ZCodeParser.ASSIGN)
                self.state = 182
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def arrayprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayprimeContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(ZCodeParser.LS)
                self.state = 186
                self.arrayprime(0)
                self.state = 187
                self.match(ZCodeParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(ZCodeParser.LS)
                self.state = 190
                self.match(ZCodeParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayelem(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayelemContext,0)


        def arrayprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayprimeContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayprime" ):
                return visitor.visitArrayprime(self)
            else:
                return visitor.visitChildren(self)



    def arrayprime(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ArrayprimeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_arrayprime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.arrayelem()
            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.ArrayprimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arrayprime)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    self.match(ZCodeParser.COMMA)
                    self.state = 198
                    self.arrayelem() 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrayelemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayelem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayelem" ):
                return visitor.visitArrayelem(self)
            else:
                return visitor.visitChildren(self)




    def arrayelem(self):

        localctx = ZCodeParser.ArrayelemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arrayelem)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.BOOLLIT, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.expr()
                pass
            elif token in [ZCodeParser.LS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LS]:
                self.state = 209
                self.match(ZCodeParser.LS)
                self.state = 210
                self.exprlist()
                self.state = 211
                self.match(ZCodeParser.RS)
                pass
            elif token in [ZCodeParser.ASSIGN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 216
            self.match(ZCodeParser.ASSIGN)
            self.state = 217
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exprlist)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.expr()
                self.state = 220
                self.match(ZCodeParser.COMMA)
                self.state = 221
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def nnls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NnlsContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NnlsContext,i)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elifstmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtlistContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElsestmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(ZCodeParser.IF)
            self.state = 227
            self.match(ZCodeParser.LP)
            self.state = 228
            self.expr()
            self.state = 229
            self.match(ZCodeParser.RP)
            self.state = 230
            self.nnls()
            self.state = 231
            self.stmt()
            self.state = 232
            self.nnls()
            self.state = 233
            self.elifstmtlist()
            self.state = 234
            self.nnls()
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 235
                self.elsestmt()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmtlist" ):
                return visitor.visitElifstmtlist(self)
            else:
                return visitor.visitChildren(self)




    def elifstmtlist(self):

        localctx = ZCodeParser.ElifstmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_elifstmtlist)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.elifstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def nnls(self):
            return self.getTypedRuleContext(ZCodeParser.NnlsContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmt" ):
                return visitor.visitElifstmt(self)
            else:
                return visitor.visitChildren(self)




    def elifstmt(self):

        localctx = ZCodeParser.ElifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_elifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ZCodeParser.ELIF)
            self.state = 244
            self.match(ZCodeParser.LP)
            self.state = 245
            self.expr()
            self.state = 246
            self.match(ZCodeParser.RP)
            self.state = 247
            self.nnls()
            self.state = 248
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = ZCodeParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_elsestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ZCodeParser.ELSE)
            self.state = 251
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nnls(self):
            return self.getTypedRuleContext(ZCodeParser.NnlsContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ZCodeParser.FOR)
            self.state = 254
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 255
            self.match(ZCodeParser.UNTIL)
            self.state = 256
            self.expr()
            self.state = 257
            self.match(ZCodeParser.BY)
            self.state = 258
            self.expr()
            self.state = 259
            self.nnls()
            self.state = 260
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_returnstmt)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(ZCodeParser.RETURN)
                self.state = 267
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(ZCodeParser.RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def n_exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.N_exprlistContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funccallstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccallstmt" ):
                return visitor.visitFunccallstmt(self)
            else:
                return visitor.visitChildren(self)




    def funccallstmt(self):

        localctx = ZCodeParser.FunccallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_funccallstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 272
            self.match(ZCodeParser.LP)
            self.state = 273
            self.n_exprlist()
            self.state = 274
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class N_exprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_n_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_exprlist" ):
                return visitor.visitN_exprlist(self)
            else:
                return visitor.visitChildren(self)




    def n_exprlist(self):

        localctx = ZCodeParser.N_exprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_n_exprlist)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.BOOLLIT, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.exprprime()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = ZCodeParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exprprime)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.expr()
                self.state = 281
                self.match(ZCodeParser.COMMA)
                self.state = 282
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def nls(self):
            return self.getTypedRuleContext(ZCodeParser.NlsContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ZCodeParser.BEGIN)
            self.state = 288
            self.nls()

            self.state = 289
            self.stmtlist()
            self.state = 290
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def nls(self):
            return self.getTypedRuleContext(ZCodeParser.NlsContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmtlist)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERTYPE, ZCodeParser.BOOLTYPE, ZCodeParser.STRINGTYPE, ZCodeParser.VARTYPE, ZCodeParser.DYNAMICTYPE, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.RETURN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.stmt()
                self.state = 293
                self.nls()
                self.state = 294
                self.stmtlist()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.expr1()
                self.state = 300
                self.match(ZCodeParser.CONCAT)
                self.state = 301
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def STRINGCOMPARE(self):
            return self.getToken(ZCodeParser.STRINGCOMPARE, 0)

        def NOTEQ(self):
            return self.getToken(ZCodeParser.NOTEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def MT(self):
            return self.getToken(ZCodeParser.MT, 0)

        def LOEQ(self):
            return self.getToken(ZCodeParser.LOEQ, 0)

        def MOEQ(self):
            return self.getToken(ZCodeParser.MOEQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.expr2(0)
                self.state = 307
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.STRINGCOMPARE) | (1 << ZCodeParser.NOTEQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.MT) | (1 << ZCodeParser.LOEQ) | (1 << ZCodeParser.MOEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 308
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 316
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 317
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 318
                    self.expr3(0) 
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 327
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 328
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 329
                    self.expr4(0) 
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 338
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 339
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 340
                    self.expr5() 
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr5)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(ZCodeParser.NOT)
                self.state = 347
                self.expr5()
                pass
            elif token in [ZCodeParser.BOOLLIT, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr6)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(ZCodeParser.SUB)
                self.state = 352
                self.expr6()
                pass
            elif token in [ZCodeParser.BOOLLIT, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.LP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def BOOLLIT(self):
            return self.getToken(ZCodeParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def funccallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallstmtContext,0)


        def elemexpr(self):
            return self.getTypedRuleContext(ZCodeParser.ElemexprContext,0)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operand)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.match(ZCodeParser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 359
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 360
                self.funccallstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 361
                self.elemexpr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 362
                self.match(ZCodeParser.LP)
                self.state = 363
                self.expr()
                self.state = 364
                self.match(ZCodeParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def indexop(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def funccallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elemexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemexpr" ):
                return visitor.visitElemexpr(self)
            else:
                return visitor.visitChildren(self)




    def elemexpr(self):

        localctx = ZCodeParser.ElemexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_elemexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 368
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 369
                self.funccallstmt()
                pass


            self.state = 372
            self.match(ZCodeParser.LS)
            self.state = 373
            self.indexop(0)
            self.state = 374
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def indexop(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)



    def indexop(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.IndexopContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_indexop, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.IndexopContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexop)
                    self.state = 379
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 380
                    self.match(ZCodeParser.COMMA)
                    self.state = 381
                    self.expr() 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NnlsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nnls(self):
            return self.getTypedRuleContext(ZCodeParser.NnlsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nnls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNnls" ):
                return visitor.visitNnls(self)
            else:
                return visitor.visitChildren(self)




    def nnls(self):

        localctx = ZCodeParser.NnlsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_nnls)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(ZCodeParser.NEWLINE)
                self.state = 388
                self.nnls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NlsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nls(self):
            return self.getTypedRuleContext(ZCodeParser.NlsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNls" ):
                return visitor.visitNls(self)
            else:
                return visitor.visitChildren(self)




    def nls(self):

        localctx = ZCodeParser.NlsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_nls)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(ZCodeParser.NEWLINE)
                self.state = 393
                self.nls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.arrayprime_sempred
        self._predicates[32] = self.expr2_sempred
        self._predicates[33] = self.expr3_sempred
        self._predicates[34] = self.expr4_sempred
        self._predicates[39] = self.indexop_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arrayprime_sempred(self, localctx:ArrayprimeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def indexop_sempred(self, localctx:IndexopContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




