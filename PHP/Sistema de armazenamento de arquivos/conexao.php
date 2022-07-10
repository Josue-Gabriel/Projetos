<?php
  $usuario = 'root';
  $senha = ''; //Senha de acesso ao banco aos bancos de dados. 
  $database = 'arquivos';
  $host = 'localhost';

  $mysqli = new mysqli($host, $usuario, $senha, $database);

  $dbh = new PDO("mysql: host=localhost ;dbname=arquivos", "root", "jo4056");
  if($dbh && $mysqli == false){
    die("Falha na conexão com o banco de dados :");
  }
