# 声调符号
tone = list('12345')

# 字母表
letter = list('abcdefghijklmnopqrstuvwxyz')

# 声母表
initials = [
  'b',    'p',    'm',    'f',
  'd',    't',    'n',    'l',
  'g',    'k',    'h',
  'j',    'q',    'x',
  'zh',   'ch',   'sh',   'r',
  'z',    'c',    's',
]
sheng = initials

# 韵母表
_finals = {
  ' ': [        'a',    'o',    'e',    'ai',   'ei',   'ao',   'ou',   'an',   'en',   'ang',  'eng',  'ong',  ],
  'i': ['i',    'ia',           'ie',                   'iao',  'iou',  'ian',  'in',   'iang', 'ing',  'iong', ],
  'u': ['u',    'ua',   'uo',           'uai',  'uei',                  'uan',  'uen',  'uang', 'ueng',         ],
  'v': ['v',                    've',                                   'van',  'vn',                           ],
}
finals = _finals[' '] + _finals['i'] + _finals['u'] + _finals['v']
yun = finals

initials_finals = initials + finals
shengyun = initials_finals

# 拼音声韵母互转词典
_pinyin_to_initial_final = {'er': ['er']}
_initial_final_to_pinyin = {'er': 'er'}
# 除'v'行韵母外，其他韵母跟声母的组合
for final in (_finals[' '] + _finals['i'] + _finals['u']):
  # iou，uei，uen前面加声母的时候，写成iu，ui，un
  if final == 'iou':
    _final = 'iu'
  elif final == 'uei':
    _final = 'ui'
  elif final == 'uen':
    _final = 'un'
  else:
    _final = final
  for initial in initials:
    pinyin = initial + _final
    _pinyin_to_initial_final[pinyin] = [initial, final]
    _initial_final_to_pinyin[initial + final] = pinyin
# ' '行韵母
for final in _finals[' ']:
  # 前面没有声母的时候
  for initial in initials:
    pinyin = final
    _pinyin_to_initial_final[pinyin] = [final]
    _initial_final_to_pinyin[final] = pinyin
# 'i'行韵母
for final in _finals['i']:
  # 前面没有声母的时候，写成yi，ya，ye，yao，you，yan，yin，yang，ying，yong
  if final in ['i', 'in', 'ing']:
    pinyin = 'y' + final
  else:
    pinyin = 'y' + final[1:]
  _pinyin_to_initial_final[pinyin] = [final]
  _initial_final_to_pinyin[final] = pinyin
# 'u'行韵母
for final in _finals['u']:
  # 前面没有声母的时候，写成wu，wa，wo，wai，wei，wan，wen，wang，weng
  if final == 'u':
    pinyin = 'wu'
  else:
    pinyin = 'w' + final[1:]
  _pinyin_to_initial_final[pinyin] = [final]
  _initial_final_to_pinyin[final] = pinyin
# 'v'行韵母
for final in _finals['v']:
  # 前面没有声母的时候，写成yu，yue，yuan，yun
  if final == 'v':
    pinyin = 'yu'
  else:
    pinyin = 'yu' + final[1:]
  _pinyin_to_initial_final[pinyin] = [final]
  _initial_final_to_pinyin[final] = pinyin
  # 跟声母j，q，x拼的时候，v写成u （自动替换之前u行韵母跟声母j，q，x的组合，如jun）
  for initial in ['j', 'q', 'x']:
    pinyin = initial + 'u' + final[1:]
    _pinyin_to_initial_final[pinyin] = [initial, final]
    _initial_final_to_pinyin[initial + final] = pinyin
  # 跟声母n，l拼的时候，v写成v（实际上不存在nvan，lvan，nvn，lvn）
  for initial in ['n', 'l']:
    pinyin = initial + final
    _pinyin_to_initial_final[pinyin] = [initial, final]
    _initial_final_to_pinyin[initial + final] = pinyin

def pinyin_to_initial_final(pinyin):
  for item in pinyin.strip().split(' '):
    yield _pinyin_to_initial_final.get(item)

def initial_final_to_pinyin(phoneme):
  for item in phoneme.strip().split(' '):
    yield _initial_final_to_pinyin.get(item)

def pinyin_to_shengyun(pinyin):
  return pinyin_to_initial_final(pinyin)

def shengyun_to_pinyin(phoneme):
  return initial_final_to_pinyin(phoneme)
