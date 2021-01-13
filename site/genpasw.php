<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css"> 
	<script type="text/javascript">
		function write(text){
			document.getElementById("info").innerHTML = text;
		}	
		
		function readInt(){
			return +document.getElementById("userAnswer").value;
		}	
			
		function RandomPassword(){
			var StringPassword = "",
				StringSymbols = "1234567890qwertyuiopasdfghjklzxcvbnm",
				CountRandom = readInt() ;
			for (var i = 0; i<CountRandom; i++){
				Random = Math.round(Math.random()*StringSymbols.length);
				var RandomUpper = Math.round(Math.random()*CountRandom);
				if (RandomUpper>=(CountRandom/2)) {StringPassword += StringSymbols[Random].toUpperCase()}
				if (RandomUpper<(CountRandom/2)) {StringPassword += StringSymbols[Random].toLowerCase()}      
			}
 
		write("Пароль: "+StringPassword);
		}
						
	</script>
</head>
<body>
<div class="content">
	<?php
		include "menu.php";
	?>

<div class="contentWrap">
    <div class="content">
        <div class="center">

			<h1>Генератор паролей</h1><br>
			<div class="box">
			<h2>Введите количество символов</h2><br>
			<input type="text" id="userAnswer">
			<br>
			<p id="info">Просто нажми кнопку!</p><br>	
			
			<a href="#" onClick="RandomPassword();" id="button">Сгенерировать пароль</a>
			</div>			
			</div>

        </div>
    </div>
</div>

	


<div class="footer">
	Copyright &copy; by Catofey Rybkin <?php echo date("Y");?>
<div>


</body>
</html>