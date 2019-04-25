# 拼音声韵母转换工具 [:us:](https://github.com/yuyq96/pyshengyun)

将拼音转为声母、韵母，或者将声母、韵母组合为拼音，可用于语音识别、语音合成。

## 安装

```bash
$ git clone https://github.com/yuyq96/pyshengyun
```

## 使用示例

```python
>>> from pyshengyun import *
>>> tone
['1', '2', '3', '4', '5']
>>> letter
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> sheng  # 等价于initials
['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's']
>>> yun  # 等价于finals
['a', 'o', 'e', 'ai', 'ei', 'ao', 'ou', 'an', 'en', 'ang', 'eng', 'ong', 'i', 'ia', 'ie', 'iao', 'iou', 'ian', 'in', 'iang', 'ing', 'iong', 'u', 'ua', 'uo', 'uai', 'uei', 'uan', 'uen', 'uang', 'ueng', 'v', 've', 'van', 'vn']
>>> shengyun  # 等价于initials_finals
['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's', 'a', 'o', 'e', 'ai', 'ei', 'ao', 'ou', 'an', 'en', 'ang', 'eng', 'ong', 'i', 'ia', 'ie', 'iao', 'iou', 'ian', 'in', 'iang', 'ing', 'iong', 'u', 'ua', 'uo', 'uai', 'uei', 'uan', 'uen', 'uang', 'ueng', 'v', 've', 'van', 'vn']
>>> list(pinyin_to_shengyun('hua yuan'))  # pinyin_to_shengyun等价于pinyin_to_initials_finals，返回一个生成器
[['h', 'ua'], ['van']]
>>> list(shengyun_to_pinyin('hua van'))  # shengyun_to_pinyin等价于initials_finals_to_pinyin，返回一个生成器
['hua', 'yuan']
```

## 相关项目

[pypinyin](https://github.com/mozillazg/python-pinyin)
