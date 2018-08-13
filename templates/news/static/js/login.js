console.log('Соеденяемся с серверами...');
var username = GetCookie('username');
var pathname = location.pathname;
var myDomain = pathname.substring(0,pathname.lastIndexOf('/')) +'/';
// Установка параметра expire на год вперед.
var largeExpDate = new Date ();
largeExpDate.setTime(largeExpDate.getTime() + (365 * 24 * 3600 * 1000));
function cook () {
username = document.getElementByld("nam").value;
}
function getCookieVal (offset) {
var endstr = document.cookie.indexOf (";", offset);
if (endstr == -1)
endstr = document.cookie.length;
return unescape(document.cookie.substring(offset, endstr));
}
function GetCookie (name) {
var arg = name + "=";
var alen = arg.length;
var clen = document.cookie.length;
var i = 0;
while (i < clen) {
var j = i + alen;
if (document.cookie.substring(i, j) == arg)
return getCookieVal (j);
i = document.cookie.indexOf(" ", i) + 1;
if (i == 0)
break;
}
return null;
}

function delCok() {
var largeExpDate = new Date (); largeExpDate.setTime(largeExpDate.getTime() + (-100));

var path = (argc > 3) ? argv[3] : null;
var domain = (argc > 4) ? argv[4] : null;
var secure = (argc > 5) ? argv[5] : false;
document.cookie = "username" + "=" + escape (value) +
((expires == null) ? "" : ("; expires=" + 
expires.toGMTString())) + 
((path == null) ? "" : ("; path=" + path)) +
((domain == null) ? "" : ("; domain=" + domain)) +
((secure == true) ? "; secure" : "");
}


function SetCookie (name, value) {
var argv = SetCookie.arguments;
var argc = SetCookie.arguments.length;
var expires = (argc > 2) ? argv[2] : null;
var path = (argc > 3) ? argv[3] : null;
var domain = (argc > 4) ? argv[4] : null;
var secure = (argc > 5) ? argv[5] : false;
document.cookie = name + "=" + escape (value) +
((expires == null) ? "" : ("; expires=" + 
expires.toGMTString())) + 
((path == null) ? "" : ("; path=" + path)) +
((domain == null) ? "" : ("; domain=" + domain)) +
((secure == true) ? "; secure" : "");
}
if (username == null || username == '') {
    console.log("Вы не авторизированы!")
document.write('<p>Авторизация</p><input type="login" placeholder="Логин" class="inp" id ="nam"><br/><input type="password" id="password" placeholder="Пароль" class="inp"><br/><input type="submit" id="sub" value="ВХОД">');
} else {
document.write('<div id="color"<p align=right>Здравствуйте, ' + username + '</p></form><form onsubmit="delCok()" action="get"><input type="submit" value="Выход" id="sub"></form></div>');
}