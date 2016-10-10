var fs=require('fs');
//var zi=fs.readFileSync('dict-zi.js').toString();

// zi=zi.replace(/[\n\r\t]/g,'');
// console.log(zi)
// fs.writeFileSync('dict-zi2.js',zi);


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






var zi=fs.readFileSync('dict-zi2.js').toString();
var dic={};
zi=zi.replace(/(.+?)([\u2E80-\u9FFF])/g,function(){
	var ten=parseInt(arguments[1],36);
    return v10toX(92,ten)+arguments[2];
	//dic[arguments[2]]=v10toX(92,ten);
	//console.log(arguments)
});
//console.log(dic)
 fs.writeFileSync('dict-zi3.js',zi);

