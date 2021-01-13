 <!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css"> 
	<script type="text/javascript">

		var answer = parseInt(Math.random() * 100);
		var tryCount = 0;
		var maxTryCount = 3;
		
		function readInt(numb){
			var number = document.getElementById(numb).value;
			return parseInt(number);
			// return +document.getElementById("userAnswer").value;
		}
		
		function numbGame(numb){
			if (numb == 'userAnswer1'){
			return "Игрок №1"
			}else if(numb == 'userAnswer2'){
			return "Игрок №2"
			}
		}
		
		function write(numb, text){
			if (numb == 'userAnswer1'){
			document.getElementById("info1").innerHTML = text;
			}else if(numb == 'userAnswer2'){
			document.getElementById("info2").innerHTML = text;
			}
		}

		function hide(numb){
			if (numb == 'userAnswer1'){
			document.getElementById('button1').style.display = "none";
			}else if(numb == 'userAnswer2'){
			document.getElementById('button2').style.display = "none";
			}
		}
		
		function hideReverse(numb){
			if (numb == 'userAnswer1'){
			document.getElementById('button2').style.display = "none";
			}else if(numb == 'userAnswer2'){
			document.getElementById('button1').style.display = "none";
			}
		}
		
		
		
		
		function guess(numb){
			tryCount++;

			var userAnswer = readInt(numb);
			if(userAnswer == answer){
				write(numb, numbGame(numb) + "<b> Поздравляю, вы угадали!</b>");
				hide(numb);
				hideReverse(numb);
				
			}else if(tryCount >= maxTryCount){
				write(numb, numbGame(numb) + " Вы проиграли<br>Правильный ответ: " + answer);
				hide(numb);
				answer = parseInt(Math.random() * 100);
				
			}else if(userAnswer > answer){
				write(numb, numbGame(numb) + " Вы ввели слишком большое число<br>Попробуйте еще раз. Введите число от 1 до 100");
			}else if(userAnswer < answer){
				write(numb, numbGame(numb) + " Вы ввели слишком маленькое число<br>Попробуйте еще раз. Введите число от 1 до 100");				
			}
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

			<h1>Игра угадайка на двоих с подвохом ;)</h1>

			<div class="box">

				<p id="info1">Игрок 1 угадайте число от 0 до 100</p>
				<input type="text" id="userAnswer1">
				<br>
				<a href="#" onClick="guess('userAnswer1');" id="button1">Начать</a>	
				<br><br><br><br>
				<p id="info2">Игрок 2 угадайте число от 0 до 100</p>
				<input type="text" id="userAnswer2"><br>
				
				<br><a href="#" onClick="guess('userAnswer2');" id="button2">Начать</a>	
				
			</div>

        </div>
    </div>
</div>

	

</div>
<div class="footer">
	Copyright &copy; by Catofey Copyright &copy; by Catofey Rybkin <?php echo date("Y");?>
<div>


</body>
</html>