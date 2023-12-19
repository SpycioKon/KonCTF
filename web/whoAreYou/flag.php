<h1>Bạn có biết blackbox pentest không??</h1>
<?php
require('./setup/User.php');

function isRole($user){
    return $user->getRole();
}
if(!isset($_COOKIE['data'])){
    die("<p>Chỉ có nguoi dep troai moi duoc o day</p>");
}
if(isset($_GET['check'])){
    highlight_file('./setup/User.php');
}
$cookie = unserialize(base64_decode($_COOKIE['data']));
if(isRole($cookie)===true){
    echo "the flag for you: KonCTF{You_4r3_handSom3}";
}
?>