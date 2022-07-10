<?php
session_start();
if ($_SESSION['acesso'] == true) {
  echo "";
}
if ($_SESSION['acesso'] == NULL){
  header('Location: login.php');
}
if($_POST == true){
  session_destroy();
  header('Location: login.php');
}
 ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <style>
      input{
        background-color: rgba(255, 0, 255, 0.2);
        color: white;
        width: 130px;
        height: 30px;
      }
    </style>
  </head>
  <body>
    <form action="" method="post">
      <input type="submit" name="botao" value="Encerrar sessão">
    </form>
  </body>
</html>
