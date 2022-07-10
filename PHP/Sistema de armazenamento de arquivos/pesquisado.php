<?php
session_start();
if ($_SESSION['acesso'] == true) {
  echo "";
}
if ($_SESSION['acesso'] == NULL){
  header('Location: login.php');
}
include('conexao.php');

if (!isset($_GET['busca'])){
  header("Location: pesquisa.php");
  exit;
}

$nome = "%".trim($_GET['busca'])."%";

$sth = $dbh->prepare('SELECT *FROM `info` WHERE `nome` LIKE :nome');
$sth->bindParam(':nome', $nome, PDO::PARAM_STR);
$sth->execute();

echo "<div class=voltar>";
  echo "<a href=pesquisa.php> <img src=imagem/seta.png width=35px> <h2>Voltar</h2> </a>";
echo "</div><br>";

echo "<div class=delet>";
  echo "<form method=post>";
    echo "<input type=submit name=deletar id=apg value=Deletar>";
echo "</div>";
while($row = $sth->fetch()){
  echo "<div class= informaçoees>";
     echo "NOME: ".$row['nome']."<br><br>";
     echo "ARQUIVO: <a href='view.php?id=".$row['id']."'>".$row['name']."</a><br><br>";
     echo "DESCRIÇÃO: ".$row['descricao']."<br><br>";
     echo "TIPO: ".$row['tipo']."<br><br>";
  echo "</div><br>";
  if(isset($_POST['deletar'])){
    $apagar = $dbh->prepare("DELETE FROM `info` WHERE `nome` LIKE :nome");
    $apagar->bindParam(':nome', $nome, PDO::PARAM_STR);
    $apagar->execute();
  }
}
?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <link rel="stylesheet" href="estilo.css">
    <meta charset="utf-8">
    <title>Pesquisa</title>
    <style>
    .informaçoees{
      color: white;
      border: solid;
      padding: 20px;
      background-color: rgba(100, 0, 255, 0.25);
    }
    #pesquisar{
      padding: 4px;
      background-color: transparent;
      border: none;
    }
    button{
      position: inherit;
      background-color: transparent;
      border: none;
    }
    .voltar{
      border: solid;
      border-radius: 10px;
      width: 130px;
      background-color: purple;
      height: 40px;
      position: fixed;
    }
    h2{
      margin-top: -33px;
      margin-left: 50px;
    }
    #apg{
      background-color: purple;
      margin-left: 150px;
      margin-top: -16px;
      padding: 10px;
    }
    </style>
  </head>
  <body>
  </body>
</html>
