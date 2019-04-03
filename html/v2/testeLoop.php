<!DOCTYPE html>
<html lang="pt-BR">
<head>
	<meta charset="UTF-8">
	<meta name="autor" content="">
	<meta name="keywords" content="">
	<meta name="description" content="">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Listas Anotadas de Medicamentos</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<link rel="stylesheet" href="style.css">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css">
</head>
<body>
	<?php include 'header.php' ?>
	
	<section>
		<div class="container">
			<?php 
			$p = 1;
			echo "<ul type='square'>";
			while ($p <= 20) {
				echo "<li><a href='' data-toggle='collapse' data-target='#M".$p."'>".$p."- Nivel 1</a></li>";
				$p2 = $p;
				$p++; 

				$s = 1;
				echo "<ul class='collapse' id='M".$p2."'>";
				while ($s <= 3) {
					echo "<li><a href='' data-toggle='collapse' data-target='#M".$p2."-".$s."'>".$p2."-".$s."- Nivel 2</a></li>";
					$s2 = $s;
					$s++;

					$t = 1;
					echo "<ul class='collapse' id='M".$p2."-".$s2."'>";
					while ($t <= 3) {
						// echo "<li>".$p2." - ".$s2." - ".$t."</li>";
						echo "<li><a href='' data-toggle='collapse' data-target='#M".$p2."-".$s2."-".$t."'>".$p2." - ".$s2." - ".$t."- Nivel 3</a></li>";
						echo "<div class='collapse' id='M".$p2."-".$s2."-".$t."'>tabela</div>";
						$t++;
					}echo "</ul>";
				}echo "</ul>";
			}echo "</ul>";
			?>
		</div>
	</section>



	<?php include 'footer.php' ?>
	<script src="js/jquery-3.3.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
</body>
</html>