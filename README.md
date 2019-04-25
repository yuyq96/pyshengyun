# PyShengYun [:cn:](https://github.com/yuyq96/pyshengyun/README_CN.md)

A converter for Chinese pinyin and shengyun (initials and finals) in python and can be utilized in automatic speech recognition or text-to-speech.

## Installation

```bash
$ git clone https://github.com/yuyq96/pyshengyun
```

## Usage

```python
>>> from pyshengyun import *
>>> tone
['1', '2', '3', '4', '5']
>>> letter
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> initials  # equivalent to 'sheng'
['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's']
>>> finals  # equivalent to 'yun'
['a', 'o', 'e', 'ai', 'ei', 'ao', 'ou', 'an', 'en', 'ang', 'eng', 'ong', 'i', 'ia', 'ie', 'iao', 'iou', 'ian', 'in', 'iang', 'ing', 'iong', 'u', 'ua', 'uo', 'uai', 'uei', 'uan', 'uen', 'uang', 'ueng', 'v', 've', 'van', 'vn']
>>> shengyun  # equivalent to 'initials_finals'
['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's', 'a', 'o', 'e', 'ai', 'ei', 'ao', 'ou', 'an', 'en', 'ang', 'eng', 'ong', 'i', 'ia', 'ie', 'iao', 'iou', 'ian', 'in', 'iang', 'ing', 'iong', 'u', 'ua', 'uo', 'uai', 'uei', 'uan', 'uen', 'uang', 'ueng', 'v', 've', 'van', 'vn']
>>> list(pinyin_to_initials_finals('hua yuan'))  # 'pinyin_to_initials_finals' is equivalent to 'pinyin_to_shengyun' and it returns a generator
[['h', 'ua'], ['van']]
>>> list(initials_finals_to_pinyin('hua van'))  # 'initials_finals_to_pinyin' is equivalent to 'shengyun_to_pinyin' and it returns a generator
['hua', 'yuan']
```

## Related Projects

[pypinyin](https://github.com/mozillazg/python-pinyin)
