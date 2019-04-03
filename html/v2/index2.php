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
	<!-- slick -->
	<link rel="stylesheet" type="text/css" href="css/slick-theme.css"/>
	<link rel="stylesheet" type="text/css" href="css/slick.css"/>

</head>
<body>
	<?php include 'header.php' ?>
	<section class="container" id="banner">
		<img src="img/banner2.jpg" class="img-fluid" alt="">	
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
					<div class="col-md-6">
						<div class="homeBox">
							<img src="img/lista1.png" alt="">
							<a href="lista.php" class="btn btn-sm btn-primary btn-block">WHO Model List of Essential Medicines 1</a>
							<a href="lista.php" class="btn btn-sm btn-primary btn-block">WHO Model List of Essential Medicines 2</a>
							<a href="lista.php" class="btn btn-sm btn-primary btn-block">WHO List of Essential Medicines Devices</a>
							
						</div>
					</div>
					<!-- lista 2 -->
					<div class="col-md-6">
						<div class="homeBox">
							<img src="img/lista2.png" alt="">
							<h6><b></b></h6>
							<a href="lista.php" class="btn btn-sm btn-primary btn-block">PAHO Strategic Fund Medicine List 1</a>
							<a href="lista.php" class="btn btn-sm btn-primary btn-block">PAHO Strategic Fund Medicine List 2</a>
							<a href="lista.php" class="btn btn-sm btn-primary btn-block">PAHO List of Essential Medicines Devices</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>


	<section class="sectionCinza padding1">
		<div class="container">
			<h3 class="titulo1"><span class="colorText">Sumários </span> de evidência</h3>
			<hr>
			<div class="row">
				<div class="col-md-4">
					<img src="img/bula.jpg" alt="" class="img-fluid">
				</div>
				<div class="col-md-8">
					<p class="text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem sint optio aspernatur nihil temporibus accusamus quod consequatur illo eum non! Delectus, velit. Magnam perferendis, architecto. Aut ipsa non magni error.</p>
					<a href="sumario.php" class="btn btn-success">Ver Sumáiros</a>
				</div>
			</div>
		</div>
	</section>

<!-- <section class="padding1">
	<div class="container">
		<h3 class="titulo1"><span class="colorText">Recursos </span>de Informação</h3>

		<div class="miniBanner">
			<div style="padding: 10px;" class="text-center">
				<a href=""><img src="img/servico1.png" alt="" class="img-fluid"></a>
			</div>
			<div style="padding: 10px;" class="text-center">
				<a href=""><img src="img/servico1.png" alt="" class="img-fluid"></a>
			</div>
			<div style="padding: 10px;" class="text-center">
				<a href=""><img src="img/servico1.png" alt="" class="img-fluid"></a>
			</div>
			<div style="padding: 10px;" class="text-center">
				<a href=""><img src="img/servico1.png" alt="" class="img-fluid"></a>
			</div>
			<div style="padding: 10px;" class="text-center">
				<a href=""><img src="img/servico1.png" alt="" class="img-fluid"></a>
			</div>
			<div style="padding: 10px;" class="text-center">
				<a href=""><img src="img/servico1.png" alt="" class="img-fluid"></a>
			</div>
		</div>
	</div>
</section> -->

<?php include 'footer.php' ?>
<script src="js/popper.min.js"></script>
<script src="js/jquery-3.3.1.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/main.js"></script>
<!-- slick -->
<script type="text/javascript" src="js/slick.min.js"></script>
<script>
	$('.miniBanner').slick({
		autoplay: true,
		autoplaySpeed: 2000,
		dots: true,
		infinite: true,
		speed: 300,
		slidesToShow: 4,
		slidesToScroll: 2,
		responsive: [
		{
			breakpoint: 1024,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 3,
				infinite: true,
				dots: true
			}
		},
		{
			breakpoint: 600,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 2
			}
		}
		]
	});
</script>
</body>
</html>