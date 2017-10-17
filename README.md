# kakasi
KAKASI - Kanji Kana Simple Inverter  

Version 2.3.6 (Code Mirror)

Copyright (C) 1992-1999 Hironobu Takahashi. All rights reserved.

Web site: http://kakasi.namazu.org/index.html.en

## Installation
```bash
git clone https://github.com/loretoparisi/kakasi.git
cd kakasi
./configure && make
make install
```

## Usage
```bash
echo "日本が好きです。" | iconv -f utf8 -t eucjp | kakasi -i euc -Ha -Ka -Ja -Ea -ka
nippongasukidesu.

echo "日本が好きです。" | iconv -f utf8 -t eucjp | kakasi -i euc -w | kakasi -i euc -Ha -Ka -Ja -Ea -ka
nippon ga suki desu .
```

## Examples
Conversion using iconv
```
echo "退屈であくびばっかしていた毎日" | iconv -f utf8 -t eucjp | kakasi -i euc -Ha -Ka -Ja -Ea -ka -s
taikutsu deakubibakkashiteita mainichi
```

Convertion from Unicode to Shift-JIS
```
echo "7月31日" | iconv -f utf8 -t shift-jis | kakasi -Ja -Ha -Ka -Ea -s 
```

Conversion from Shift-JIS to Unicode
```
echo "7月31日" | iconv -f utf8 -t shift-jis | kakasi -Ja -Ha -Ka -Ea -s | iconv -f shift-jis -t utf8

7 gatsu 31 nichi
```

To convert into Hiragana:
```
echo "7月31日" | iconv -f utf8 -t shift-jis | kakasi -JH -KH -Ea -s | iconv -f shift-jis -t utf8

7 がつ 31 にち
```

Using utf-8 input and output parameters
```
echo "7月31日" | kakasi -JH -KH -Ea -s -iutf8 -outf8

7 がつ 31 にち
```

## Supported Charset
Character Sets:

a: ascii  j: jisroman  g: graphic  k: kana (j,k     defined in jisx0201)

E: kigou  K: katakana  H: hiragana J: kanji(E,K,H,J defined in jisx0208)


## Dictionaries
Dictionaries after installation with `make install` are available at `/usr/local/share/kakasi/kanwadict` and `/usr/local/share/kakasi/itaijidict`. To copy the dictionaries in another location, please set your env:

```bash
export ITAIJIDICTPATH=./itaijidict
export KANWADICTPATH=./kanwadict
```

## Help
```
Usage: kakasi -a[jE] -j[aE] -g[ajE] -k[ajKH] -E[aj] -K[ajkH] -H[ajkKH] -J[ajkKH]
              -i{oldjis,newjis,dec,euc,sjis,utf8} -o{oldjis,newjis,dec,euc,sjis,utf8}
              -r{hepburn,kunrei} -p -s -f -c"chars"  [jisyo1, jisyo2,,,]

      Character Sets:
       a: ascii  j: jisroman  g: graphic  k: kana (j,k     defined in jisx0201)
       E: kigou  K: katakana  H: hiragana J: kanji(E,K,H,J defined in jisx0208)

      Options:
      -i: input coding system    -o: output coding system
      -r: romaji conversion system
      -p: list all readings (with -J option)
      -s: insert separate characters (with -J option)  -S"chars": set separator
      -f: furigana mode (with -J option)
      -F[rl]"chars": set parentheses around furigana
      -c: skip chars within jukugo (with -J option: default TAB CR LF BLANK)
      -C: romaji Capitalize (with -Ja or -Jj option)
      -U: romaji Upcase     (with -Ja or -Jj option)
      -u: call fflush() after 1 character output
      -t: use old romaji table
      -w: wakatigaki mode
      -{l,L}: level {hiragana,furigana} mode (-{l,L}[123456jn])
      -y: display yomi of each kanji characters

Report bugs to <bug-kakasi@namazu.org>.
```
