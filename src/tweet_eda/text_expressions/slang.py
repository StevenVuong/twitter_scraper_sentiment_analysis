from typing import Union, List, Dict
# Ref: https://github.com/rishabhverma17/sms_slang_translator/blob/master/slang.txt

SLANG = \
"""
AFAIK=As Far As I Know
AFK=Away From Keyboard
ASAP=As Soon As Possible
ATK=At The Keyboard
ATM=At The Moment
A3=Anytime, Anywhere, Anyplace
BAK=Back At Keyboard
BBL=Be Back Later
BBS=Be Back Soon
BFN=Bye For Now
B4N=Bye For Now
BRB=Be Right Back
BRT=Be Right There
BTW=By The Way
B4=Before
B4N=Bye For Now
CU=See You
CUL8R=See You Later
CYA=See You
FAQ=Frequently Asked Questions
FC=Fingers Crossed
FWIW=For What It's Worth
FYI=For Your Information
GAL=Get A Life
GG=Good Game
GN=Good Night
GMTA=Great Minds Think Alike
GR8=Great!
G9=Genius
IC=I See
ICQ=I Seek you (also a chat program)
ILU=ILU: I Love You
IMHO=In My Honest/Humble Opinion
IMO=In My Opinion
IOW=In Other Words
IRL=In Real Life
KISS=Keep It Simple, Stupid
LDR=Long Distance Relationship
LMAO=Laugh My A.. Off
LOL=Laughing Out Loud
LTNS=Long Time No See
L8R=Later
MTE=My Thoughts Exactly
M8=Mate
NRN=No Reply Necessary
OIC=Oh I See
PITA=Pain In The A..
PRT=Party
PRW=Parents Are Watching
QPSA?=Que Pasa?
ROFL=Rolling On The Floor Laughing
ROFLOL=Rolling On The Floor Laughing Out Loud
ROTFLMAO=Rolling On The Floor Laughing My A.. Off
SK8=Skate
STATS=Your sex and age
ASL=Age, Sex, Location
THX=Thank You
TTFN=Ta-Ta For Now!
TTYL=Talk To You Later
U=You
U2=You Too
U4E=Yours For Ever
WB=Welcome Back
WTF=What The F...
WTG=Way To Go!
WUF=Where Are You From?
W8=Wait...
7K=Sick:-D Laugher
"""

SLANG_LIST = ['FWIW', 'L8R', 'M8', 'TTYL', 'WB', 'U4E', '7K', 'THX', 'BAK', 'U2', 'ILU', 'ASL', 'SK8', 'LMAO', 'WTF', 'ATK', 'A3', 'GG', 'U', 'ATM', 'NRN', 'GAL', 'GMTA', 'PRW', 'BTW', 'ASAP', 'FAQ', 'OIC', 'ROFL', 'CUL8R', 'MTE', 'LTNS', 'FYI', 'BRB', 'BBS', 'B4', 'IRL', 'KISS', 'GN', 'IC', 'IMO', 'ROTFLMAO', 'AFAIK', 'B4N', 'BRT', 'GR8', 'PRT', 'TTFN', 'WTG', 'WUF', 'BFN', 'W8', 'CU', 'G9', 'FC', 'LOL', 'PITA', 'BBL', 'ICQ', 'AFK', 'LDR', 'QPSA?', 'STATS', 'ROFLOL', 'IMHO', 'CYA', 'IOW']
SLANG_DICT = {'AFAIK': 'As Far As I Know', 'AFK': 'Away From Keyboard', 'ASAP': 'As Soon As Possible', 'ATK': 'At The Keyboard', 'ATM': 'At The Moment', 'A3': 'Anytime, Anywhere, Anyplace', 'BAK': 'Back At Keyboard', 'BBL': 'Be Back Later', 'BBS': 'Be Back Soon', 'BFN': 'Bye For Now', 'B4N': 'Bye For Now', 'BRB': 'Be Right Back', 'BRT': 'Be Right There', 'BTW': 'By The Way', 'B4': 'Before', 'CU': 'See You', 'CUL8R': 'See You Later', 'CYA': 'See You', 'FAQ': 'Frequently Asked Questions', 'FC': 'Fingers Crossed', 'FWIW': "For What It's Worth", 'FYI': 'For Your Information', 'GAL': 'Get A Life', 'GG': 'Good Game', 'GN': 'Good Night', 'GMTA': 'Great Minds Think Alike', 'GR8': 'Great!', 'G9': 'Genius', 'IC': 'I See', 'ICQ': 'I Seek you (also a chat program)', 'ILU': 'ILU: I Love You', 'IMHO': 'In My Honest/Humble Opinion', 'IMO': 'In My Opinion', 'IOW': 'In Other Words', 'IRL': 'In Real Life', 'KISS': 'Keep It Simple, Stupid', 'LDR': 'Long Distance Relationship', 'LMAO': 'Laugh My A.. Off', 'LOL': 'Laughing Out Loud', 'LTNS': 'Long Time No See', 'L8R': 'Later', 'MTE': 'My Thoughts Exactly', 'M8': 'Mate', 'NRN': 'No Reply Necessary', 'OIC': 'Oh I See', 'PITA': 'Pain In The A..', 'PRT': 'Party', 'PRW': 'Parents Are Watching', 'QPSA?': 'Que Pasa?', 'ROFL': 'Rolling On The Floor Laughing', 'ROFLOL': 'Rolling On The Floor Laughing Out Loud', 'ROTFLMAO': 'Rolling On The Floor Laughing My A.. Off', 'SK8': 'Skate', 'STATS': 'Your sex and age', 'ASL': 'Age, Sex, Location', 'THX': 'Thank You', 'TTFN': 'Ta-Ta For Now!', 'TTYL': 'Talk To You Later', 'U': 'You', 'U2': 'You Too', 'U4E': 'Yours For Ever', 'WB': 'Welcome Back', 'WTF': 'What The F...', 'WTG': 'Way To Go!', 'WUF': 'Where Are You From?', 'W8': 'Wait...', '7K': 'Sick:-D Laugher'}

def get_slang_list(slang_docstring:str = SLANG) -> Union[List, Dict]:
    """Get list of slang words and dict from single docstring.
    Args:
        - slang_docstring(str)
    Return:
        - SLANG_LIST (List(str))
        - SLANG_MAP_DICT (Dict(str:str))
    """
    slang_map_dict = {}
    slang_list = []

    for line in slang_docstring.split("\n"):
        if line != "":
            cw = line.split("=")[0]
            cw_expanded = line.split("=")[1]
            slang_list.append(cw)
            slang_map_dict[cw] = cw_expanded
    slang_list = list(set(slang_list))
    return slang_list, slang_map_dict
