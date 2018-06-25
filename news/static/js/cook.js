
        console.log("Вы не авторизированы!")
        document.write('<div id="login-form"><h1>Авторизация на сайте</h1><fieldset><input type="login" placeholder="Логин" id ="nam"><br/><input type="password" id="password" placeholder="Пароль"><br/><input type="submit" value="ВХОД"><footer class="clearfix"><p><span class="info">?</span><a href="#">Забыли пароль?</a></p></footer></form></fieldset></div>');
    } else {
        console.log("Вы авторизированы как, " + username)
        document.write('<div id="login-form"><h1>Здравствуйте, ' + username + '</h1><fieldset></form><form onsubmit="delCok()" action="get"><input type="submit" value="Выход"></form></fieldset></div>');
    }