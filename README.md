# twcn -- 繁體轉簡體

## 系統功能描述

給定一個繁體字串，寫一個函數將該字串轉為簡體

## 程式範例

```js
var converter = require('twcn')
var tc = '寫一個函數將該字串轉為簡體'
var sc = converter.convert(tc)
console.log('tc=', tc, ' sc=', sc)
```

輸出

```
tc=寫一個函數將該字串轉為簡體 sc=写一个函数将该字串转为简体
```



