import nltk
from nltk.chat.util import Chat, reflenctions

pairs = [ 
    [ 
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],

    [
        r"hi|wsg|wassup|hello",
        ["Hey!", "wasgood gang"]

    ],
    [ 
        r"if i was a animal, what animal would i be?",
        ["losersauras",]
    ],

    [ 
        r"whats a (.*)",
        ["like i know what a %1 is",]
    ],
    [ 
        r"6|7",
        ["SIX SEVENNNN",]
    ],

    [ 
        r"i love lebron",
        ["shaboingboing??",]
    ],

    [ 
        r"grenade",
        ["grenade",]
    ],

    [ 
        r"my brother passed away",
        ["man im sorry for your lost. heres 5 big booms. BOOM BOOM BOOM BOOM BOOM!",]
    ],
]