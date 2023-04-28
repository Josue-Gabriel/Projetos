<?php
include('conexao.php');
if(isset($_POST['email']) || isset($_POST['senha'])){

  if(strlen($_POST['email']) == 0){
    echo "<div class=erro>";
      echo "Por favor preencher o e-mail";
    echo "</div>";
  } else if(strlen($_POST['senha']) == 0){
    echo "<div class=erro>";
      echo "Por favor preencher a senha";
    echo "</div>";
  }else {

    $email = $mysqli->real_escape_string($_POST['email']);
    $senha = $mysqli->real_escape_string($_POST['senha']);

    $sql_code = "SELECT *FROM login WHERE email = '$email'";
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
      @media screen and (max-width: 1068px){
        .Acesso{
          border: solid;
          width: 450px;
          padding: 20px;
          background-color: rgba(100, 0, 200, 0.3);
          border-radius: 10px;
          margin-left: 25%;
          margin-top: 55%;
          font-size: 45px;
        }
        body{
          background-size: 200%, 50%, -200%;
        }
        input{
          font-size: 30px;
        }
        #botao{
          margin-left: 150px;
        }
        h1{
          margin-left: 100px;
          margin-bottom: 10px;
        }
      }
    </style>
  </head>
  <body>
    <div class="Acesso">
      <form action="" method="post">
        <font face="Arial"> <h1>LOGIN</h1> </font><br>
        <input type="text" placeholder="Usuario" name="email"><br><br>
        <input type="password" placeholder="Senha" name ="senha"><br><br>
        <input type="submit" value="Acessar" id="botao">
      </form>
    </div>
  </body>
</html>
