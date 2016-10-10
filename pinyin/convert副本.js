ss = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_@";
/*
params 源进制，源数据
return 目标进制数据
*/
function v10toX(n, m) {
    m = String(m).replace(/ /gi, "");
    if (m == "") {
        return ""
    }
    var a = ss.substr(0, 10);
    var b = a + ".";
    if (eval("m.replace(/[" + b + "]/gi,'')") != "") {
        M("请输入有效的进制数！");
        return ""
    }
    m = m.split(".");
    if (m.length > 2) {
        M("请输入有效的进制数！");
        return ""
    }
    var a = ss.substr(0, n);
    if (m.length == 1) {
        m = m[0];
        var t = "";
        while (m != 0) {
            var b = m % n;
            t = a.charAt(b) + t;
            m = (m - b) / n
        }
        return t
    } else {
        var m0 = m[0];
        var t = "";
        while (m0 != 0) {
            var b = m0 % n;
            t = a.charAt(b) + t;
            m0 = (m0 - b) / n
        }
        var cnt = 18;
        var m1 = m[1];
        m1 = parseFloat("0." + m1);
        var d = "",
            b = 0;
        while (m1 != 0 && cnt > 0) {
            m1 = m1 * n;
            b = parseInt(m1);
            d = d + a.charAt(b);
            m1 = m1 - b;
            cnt--
        };
        return t + "." + d
    }
}
/*
params 源进制，源数据
return 目标10进制数据
*/
function vXto10(n, m) {
    m = String(m).replace(/ /gi, "");
    if (m == "") {
        return ""
    }
    var a = ss.substr(0, n);
    var b = a + ".";
    if (eval("m.replace(/[" + b + "]/gi,'')") != "") {
        M("请输入有效的" + n + "进制数！");
        return ""
    }
    m = m.split(".");
    if (m.length > 2) {
        M("请输入有效的" + n + "进制数！");
        return ""
    }
    if (m.length == 1) {
        m = m[0];
        var t = 0,
            c = 1;
        for (var x = m.length - 1; x > -1; x--) {
            t += c * (a.indexOf(m.charAt(x)));
            c *= n
        }
        return t
    } else {
        var m0 = m[0];
        var t = 0,
            c = 1;
        for (var x = m0.length - 1; x > -1; x--) {
            t += c * (a.indexOf(m0.charAt(x)));
            c *= n
        }
        var m1 = m[1];
        var d = 0,
            c = 1 / n;
        for (var x = 0; x < m1.length; x++) {
            d += c * (a.indexOf(m1.charAt(x)));
            c /= n
        }
        return t + d
    }
}
/*
params 源进制，源数据
return 目标进制
*/
function vXtoY(d, b, c) {
    a = vXto10(d * 1, b);
    if (a == "") {
        return ""
    }
    a = v10toX(c, a);
    return a
}

function M(b) { alert(b) }
