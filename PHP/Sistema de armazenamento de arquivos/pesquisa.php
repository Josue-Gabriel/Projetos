<?php
session_start();
if ($_SESSION['acesso'] == true) {
  echo "";
}
if ($_SESSION['acesso'] == NULL){
  header('Location: login.php');
}
 include('conexao.php');

 $stat = $dbh->prepare("select *from info");
 $stat->execute();

 echo "<div class=voltar>";
   echo "<a href=index.php> <img src=imagem/seta.png width=35px> <h2>Voltar</h2> </a>";
 echo "</div><br>";

echo "<div class=busca>";
  echo "<form action=pesquisado.php method=GET>";
    echo "<input type=text name=busca id=pesquisar placeholder=Buscar...>";
    echo "<button><img src=imagem/lupa.png width=13px></button>";
  echo "</div>";
echo "</div><br>";

 while($row = $stat->fetch()){
   echo "<div class= informaçoees>";
      echo "NOME: ".$row['nome']."<br><br>";
      echo "ARQUIVO: <a href='view.php?id=".$row['id']."'>".$row['name']."</a><br><br>";
      echo "DESCRIÇÃO: ".$row['descricao']."<br><br>";
      echo "TIPO: ".$row['tipo']."<br><br>";
   echo "</div><br>";
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
    .busca{
      border: solid;
      width: 200px;
      height: 23px;
      color: purple;
      background-color: purple;
      margin-left: 150px;
      margin-top: -11px;
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
    </style>
  </head>
  <body>
  </body>
</html>
