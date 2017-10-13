# twcn -- 簡繁體轉換

Convert Traditional Chinese into Simplified Chinese

## 系統功能描述

twcn.convert() : 將字串中的繁體字轉為簡體字
twcn.iconvert() : 將字串中的簡體字轉為繁體字

## 程式範例

## 繁體轉簡體 ：twcn.convert(）

```js
var twcn = require('twcn')
var tc = 'todo:寫一個函數將該字串轉為簡體。'
var sc = twcn.convert(tc)
console.log('tc=', tc, ' sc=', sc)
```

輸出

```
tc=todo:寫一個函數將該字串轉為簡體。 sc=todo:写一个函数将该字串转为简体。
```

## 簡體轉繁體 : twcn.iconvert(）

```js
var twcn = require('twcn')
var sc = 'todo:写一个函数将该字串转为简体。'
var tc = twcn.iconvert(sc)
console.log('sc=', sc, ' tc=', tc)
```

輸出

```
sc=todo:写一个函数将该字串转为简体。 tc=todo:寫一個函數將該字串轉為簡體。 
```


