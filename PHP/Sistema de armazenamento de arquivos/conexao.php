<?php

  $usuario = '';
  $senha = '';
  $database = 'arquivos';
  $host = 'localhost';

  $mysqli = new mysqli($host, $usuario, $senha, $database);

  $dbh = new PDO("mysql: host=localhost ;dbname=arquivos", "", "");
  if($dbh && $mysqli == false){
    die("Falha na conexão com o banco de dados :");
  }
