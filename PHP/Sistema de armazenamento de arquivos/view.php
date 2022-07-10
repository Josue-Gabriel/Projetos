<?php
include('conexao.php');
$id = isset($_GET['id'])? $_GET['id'] : "";
$stat = $dbh->prepare("select *from info where id=?");
$stat->bindParam(1, $id); 
$stat->execute();
$row = $stat->fetch();
header('Content-Type:'.$row['mime']);
echo $row['arquivo'];
?>
