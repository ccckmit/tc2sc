# twcn -- 繁體轉簡體

Convert Traditional Chinese into Simplified Chinese

## 系統功能描述

寫一個函數將字串中的繁體字轉為簡體字

## 程式範例

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



