<?php
include('conexao.php');
if(isset($_POST['Usuario']) || isset($_POST['senha'])){

  if(strlen($_POST['usuario']) == 0){
    echo "<div class=erro>";
      echo "Por favor preencher o campo de usuario";
    echo "</div>";
  } else if(strlen($_POST['senha']) == 0){
    echo "<div class=erro>";
      echo "Por favor preencher a senha";
    echo "</div>";
  }else {

    $usuario = $mysqli->real_escape_string($_POST['usuario']);
    $senha = $mysqli->real_escape_string($_POST['senha']);

    $sql_code = "SELECT *FROM login WHERE usuario = '$email'";
    $sql_query = $mysqli->query($sql_code) or die("Falha no codigo SQL: " . $mysqli->error);

    $quantidade = $sql_query->num_rows;

    if($quantidade == 1){

      $usuario = $sql_query->fetch_assoc();

      if(password_verify($senha, $usuario['senha'])){

        if(!isset($_SESSION)){
          session_start();
        }
        $_SESSION['acesso'] = true;
        if($_SESSION['acesso'] == true){
          echo "";
        }

        header("Location: index.php");
      }
    } else {
      echo "<div class=erro>";
        echo "Falha ao logar! E-mail e/ou senha incorretos";
      echo "</div>";
    }
  }
}
?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link rel="stylesheet" href="estilo.css">
    <style>
      .Acesso{
        border: solid;
        width: 200px;
        padding: 40px;
        border-radius: 10px;
        background-color: rgba(100, 0, 200, 0.3);
        margin-left: 40%;
        margin-top: 15%;
      }
      #botao{
        margin-left: 65px;
      }
      input{
        margin-left: 13px;
        border-radius: 10px;
      }
      h1{
        margin-left: 50px;
      }
      .erro{
        background-color: rgba(255, 0, 0, 0.5);
        padding: 5px;
        width: 290px;
        margin: 320px 10px 10px 585px;
        position: fixed;
        border-radius: 10px;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div class="Acesso">
      <form action="" method="post">
        <font face="Arial"> <h1>LOGIN</h1> </font><br>
        <input type="text" placeholder="Usuario" name="usuario"><br><br>
        <input type="password" placeholder="Senha" name ="senha"><br><br>
        <input type="submit" value="Acessar" id="botao">
      </form>
    </div>
  </body>
</html>
