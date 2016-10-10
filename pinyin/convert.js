//ss = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_@";
ss = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~";
/*
params 源进制，源数据
return 目标进制数据
*/
function v10toX(n, m) {
    
    var a = ss.substr(0, n);
    var t = "";
    while (m != 0) {
        var b = m % n;
        t = a.charAt(b) + t;
        m = (m - b) / n
    }
    return t
}

/*
params 源进制，源数据
return 目标10进制数据
*/
function vXto10(n, m) {
    var a = ss.substr(0, n);
    var t = 0,
        c = 1;
    for (var x = m.length - 1; x > -1; x--) {
        t += c * (a.indexOf(m.charAt(x)));
        c *= n
    }
    return t
}


// for(var i=32;i<127;i++){
//     console.log(String.fromCharCode(i))
//    // console.log('±')
// }

console.log(":",v10toX(92,18999887766))