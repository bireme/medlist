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
	<section class="container">
		<nav aria-label="breadcrumb">
			<ol class="breadcrumb">
				<li class="breadcrumb-item"><a href="index.php">Home</a></li>
				<li class="breadcrumb-item active" aria-current="page">Comprar Listas</li>
			</ol>
		</nav>

		<h1 class="titulo1"><span class="colorText">Comprar</span> Listas</h1>

		<div class="alert alert-secondary">
			<h4>Filtros:</h4>
			<hr>
			<form action="" >
				<b>Listas: </b>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="who" value="option1" checked="">
					<label class="form-check-label" for="who">WHO EML 1</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="who1" value="option1">
					<label class="form-check-label" for="who2">WHO EML 1</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="paho" value="option2" checked="">
					<label class="form-check-label" for="paho">PAHO SF 1</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="paho2" value="option2">
					<label class="form-check-label" for="paho2">PAHO SF 2</label>
				</div>
				<!--
				<hr>
				<b>Países</b>        
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="BOL" value="option1">
					<label class="form-check-label" for="BOL">BOL</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="COL" value="option2">
					<label class="form-check-label" for="COL">COL</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="BRA" value="option1">
					<label class="form-check-label" for="BRA">BRA</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="PER" value="option2">
					<label class="form-check-label" for="PER">PER</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="ECU" value="option1">
					<label class="form-check-label" for="ECU">ECU</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="CHI" value="option2">
					<label class="form-check-label" for="CHI">CHI</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="CU" value="option1">
					<label class="form-check-label" for="CU">CU</label>
				</div>
				<div class="form-check form-check-inline">
					<input class="form-check-input" type="checkbox" id="VEN" value="option2">
					<label class="form-check-label" for="VEN">VEN</label>
				</div> -->
			</form>
		</div>
		<!-- Paginação 1 -->
		<nav aria-label="Page navigation example">
			<ul class="pagination justify-content-center pagination-sm">
				<li class="page-item">
					<a class="page-link" href="#"><i class="fas fa-backward"></i></a>
				</li>
				<li class="page-item">
					<a class="page-link" href="#"><i class="fas fa-caret-left"></i></a>
				</li>
				<li class="page-item"><a class="page-link" href="#">1</a></li>
				<li class="page-item active"><a class="page-link" href="#">2</a></li>
				<li class="page-item"><a class="page-link" href="#">3</a></li>
				<li class="page-item"><a class="page-link" href="#">4</a></li>
				<li class="page-item"><a class="page-link" href="#">5</a></li>
				<li class="page-item"><a class="page-link" href="#">6</a></li>
				<li class="page-item"><a class="page-link" href="#">7</a></li>
				<li class="page-item"><a class="page-link" href="#">8</a></li>
				<li class="page-item"><a class="page-link" href="#">9</a></li>
				<li class="page-item">
					<a class="page-link" href="#"><i class="fas fa-caret-right"></i></a>
				</li>
				<li class="page-item">
					<a class="page-link" href="#"><i class="fas fa-forward"></i></a>
				</li>
			</ul>
		</nav>

		<!-- Tabela -->
		<div class="table-responsive">
			<table class="table table-sm table-hover table-striped">
				<thead>
					<tr>
						<th>Nome</th>
						<th>Formas Farmacêuticas</th>
						<th class="text-center">WHO EML</th>
						<th class="text-center">PAHO SF</th>
						<th class="text-center">BOL</th>
						<th class="text-center">COL</th>
						<th class="text-center">BRA</th>
						<th class="text-center">PER</th>
						<th class="text-center">ECU</th>
						<th class="text-center">CHI</th>
						<th class="text-center">CU</th>
						<th class="text-center">VEN</th>
					</tr>
				</thead>
				<tbody>
					<?php 
					for ($i=0; $i < 20; $i++) { 
						?>
						<tr>
							<td class="tbLargura"><a href="medicamento.php">Abacavir</a></td>
							<td class="tbLargura">Oral liquid 20mg/ml.</td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
							<td class="text-center"><i class="fas fa-check"></i></td>
						</tr>
					<?php } ?>
				</tbody>
			</table>
		</div>

		<!-- Paginação 2 -->
		<nav aria-label="Page navigation example">
			<ul class="pagination justify-content-center pagination-sm">
				<li class="page-item">
					<a class="page-link" href="#"><i class="fas fa-backward"></i></a>
				</li>
				<li class="page-item">
					<a class="page-link" href="#"><i class="fas fa-caret-left"></i></a>
				</li>
				<li class="page-item"><a class="page-link" href="#">1</a></li>
				<li class="page-item active"><a class="page-link" href="#">2</a></li>
				<li class="page-item"><a class="page-link" href="#">3</a></li>
				<li class="page-item"><a class="page-link" href="#">4</a></li>
				<li class="page-item"><a class="page-link" href="#">5</a></li>
				<li class="page-item"><a class="page-link" href="#">6</a></li>
				<li class="page-item"><a class="page-link" href="#">7</a></li>
				<li class="page-item"><a class="page-link" href="#">8</a></li>
				<li class="page-item"><a class="page-link" href="#">9</a></li>
				<li class="page-item">
					<a class="page-link" href="#"><i class="fas fa-caret-right"></i></a>
				</li>
				<li class="page-item">
					<a class="page-link" href="#"><i class="fas fa-forward"></i></a>
				</li>
			</ul>
		</nav>
	</section>

	

	<?php include 'footer.php' ?>
	<script src="js/jquery-3.3.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
</body>
</html>