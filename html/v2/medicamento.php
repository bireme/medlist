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
				<li class="breadcrumb-item"><a href="index.php">WHO Model List of Essential Medicines</a></li>				
				<li class="breadcrumb-item active" aria-current="page">Tiopental Sódico</li>
			</ol>
		</nav>

		<h1 class="titulo1"><span class="colorText">Tiopental</span>  Sódico</h1>
		<!-- <div class="table-responsive">
			<table class="table table-bordered">
				<tr valign="top" style="font-size: 12px;">
					<td><span class="badge badge-primary">YES</span></td>
					<td><a href="lista.php">WHO Model List of Essential Medicines</a></td>
					<td><span class="badge badge-danger">NO</span></td>
					<td> <a href="lista.php">PAHO Strategic Fund Medicine List</a></td>
					<td><span class="badge badge-primary">YES</span></td>
					<td><a href="lista.php">WHO Model List of Essential Medicines</a></td>
					<td><span class="badge badge-danger">NO</span></td>
					<td> <a href="lista.php">PAHO Strategic Fund Medicine List</a></td>
				</tr>
			</table>
			<div class="text-center setaTab">
				<i class="fas fa-arrows-alt-h"></i>
			</div>
		</div>	 -->

		<ul class="nav nav-tabs" id="myTab" role="tablist">
			<li class="nav-item">
				<a class="nav-link active" id="home-tab" data-toggle="tab" href="#lista1" role="tab" aria-controls="home" aria-selected="true">WHO Model List of Essential Medicines</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" id="profile-tab" data-toggle="tab" href="#lista2" role="tab" aria-controls="profile" aria-selected="false">PAHO Strategic Fund Medicine List</a>
			</li>
			<li class="nav-item">
				<a class="nav-link disabled" id="home-tab" data-toggle="tab" href="#lista1" role="tab" aria-controls="home" aria-selected="true">WHO Model List of Essential Medicines</a>
			</li>
			<li class="nav-item">
				<a class="nav-link disabled" id="profile-tab" data-toggle="tab" href="#lista2" role="tab" aria-controls="profile" aria-selected="false">PAHO Strategic Fund Medicine List</a>
			</li>
		</ul>
		<div class="tab-content" id="myTabContent">
			<div class="tab-pane fade show active" id="lista1" role="tabpanel" aria-labelledby="home-tab">
				<div class="row">
					<div class="col-md-4">
						<h4><b>Observações:</b></h4>
						<b><u>WHO Model List of Essential Medicines</u></b><br>
						<i>12.1. Oxytocics</i><br>
						<ul>
							<li>Outras observações: Thiopental may be used as an alternative depending on local availability and cost.</li>
						</ul>
					</div>
					<div class="col-md-8">

						<h4><b><span class="colorText">Formas</span>  Farmacêuticas</b></h4>
						<div class="row">
							<div class="col-12 col-md-4 medPills">
								<div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist">
									<a class="nav-link active" data-toggle="pill" href="#med1" role="tab" aria-controls="v-pills-messages" aria-selected="ture">Powder for injection Lorem ipsum dolor sit amet.</a>
									<a class="nav-link" data-toggle="pill" href="#med2" role="tab" aria-controls="v-pills-messages" aria-selected="false">Oral liquid</a>
									<a class="nav-link" data-toggle="pill" href="#med3" role="tab" aria-controls="v-pills-messages" aria-selected="false">Tablet (chewable)</a>
									<a class="nav-link" data-toggle="pill" href="#med4" role="tab" aria-controls="v-pills-messages" aria-selected="false">Tablet (scored)</a>
									<a class="nav-link" data-toggle="pill" href="#med5" role="tab" aria-controls="v-pills-messages" aria-selected="false">Comprimido</a>
								</div>
							</div>
							<div class="col-12 col-md-8">
								<div class="tab-content substancia2" id="v-pills-tabContent">
									<div class="tab-pane fade show active" id="med1" role="tabpanel" aria-labelledby="v-pills-home-tab">
										<b>Composição:</b> <br> 2% (hydrochloride) + epinephrine 1:50 000
										<hr>
										<b>ATC:</b> N/A
									</div>
									<div class="tab-pane fade" id="med2" role="tabpanel" aria-labelledby="v-pills-profile-tab">
										<b>Composição:</b> <br> 125 mg amoxicillin + 31.25 mg clavulanic acid/5 ml
										<hr>
										<b>ATC:</b> N/A
									</div>
									<div class="tab-pane fade" id="med3" role="tabpanel" aria-labelledby="v-pills-messages-tab">
										<b>Composição:</b> <br> 250 mg amoxicillin + 62.5 mg clavulanic acid/5 ml
										<hr>
										<b>ATC:</b> N/A
									</div>
									<div class="tab-pane fade" id="med4" role="tabpanel" aria-labelledby="v-pills-messages-tab">
										<b>Composição:</b> <br> 2% (hydrochloride) + epinephrine 1:50 000
										<hr>
										<b>ATC:</b> N/A
									</div>
									<div class="tab-pane fade" id="med5" role="tabpanel" aria-labelledby="v-pills-messages-tab">
										<b>Composição:</b> <br> 500 mg (as trihydrate) + 125 mg (as potassium salt)
										<hr>
										<b>ATC:</b> N/A
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="tab-pane fade" id="lista2" role="tabpanel" aria-labelledby="profile-tab">
				<h4><b>Observações:</b></h4>
				<b><u>PAHO Strategic Fund Medicine List</u></b><br>
				<i>6.2. Antianginal medicines</i><br>
				<ul>
					<li>Outras observações: Limited supply options (normally, none or only one supplier identified / prequalified); may result in longer delivery times.</li>
				</ul>
				<i>12.1 Antianginosos</i><br>
				<ul>
					<li>Outras observações: Limited supply options (normally, none or only one supplier identified / prequalified); may result in longer delivery times.</li>
				</ul>
				<hr>
				<h4><b><span class="colorText">Formas</span>  Farmacêuticas</b></h4>
				<div class="row">
					<div class="col-12 col-md-3 medPills">
						<div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist">
							<a class="nav-link active" data-toggle="pill" href="#med1b" role="tab" aria-controls="v-pills-messages" aria-selected="ture">Powder for injection</a>
							<a class="nav-link" data-toggle="pill" href="#med2b" role="tab" aria-controls="v-pills-messages" aria-selected="false">Oral liquid</a>
							<a class="nav-link" data-toggle="pill" href="#med3b" role="tab" aria-controls="v-pills-messages" aria-selected="false">Tablet (chewable)</a>
							<a class="nav-link" data-toggle="pill" href="#med4b" role="tab" aria-controls="v-pills-messages" aria-selected="false">Tablet (scored)</a>
							<a class="nav-link" data-toggle="pill" href="#med5b" role="tab" aria-controls="v-pills-messages" aria-selected="false">Comprimido</a>
						</div>
					</div>
					<div class="col-12 col-md-9">
						<div class="tab-content" id="v-pills-tabContent">
							<div class="tab-pane fade show active" id="med1b" role="tabpanel" aria-labelledby="v-pills-home-tab">
								<h5><b>Powder for injection</b></h5>
								<b>Composição:</b> <br> 2% (hydrochloride) + epinephrine 1:50 000
								<hr>
								<b>ATC:</b> N/A
							</div>
							<div class="tab-pane fade" id="med2b" role="tabpanel" aria-labelledby="v-pills-profile-tab">
								<h5><b>Oral liquid</b></h5>
								<b>Composição:</b> <br> 125 mg amoxicillin + 31.25 mg clavulanic acid/5 ml
								<hr>
								<b>ATC:</b> N/A
							</div>
							<div class="tab-pane fade" id="med3b" role="tabpanel" aria-labelledby="v-pills-messages-tab">
								<h5><b>Tablet (chewable)</b></h5>
								<b>Composição:</b> <br> 250 mg amoxicillin + 62.5 mg clavulanic acid/5 ml
								<hr>
								<b>ATC:</b> N/A
							</div>
							<div class="tab-pane fade" id="med4b" role="tabpanel" aria-labelledby="v-pills-messages-tab">
								<h5><b>Tablet (scored)</b></h5>
								<b>Composição:</b> <br> 2% (hydrochloride) + epinephrine 1:50 000
								<hr>
								<b>ATC:</b> N/A
							</div>
							<div class="tab-pane fade" id="med5b" role="tabpanel" aria-labelledby="v-pills-messages-tab">
								<h5><b>Comprimido</b></h5>
								<b>Composição:</b> <br> 500 mg (as trihydrate) + 125 mg (as potassium salt)
								<hr>
								<b>ATC:</b> N/A
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
	<section class="sectionCinza2 padding1">
		<div class="container">
			<h1 class="titulo1"><span class="colorText">Recursos</span> de Informação: <small><b>Tiopental Sódico</b></small></h1>
			<ul class="nav nav-tabs" id="myTab" role="tablist">
				<li class="nav-item">
					<a class="nav-link active" id="home-tab" data-toggle="tab" href="#servico1" role="tab" aria-controls="home" aria-selected="true">Categorização</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" id="profile-tab" data-toggle="tab" href="#servico2" role="tab" aria-controls="profile" aria-selected="false">Informações de Avaliação</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" id="profile-tab" data-toggle="tab" href="#servico3" role="tab" aria-controls="profile" aria-selected="false">Legislação</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" id="home-tab" data-toggle="tab" href="#servico4" role="tab" aria-controls="home" aria-selected="true">Sumário de Evidências</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" id="profile-tab" data-toggle="tab" href="#servico5" role="tab" aria-controls="profile" aria-selected="false">Preço por país</a>
				</li>
				<!-- <li class="nav-item">
					<a class="nav-link" id="profile-tab" data-toggle="tab" href="#servico6" role="tab" aria-controls="profile" aria-selected="false">Fórmula Farmacológica</a>
				</li> -->
				<li class="nav-item">
					<a class="nav-link" id="profile-tab" data-toggle="tab" href="#servico7" role="tab" aria-controls="profile" aria-selected="false">Produção Cientifica</a>
				</li>
			</ul>
			<div class="tab-content font12 containerTab" id="myTabContent">
				<!---------------------------------------------------------------------- Serviço 1-->
				<div class="tab-pane fade show active conteudoPainel" id="servico1" role="tabpanel" aria-labelledby="home-tab">
					<div class="row">
						<div class="col-md-4">
							<h6>Brand Name</h6>
							<ul>
								<li><a href="">Absorbine</a></li>
								<li><a href="">Absorbine Jr</a></li>
								<li><a href="">Angidol</a></li>
								<li><a href="">Dorflex</a></li>
								<li><a href="">Absorbine</a></li>
								<li><a href="">Absorbine Jr</a></li>
								<li><a href="">Angidol</a></li>
								<li><a href="">Dorflex</a></li>
							</ul>							
						</div>
						<div class="col-md-4">
							<h6>Branded Drug Comonent</h6>
							<ul>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
							</ul>						
						</div>
						<div class="col-md-4">
							<h6>Branded Dose Form Group</h6>
							<ul>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
								<li><a href=""> Angidol (benzocaine 15 MG / menthol 2.6 MG) Oral Lozenge</a></li>
							</ul>						
						</div>
					</div>
				</div>
				<!---------------------------------------------------------------------- Serviço 2-->
				<div class="tab-pane fade" id="servico2" role="tabpanel" aria-labelledby="profile-tab">
					<a href=""><b>Cabazitaxel, abiraterona y enzalutamida en cáncer de próstata metastásico resistente a la castración con fracaso a docetaxel</b><br>
					INTRODUCCIÓN: El cáncer de próstata es la neoplasia maligna no cutánea más frecuente en varones. En estadíos tempranos el tratamiento es quirúrgico y radioterapéutico mientras que si la enfermedad está localmente avanzada o hay metástasis los pacientes son tratados con terapia anti-androgénica...</a>
					<hr>

					<a href=""><b>Tobramicina inhalatoria en polvo versus tobramicina inhalatoria en solución en fibrosis quística</b><br>
					INTRODUCCIÓN: La fibrosis quística (FQ) es una enfermedad genética autosómica recesiva causada por alteración del gen CFTR (del inglés Cystic Fibrosis Transmembrane Conductance Regulator), que afecta aproximadamente a 1 cada 2.000-3.000 nacidos en Europa y 1 cada 3.500 nacimientos en EE.UU. Esta al...</a>
					<hr>

					<a href=""><b>Pruebas de expresión genómica en pacientes con cáncer de mama: MammaPrint®, OncotypeDX® y Prosigna®</b><br>
					INTRODUCCIÓN: El cáncer de mama es la neoplasia más frecuente y principal causa de muerte por cáncer en mujeres. El 70% de los casos diagnostican en estadios tempranos. La decisión de administrar quimioterapia adyuvante se fundamenta en el riesgo estimado de recidiva. Su cálculo se basa en diversos...</a>
					<hr>

					<div class="float-right"><a href="" class="btn btn-sm btn-primary">Ver Mais</a></div><br>
				</div>
				<!---------------------------------------------------------------------- Serviço 3-->
				<div class="tab-pane fade" id="servico3" role="tabpanel" aria-labelledby="home-tab">
					<a href="">Português</a>  |  <a href="">English</a>  |  <a href="">Español</a>  |  <a href="">Français</a><br> <br>
					<p class="justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ratione quod explicabo totam, id, minus laboriosam eius deleniti reprehenderit officia placeat illo itaque aut corporis labore dolores ipsam ut inventore eveniet, repellat impedit commodi. Repudiandae laborum dolores nisi, autem quibusdam odit rerum, iure laboriosam quod vel ex doloribus a. Laboriosam, expedita..</p>
					<p class="justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat atque labore, delectus perspiciatis fuga distinctio ullam minus itaque provident, deserunt doloribus, amet adipisci voluptas id odio nulla esse voluptatum cumque impedit! Possimus recusandae adipisci beatae non id, culpa veniam laborum dolores eligendi vitae excepturi, dicta impedit hic pariatur atque repellat quasi! Nesciunt, facere voluptatem reiciendis. Aliquam porro amet dignissimos exercitationem quae repudiandae omnis provident ipsa, quos reiciendis, cum asperiores perspiciatis assumenda molestias totam vitae dolores suscipit quo corporis in nulla.</p>
					<p class="justify">Consequuntur quasi reiciendis quos aliquam saepe et ullam amet mollitia laboriosam quae excepturi nisi, dolorem soluta odit rem dolorum dolores tempore expedita porro aut, consectetur, laborum officiis fugit? Et, distinctio!</p>
					<p class="justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatem tempore aliquam mollitia et quas iste enim officia aspernatur delectus dolorum quisquam, id ipsa consectetur? Voluptate est numquam blanditiis ea modi fugiat culpa, nihil accusantium natus? Aspernatur nihil, alias, excepturi magnam veritatis eveniet rerum, eaque odit omnis quibusdam repellat fugiat minus explicabo sed itaque aliquid ullam natus voluptate modi dolore animi. Obcaecati omnis fugit nihil quam voluptatem dolores, non ipsum ad architecto labore, reiciendis, cumque officia, aliquid ut tempore beatae nulla.</p>
				</div>
				<!---------------------------------------------------------------------- Serviço 4-->
				<div class="tab-pane fade" id="servico4" role="tabpanel" aria-labelledby="profile-tab">
					<h4><b>Resumo</b></h4>
					<p class="text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos eius consequuntur molestiae sapiente eaque eveniet optio quam laboriosam et! Id soluta maxime quisquam eum dolores, blanditiis, reiciendis quia et doloribus, asperiores eos tempore dignissimos hic illo possimus assumenda dicta vel. Consequuntur provident pariatur, necessitatibus consequatur corporis minima! Quis excepturi soluta explicabo nihil facilis at dolorum blanditiis, obcaecati maiores eos mollitia accusamus ea sequi ipsum labore officia ab inventore eum harum quasi, totam, saepe provident. Inventore a incidunt dignissimos ducimus, ullam repudiandae maxime quibusdam quaerat laudantium ea velit, exercitationem et dolorum voluptatibus saepe corrupti vitae delectus iure labore dolores eveniet enim fugiat! Laboriosam praesentium, atque quae nisi dolore repudiandae illo eum, voluptatibus assumenda quia quam omnis tempora id. Excepturi alias sit officiis adipisci, animi odio qui esse suscipit voluptate eaque sunt ullam modi amet voluptatem vel possimus cupiditate necessitatibus exercitationem temporibus laborum saepe eligendi quidem quas dignissimos optio? Explicabo illum delectus repellat facilis cum consectetur autem quas ipsam rem nulla inventore adipisci voluptas, consequuntur incidunt ipsum libero nobis sapiente! Recusandae ad ratione saepe tempore unde ipsa quia commodi? Quia aperiam minus exercitationem blanditiis voluptatum tempora enim, debitis aut pariatur. Maiores, laborum accusantium soluta error est minima, sapiente amet eos similique voluptate odio ea, sed nesciunt assumenda tempore debitis. Ex molestiae quibusdam, quod, magni error neque praesentium! Ullam ea dolore maxime esse molestiae iste omnis fugit mollitia cum illum fuga tempora, commodi quam odio enim nesciunt distinctio, sequi iusto vero libero deleniti laudantium! Expedita voluptatibus officia deleniti earum accusantium dolores, reiciendis a omnis enim quibusdam voluptate, necessitatibus id ducimus blanditiis vel optio nisi? Distinctio, eum, ea. Harum eveniet aperiam esse, unde, ex laudantium eos, animi exercitationem perspiciatis omnis consectetur eius expedita, impedit vitae. Necessitatibus aperiam modi cumque doloremque, inventore odio sed possimus totam eius optio iure magnam amet tempore qui, expedita nobis.</p>

					<b>Autor Institucional: </b>World Health Organization <br>
					<b>Título Origninal: </b> Summary of the evidence br
					<b>Data da Publicação: </b> 04/2019 <br>
					<b>Link: </b> <a href="" target="_blank">https://www.who.int/</a>
				</div>
				<!---------------------------------------------------------------------- Serviço 5-->
				<div class="tab-pane fade" id="servico5" role="tabpanel" aria-labelledby="home-tab">
					<div class="table-responsive">
						<table class="table table-bordered tabPrincipal table-hover">
							<thead>
								<tr class="text-center">
									<th>País</th>
									<th>Última Atualização</th>
									<th>Lista de Produtos</th>
								</tr>
							</thead>
							<tbody>							
								<tr>
									<td>Brasil</td>
									<td class="text-center bg-light"><b>10/02/2019</b></td>
									<td class="text-center">
										<span class="fa-stack cursor" data-toggle="collapse" data-target="#brasil" style="vertical-align: top;">
											<i class="fas fa-circle fa-stack-2x"></i>
											<i class="fas fa-list fa-stack-1x fa-inverse"></i>
										</span>
									</td>
								</tr>
								<tr class="collapse" id="brasil">
									<td colspan="3">
										<table class="table table-bordered table-hover tabInterna" >
											<thead class="text-center">
												<tr>
													<th>Protudo</th>
													<th>Forma Farmacêutica</th>
													<th>Estimativa de Preço</th>
												</tr>
											</thead>
											<tbody>
												<tr>
													<td>Absorbine</td>
													<td>Tablet</td>
													<td class="text-right">2,50</td>
												</tr>
												<tr>
													<td>Absorbine Jr</td>
													<td>Inalação</td>
													<td class="text-right">430,49</td>
												</tr>
												<tr>
													<td>Absorbine</td>
													<td>Insetável</td>
													<td class="text-right">27,63</td>
												</tr>
												<tr>
													<td>Angidol</td>
													<td>Oral Liquido</td>
													<td class="text-right">0,64</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>



								<tr>
									<td>Chile</td>
									<td class="text-center bg-light"><b>01/07/2018</b></td>
									<td class="text-center">
										<span class="fa-stack cursor" data-toggle="collapse" data-target="#chile" style="vertical-align: top;">
											<i class="fas fa-circle fa-stack-2x"></i>
											<i class="fas fa-list fa-stack-1x fa-inverse"></i>
										</span>
									</td>
								</tr>
								<tr class="collapse" id="chile">
									<td colspan="3">
										<table class="table table-bordered table-hover tabInterna" >
											<thead class="text-center">
												<tr>
													<th>Protudo</th>
													<th>Forma Farmacêutica</th>
													<th>Estimativa de Preço</th>
												</tr>
											</thead>
											<tbody>
												<tr>
													<td>Absorbine</td>
													<td>Tablet</td>
													<td class="text-right">2,50</td>
												</tr>
												<tr>
													<td>Absorbine Jr</td>
													<td>Inalação</td>
													<td class="text-right">430,49</td>
												</tr>
												<tr>
													<td>Absorbine</td>
													<td>Insetável</td>
													<td class="text-right">27,63</td>
												</tr>
												<tr>
													<td>Angidol</td>
													<td>Oral Liquido</td>
													<td class="text-right">0,64</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>


								<tr >
									<td>Bolivia</td>
									<td class="text-center bg-light"><b>01/07/2016</b></td>
									<td class="text-center">
										<span class="fa-stack cursor" data-toggle="collapse" data-target="#bolivia" style="vertical-align: top;">
											<i class="fas fa-circle fa-stack-2x"></i>
											<i class="fas fa-list fa-stack-1x fa-inverse"></i>
										</span>
									</td>
								</tr>
								<tr class="collapse" id="bolivia">
									<td colspan="3">
										<table class="table table-bordered table-hover tabInterna" >
											<thead class="text-center">
												<tr>
													<th>Protudo</th>
													<th>Forma Farmacêutica</th>
													<th>Estimativa de Preço</th>
												</tr>
											</thead>
											<tbody>
												<tr>
													<td>Absorbine</td>
													<td>Tablet</td>
													<td class="text-right">2,50</td>
												</tr>
												<tr>
													<td>Absorbine Jr</td>
													<td>Inalação</td>
													<td class="text-right">430,49</td>
												</tr>
												<tr>
													<td>Absorbine</td>
													<td>Insetável</td>
													<td class="text-right">27,63</td>
												</tr>
												<tr>
													<td>Angidol</td>
													<td>Oral Liquido</td>
													<td class="text-right">0,64</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>

								

							</tbody>
						</table>
					</div>
				</div>
				<!---------------------------------------------------------------------- Serviço 6-->
				<div class="tab-pane fade" id="servico6" role="tabpanel" aria-labelledby="profile-tab">
					<a href="">Português</a>  |  <a href="">English</a>  |  <a href="">Español</a>  |  <a href="">Français</a><br> <br>
					<h4>Tiopental</h4>
					<p class="justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ratione quod explicabo totam, id, minus laboriosam eius deleniti reprehenderit officia placeat illo itaque aut corporis labore dolores ipsam ut inventore eveniet, repellat impedit commodi. Repudiandae laborum dolores nisi, autem quibusdam odit rerum, iure laboriosam quod vel ex doloribus a. Laboriosam, expedita..</p>
					<p class="justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat atque labore, delectus perspiciatis fuga distinctio ullam minus itaque provident, deserunt doloribus, amet adipisci voluptas id odio nulla esse voluptatum cumque impedit! Possimus recusandae adipisci beatae non id, culpa veniam laborum dolores eligendi vitae excepturi, dicta impedit hic pariatur atque repellat quasi! Nesciunt, facere voluptatem reiciendis. Aliquam porro amet dignissimos exercitationem quae repudiandae omnis provident ipsa, quos reiciendis, cum asperiores perspiciatis assumenda molestias totam vitae dolores suscipit quo corporis in nulla.</p>
					<p class="justify">Consequuntur quasi reiciendis quos aliquam saepe et ullam amet mollitia laboriosam quae excepturi nisi, dolorem soluta odit rem dolorum dolores tempore expedita porro aut, consectetur, laborum officiis fugit? Et, distinctio!</p>
					<p class="justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatem tempore aliquam mollitia et quas iste enim officia aspernatur delectus dolorum quisquam, id ipsa consectetur? Voluptate est numquam blanditiis ea modi fugiat culpa, nihil accusantium natus? Aspernatur nihil, alias, excepturi magnam veritatis eveniet rerum, eaque odit omnis quibusdam repellat fugiat minus explicabo sed itaque aliquid ullam natus voluptate modi dolore animi. Obcaecati omnis fugit nihil quam voluptatem dolores, non ipsum ad architecto labore, reiciendis, cumque officia, aliquid ut tempore beatae nulla.</p>
					<hr>

					<div class="float-right"><a href="" class="btn btn-sm btn-primary">Ver Mais</a></div><br>
				</div>
				<!---------------------------------------------------------------------- Serviço 7-->
				<div class="tab-pane fade" id="servico7" role="tabpanel" aria-labelledby="profile-tab">
					<table class="table table-hover tableSumario">
						<thead>
							<tr>
								<th>Descrição</th>
								<th width="150" class="text-center">Ação</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>
									<h6><b>Benzoyl peroxide for treating mild-moderate acne</b></h6>
									Contexto: Acne vulgaris. <br>
									Questão: Should children or adults with mild to moderate acne be treated with benzoyl peroxide compared to other topical preparations for acne? <br>
									Idioma: Inglês
								</td>
								<td class="text-center">
									<div class="btn-group">
										<a href="" class="btn btn-sm btn-success" title="PDF" ><i class="far fa-file-pdf iconeSumario"></i></a>
										<a href="" class="btn btn-sm btn-success" title="Download" ><i class="fas fa-download iconeSumario"></i></a>
										<a href="" class="btn btn-sm btn-success" title="Imprimir" ><i class="fas fa-print iconeSumario"></i></a>
									</div>
								</td>
							</tr>

							<tr>
								<td>
									<h6><b>Benzoyl peroxide for treating mild-moderate acne</b></h6>
									Contexto: Acne vulgaris. <br>
									Questão: Should children or adults with mild to moderate acne be treated with benzoyl peroxide compared to other topical preparations for acne? <br>
									Idioma: Inglês
								</td>
								<td class="text-center">
									<div class="btn-group">
										<a href="" class="btn btn-sm btn-success" title="PDF" ><i class="far fa-file-pdf iconeSumario"></i></a>
										<a href="" class="btn btn-sm btn-success" title="Download" ><i class="fas fa-download iconeSumario"></i></a>
										<a href="" class="btn btn-sm btn-success" title="Imprimir" ><i class="fas fa-print iconeSumario"></i></a>
									</div>
								</td>
							</tr>

							<tr>
								<td>
									<h6><b>Benzoyl peroxide for treating mild-moderate acne</b></h6>
									Contexto: Acne vulgaris. <br>
									Questão: Should children or adults with mild to moderate acne be treated with benzoyl peroxide compared to other topical preparations for acne? <br>
									Idioma: Inglês
								</td>
								<td class="text-center">
									<div class="btn-group">
										<a href="" class="btn btn-sm btn-success" title="PDF" ><i class="far fa-file-pdf iconeSumario"></i></a>
										<a href="" class="btn btn-sm btn-success" title="Download" ><i class="fas fa-download iconeSumario"></i></a>
										<a href="" class="btn btn-sm btn-success" title="Imprimir" ><i class="fas fa-print iconeSumario"></i></a>
									</div>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	</section>
	

	<?php include 'footer.php' ?>
	<script src="js/jquery-3.3.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
</body>
</html>