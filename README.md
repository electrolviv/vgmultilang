# vgmultilang

---
Multi-Language converter : string resources in json format to .c 

JSON formatted data converted to:
1. *.h / *.c files content : As `char *text array[] = { ... };`
2. Binary file : As raw-data binary block 
   + strings count 
   + strings offsets
   + strings lengths
   + strings content

---
##### JSON File example

```json
{
    "#ver"  : 1.0,
    "#pfx"  : "MLang_",

    "hello"   : {
      "idx"   : 1,
      "en"    : "hello",
      "de"    : "hallo",
      "ru"    : "привет"
    },

    "welcome" : {
      "idx"   : 3,
      "en"    : "welcome",
      "de"    : "willkommen",
      "ru"    : "добро пожаловать"
    },

    "console" : {
      "en"    : "console",
      "de"    : "konsole",
      "ru"    : "консоль"
    }
}
```

---
String prefix is *MLang_*<br>
First string is **MLang_hello** , index 1<br>
Second string is **MLang_welcome** ,  index 3<br>
Third string is **MLang_console** , index 4 (auto)<br>

---

##### Generated files
    file_en.c ; C-Style
    file_de.c ; C-Style
    file_ru.c ; C-Style

##### Files content

`output.h` Generated Header File 
```c
enum enMultiLangStrID {
   MLang_bank0_ = 0,
   MLang_hello,
   MLang_bank2_,
   MLang_welcome,
   MLang_console,
   MLang_LastValidValue_
};
```

`output_xx.c` Generated Source Files en / de / it / ru / ua ... 
```c++
static const int last_idx = 3;

static const char * str1txt = "...";
static const uint16_t str1len = 0;

static const char * str2txt = "...";
static const uint16_t str2len = 0;

static const char * str3txt = "...";
static const uint16_t str3len = 0;

static const char *tbl[] = {
    str1txt,
    str2txt,
    str3txt
};


const char * GetString(uint16_t idx) {
    return (idx < last_idx) ? tbl[idx] : 
}

```



(C) 2021 V01G04A81
