from pathlib import Path
import sys
"""
A collection of channel lookup functions.
"""


def lookup(i):
    """
    Find the coordinates of a channel
    :param i: channel number, int
    :return: tuple (x, y)
    """
    chanlookup = {1: (31, 0), 2: (31, 1), 3: (31, 2), 4: (31, 3), 5: (31, 4), 6: (31, 5), 7: (31, 6), 8: (31, 7),
                  9: (30, 0), 10: (30, 1), 11: (30, 2), 12: (30, 3), 13: (30, 4), 14: (30, 5), 15: (30, 6), 16: (30, 7),
                  17: (29, 0), 18: (29, 1), 19: (29, 2), 20: (29, 3), 21: (29, 4), 22: (29, 5), 23: (29, 6),
                  24: (29, 7), 25: (28, 0), 26: (28, 1), 27: (28, 2), 28: (28, 3), 29: (28, 4), 30: (28, 5),
                  31: (28, 6), 32: (28, 7), 33: (31, 15), 34: (31, 14), 35: (31, 13), 36: (31, 12), 37: (31, 11),
                  38: (31, 10), 39: (31, 9), 40: (31, 8), 41: (30, 15), 42: (30, 14), 43: (30, 13), 44: (30, 12),
                  45: (30, 11), 46: (30, 10), 47: (30, 9), 48: (30, 8), 49: (29, 15), 50: (29, 14), 51: (29, 13),
                  52: (29, 12), 53: (29, 11), 54: (29, 10), 55: (29, 9), 56: (29, 8), 57: (28, 15), 58: (28, 14),
                  59: (28, 13), 60: (28, 12), 61: (28, 11), 62: (28, 10), 63: (28, 9), 64: (28, 8), 65: (3, 0),
                  66: (3, 1), 67: (3, 2), 68: (3, 3), 69: (3, 4), 70: (3, 5), 71: (3, 6), 72: (3, 7), 73: (2, 0),
                  74: (2, 1), 75: (2, 2), 76: (2, 3), 77: (2, 4), 78: (2, 5), 79: (2, 6), 80: (2, 7), 81: (1, 0),
                  82: (1, 1), 83: (1, 2), 84: (1, 3), 85: (1, 4), 86: (1, 5), 87: (1, 6), 88: (1, 7), 89: (0, 0),
                  90: (0, 1), 91: (0, 2), 92: (0, 3), 93: (0, 4), 94: (0, 5), 95: (0, 6), 96: (0, 7), 97: (3, 15),
                  98: (3, 14), 99: (3, 13), 100: (3, 12), 101: (3, 11), 102: (3, 10), 103: (3, 9), 104: (3, 8),
                  105: (2, 15), 106: (2, 14), 107: (2, 13), 108: (2, 12), 109: (2, 11), 110: (2, 10), 111: (2, 9),
                  112: (2, 8), 113: (1, 15), 114: (1, 14), 115: (1, 13), 116: (1, 12), 117: (1, 11), 118: (1, 10),
                  119: (1, 9), 120: (1, 8), 121: (0, 15), 122: (0, 14), 123: (0, 13), 124: (0, 12), 125: (0, 11),
                  126: (0, 10), 127: (0, 9), 128: (0, 8), 129: (7, 0), 130: (7, 1), 131: (7, 2), 132: (7, 3),
                  133: (7, 4), 134: (7, 5), 135: (7, 6), 136: (7, 7), 137: (6, 0), 138: (6, 1), 139: (6, 2),
                  140: (6, 3), 141: (6, 4), 142: (6, 5), 143: (6, 6), 144: (6, 7), 145: (5, 0), 146: (5, 1),
                  147: (5, 2), 148: (5, 3), 149: (5, 4), 150: (5, 5), 151: (5, 6), 152: (5, 7), 153: (4, 0),
                  154: (4, 1), 155: (4, 2), 156: (4, 3), 157: (4, 4), 158: (4, 5), 159: (4, 6), 160: (4, 7),
                  161: (7, 15), 162: (7, 14), 163: (7, 13), 164: (7, 12), 165: (7, 11), 166: (7, 10), 167: (7, 9),
                  168: (7, 8), 169: (6, 15), 170: (6, 14), 171: (6, 13), 172: (6, 12), 173: (6, 11), 174: (6, 10),
                  175: (6, 9), 176: (6, 8), 177: (5, 15), 178: (5, 14), 179: (5, 13), 180: (5, 12), 181: (5, 11),
                  182: (5, 10), 183: (5, 9), 184: (5, 8), 185: (4, 15), 186: (4, 14), 187: (4, 13), 188: (4, 12),
                  189: (4, 11), 190: (4, 10), 191: (4, 9), 192: (4, 8), 193: (11, 0), 194: (11, 1), 195: (11, 2),
                  196: (11, 3), 197: (11, 4), 198: (11, 5), 199: (11, 6), 200: (11, 7), 201: (10, 0), 202: (10, 1),
                  203: (10, 2), 204: (10, 3), 205: (10, 4), 206: (10, 5), 207: (10, 6), 208: (10, 7), 209: (9, 0),
                  210: (9, 1), 211: (9, 2), 212: (9, 3), 213: (9, 4), 214: (9, 5), 215: (9, 6), 216: (9, 7),
                  217: (8, 0), 218: (8, 1), 219: (8, 2), 220: (8, 3), 221: (8, 4), 222: (8, 5), 223: (8, 6),
                  224: (8, 7), 225: (11, 15), 226: (11, 14), 227: (11, 13), 228: (11, 12), 229: (11, 11), 230: (11, 10),
                  231: (11, 9), 232: (11, 8), 233: (10, 15), 234: (10, 14), 235: (10, 13), 236: (10, 12), 237: (10, 11),
                  238: (10, 10), 239: (10, 9), 240: (10, 8), 241: (9, 15), 242: (9, 14), 243: (9, 13), 244: (9, 12),
                  245: (9, 11), 246: (9, 10), 247: (9, 9), 248: (9, 8), 249: (8, 15), 250: (8, 14), 251: (8, 13),
                  252: (8, 12), 253: (8, 11), 254: (8, 10), 255: (8, 9), 256: (8, 8), 257: (15, 0), 258: (15, 1),
                  259: (15, 2), 260: (15, 3), 261: (15, 4), 262: (15, 5), 263: (15, 6), 264: (15, 7), 265: (14, 0),
                  266: (14, 1), 267: (14, 2), 268: (14, 3), 269: (14, 4), 270: (14, 5), 271: (14, 6), 272: (14, 7),
                  273: (13, 0), 274: (13, 1), 275: (13, 2), 276: (13, 3), 277: (13, 4), 278: (13, 5), 279: (13, 6),
                  280: (13, 7), 281: (12, 0), 282: (12, 1), 283: (12, 2), 284: (12, 3), 285: (12, 4), 286: (12, 5),
                  287: (12, 6), 288: (12, 7), 289: (15, 15), 290: (15, 14), 291: (15, 13), 292: (15, 12), 293: (15, 11),
                  294: (15, 10), 295: (15, 9), 296: (15, 8), 297: (14, 15), 298: (14, 14), 299: (14, 13), 300: (14, 12),
                  301: (14, 11), 302: (14, 10), 303: (14, 9), 304: (14, 8), 305: (13, 15), 306: (13, 14), 307: (13, 13),
                  308: (13, 12), 309: (13, 11), 310: (13, 10), 311: (13, 9), 312: (13, 8), 313: (12, 15), 314: (12, 14),
                  315: (12, 13), 316: (12, 12), 317: (12, 11), 318: (12, 10), 319: (12, 9), 320: (12, 8), 321: (19, 0),
                  322: (19, 1), 323: (19, 2), 324: (19, 3), 325: (19, 4), 326: (19, 5), 327: (19, 6), 328: (19, 7),
                  329: (18, 0), 330: (18, 1), 331: (18, 2), 332: (18, 3), 333: (18, 4), 334: (18, 5), 335: (18, 6),
                  336: (18, 7), 337: (17, 0), 338: (17, 1), 339: (17, 2), 340: (17, 3), 341: (17, 4), 342: (17, 5),
                  343: (17, 6), 344: (17, 7), 345: (16, 0), 346: (16, 1), 347: (16, 2), 348: (16, 3), 349: (16, 4),
                  350: (16, 5), 351: (16, 6), 352: (16, 7), 353: (19, 15), 354: (19, 14), 355: (19, 13), 356: (19, 12),
                  357: (19, 11), 358: (19, 10), 359: (19, 9), 360: (19, 8), 361: (18, 15), 362: (18, 14), 363: (18, 13),
                  364: (18, 12), 365: (18, 11), 366: (18, 10), 367: (18, 9), 368: (18, 8), 369: (17, 15), 370: (17, 14),
                  371: (17, 13), 372: (17, 12), 373: (17, 11), 374: (17, 10), 375: (17, 9), 376: (17, 8), 377: (16, 15),
                  378: (16, 14), 379: (16, 13), 380: (16, 12), 381: (16, 11), 382: (16, 10), 383: (16, 9), 384: (16, 8),
                  385: (23, 0), 386: (23, 1), 387: (23, 2), 388: (23, 3), 389: (23, 4), 390: (23, 5), 391: (23, 6),
                  392: (23, 7), 393: (22, 0), 394: (22, 1), 395: (22, 2), 396: (22, 3), 397: (22, 4), 398: (22, 5),
                  399: (22, 6), 400: (22, 7), 401: (21, 0), 402: (21, 1), 403: (21, 2), 404: (21, 3), 405: (21, 4),
                  406: (21, 5), 407: (21, 6), 408: (21, 7), 409: (20, 0), 410: (20, 1), 411: (20, 2), 412: (20, 3),
                  413: (20, 4), 414: (20, 5), 415: (20, 6), 416: (20, 7), 417: (23, 15), 418: (23, 14), 419: (23, 13),
                  420: (23, 12), 421: (23, 11), 422: (23, 10), 423: (23, 9), 424: (23, 8), 425: (22, 15), 426: (22, 14),
                  427: (22, 13), 428: (22, 12), 429: (22, 11), 430: (22, 10), 431: (22, 9), 432: (22, 8), 433: (21, 15),
                  434: (21, 14), 435: (21, 13), 436: (21, 12), 437: (21, 11), 438: (21, 10), 439: (21, 9), 440: (21, 8),
                  441: (20, 15), 442: (20, 14), 443: (20, 13), 444: (20, 12), 445: (20, 11), 446: (20, 10),
                  447: (20, 9), 448: (20, 8), 449: (27, 0), 450: (27, 1), 451: (27, 2), 452: (27, 3), 453: (27, 4),
                  454: (27, 5), 455: (27, 6), 456: (27, 7), 457: (26, 0), 458: (26, 1), 459: (26, 2), 460: (26, 3),
                  461: (26, 4), 462: (26, 5), 463: (26, 6), 464: (26, 7), 465: (25, 0), 466: (25, 1), 467: (25, 2),
                  468: (25, 3), 469: (25, 4), 470: (25, 5), 471: (25, 6), 472: (25, 7), 473: (24, 0), 474: (24, 1),
                  475: (24, 2), 476: (24, 3), 477: (24, 4), 478: (24, 5), 479: (24, 6), 480: (24, 7), 481: (27, 15),
                  482: (27, 14), 483: (27, 13), 484: (27, 12), 485: (27, 11), 486: (27, 10), 487: (27, 9), 488: (27, 8),
                  489: (26, 15), 490: (26, 14), 491: (26, 13), 492: (26, 12), 493: (26, 11), 494: (26, 10),
                  495: (26, 9), 496: (26, 8), 497: (25, 15), 498: (25, 14), 499: (25, 13), 500: (25, 12), 501: (25, 11),
                  502: (25, 10), 503: (25, 9), 504: (25, 8), 505: (24, 15), 506: (24, 14), 507: (24, 13), 508: (24, 12),
                  509: (24, 11), 510: (24, 10), 511: (24, 9), 512: (24, 8)}
    return chanlookup[i]


def reverse_lookup(x,y):
    """
    For a given pair of coordinates find the corresponding channel on the flowcell
    :param x: int, x coord from lookup
    :param y: int, y coord from lookup
    :return: int, channel number at given coords
    """
    coordinate_lookup = {31: {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8,
                              15: 33, 14: 34, 13: 35, 12: 36, 11: 37, 10: 38, 9: 39, 8: 40},
                         30: {0: 9, 1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16, 
                              15: 41, 14: 42, 13: 43, 12: 44, 11: 45, 10: 46, 9: 47, 8: 48},
                         29: {0: 17, 1: 18, 2: 19, 3: 20, 4: 21, 5: 22, 6: 23, 7: 24, 
                              15: 49, 14: 50, 13: 51, 12: 52, 11: 53, 10: 54, 9: 55, 8: 56},
                         28: {0: 25, 1: 26, 2: 27, 3: 28, 4: 29, 5: 30, 6: 31, 7: 32, 
                              15: 57, 14: 58, 13: 59, 12: 60, 11: 61, 10: 62, 9: 63, 8: 64},
                         3:  {0: 65, 1: 66, 2: 67, 3: 68, 4: 69, 5: 70, 6: 71, 7: 72, 
                              15: 97, 14: 98, 13: 99, 12: 100, 11: 101, 10: 102, 9: 103, 8: 104},
                         2:  {0: 73, 1: 74, 2: 75, 3: 76, 4: 77, 5: 78, 6: 79, 7: 80, 
                              15: 105, 14: 106, 13: 107, 12: 108, 11: 109, 10: 110, 9: 111, 8: 112},
                         1:  {0: 81, 1: 82, 2: 83, 3: 84, 4: 85, 5: 86, 6: 87, 7: 88, 
                              15: 113, 14: 114, 13: 115, 12: 116, 11: 117, 10: 118, 9: 119, 8: 120},
                         0:  {0: 89, 1: 90, 2: 91, 3: 92, 4: 93, 5: 94, 6: 95, 7: 96, 
                              15: 121, 14: 122, 13: 123, 12: 124, 11: 125, 10: 126, 9: 127, 8: 128},
                         7:  {0: 129, 1: 130, 2: 131, 3: 132, 4: 133, 5: 134, 6: 135, 7: 136, 
                              15: 161, 14: 162, 13: 163, 12: 164, 11: 165, 10: 166, 9: 167, 8: 168},
                         6:  {0: 137, 1: 138, 2: 139, 3: 140, 4: 141, 5: 142, 6: 143, 7: 144, 
                              15: 169, 14: 170, 13: 171, 12: 172, 11: 173, 10: 174, 9: 175, 8: 176},
                         5:  {0: 145, 1: 146, 2: 147, 3: 148, 4: 149, 5: 150, 6: 151, 7: 152, 
                              15: 177, 14: 178, 13: 179, 12: 180, 11: 181, 10: 182, 9: 183, 8: 184},
                         4:  {0: 153, 1: 154, 2: 155, 3: 156, 4: 157, 5: 158, 6: 159, 7: 160, 
                              15: 185, 14: 186, 13: 187, 12: 188, 11: 189, 10: 190, 9: 191, 8: 192},
                         11: {0: 193, 1: 194, 2: 195, 3: 196, 4: 197, 5: 198, 6: 199, 7: 200, 
                              15: 225, 14: 226, 13: 227, 12: 228, 11: 229, 10: 230, 9: 231, 8: 232},
                         10: {0: 201, 1: 202, 2: 203, 3: 204, 4: 205, 5: 206, 6: 207, 7: 208, 
                              15: 233, 14: 234, 13: 235, 12: 236, 11: 237, 10: 238, 9: 239, 8: 240},
                         9:  {0: 209, 1: 210, 2: 211, 3: 212, 4: 213, 5: 214, 6: 215, 7: 216, 
                              15: 241, 14: 242, 13: 243, 12: 244, 11: 245, 10: 246, 9: 247, 8: 248},
                         8:  {0: 217, 1: 218, 2: 219, 3: 220, 4: 221, 5: 222, 6: 223, 7: 224, 
                              15: 249, 14: 250, 13: 251, 12: 252, 11: 253, 10: 254, 9: 255, 8: 256},
                         15: {0: 257, 1: 258, 2: 259, 3: 260, 4: 261, 5: 262, 6: 263, 7: 264,
                              15: 289, 14: 290, 13: 291, 12: 292, 11: 293, 10: 294, 9: 295, 8: 296},
                         14: {0: 265, 1: 266, 2: 267, 3: 268, 4: 269, 5: 270, 6: 271, 7: 272, 
                              15: 297, 14: 298, 13: 299, 12: 300, 11: 301, 10: 302, 9: 303, 8: 304},
                         13: {0: 273, 1: 274, 2: 275, 3: 276, 4: 277, 5: 278, 6: 279, 7: 280, 
                              15: 305, 14: 306, 13: 307, 12: 308, 11: 309, 10: 310, 9: 311, 8: 312},
                         12: {0: 281, 1: 282, 2: 283, 3: 284, 4: 285, 5: 286, 6: 287, 7: 288, 
                              15: 313, 14: 314, 13: 315, 12: 316, 11: 317, 10: 318, 9: 319, 8: 320},
                         19: {0: 321, 1: 322, 2: 323, 3: 324, 4: 325, 5: 326, 6: 327, 7: 328, 
                              15: 353, 14: 354, 13: 355, 12: 356, 11: 357, 10: 358, 9: 359, 8: 360},
                         18: {0: 329, 1: 330, 2: 331, 3: 332, 4: 333, 5: 334, 6: 335, 7: 336, 
                              15: 361, 14: 362, 13: 363, 12: 364, 11: 365, 10: 366, 9: 367, 8: 368},
                         17: {0: 337, 1: 338, 2: 339, 3: 340, 4: 341, 5: 342, 6: 343, 7: 344, 
                              15: 369, 14: 370, 13: 371, 12: 372, 11: 373, 10: 374, 9: 375, 8: 376},
                         16: {0: 345, 1: 346, 2: 347, 3: 348, 4: 349, 5: 350, 6: 351, 7: 352, 
                              15: 377, 14: 378, 13: 379, 12: 380, 11: 381, 10: 382, 9: 383, 8: 384},
                         23: {0: 385, 1: 386, 2: 387, 3: 388, 4: 389, 5: 390, 6: 391, 7: 392, 
                              15: 417, 14: 418, 13: 419, 12: 420, 11: 421, 10: 422, 9: 423, 8: 424},
                         22: {0: 393, 1: 394, 2: 395, 3: 396, 4: 397, 5: 398, 6: 399, 7: 400, 
                              15: 425, 14: 426, 13: 427, 12: 428, 11: 429, 10: 430, 9: 431, 8: 432},
                         21: {0: 401, 1: 402, 2: 403, 3: 404, 4: 405, 5: 406, 6: 407, 7: 408, 
                              15: 433, 14: 434, 13: 435, 12: 436, 11: 437, 10: 438, 9: 439, 8: 440},
                         20: {0: 409, 1: 410, 2: 411, 3: 412, 4: 413, 5: 414, 6: 415, 7: 416, 
                              15: 441, 14: 442, 13: 443, 12: 444, 11: 445, 10: 446, 9: 447, 8: 448},
                         27: {0: 449, 1: 450, 2: 451, 3: 452, 4: 453, 5: 454, 6: 455, 7: 456, 
                              15: 481, 14: 482, 13: 483, 12: 484, 11: 485, 10: 486, 9: 487, 8: 488},
                         26: {0: 457, 1: 458, 2: 459, 3: 460, 4: 461, 5: 462, 6: 463, 7: 464, 
                              15: 489, 14: 490, 13: 491, 12: 492, 11: 493, 10: 494, 9: 495, 8: 496},
                         25: {0: 465, 1: 466, 2: 467, 3: 468, 4: 469, 5: 470, 6: 471, 7: 472, 
                              15: 497, 14: 498, 13: 499, 12: 500, 11: 501, 10: 502, 9: 503, 8: 504},
                         24: {0: 473, 1: 474, 2: 475, 3: 476, 4: 477, 5: 478, 6: 479, 7: 480, 
                              15: 505, 14: 506, 13: 507, 12: 508, 11: 509, 10: 510, 9: 511, 8: 512}
                        }
    return coordinate_lookup[x][y]


def surround_channels(ch, s):
    """
    For a given channel return a list of the surrounding channels
    :param ch: channel as int
    :param s: steps away from the 'central' channel (ch) int
    :return: set of int (channel numbers)
    """
    x, y = lookup(ch)
    r = range(-s, s+1, 1)
    channels = set()
    for i in r:
        for j in r:
            try:
                channels.add(reverse_lookup(i+x, j+y))
            except KeyError:
                continue
    return channels


if __name__ == "__main__":
    print("Sorry, {f} is not designed to be run directly.".format(f=Path(__file__).name))
    sys.exit()