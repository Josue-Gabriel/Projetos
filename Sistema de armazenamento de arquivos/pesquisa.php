<?php
session_start();
if ($_SESSION['acesso'] == true) {
  echo "";
}
if ($_SESSION['acesso'] == NULL){
  header('Location: login.php');
}
 include('conexao.php');

 $stat = $dbh->prepare("select *from informações order by data desc");
 $stat->execute();
echo "<div class=navbar navbar-expand-lg fixed-top pesquisas>";
  echo "<div class=voltar>";
    echo "<a href=index.php> <img src=imagem/seta.png width=35px id='seta'> <h5>Voltar</h5> </a>";
  echo "</div><br>";

  echo "<div class=busca>";
    echo "<form action=pesquisado.php method=GET>";
      echo "<input type=text name=busca id=pesquisar placeholder=Buscar...>";
      echo "<button><img src=imagem/lupa.png width=13px></button>";
    echo "</div>";
  echo "</div>";
echo "</div><br>";

 while($row = $stat->fetch()){
   echo "<div class= informaçoees>";
      echo "NOME: ".$row['nome']."<br><br>";
      echo "ARQUIVO: <a href='view.php?id=".$row['id']."'>".$row['name']."</a><br><br>";
      echo "DESCRIÇÃO: ".$row['descricao']."<br><br>";
      echo "TIPO: ".$row['tipo']."<br><br>";
      echo "Data de envio: ".date("d/m/Y", strtotime($row["data"]))."<br><br>";
   echo "</div><br>";
 }
?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <link rel="stylesheet">
    <meta charset="utf-8">
    <title>Pesquisa</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
    rel="stylesheet"
    integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
    crossorigin="anonymous">
    <script type="text/javascript" src="configurações.js"></script>
    <style>
    .informaçoees{
      color: white;
      border: solid;
      padding: 20px;
      background-color: rgba(100, 0, 255, 0.25);
    }
    #pesquisar{
      display: flex;
      justify-content: center;
      width: 100%;
      background-color: transparent;
      border: none;
    }
    .busca{
      border: solid;
      width: 40%;
      height: 26px;
      color: purple;
      background-color: purple;
      margin-left: 150px;
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
    }
    h5{
      margin-top: -33px;
      margin-left: 50px;
    }
    body{
      background-color: black;
    }
    @media screen and (max-width: 1068px){
      .voltar{
        font-size: 30px;
        width: 200px;
        height: 60px;
      }
      #seta{
        width: 45px;
      }
      h2{
        margin-top: -45px;
      }
      #pesquisar{
        font-size: 100%;
      }
      .busca{
        height: 30px;
      }
    }
    </style>
  </head>
  <body>
  </body>
</html>
