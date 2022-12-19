# Test files generator

### Glossaries CSV generator `glossaries_generator.py`

#### 1. Non-translatable

```
generate_dnt_glossary(size=10000, language="en_us", cs_types=["lower", "upper", "regular", "custom"], file_name="dnt")
```
- `size` - how many terms to generate
- `language` - terms' language (e.g., `en_us`, `ru_ru`, `ja_jp`, `fr_fr`, `zh_tw`, `zh_cn`, `ar_aa`, `pt_pt`)
- `cs_types` - a ***list*** of case sensitivity types to be presented in the glossary
  - `["lower", "upper", "regular", "custom"]` or `["upper"]` - all terms will have a random CS type from this range;  specify from one to four available CS types
- `file_name` - if you want the file to be named in you way (e.g., `my_little_ponny`)

An example of generated CSV file (all CS types enabled):
```
WIFE POPULAR
Congress occur
laugh trouble
sEat off
```

#### 2. Unidirectional
```
generate_unidirectional_glossary(size=10000, source_language="en_us", target_language="ru_ru", cs_types=["lower", "upper", "regular", "custom"], file_name="dnt")
```
- `size` - how many terms
- `source_language` - terms' source language (e.g., `en_us`, `ru_ru`, `ja_jp`, `fr_fr`, `zh_tw`, `zh_cn`, `ar_aa`, `pt_pt`)
- `target_language` - terms' target language (e.g., `en_us`, `ru_ru`, `ja_jp`, `fr_fr`, `zh_tw`, `zh_cn`, `ar_aa`, `pt_pt`)
- `cs_types` - a ***list*** of case sensitivity types to be presented in the glossary
  - `["lower", "upper", "regular", "custom"]` or `["upper"]` - all terms will have a random CS type from this range;  specify from one to four available CS types
- `file_name` - prefix to the file (if you want the file to be named in you way, e.g., `my_little_ponny`)

An example of generated CSV file:
```
For including, Грустный возбуждение
source choice, неправда выбирать
PARTY VOICE, ДОСТОИНСТВО СЫНОК
mOve style, бЕгать порог
```
