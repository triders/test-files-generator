# Test files generator

### Glossaries CSV generator `glossaries_generator.py`

#### 1. Non-translatable

```
generate_dnt_glossary(
  size=10000, 
  language="en_us", 
  cs_types=("lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM"),
  words_in_term=2, 
  file_name="dnt"
  )
```
- `size` - how many terms
- `language` - terms' language (e.g., `en_us`, `ru_ru`, `ja_jp`, `fr_fr`, `zh_tw`, `zh_cn`, `ar_aa`, `pt_pt`)
- `cs_types = ("lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM")` - a ***tuple*** of case sensitivity types for each term. Specify from 1 to 8 available CS types (5 of them are custom)
- `words_in_term` - how many words will be in each term
- `file_name` - if you want the file to be named in you way (e.g., `my_little_ponny`)

An example of generated term from CSV file (all CS types are enabled):
```
...
important impact 
IMPORTANT IMPACT 
Important impact 
iMportant impact 
important impact 
iMPORTANT IMPACT 
IMPORTANT IMPACT 
Important impact
...
```

#### 2. Unidirectional
```
generate_unidirectional_glossary(
  size=10000, 
  source_language="en_us",  
  target_language="ru_ru",
  cs_types=("lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM"),
  words_in_term=2, 
  file_name="unidir"
  )
```
- `size` - how many terms
- `source_language` - terms' source language (e.g., `en_us`, `ru_ru`, `ja_jp`, `fr_fr`, `zh_tw`, `zh_cn`, `ar_aa`, `pt_pt`)
- `target_language` - terms' target language (e.g., `en_us`, `ru_ru`, `ja_jp`, `fr_fr`, `zh_tw`, `zh_cn`, `ar_aa`, `pt_pt`)
- `cs_types = ("lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM")` - a ***tuple*** of case sensitivity types for each term. Specify from 1 to 8 available CS types (5 of them are custom)
- `words_in_term` - how many words will be in each term
- `file_name` - prefix to the file (if you want the file to be named in you way, e.g., `my_little_ponny`)

An example of generated term from CSV file (all CS types are enabled):
```
...
every above, палец левый
EVERY ABOVE, ПАЛЕЦ ЛЕВЫЙ
Every above, Палец левый
eVery above, пАлец левый
every abovE, палец левыЙ
eVERY ABOVE, пАЛЕЦ ЛЕВЫЙ
EVERY ABOVe, ПАЛЕЦ ЛЕВЫй
Every abovE, Палец левыЙ
...
```
