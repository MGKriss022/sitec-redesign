from django.db import models
import requests
from bs4 import BeautifulSoup
from enum import IntEnum

class NotConnectedException(Exception):
    def __init__(self, message='Not connected to API.'):
        self.message = message
        super().__init__(self.message)


class SitecApi:

    BASE_URL = 'https://sitec.tijuana.tecnm.mx/'
    PANEL_URL = BASE_URL + 'panel/'
    REINSCRIPTION_URL = BASE_URL + 'reinscripcion/'
    CYCLE_ADVANCE_URL = BASE_URL + 'avance-ciclo/'
    KARDEX_URL = BASE_URL + 'kardex/'
    LOG_URL = BASE_URL + 'log/'
    LOGIN_URL = BASE_URL + 'wp-content/themes/fuente/base/validacion.php'

    is_connected = False
    headers = { 'User-Agent': 'Mozilla/5.0'}

    def __init__(self, session=None):
        self.session = session
        if not session:
            self.session = requests.Session()
            self.is_connected = True
        
    def login(self, **kwargs):
        response = self.session.post(self.LOGIN_URL, data={
            'numero_control': kwargs.pop('username'),
            'clave': kwargs.pop('password'),
            'g-recaptcha-response': kwargs.pop('captcha')
        })
        if response.status_code == 200:
            self.is_connected = True
        return response

    def retrieve_captcha(self):
        response = self.session.get(self.LOGIN_URL)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            
            captcha = None
            return captcha
        return None
            

    def retrieve_panel_data(self):
        if not self.is_connected:
            raise NotConnectedException()

        html = self.session.get(self.PANEL_URL).text
        soup = BeautifulSoup(html, 'html.parser')
        personal_information_html = soup.find_all('div', class_='student-school-info-escolar')[0]
        personal_information = {}
        for div in personal_information_html.find_all('div'):
            name = div.get('class')[0]
            title = div.find('strong').text
            value = div.find('span').text
            personal_information[name] = {
                'title': title,
                'value': value
            }
        return personal_information

    def retrieve_reinscription_data(self):
        return None

    def retrieve_cycle_advance_data(self):
        html = '''
<body class="page-template-default page page-id-395 custom-background sie" cz-shortcut-listen="true">
   
<header id="site_header" class="site_header">
	 
	<div class="container">
     	<div class="header">
       		<!--
            <div class="search_section">
                                
                <form  class="search-form" id="search-form" method="get" action="https://sitec.tijuana.tecnm.mx" role="search">
                    <input type="text" name="s" placeholder="Buscar" title="Ingresa tu b�squeda"/>
                    <button type="submit">Buscar</button>
                </form>
            </div>
            -->
            <div class="encabezado">
				<div class="logo-tnm">
                	<a href="javascript:void(null);"><img src="/wp-content/themes/fuente/images/LogoTNM.png"></a>
                </div>
                <div class="text-tnm">
                	<a href="javascript:void(null);"> <img src="/wp-content/themes/fuente/images/LogoTecNM_Horizontal.svg"></a>
                </div>
                <div class="logo">
                    <a href="https://sitec.tijuana.tecnm.mx"><img src="https://sitec.tectijuana.edu.mx/wp-content/plugins/website-logo/images/logo_ITT1.png" title="Instituto Tecnológico de Tijuana" alt="Instituto Tecnológico de Tijuana"></a>
                </div><!--logo-->
            </div>            
            <nav class="site_nav">
                <div class="nav_section">
                                <div id="mega-menu-wrap-header_navigation-2" class="mega-menu-wrap"><input type="checkbox" id="mega-menu-toggle-header_navigation-2" class="mega-menu-toggle">
                <label for="mega-menu-toggle-header_navigation-2"></label>
                <ul id="mega-menu-header_navigation-2" class="mega-menu mega-menu-horizontal mega-no-js" data-event="hover" data-effect="slide">
                                        <li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-313" id="mega-menu-item-313"><a href="https://sitec.tijuana.tecnm.mx/panel/">Mi Panel</a></li>
                                        <li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-311" id="mega-menu-item-311"><a href="https://sitec.tijuana.tecnm.mx/cambiar-clave/">Cambiar clave</a></li>
                    <li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-312" id="mega-menu-item-312"><a href="https://sitec.tijuana.tecnm.mx/email/">Cambiar email</a></li>
                    <li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-314" id="mega-menu-item-314"><a href="https://sitec.tijuana.tecnm.mx/reinscripcion/">Reinscripción</a></li>
                                        <li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-319" id="mega-menu-item-319"><a href="https://sitec.tijuana.tecnm.mx/avance-ciclo/">Avance Ciclo</a></li>
                                        <li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-319" id="mega-menu-item-319"><a href="https://sitec.tijuana.tecnm.mx/kardex/">Kardex</a></li>
                    <li class="mega-menu-item mega-menu-item-type-post_type mega-menu-item-object-page mega-align-bottom-left mega-menu-flyout mega-menu-item-312" id="mega-menu-item-312"><a href="https://sitec.tijuana.tecnm.mx/log/">Log</a></li>
                                        <li class="mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-align-bottom-left mega-menu-flyout mega-menu-item-315" id="mega-menu-item-315"><a href="https://sitec.tijuana.tecnm.mx/wp-content/themes/fuente/base/validacion.php?doLogout=true">Salir Sistema</a></li>
                </ul>
                </div>
                            </div><!--nav_section-->
            </nav><!-- #site-nav --> 
        </div><!--header-->
   </div> <!--wrapper-->
   	   
	<div id="barraAlertas" style="">
		
	</div>
	</header><!-- #site-header -->


        
<div class="con_bg all_con_bg">
	<div class="container">
		<div id="content"> 
             <div class="content_section bg1">
                <div class="col12 generic_page">
                  	
                  	<div class="animateblock top common animated">
<h1 class="title">Avance del Ciclo</h1>
<h2 class="student-name">VICTOR IVAN DIAZ DZIB <br> <span>(18212170 – FEB-JUL 21)</span></h2>
<p>A continuación se muestran las materias que fueron cargadas y las evaluaciones correspondientes por unidades para el presente ciclo. La columna REP indica si la materia fue cargada por reprobación o curso espacial. U01 indica la calificación para la unidad 1 de la materia y así sucesivamente. Opción es el tipo de evaluación de la unidad NP: No Presentó, ORD: Ordinario/Normal, REG: Regularización y EXT: Extraordinario. Prom Est es el promedio estimado en la materia para el alumno y solo el que se muestra en el Kardex es el definitivo. Si existe alguna duda sobre la presente información verifícalo con el maestro o el coordinador de carrera.</p>
					<table width="100%" border="0">
					  <tbody><tr style="background-color:#900; color:#FFF;">
						<td width="15%"><strong>Materia</strong></td>
						<td width="85%">ACA-0909SC7B – DRA MARIA DE LOS ANGELES QUEZADA CISNERO</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td>TALLER DE INVESTIGACION I</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td><table width="100%" border="0">
							<tbody><tr>
							  <td><p align="center">Lunes</p></td>
							  <td><p align="center">Martes</p></td>
							  <td><p align="center">Miercoles</p></td>
							  <td><p align="center">Jueves</p></td>
							  <td><p align="center">Viernes</p></td>
							  <td><p align="center">Sabado</p></td>
							  <td><p align="center">Domingo</p></td>
							</tr>
							<tr>
								<td><p align="center">14001500<br>
							  9302</p></td>
								<td><p align="center">14001500<br>
							  9302</p></td>
								<td><p align="center">14001500<br>
							  9302</p></td>
								<td><p align="center">14001500<br>
							  9302</p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
							</tr>
						</tbody></table></td>
					  </tr>
					</tbody></table>
										<table border="0" width="100%">
					  <tbody><tr>
						<td><p align="center">Rep</p></td>
					 						<td><p align="center">U01</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U02</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U03</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					                                                 <td><p align="center">Prom Est</p></td>
					 </tr>
					                                                     <tr>
                                                        <td><p align="center">—</p></td>                                                        <td><p align="center"><input id="P01" name="LISPA01" type="text" size="2" value="71" readonly=""></p></td>
                                                        <td><p align="center"><input id="F01" name="LISFA01" type="text" size="2" value="1" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P02" name="LISPA02" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F02" name="LISFA02" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P03" name="LISPA03" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F03" name="LISFA03" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="-ACA-0909" name="-ACA-0909" type="text" size="2" value="0" readonly=""></p></td>
                                                    </tr>
                                                										</tbody></table>
					<p>&nbsp;</p>
									<table width="100%" border="0">
					  <tbody><tr style="background-color:#900; color:#FFF;">
						<td width="15%"><strong>Materia</strong></td>
						<td width="85%">ACF-0905SC4A – ING. TONALLI CUAUHTEMOC GALICIA LOPEZ</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td>ECUACIONES DIFERENCIALES</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td><table width="100%" border="0">
							<tbody><tr>
							  <td><p align="center">Lunes</p></td>
							  <td><p align="center">Martes</p></td>
							  <td><p align="center">Miercoles</p></td>
							  <td><p align="center">Jueves</p></td>
							  <td><p align="center">Viernes</p></td>
							  <td><p align="center">Sabado</p></td>
							  <td><p align="center">Domingo</p></td>
							</tr>
							<tr>
								<td><p align="center">13001400<br>
							  9206</p></td>
								<td><p align="center">13001400<br>
							  9206</p></td>
								<td><p align="center">13001400<br>
							  9206</p></td>
								<td><p align="center">13001400<br>
							  9206</p></td>
								<td><p align="center">13001400<br>
							  9206</p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
							</tr>
						</tbody></table></td>
					  </tr>
					</tbody></table>
										<table border="0" width="100%">
					  <tbody><tr>
						<td><p align="center">Rep</p></td>
					 						<td><p align="center">U01</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U02</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U03</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U04</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U05</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					                                                 <td><p align="center">Prom Est</p></td>
					 </tr>
					                                                     <tr>
                                                        <td><p align="center">—</p></td>                                                        <td><p align="center"><input id="P01" name="LISPA01" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F01" name="LISFA01" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P02" name="LISPA02" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F02" name="LISFA02" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P03" name="LISPA03" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F03" name="LISFA03" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P04" name="LISPA04" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F04" name="LISFA04" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P05" name="LISPA05" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F05" name="LISFA05" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="-ACF-0905" name="-ACF-0905" type="text" size="2" value="0" readonly=""></p></td>
                                                    </tr>
                                                										</tbody></table>
					<p>&nbsp;</p>
									<table width="100%" border="0">
					  <tbody><tr style="background-color:#900; color:#FFF;">
						<td width="15%"><strong>Materia</strong></td>
						<td width="85%">SCA-1025SC5C – MC ADRIAN SILVA RAMIREZ</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td>TALLER DE BASES DE DATOS</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td><table width="100%" border="0">
							<tbody><tr>
							  <td><p align="center">Lunes</p></td>
							  <td><p align="center">Martes</p></td>
							  <td><p align="center">Miercoles</p></td>
							  <td><p align="center">Jueves</p></td>
							  <td><p align="center">Viernes</p></td>
							  <td><p align="center">Sabado</p></td>
							  <td><p align="center">Domingo</p></td>
							</tr>
							<tr>
								<td><p align="center">19002000<br>
							  91L8</p></td>
								<td><p align="center">19002000<br>
							  91L8</p></td>
								<td><p align="center">19002000<br>
							  91L8</p></td>
								<td><p align="center">19002000<br>
							  91L8</p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
							</tr>
						</tbody></table></td>
					  </tr>
					</tbody></table>
										<table border="0" width="100%">
					  <tbody><tr>
						<td><p align="center">Rep</p></td>
					 						<td><p align="center">U01</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U02</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U03</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U04</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U05</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U06</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					                                                 <td><p align="center">Prom Est</p></td>
					 </tr>
					                                                     <tr>
                                                        <td><p align="center">—</p></td>                                                        <td><p align="center"><input id="P01" name="LISPA01" type="text" size="2" value="75" readonly=""></p></td>
                                                        <td><p align="center"><input id="F01" name="LISFA01" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P02" name="LISPA02" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F02" name="LISFA02" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P03" name="LISPA03" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F03" name="LISFA03" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P04" name="LISPA04" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F04" name="LISFA04" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P05" name="LISPA05" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F05" name="LISFA05" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P06" name="LISPA06" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F06" name="LISFA06" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="-SCA-1025" name="-SCA-1025" type="text" size="2" value="0" readonly=""></p></td>
                                                    </tr>
                                                										</tbody></table>
					<p>&nbsp;</p>
									<table width="100%" border="0">
					  <tbody><tr style="background-color:#900; color:#FFF;">
						<td width="15%"><strong>Materia</strong></td>
						<td width="85%">SCC-1014SC6B – LIC. RODRIGO CA�EZ VALLE</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td>LENGUAJES DE INTERFAZ</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td><table width="100%" border="0">
							<tbody><tr>
							  <td><p align="center">Lunes</p></td>
							  <td><p align="center">Martes</p></td>
							  <td><p align="center">Miercoles</p></td>
							  <td><p align="center">Jueves</p></td>
							  <td><p align="center">Viernes</p></td>
							  <td><p align="center">Sabado</p></td>
							  <td><p align="center">Domingo</p></td>
							</tr>
							<tr>
								<td><p align="center">18001900<br>
							  0310</p></td>
								<td><p align="center">18001900<br>
							  0310</p></td>
								<td><p align="center">18001900<br>
							  0310</p></td>
								<td><p align="center">18001900<br>
							  0310</p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
							</tr>
						</tbody></table></td>
					  </tr>
					</tbody></table>
										<table border="0" width="100%">
					  <tbody><tr>
						<td><p align="center">Rep</p></td>
					 						<td><p align="center">U01</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U02</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U03</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U04</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					                                                 <td><p align="center">Prom Est</p></td>
					 </tr>
					                                                     <tr>
                                                        <td><p align="center">—</p></td>                                                        <td><p align="center"><input id="P01" name="LISPA01" type="text" size="2" value="85" readonly=""></p></td>
                                                        <td><p align="center"><input id="F01" name="LISFA01" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P02" name="LISPA02" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F02" name="LISFA02" type="text" size="2" value="8" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P03" name="LISPA03" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F03" name="LISFA03" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P04" name="LISPA04" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F04" name="LISFA04" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="-SCC-1014" name="-SCC-1014" type="text" size="2" value="0" readonly=""></p></td>
                                                    </tr>
                                                										</tbody></table>
					<p>&nbsp;</p>
									<table width="100%" border="0">
					  <tbody><tr style="background-color:#900; color:#FFF;">
						<td width="15%"><strong>Materia</strong></td>
						<td width="85%">SCC-1014SC6B – LIC. RODRIGO CA�EZ VALLE</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td>LENGUAJES DE INTERFAZ</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td><table width="100%" border="0">
							<tbody><tr>
							  <td><p align="center">Lunes</p></td>
							  <td><p align="center">Martes</p></td>
							  <td><p align="center">Miercoles</p></td>
							  <td><p align="center">Jueves</p></td>
							  <td><p align="center">Viernes</p></td>
							  <td><p align="center">Sabado</p></td>
							  <td><p align="center">Domingo</p></td>
							</tr>
							<tr>
								<td><p align="center">18001900<br>
							  0310</p></td>
								<td><p align="center">18001900<br>
							  0310</p></td>
								<td><p align="center">18001900<br>
							  0310</p></td>
								<td><p align="center">18001900<br>
							  0310</p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
							</tr>
						</tbody></table></td>
					  </tr>
					</tbody></table>
										<table border="0" width="100%">
					  <tbody><tr>
						<td><p align="center">Rep</p></td>
					 						<td><p align="center">U01</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U02</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U03</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U04</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					                                                 <td><p align="center">Prom Est</p></td>
					 </tr>
					                                                     <tr>
                                                        <td><p align="center">—</p></td>                                                        <td><p align="center"><input id="P01" name="LISPA01" type="text" size="2" value="85" readonly=""></p></td>
                                                        <td><p align="center"><input id="F01" name="LISFA01" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P02" name="LISPA02" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F02" name="LISFA02" type="text" size="2" value="8" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P03" name="LISPA03" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F03" name="LISFA03" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P04" name="LISPA04" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F04" name="LISFA04" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="-SCC-1014" name="-SCC-1014" type="text" size="2" value="0" readonly=""></p></td>
                                                    </tr>
                                                										</tbody></table>
					<p>&nbsp;</p>
									<table width="100%" border="0">
					  <tbody><tr style="background-color:#900; color:#FFF;">
						<td width="15%"><strong>Materia</strong></td>
						<td width="85%">SCD-1003SC5C – M.C. MARIA GUADALUPE RODRIGUEZ LOPEZ</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td>ARQUITECTURA DE COMPUTADORAS</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td><table width="100%" border="0">
							<tbody><tr>
							  <td><p align="center">Lunes</p></td>
							  <td><p align="center">Martes</p></td>
							  <td><p align="center">Miercoles</p></td>
							  <td><p align="center">Jueves</p></td>
							  <td><p align="center">Viernes</p></td>
							  <td><p align="center">Sabado</p></td>
							  <td><p align="center">Domingo</p></td>
							</tr>
							<tr>
								<td><p align="center">17001800<br>
							  91L8</p></td>
								<td><p align="center">17001800<br>
							  91L8</p></td>
								<td><p align="center">17001800<br>
							  91L8</p></td>
								<td><p align="center">17001800<br>
							  91L8</p></td>
								<td><p align="center">17001800<br>
							  91L8</p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
							</tr>
						</tbody></table></td>
					  </tr>
					</tbody></table>
										<table border="0" width="100%">
					  <tbody><tr>
						<td><p align="center">Rep</p></td>
					 						<td><p align="center">U01</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U02</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U03</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U04</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					                                                 <td><p align="center">Prom Est</p></td>
					 </tr>
					                                                     <tr>
                                                        <td><p align="center">—</p></td>                                                        <td><p align="center"><input id="P01" name="LISPA01" type="text" size="2" value="94" readonly=""></p></td>
                                                        <td><p align="center"><input id="F01" name="LISFA01" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P02" name="LISPA02" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F02" name="LISFA02" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P03" name="LISPA03" type="text" size="2" value="97" readonly=""></p></td>
                                                        <td><p align="center"><input id="F03" name="LISFA03" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P04" name="LISPA04" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F04" name="LISFA04" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="-SCD-1003" name="-SCD-1003" type="text" size="2" value="0" readonly=""></p></td>
                                                    </tr>
                                                										</tbody></table>
					<p>&nbsp;</p>
									<table width="100%" border="0">
					  <tbody><tr style="background-color:#900; color:#FFF;">
						<td width="15%"><strong>Materia</strong></td>
						<td width="85%">SCD-1011SC6C – MI MARIA FERNANDA MURILLO MU�OZ</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td>INGENIERIA DE SOFTWARE</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td><table width="100%" border="0">
							<tbody><tr>
							  <td><p align="center">Lunes</p></td>
							  <td><p align="center">Martes</p></td>
							  <td><p align="center">Miercoles</p></td>
							  <td><p align="center">Jueves</p></td>
							  <td><p align="center">Viernes</p></td>
							  <td><p align="center">Sabado</p></td>
							  <td><p align="center">Domingo</p></td>
							</tr>
							<tr>
								<td><p align="center">15001600<br>
							  9205</p></td>
								<td><p align="center">15001600<br>
							  9205</p></td>
								<td><p align="center">15001600<br>
							  9205</p></td>
								<td><p align="center">15001600<br>
							  9205</p></td>
								<td><p align="center">15001600<br>
							  9205</p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
							</tr>
						</tbody></table></td>
					  </tr>
					</tbody></table>
										<table border="0" width="100%">
					  <tbody><tr>
						<td><p align="center">Rep</p></td>
					 						<td><p align="center">U01</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U02</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U03</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U04</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					                                                 <td><p align="center">Prom Est</p></td>
					 </tr>
					                                                     <tr>
                                                        <td><p align="center">—</p></td>                                                        <td><p align="center"><input id="P01" name="LISPA01" type="text" size="2" value="89" readonly=""></p></td>
                                                        <td><p align="center"><input id="F01" name="LISFA01" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P02" name="LISPA02" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F02" name="LISFA02" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P03" name="LISPA03" type="text" size="2" value="100" readonly=""></p></td>
                                                        <td><p align="center"><input id="F03" name="LISFA03" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">Ord</p></td>
                                                                                                                <td><p align="center"><input id="P04" name="LISPA04" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F04" name="LISFA04" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="-SCD-1011" name="-SCD-1011" type="text" size="2" value="0" readonly=""></p></td>
                                                    </tr>
                                                										</tbody></table>
					<p>&nbsp;</p>
									<table width="100%" border="0">
					  <tbody><tr style="background-color:#900; color:#FFF;">
						<td width="15%"><strong>Materia</strong></td>
						<td width="85%">SCD-1015SC6B – ING. ERASMO ESTRADA PENA</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td>LENGUAJES Y AUTOMATAS I</td>
					  </tr>
					  <tr>
						<td>&nbsp;</td>
						<td><table width="100%" border="0">
							<tbody><tr>
							  <td><p align="center">Lunes</p></td>
							  <td><p align="center">Martes</p></td>
							  <td><p align="center">Miercoles</p></td>
							  <td><p align="center">Jueves</p></td>
							  <td><p align="center">Viernes</p></td>
							  <td><p align="center">Sabado</p></td>
							  <td><p align="center">Domingo</p></td>
							</tr>
							<tr>
								<td><p align="center">16001700<br>
							  0310</p></td>
								<td><p align="center">16001700<br>
							  0310</p></td>
								<td><p align="center">16001700<br>
							  0310</p></td>
								<td><p align="center">16001700<br>
							  0310</p></td>
								<td><p align="center">16001700<br>
							  0310</p></td>
								<td><p align="center"><br>
							  </p></td>
								<td><p align="center"><br>
							  </p></td>
							</tr>
						</tbody></table></td>
					  </tr>
					</tbody></table>
										<table border="0" width="100%">
					  <tbody><tr>
						<td><p align="center">Rep</p></td>
					 						<td><p align="center">U01</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U02</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U03</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U04</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U05</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					 						<td><p align="center">U06</p></td>
						<td><p align="center">Faltas</p></td>
						<td><p align="center">Opción</p></td>
					                                                 <td><p align="center">Prom Est</p></td>
					 </tr>
					                                                     <tr>
                                                        <td><p align="center">—</p></td>                                                        <td><p align="center"><input id="P01" name="LISPA01" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F01" name="LISFA01" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P02" name="LISPA02" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F02" name="LISFA02" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P03" name="LISPA03" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F03" name="LISFA03" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P04" name="LISPA04" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F04" name="LISFA04" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P05" name="LISPA05" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F05" name="LISFA05" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="P06" name="LISPA06" type="text" size="2" value="0" readonly=""></p></td>
                                                        <td><p align="center"><input id="F06" name="LISFA06" type="text" size="2" value="0" readonly=""></p></td>                                                        <td><p align="center">NP</p></td>
                                                                                                                <td><p align="center"><input id="-SCD-1015" name="-SCD-1015" type="text" size="2" value="0" readonly=""></p></td>
                                                    </tr>
                                                										</tbody></table>
					<p>&nbsp;</p>
				<!-- AQUI ESTA EL ALERT -->
<div id="dialog-message" title="SITEC - Informa" style="display:none !important;">
  <p>
      <span class="ui-icon ui-icon-circle-check" style="float: left; margin: 0 7px 50px 0;"></span>
      <span id="msg"></span>
  </p>              
</div>	
<!-- AQUI TERMINA EL ALERT -->
<script type="text/javascript">
$(document).ready(function() {
	});
</script></div>
				                  </div><!--col12-->
            </div><!--row home_content--> 
		</div> <!--content-->      
	</div><!-- #wrapper -->
</div><!--con_bg-->
<div class="clear"></div>
<div class="container">
<footer id="site-footer">	
        <div class="bottom">
            <div id="text-27" class="widget_text">			<div class="textwidget"><p>Instituto Tecnológico de Tijuana<br>
Calzada Del Tecnológico S/N, Fraccionamiento Tomas Aquino. Tijuana, Baja California. C.P. 22414 Teléfono: +52 (664) 607 8400<br>
Tecnológico Nacional de México – Algunos derechos reservados © 2014-2018<br>
<a href="/politica-de-privacidad/">Política de Privacidad</a></p>
<p>SITEC v5.7</p>
</div>
		</div>			<center>2021-06-09 14:32:05</center>        </div>
    </footer></div><!-- #wrapper -->

<!-- #site-footer -->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-58411122-1', 'auto');
  ga('send', 'pageview');

</script>

</body>
        '''
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find_all('table')
        print(len(tables))

    def retrieve_kardex_data(self):
        html = self.session.get(self.KARDEX_URL).text
        soup = BeautifulSoup(html, 'html.parser')
        subject_rows = soup.find('table', {'id': 'alumno'}).find('tbody').find_all('tr')
        data = {
            'subjects': {}
        }
        for subject_row in subject_rows:
            for subject_column in subject_row.find_all('td'):
                id = subject_column.get('id')
                #Get rid of all strongs to get the a    ctual data without the "title"
                for strong in subject_column.find_all('strong'):
                    strong.decompose()
                if id is not None:
                    status = subject_column.get('class')[0]
                    subject_data = {}
                    subject_data['status'] = status
                    subject_data['slug'] = subject_column.select('.matcve')[0].string
                    subject_data['name'] = subject_column.select('.matnom')[0].string
                    subject_data['credits'] = subject_column.select('.matcre')[0].string
                    if status == 'aprobada':
                        subject_data['score'] = subject_column.select('.karcal')[0].string
                        subject_data['tc'] = subject_column.select('.tcacve')[0].string
                        subject_data['period'] = subject_column.select('.pdocve')[0].string
                        subject_data['taken_on'] = subject_column.select('.karnpe')[0].string
                    data['subjects'][id] = subject_data
        return data
                    
        

    def retrieve_log_data(self):
        return None

    def retrieve_all_data(self):
        return {
            'panel_data': self.retrieve_panel_data(),
            'reinscription_data': self.retrieve_reinscription_data(),
            'cycle_advance_data': self.retrieve_cycle_advance_data(),
            'kardex_data': self.retrieve_kardex_data(),
            'log_data': self.retrieve_log_data()
        }
