<!DOCTYPE html>
<html lang="pt-BR">
<head>
	<meta charset="UTF-8">
	<meta name="autor" content="">
	<meta name="keywords" content="">
	<meta name="description" content="">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Listas Anotadas de Medicamentos e Dispostivos</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<link rel="stylesheet" href="style.css">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css">
</head>
<body>
	<?php include 'header.php' ?>
	<section class="container" id="banner">
		<img src="img/banner.jpg" class="img-fluid" alt="">	
		<div id="bannerTexto">
			<h1 class="text-center counter-up" data-count-to="12000"><span></span></h1>
			<h3 class="text-center">Medicamentos Cadastrados</h3>
		</div>
	</section>
	
	<section class="container">
		<div class="row">
			<div class="col-md-10 offset-md-1">
				<div class="row">
					<!-- lista 1 -->
					<div class="col-md-3">
						<div class="homeBox">
							<img src="img/lista1.png" alt="">
							<a href="lista.php" class="btn btn-sm btn-primary btn-block">WHO Model List of Essential Medicines</a>
							<button type="button" class="btn btn-outline-primary btn-sm btn-block dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Comparar Listas</button>
							<div class="dropdown-menu">
								<a class="dropdown-item" href="comparar.php">Listas 1</a>
								<a class="dropdown-item" href="comparar.php">Listas 2</a>
							</div>
						</div>
					</div>
					<!-- lista 2 -->
					<div class="col-md-3">
						<div class="homeBox">
							<img src="img/lista2.png" alt="">
							<a href="lista.php" class="btn btn-sm btn-primary btn-block">PAHO Strategic Fund Medicine List</a>
							<button type="button" class="btn btn-outline-primary btn-sm btn-block dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Comparar Listas</button>
							<div class="dropdown-menu">
								<a class="dropdown-item" href="comparar.php">Listas 1</a>
								<a class="dropdown-item" href="comparar.php">Listas 2</a>
							</div>	
						</div>
					</div>
					<!-- lista 3 -->
					<div class="col-md-3">
						<div class="homeBox">
							<img src="img/lista3.png" alt="">
							<a href="sumario.php" class="btn btn-sm btn-primary btn-block">Exibir todos sumários de evidência</a>
						</div>
					</div>
					<!-- lista 4 -->
					<div class="col-md-3">
						<div class="homeBox">
							<img src="img/lista4.png" alt="">
							<a href="" class="btn btn-sm btn-primary btn-block">Exibir todos sumários de evidência</a>
						</div>
					</div>
				</div>
			</div>
			
		</div>
	</section>


	<section class="sectionCinza padding1">
		<div class="container">
			<h3 class="titulo1"><span class="colorText">Novo</span> Tituto</h3>
			<hr>
			<p class="text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellat eius nobis a adipisci accusantium accusamus aut veniam ad deserunt iusto aperiam excepturi deleniti, eum earum quisquam, voluptas tenetur nulla praesentium voluptatibus? Quod magnam rem, illo facilis natus odio, cumque, minus porro debitis fugit similique vitae sequi. Illum fuga recusandae voluptates adipisci impedit, vitae voluptate excepturi? Assumenda ullam quibusdam non reiciendis, repellat libero, atque, molestias nisi eum a blanditiis voluptate fuga eos officia! Rem tempora, quae quaerat harum tenetur aut cupiditate. Quisquam quasi obcaecati quae vel aut inventore, labore! Voluptatibus qui quod eius rem, in minus excepturi illum expedita voluptas placeat doloribus aliquid laboriosam nisi, consequuntur architecto tenetur. Ducimus a optio iure odit, neque delectus, ullam harum expedita inventore consectetur facilis sapiente esse molestiae, provident temporibus magni vel beatae! Tenetur aut magni possimus explicabo, fugiat unde. Dolorem sed, et ipsum nostrum totam mollitia ex, earum consequatur minima labore qui facere veniam!</p>
		</div>
	</section>

	<?php include 'footer.php' ?>
	<script src="js/popper.min.js"></script>
	<script src="js/jquery-3.3.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
</body>
</html>