/* ------------------------ */
/*  XMLHTTPRequest Enable   */
/* ------------------------ */
function createObject() {
var request_type;
var browser = navigator.appName;
if(browser == "Microsoft Internet Explorer"){
request_type = new ActiveXObject("Microsoft.XMLHTTP");
}else{
request_type = new XMLHttpRequest();
}
return request_type;
}

var http = createObject();


/* ----------------------- */
/*      LOGIN              */
/* ----------------------- */
/* ѕеременна€ nocache содержит случайное число, добавл€емое в запрос
   дл€ предотвращени€ кешировани€ браузером запроса */
var nocache = 0;
function login() {
 // ќтображаем соощение в области ID ajax_response
 document.getElementById('login_response').innerHTML = "Loading..."
    // ѕровер€ем, что все пол€ не пустые. »спользуем encodeURI() дл€ кодировани€ недопустимых символов в запросе.
var email = encodeURI(document.getElementById('emailLogin').value);
var psw = encodeURI(document.getElementById('pswLogin').value);
 // ѕолучаем случайное число
nocache = Math.random();
 // Pass the login variables like URL variable
http.open('get', 'login.php?email='+email+'&psw='+psw+'&nocache = '+nocache);
http.onreadystatechange = loginReply;
http.send(null);
}
function loginReply() {
if(http.readyState == 4){ 
var response = http.responseText;
 if(response == '0'){
// if login fails
  document.getElementById('login_response').innerHTML = 'Login failed! Verify user and password';
// else if login is ok show a message: "Welcome + the user name".
  } else {
document.getElementById('login_response').innerHTML = 'Welcome'+response;
  }
}
 }