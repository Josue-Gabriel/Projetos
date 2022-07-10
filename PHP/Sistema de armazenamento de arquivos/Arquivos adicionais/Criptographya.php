
<!DOCTYPE html>
<?php
//Sistema de cadastro de usuario e senha criptografada.
$usuario = 'root';
$senha = ''; //Senha de acesso aos bancos de dados.
$database = ''; //nome do banco de dados que sera usado.
$host = 'localhost';

$mysqli = new mysqli($host, $email, $senha, $database);

if(isset($_POST['email'])){

  $email = $_POST['email'];
  $senha = password_hash($_POST['senha'], PASSWORD_DEFAULT);

  $mysqli->query("INSERT INTO login (email, senha) VALUES ('$email', '$senha')");

}
?>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Por favor fassa o seu registro para continuar nessa jornada de PHP</h1>
    <form action="" method="post">
      <input type="text" name="email"><p>
      <input type="text" name="senha"><p>
      <button type="submit">Cadastrar</button>
    </form>
  </body>
</html>
