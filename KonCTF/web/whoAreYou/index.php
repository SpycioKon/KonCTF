<?php
// @error_reporting(1);
require('setup/User.php');

if($_SERVER['REQUEST_METHOD'] == 'POST'){
  if(isset($_POST['user'])){
    $user = new User($_POST['user']);
    $userSeri = base64_encode(serialize($user));
    setcookie("data",$userSeri);
  }
}
?>
<!DOCTYPE html>
<html>
  <head>
    <title>Pentest</title>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
      <!-- jQuery library -->
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
      <!-- Latest compiled JavaScript -->
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
      <!-- Reactjs library -->
      <script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
  </head>
  <body>
    <div class="container">
      <form action="#" method="post" enctype="application/x-www-form-urlencoded" class="d-flex" style="margin-top:3em">
        <input type="search" placeholder="Toi dep troai" class="form-control me 2" name="user">
        <button type="send" class="btn btn-outline-info">Send</button>
      </form>
    </div>
  </body>
</html>
