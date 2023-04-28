<?php
include_once 'proteção.php';
 ?>
<!DOCTYPE html>
<html>
<head>
  <title>Index</title>
  <link rel="stylesheet" href="estilo.css">
  <style>

    button{
      background: rgba(255, 0, 200, 0.2);
    }
    img{
      width: 250px;
    }
    .botao{
      margin-left: 25%;
      margin-top: 15%;
    }
    #pesquisa{
      margin: 10px 100px 10px 50px;
      transition: transform 0.5s;
    }
    #salvar{
      margin: 10px 10px 10px 50px;
      transition: transform 0.5s;
    }
    #pesquisa:hover{
      transform: scale(1.2);
    }
    #salvar:hover{
      transform: scale(1.2);
    }
    @media screen and (max-width: 1068px){
      .botao{
        margin-left: 9%;
        margin-top: 60%;
      }
      
    }

  </style>
</head>
<body>
  <div class="botao">
    <button type="button" name="button" id="pesquisa"> <a href="Salvar.php"> <img src="imagem/banco de dados.png"> </a> </button>
    <button type="button" name="button" id="salvar"> <a href="pesquisa.php"> <img src="imagem/lupa.png"> </a> </button>
  </div>
</body>
</html>
