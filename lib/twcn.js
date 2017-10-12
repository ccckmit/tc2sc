var M = module.exports = {
  t2s : require('./dtable')
}

M.convert = function (twStr) {
    
    var cnStr = ''
    for (var i = 0; i < twStr.length; i++)
        if(M.t2s.table[twStr[i]] !== undefined) {    
            cnStr += M.t2s.table[twStr[i]]
        }
        else {
            cnStr += twStr[i]
        }
    // throw new Error('twcn.convert() not implemented !')
  
    return cnStr
}
