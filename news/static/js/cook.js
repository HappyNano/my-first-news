    console.log('Соеденяемся с серверами...');
    var username = GetCookie('username');
    var pathname = location.pathname;
    var myDomain = pathname.substring(0, pathname.lastIndexOf('/')) + '/';
    // Установка параметра expire на год вперед.
    var largeExpDate = new Date();
    largeExpDate.setTime(largeExpDate.getTime() + (365 * 24 * 3600 * 1000));
    function cook() {
        username = document.getElementByld("nam").value;
    }
    function getCookieVal(offset) {
        var endstr = document.cookie.indexOf(";", offset);
        if (endstr == -1)
            endstr = document.cookie.length;
        return unescape(document.cookie.substring(offset, endstr));
    }
    function GetCookie(name) {
        var arg = name + "=";
        var alen = arg.length;
        var clen = document.cookie.length;
        var i = 0;
        while (i < clen) {
            var j = i + alen;
            if (document.cookie.substring(i, j) == arg)
                return getCookieVal(j);
            i = document.cookie.indexOf(" ", i) + 1;
            if (i == 0)
                break;
        }
        return null;
    }

    function delCok() {
        var largeExpDate = new Date();
        largeExpDate.setTime(largeExpDate.getTime() + (-100));
        var path = (argc > 3) ? argv[3] : null;
        var domain = (argc > 4) ? argv[4] : null;
        var secure = (argc > 5) ? argv[5] : false;
        document.cookie = "username" + "=" + escape(value) +
            ((expires == null) ? "" : ("; expires=" +
                expires.toGMTString())) +
            ((path == null) ? "" : ("; path=" + path)) +
            ((domain == null) ? "" : ("; domain=" + domain)) +
            ((secure == true) ? "; secure" : "");
    }


    function SetCookie(name, value) {
        var argv = SetCookie.arguments;
        var argc = SetCookie.arguments.length;
        var expires = (argc > 2) ? argv[2] : null;
        var path = (argc > 3) ? argv[3] : null;
        var domain = (argc > 4) ? argv[4] : null;
        var secure = (argc > 5) ? argv[5] : false;
        document.cookie = name + "=" + escape(value) +
            ((expires == null) ? "" : ("; expires=" +
                expires.toGMTString())) +
            ((path == null) ? "" : ("; path=" + path)) +
            ((domain == null) ? "" : ("; domain=" + domain)) +
            ((secure == true) ? "; secure" : "");
    }
    if (username == null || username == '') {
        console.log("Вы не авторизированы!")
        document.write('<div id="login-form"><h1>Авторизация на сайте</h1><fieldset><input type="login" placeholder="Логин" id ="nam"><br/><input type="password" id="password" placeholder="Пароль"><br/><input type="submit" value="ВХОД"><footer class="clearfix"><p><span class="info">?</span><a href="#">Забыли пароль?</a></p></footer></form></fieldset></div>');
    } else {
        console.log("Вы авторизированы как, " + username)
        document.write('<div id="login-form"><h1>Здравствуйте, ' + username + '</h1><fieldset></form><form onsubmit="delCok()" action="get"><input type="submit" value="Выход"></form></fieldset></div>');
    }