import board


from kb import KMKKeyboard

from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.tapdance import TapDance
from kmk.handlers.sequences import compile_unicode_string_sequences as cuss
from kmk.handlers.sequences import send_string

# Initially copied from lily58

keyboard = KMKKeyboard()
layers_ext = Layers()
split = Split(data_pin=board.RX, data_pin2=board.TX, uart_flip=False)
keyboard.tap_time = 750
tapdance = TapDance()
keyboard.modules = [layers_ext, split, tapdance]

keyboard.debug_enabled = False 
keyboard.unicode_mode = UnicodeMode.ALTPLUS
print('Loading code.py')

_______ = KC.TRNS
xxxxxxx = KC.NO

emoticons = cuss({
    # Emojis
    'BEER': r'🍺',
    'BEER_TOAST': r'🍻',
    'FACE_CUTE_SMILE': r'😊',
    'FACE_HEART_EYES': r'😍',
    'FACE_JOY': r'😂',
    'FACE_SWEAT_SMILE': r'😅',
    'FACE_THINKING': r'🤔',
    'FIRE': r'🔥',
    'FLAG_CA': r'🇨🇦',
    'FLAG_US': r'🇺🇸',
    'HAND_CLAP': r'👏',
    'HAND_HORNS': r'🤘',
    'HAND_OK': r'👌',
    'HAND_THUMB_DOWN': r'👎',
    'HAND_THUMB_UP': r'👍',
    'HAND_WAVE': r'👋',
    'HEART': r'❤️',
    'MAPLE_LEAF': r'🍁',
    'POOP': r'💩',
    'TADA': r'🎉',
    'SHRUG_EMOJI': r'🤷',

    # Emoticons, but fancier
    'ANGRY_TABLE_FLIP': r'(ノಠ痊ಠ)ノ彡┻━┻',
    'CELEBRATORY_GLITTER': r'+｡:.ﾟヽ(´∀｡)ﾉﾟ.:｡+ﾟﾟ+｡:.ﾟヽ(*´∀)ﾉﾟ.:｡+ﾟ',
    'SHRUGGIE': r'¯\_(ツ)_/¯',
    'TABLE_FLIP': r'(╯°□°）╯︵ ┻━┻',
})

CALTDEL = KC.LCTL(KC.LALT(KC.DELETE))
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
ALT_TAB = KC.LALT(KC.TAB)
SH_TAB = KC.LSHIFT(KC.TAB)
AL_SH_T = KC.LALT(SH_TAB)
GRA_ACC = KC.TD( #KC.GRAVE_ACCENT 
    KC.GRAVE,
    KC.TILDE
)

keyboard.keymap = [
    [
        GRA_ACC,  KC.N1,  KC.N2,     KC.N3,    KC.N4,      KC.N5,      KC.N6,     KC.N7,    KC.N8,        KC.N9,       KC.N0,      KC.MINUS,
        KC.HOME,  KC.Q,   KC.W,      KC.E,     KC.R,       KC.T,       KC.Y,      KC.U,     KC.I,         KC.O,        KC.P,       KC.EQUAL,
        KC.END,   KC.A,   KC.S,      KC.D,     KC.F,       KC.G,       KC.H,      KC.J,     KC.K,         KC.L,        KC.SCOLON,  KC.QUOT,
        KC.LGUI,  KC.Z,   KC.X,      KC.C,     KC.V,       KC.B,       KC.N,      KC.M,     KC.COMMA,     KC.DOT,      KC.SLSH,    KC.BSLASH,
                          KC.MINUS,  KC.EQUAL,                                              KC.LBRACKET,  KC.RBRACKET,       
                                     KC.TAB,   KC.SPACE,                          KC.SPACE, KC.TAB,           
                                               KC.LSHIFT,  KC.LCTRL,   KC.ENTER,  KC.BSPC,                
                                               KC.MO(1),   KC.MO(2),   KC.MO(2),  KC.MO(1),               
    ],
    [
        KC.ESC,     KC.F1,      KC.F2,      KC.F3,      KC.F4,       KC.F5,          KC.F6,      KC.F7,      KC.F8,      KC.F9,  KC.F10,             KC.F11,
        CALTDEL,    KC.TILDE,   AL_SH_T,    KC.UP,      ALT_TAB,     KC.BSPC,        xxxxxxx,    KC.P7,      KC.P8,      KC.P9,  KC.NUMPAD_MINUS,    KC.NUMPAD_SLASH,
        KC.VOLU,    KC.PSCREEN, KC.LEFT,    KC.DOWN,    KC.RIGHT,    KC.DEL,         xxxxxxx,    KC.P4,      KC.P5,      KC.P6,  KC.NUMPAD_PLUS,     KC.NUMPAD_ASTERISK,
        KC.VOLD,    KC.MUTE,    KC.PGUP,    xxxxxxx,    KC.PGDN,     KC.CAPSLOCK,    KC.P0,      KC.P1,      KC.P2,      KC.P3,  xxxxxxx,            xxxxxxx,
                                COPY,       PASTE,                                                           xxxxxxx,    xxxxxxx,    
                                            SH_TAB,     KC.TAB,                                  xxxxxxx,    xxxxxxx,    
                                                        KC.LALT,     KC.LALT,        xxxxxxx,    KC.NUMLOCK,    
                                                        _______,     _______,        _______,    _______,    
    ],
    [
        KC.ESC,    xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,   emoticons.ANGRY_TABLE_FLIP,         xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,             xxxxxxx,
        xxxxxxx,    emoticons.BEER_TOAST,    emoticons.FACE_HEART_EYES,    emoticons.HAND_THUMB_UP,    emoticons.HAND_HORNS,   emoticons.TABLE_FLIP,         xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,
        xxxxxxx,    emoticons.BEER, emoticons.HEART,emoticons.HAND_THUMB_DOWN,emoticons.HAND_CLAP,    emoticons.SHRUGGIE,         xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,     xxxxxxx,
        xxxxxxx,    xxxxxxx,    emoticons.FIRE,    emoticons.FACE_JOY,    xxxxxxx,   emoticons.SHRUG_EMOJI,         xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,            xxxxxxx,
                                xxxxxxx,    KC.RALT,                                                        xxxxxxx,    xxxxxxx,    
                                            xxxxxxx,    xxxxxxx,                                xxxxxxx,    xxxxxxx,    
                                                        xxxxxxx,    xxxxxxx,    xxxxxxx,    xxxxxxx,    
                                                        _______,    _______,    _______,    _______,
    ],
]

print('code.py loaded successfully')

if __name__ == '__main__':
    keyboard.go()
