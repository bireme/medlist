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
		<div class="row">
			<div class="col-md-9">
				<ul class="listaN1">
					<!-- Nivel1 -->
					<li>
						<a data-toggle="collapse" data-target="#M1-1" href="">1 - Anaesthetics</a>
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
											<table class="table table-bordered table-sm table-hover table-striped font12">
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

					<!-- Nivel1 -->
					<li><a href="">2 - Analgesics, antipyretics, non-steroidal anti-inflammatory medicines (NSAIMs), medicines used to treat gout and disease modifying agents in rheumatoid disorders (DMARDs)</a></li>
					<li><a href="">3 - Antiallergics and medicines used in anaphylaxis</a></li>
					<li><a href="">4 - Antidotes and other substances used in poisonings</a></li>
					<li><a href="">5 - Anticonvulsants/antiepileptics</a></li>
					<li><a href="">6 - Anti-infective medicines</a></li>
					<li><a href="">7 - Antimigraine medicines</a></li>
					<li><a href="">8 - Antineoplastic, immunosuppressives and medicines used in Palliative care</a></li>
					<li><a href="">9 - Antiparkinsonism medicines</a></li>
					<li><a href="">10 - Medicines affecting the blood</a></li>
					<li><a href="">11 - Blood products and plasma substitutes</a></li>
					<li><a href="">12 - Cardiovascular medicines</a></li>
					<li><a href="">13 - Analgesics, antipyretics, non-steroidal anti-inflammatory medicines (NSAIMs), medicines used to treat gout and disease modifying agents in rheumatoid disorders (DMARDs)</a></li>
					<li><a href="">14 - Antiallergics and medicines used in anaphylaxis</a></li>
					<li><a href="">15 - Antidotes and other substances used in poisonings</a></li>
					<li><a href="">16 - Anticonvulsants/antiepileptics</a></li>
					<li><a href="">17 - Anti-infective medicines</a></li>
					<li><a href="">19 - Antimigraine medicines</a></li>
					<li><a href="">20 - Antiparkinsonism medicines</a></li>
					<li><a href="">21 - Medicines affecting the blood</a></li>
					<li><a href="">22 - Blood products and plasma substitutes</a></li>
					<li><a href="">23 - Cardiovascular medicines</a></li>
					<li><a href="">24 - Antineoplastic, immunosuppressives and medicines used in Palliative care</a></li>
				</ul>
			</div>
			<div class="col-md-3">
				<form action=""  style="background: #eee; padding: 10px; border-radius: 5px; position: sticky; top: 20px;">
					<h4>Pesquisar</h4>
					<hr>
					<div class="form-group">
						<select name="" id="" class="form-control">
							<option value="">Medicamento</option>
							<option value="">Forma Farmacêutica</option>							
						</select>
					</div>
					<div class="form-group">
						<input type="text" class="form-control" placeholder="Digite sua busca" required="required">
					</div>
					<div class="form-group">
						<input type="submit" value="Pesquisar" class="btn btn-block btn-primary">
					</div>
				</form>
			</div>
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