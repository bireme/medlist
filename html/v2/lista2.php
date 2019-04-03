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
				<li class="breadcrumb-item active" aria-current="page">WHO Model List of Essential Medicines</li>
			</ol>
		</nav>

		<h1 class="titulo1"><span class="colorText">WHO</span>  Model List of Essential Medicines</h1>
		<div>
			<ul>
				<!-- Nivel1 -->
				<li>
					<a data-toggle="collapse" data-target="#M1-1" href="">01 Anaesthetics</a>
					<!-- Nivel2 -->
					<ul id="M1-1" class="collapse" >
						<li>
							<a data-toggle="collapse" data-target="#M1-1-1" href="">1.1. General anaesthetics and oxygen</a>
							<!-- Nivel3 -->
							<ul id="M1-1-1" class="collapse">
								<li data-toggle="collapse" href="#1-1-1">
									<a data-toggle="collapse" data-target="#tableM1" href="">1.1.1 Inhalational medicines</a>	
									<!-- Tabela -->
									<div class="table-responsive collapse" id="tableM1">
										<table class="table table-bordered table-sm table-hover table-striped">
											<thead>
												<tr>
													<th>Medicamento</th>
													<th>Formas Farmacêuticas</th>
													<th class="text-center">Composição</th>
													<th class="text-center">Observações</th>
													<th class="text-center">Artigo</th>
												</tr>
											</thead>
											<tbody>
												<?php 
												for ($i=0; $i < 4; $i++) { 
													?>
													<tr>
														<td><a href="medicamento.php">oxygen</a></td>
														<td>Inhalation (medicine gas)</td>
														<td class="text-center">N/A</td>
														<td class="text-center"><a href="" data-toggle="modal" data-target="#modalObservacoes"><i class="fas fa-info-circle"></i></a></td>
														<td class="text-center"><a href="" data-toggle="modal" data-target="#modalArtigos"><i class="fas fa-newspaper"></i></a></td>
													</tr>
												<?php } ?>
											</tbody>
										</table>
									</div>
								</li>
								<li>
									<a href="">1.1.2 General anaesthetics and oxygen</a>
								</li>
								<li>
									<a href="">1.1.3 General anaesthetics and oxygen</a>
								</li>
							</ul>
						</li>
					</ul>
				</li>
			</ul>
		</div>
	</section>

	<!-- --------Modal Observações-------- -->
	<div id="modalObservacoes" class="modal bd-example-modal-xl fade" tabindex="-1" role="dialog">
		<div class="modal-dialog modal-dialog modal-xl modal-dialog-centered" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title">Observações</h5>
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body">
					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime eos, dolor recusandae officiis id, nam praesentium ipsam, vitae magni ab debitis similique dignissimos ut impedit est commodi nemo ipsa nulla. Mollitia impedit iure magnam quod maxime non fugiat iusto perferendis vitae excepturi, necessitatibus eius dignissimos accusamus ab quis atque distinctio laborum fuga odio quas sequi facilis ut minima. Minus ab id minima repudiandae, laboriosam accusamus dolores aliquid, eveniet consectetur quod nesciunt magnam adipisci eos dolorem placeat veniam saepe ex cupiditate alias explicabo accusantium quo aperiam! Aspernatur maiores consequuntur maxime ipsa, itaque laudantium perspiciatis, quam corrupti possimus eius, facilis, ex repudiandae sit suscipit fugiat beatae commodi voluptate. Quo qui inventore eveniet non molestias quae reprehenderit! Ducimus provident hic laudantium repudiandae pariatur distinctio adipisci omnis accusantium deleniti dolorum similique culpa facere, animi delectus tempora itaque vitae repellat ipsa, atque qui, ea fuga! Veniam minima animi incidunt et similique, molestias accusantium nesciunt aliquid!.</p>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-primary" data-dismiss="modal">Fechar</button>
				</div>
			</div>
		</div>
	</div>


	<!-- --------Modal Artigos-------- -->
	<div id="modalArtigos" class="modal bd-example-modal-xl fade" tabindex="-1" role="dialog">
		<div class="modal-dialog modal-dialog modal-xl modal-dialog-centered" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title">Artigos</h5>
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body">
					<ul>
						<li>
							<a href=""><b>Benzoyl peroxide for treating mild-moderate acne</b></a> <br>
							<small>Contexto: Acne vulgaris. <br>
							Questão: Should children or adults with mild to moderate acne be treated with benzoyl peroxide compared to other topical preparations for acne? <br>
							Idioma: Inglês</small>
						</li>
						<li>
							<a href=""><b>H2-antagonists versus proton pump inhibitors for gastro-esophageal reflux in adults</b></a> <br>
							<small>Contexto: Acne vulgaris. <br>
							Questão: Should children or adults with mild to moderate acne be treated with benzoyl peroxide compared to other topical preparations for acne? <br>
							Idioma: Inglês</small>
						</li>
						<li>
							<a href=""><b>Propofol for Neonates Undergoing Surgical Procedures</b></a><br>
							<small>Contexto: Acne vulgaris. <br>
							Questão: Should children or adults with mild to moderate acne be treated with benzoyl peroxide compared to other topical preparations for acne? <br>
							Idioma: Inglês</small>
						</li>
					</ul>

					<div class="text-center">
						<a href="sumario.php" class="btn btn-primary btn-sm">Visualizar outros artigos</a>
					</div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-primary" data-dismiss="modal">Fechar</button>
				</div>
			</div>
		</div>
	</div>


	<?php include 'footer.php' ?>
	<script src="js/jquery-3.3.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
</body>
</html>