<?php
session_start();
if ($_SESSION['acesso'] == true) {
  echo "";
}
if ($_SESSION['acesso'] == NULL){
  header('Location: login.php');
}

include('conexao.php');

echo "<div class=voltar>";
  echo "<a href=index.php> <img src=imagem/seta.png width=35px id='seta'> <h2>Voltar</h2> </a>";
echo "</div><br>";

?>
<!DOCTYPE html>
<html>
<head>
  <title>Armazenamento</title>
  <link rel="stylesheet" href="estilo.css">
  <meta charset="utf-8"/>
  <title>My test Blob</title>
  <style>
    .information{
      position: absolute;
      border: solid;
      border-radius: 10px;
      margin-left: 35%;
      margin-top: 15%;
      padding: 50px;
      background-color: rgba(100, 0, 200, 0.3);
    }
    button{
      margin: 10px 10px 10px 110px;
    }
    #nome{
      width: 338px;
    }
    #descrição{
      width: 260px;
    }
    #tipo{
      width: 65px;
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
    .save{
      background-color: rgba(0, 255, 0, 0.5);
      padding: 5px;
      width: 290px;
      margin: 500px 10px 10px 595px;
      position: fixed;
      border-radius: 10px;
      text-align: center;
    }
    @media screen and (max-width: 1068px){
      .information{
        margin-left: 13%;
        margin-top: 58%;
      }
      input{
        font-size: 30px;
      }
      #nome{
        width: 600px;
      }
      #descrição{
        width: 445px;
      }
      #tipo{
        width: 150px;
      }
      button{
        font-size: 30px;
        margin-left: 250px;
      }
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
      .save{
        margin-top: 950px;
        margin-left: 225px;
        font-size: 50px;
        width: 500px;
      }
    }
  </style>
</head>
<body>
  <?php
  if(isset($_POST['btn'])){
    $data = date("Ymd");
    $name = $_FILES['myfile']['name'];
    $type = $_FILES['myfile']['type'];
    $nome = addslashes($_POST['nome']);
    $descricao = addslashes($_POST['descricao']);
    $tipo = addslashes($_POST['tipo']);
    $date = file_get_contents($_FILES['myfile']['tmp_name']);
    $stmt = $dbh->prepare("insert into informações values(default,?,?,?,?,?,?,$data)");
    $stmt->bindParam(1,$name);
    $stmt->bindParam(2,$type);
    $stmt->bindParam(3,$date);
    $stmt->bindParam(4,$nome);
    $stmt->bindParam(5,$descricao);
    $stmt->bindParam(6,$tipo);
    $stmt->execute();
    echo "<div class=save>";
      echo "Informações salvas com sucesso";
    echo "</div>";
  }
  ?>
  <form method="post" enctype="multipart/form-data">
    <div class="information">
      <input type="text" placeholder="nome" name="nome" id="nome"><br><br>
      <input type="text" placeholder="Descrição" name="descricao" id="descrição">
      <input type="text" placeholder="Tipo" name="tipo" id="tipo"><br><br>
      <input type="file" name="myfile"/><br><br>
      <button name="btn">Upload</button>
    </div>
  </form>
</body>
</html>
