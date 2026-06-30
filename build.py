#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for igornovaeslins.github.io
Trilingual (EN / PT / ES), 5 pages, Economist-style sidebar layout.
Run:  python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://igornovaeslins.github.io"
LANGS = ["en", "pt", "es"]
DEFAULT = "en"
PAGES = ["index", "research", "publications", "writing", "consulting"]
HREFLANG = {"en": "en", "pt": "pt-BR", "es": "es"}
HAS_PHOTO = True
OG_IMAGE = SITE + "/assets/portrait.jpg"
MAP_URL = "https://igornovaeslins.github.io/mobilidade-raca-sp/mapa.html"
NAME = "Igor Novaes Lins"

def base(lang): return "/" if lang == DEFAULT else "/%s/" % lang
def page_url(lang, page):
    b = base(lang)
    return b if page == "index" else "%s%s.html" % (b, page)
def abs_url(lang, page): return SITE + page_url(lang, page)

CONTACTS = [
    ("Email", "mailto:igornovaeslins@gmail.com"),
    ("Google Scholar", "https://scholar.google.com/citations?user=pD8sQZAAAAAJ&hl=en"),
    ("ORCID", "https://orcid.org/0000-0003-0510-8355"),
    ("Academia.edu", "https://unb.academia.edu/IgorNovaesLins"),
    ("LinkedIn", "https://www.linkedin.com/in/igornovaeslins"),
]

PUBS = [
    ("articles", [
        'Lins, I. N., &amp; Machado, C. A. M. (2024). The geography of militia voting in the city of Rio de Janeiro. <em>Teoria &amp; Pesquisa</em>, <span class="venue">33, 1&ndash;54.</span>',
        'Lins, I. N., &amp; Machado, C. A. M. (2023). Crime is political: theoretical elements for a neoinstitutionalist analysis of paramilitary groups in Rio de Janeiro. <em>Brazilian Journal of Political Science</em>.',
        'Lins, I. N. (2023). From the Baixada to the South Zone: paths of racial political violence in Rio de Janeiro. <em>Brazilian Public Security Review</em>, <span class="venue">17, 188&ndash;207.</span>',
        'Lins, I. N., &amp; Ferreira, J. V. B. (2022). Penal populism in parliamentary discourse: the debate on police violence in the Brazilian Chamber of Deputies (2019&ndash;2021). <em>Revista Eletr&ocirc;nica de Ci&ecirc;ncia Pol&iacute;tica</em>, <span class="venue">13.</span>',
        'Parnes, H. R., Lins, I. N., &amp; Trindade, P. S. (2020). Engagement, networks, and identity: a case study of the School Without Party movement. <em>Revista Eletr&ocirc;nica Intera&ccedil;&otilde;es Sociais</em>, <span class="venue">4, 79&ndash;92.</span>',
    ]),
    ("chapters", [
        'Giannini, R., Lins, I. N., Cerqueira, M., &amp; Leite, R. (2023). The merit system in Brazil and worldwide. In G. Lotta &amp; V. Campagnac (Eds.), <em>Rep&uacute;blica em Notas</em> (Vol. 1, pp. 331&ndash;354). Rio de Janeiro: Cobog&oacute;. <span class="venue">(Jabuti Prize semifinalist)</span>',
        'Giannini, R., Lins, I. N., Cerqueira, M., &amp; Leite, R. (2023). Recommendations to strengthen the public service merit system. In G. Lotta &amp; V. Campagnac (Eds.), <em>Rep&uacute;blica em Notas</em> (Vol. 1, pp. 355&ndash;365). Rio de Janeiro: Cobog&oacute;.',
    ]),
    ("reports", [
        'Lins, I. N. (2025). Women, peace and security: gender violence prevention policies in the Brazilian Armed Forces and Police. <span class="venue">RESDAL.</span>',
        'Giannini, R. A., Lins, I. N., &amp; Aguirre, K. (2024). Challenges and recommendations for the Amazon from women human rights and environmental defenders in Peru. <span class="venue">Igarap&eacute; Institute.</span> <a href="https://igarape.org.br/en/challenges-and-recommendations-for-the-amazon-peru/" rel="noopener" target="_blank">igarape.org.br</a>',
    ]),
    ("papers", [
        'Lins, I. N. (2026). Voting under criminal governance: electoral mobilization by criminal organizations. <em>SSRN</em>. <span class="tag">under review</span><br><a href="https://ssrn.com/abstract=6672040" rel="noopener" target="_blank">ssrn.com/abstract=6672040</a>',
        'Lins, I. N. (2026). Who can compete under criminal governments? Political selection in local elections. <em>SSRN</em>.<br><a href="https://ssrn.com/abstract=6849338" rel="noopener" target="_blank">ssrn.com/abstract=6849338</a>',
        'Lins, I. N. (2026). Criminal order and gendered violence: gang control, state repression, and violence against women in Chicago. <em>SSRN</em>.<br><a href="https://ssrn.com/abstract=6873281" rel="noopener" target="_blank">ssrn.com/abstract=6873281</a>',
        'Lins, I. N. (2026). Criminal governance and electoral capture in Rio de Janeiro: a spatial typology of the vote (2008&ndash;2024). <span class="venue">Working paper.</span>',
        'Lins, I. N. (2026). When police governance redraws the territorial borders of criminal governance. <span class="venue">Working paper.</span>',
        'Lins, I. N., &amp; Albarrac&iacute;n, J. (2026). When it overflows: the national turn of criminalised politics in Brazilian democracy. <span class="venue">Working paper.</span>',
        'Lins, I. N., &amp; Maia, B. (2026). Who can commit violence? Criminal governance and the reorganization of gender violence (Rio, Bel&eacute;m, Chicago). <span class="venue">Working paper.</span>',
    ]),
]

OPEDS = [
    'Lins, I. N. (2026). Redu&ccedil;&atilde;o da maioridade penal vai criar novo ex&eacute;rcito do PCC. <em>CartaCapital</em>. <a href="https://www.cartacapital.com.br/artigo/reducao-da-maioridade-penal-vai-criar-novo-exercito-do-pcc/" rel="noopener" target="_blank">cartacapital.com.br</a>',
    'Lins, I. N., &amp; Giannini, R. (2022). O medo n&atilde;o vencer&aacute; a democracia. <em>Correio Braziliense</em>.',
    'Lins, I. N. (2021). No Brasil, vidas negras n&atilde;o importam: discursos sobre a viol&ecirc;ncia policial na C&acirc;mara dos Deputados. <em>Boletim Lua Nova</em>.',
]

T = {
"en": {
  "nav": [("index","About"),("research","Research"),("publications","Publications"),("writing","Writing"),("consulting","Consulting")],
  "tagline": "Criminal governance and politics in Latin America",
  "kicker_index": "Political Scientist",
  "current": "PhD candidate, <strong>University of Bras&iacute;lia</strong> &middot; Visiting researcher, <strong>University of Illinois at Chicago</strong>",
  "footer": "&copy; 2026 Igor Novaes Lins",
  "skip_alt": "Igor Novaes Lins",
  "titles": {
     "index": "Igor Novaes Lins &mdash; Criminal governance &amp; politics in Latin America",
     "research": "Research &mdash; Igor Novaes Lins",
     "publications": "Publications &mdash; Igor Novaes Lins",
     "writing": "Writing &mdash; Igor Novaes Lins",
     "consulting": "Consulting &mdash; Igor Novaes Lins",
  },
  "desc": {
     "index": "Igor Novaes Lins studies criminal governance and politics in Latin America — how armed criminal groups reshape political life, with Rio de Janeiro as the main case.",
     "research": "Research on criminal governance and the vote, the state and crime, collapse and gendered violence, and racial political violence in Latin America.",
     "publications": "Articles, book chapters, reports, and working papers by Igor Novaes Lins on criminal governance, elections, and political violence.",
     "writing": "Op-eds and public writing by Igor Novaes Lins on crime, security, and democracy in Brazil.",
     "consulting": "Data, maps, and reproducible analysis for organizations working on cities, security, and inequality in Latin America.",
  },
  "page_h1": {"index":"About","research":"Research","publications":"Publications","writing":"Writing","consulting":"Research &amp; Consulting"},
  "about": [
     "Born in S&atilde;o Paulo, I am a political scientist, a doctoral candidate at the University of Bras&iacute;lia and a visiting researcher at the University of Illinois at Chicago. I study how organized crime and political violence shape political life in Latin American cities, especially in Brazil, combining quantitative and qualitative methods.",
     "My interests are criminal governance, electoral behavior, political violence, and subnational politics in Latin America, with attention to public security and racial inequality.",
     "My work has lived inside and outside the academy. I was a researcher at the Igarap&eacute; Institute, working on public security and civic space, and I authored a report on women environmental defenders in Peru, presented at COP28. I have also worked in the Brazilian federal government, where I led the Ministry of Racial Equality&rsquo;s strategy to pass the higher-education quota law, and I co-authored chapters in <em>Rep&uacute;blica em Notas</em>, a Jabuti Prize semifinalist, on the merit-based civil service.",
     "From 2026 I will be a postdoctoral researcher at CEBRAP, in S&atilde;o Paulo. I hold a Bachelor&rsquo;s and a Master&rsquo;s in political science from the University of Bras&iacute;lia, and I work in Portuguese, Spanish, and English.",
  ],
  "research_lead": "My research centers on criminal governance and politics. I ask how armed groups that rule territory, and set the rules of daily life there, reshape who votes, who can run, who wins, and who gets hurt. Rio de Janeiro is my main case, and georeferenced administrative microdata is my main material.",
  "threads": [
     ("Criminal governance and the vote", "Not all armed control is alike. Where politically integrated militias govern, turnout rises and registration moves with them. Where peripheral drug factions like the Comando Vermelho rule, participation falls. The spatial signature is diffuse dominance. Criminally linked candidates dominate locally while spreading thin across the map rather than forming a single stronghold."),
     ("The state redraws crime", "Who the state appoints to command a police battalion reorganizes the borders of criminal control. I use the timing of commander turnover to show how a formal policing decision expands militia frontiers and raises police lethality. I treat the state as part of the criminal order rather than its opposite."),
     ("Collapse and gendered violence", "When a criminal, police, or hybrid authority collapses, the violence that follows is what the prior order was containing. After leadership ruptures in Rio&rsquo;s Liga da Justi&ccedil;a, attempted femicide rises sharply, and the same logic appears in Chicago after the Laquan McDonald shooting. Crime also extends its authority into the domestic sphere, becoming a judge of private conflict at the cost of substituting for the state."),
     ("Race and political violence", "I map racially motivated violence against Black activists and political leaders in Rio, and how its grammar shifts from the Baixada Fluminense to the Zona Sul."),
  ],
  "groups": {"articles":"Peer-reviewed articles","chapters":"Book chapters","reports":"Technical reports","papers":"Working papers &amp; preprints"},
  "writing_lead": "I write for broader audiences on crime, security, and democracy.",
  "map_caption": "Where Black residents live in S&atilde;o Paulo, the bus runs slower. Bus speed by district, crossed with race and income. By Igor Novaes Lins.",
  "map_full": "Open full screen",
  "consulting": [
     "I bring research-grade data work to public-interest questions. I take a question about a city or a population, find or build the data to answer it, cross it with race, income, gender, and territory, and turn it into a map, an index, and a technical note that an organization can act on and audit.",
     "When the official record is thin, I collect the data myself. For S&atilde;o Paulo I built a real-time collector of the city&rsquo;s bus-position feed that has gathered tens of millions of GPS readings, runs unattended in the cloud, and alerts me when it falls. Crossing that collection with the racial composition of each district, I find that where most Black residents live the bus runs about 16% slower, and a Black resident reaches by public transport about 60% of the jobs a white resident reaches in the same hour.",
     "Every number I hand over comes from a script that ran and is registered, so the product is reproducible and auditable by the people who use it. I name what the data does not show, and I read race and territory as separate things rather than collapsing them into one label.",
     "I work with observatories, NGOs, think tanks, and public bodies that need this kind of evidence for advocacy and policy. Deliverables include interactive and static maps, spatial briefings and technical notes, open georeferenced datasets, dashboards, and composite indicators, built in R with a documented, reproducible pipeline.",
  ],
},
"pt": {
  "nav": [("index","Sobre"),("research","Pesquisa"),("publications","Publica&ccedil;&otilde;es"),("writing","Na m&iacute;dia"),("consulting","Consultoria")],
  "tagline": "Governan&ccedil;a criminal e pol&iacute;tica na Am&eacute;rica Latina",
  "kicker_index": "Cientista pol&iacute;tico",
  "current": "Doutorando, <strong>Universidade de Bras&iacute;lia</strong> &middot; Pesquisador visitante, <strong>University of Illinois at Chicago</strong>",
  "footer": "&copy; 2026 Igor Novaes Lins",
  "skip_alt": "Igor Novaes Lins",
  "titles": {
     "index": "Igor Novaes Lins &mdash; Governan&ccedil;a criminal e pol&iacute;tica",
     "research": "Pesquisa &mdash; Igor Novaes Lins",
     "publications": "Publica&ccedil;&otilde;es &mdash; Igor Novaes Lins",
     "writing": "Na m&iacute;dia &mdash; Igor Novaes Lins",
     "consulting": "Consultoria &mdash; Igor Novaes Lins",
  },
  "desc": {
     "index": "Igor Novaes Lins estuda governança criminal e política na América Latina — como grupos criminais armados reconfiguram a vida política, tendo o Rio de Janeiro como caso principal.",
     "research": "Pesquisa sobre governança criminal e o voto, o Estado e o crime, colapso e violência de gênero, e violência política racial na América Latina.",
     "publications": "Artigos, capítulos, relatórios e working papers de Igor Novaes Lins sobre governança criminal, eleições e violência política.",
     "writing": "Artigos de opinião e textos de Igor Novaes Lins sobre crime, segurança e democracia no Brasil.",
     "consulting": "Dados, mapas e análise reprodutível para organizações que trabalham com cidades, segurança e desigualdade na América Latina.",
  },
  "page_h1": {"index":"Sobre","research":"Pesquisa","publications":"Publica&ccedil;&otilde;es","writing":"Na m&iacute;dia","consulting":"Pesquisa e Consultoria"},
  "about": [
     "Natural de S&atilde;o Paulo, sou cientista pol&iacute;tico, doutorando na Universidade de Bras&iacute;lia e pesquisador visitante na Universidade de Illinois em Chicago. Estudo como o crime organizado e a viol&ecirc;ncia pol&iacute;tica moldam a vida pol&iacute;tica nas cidades latino-americanas, especialmente no Brasil, combinando m&eacute;todos quantitativos e qualitativos.",
     "Meus interesses s&atilde;o governan&ccedil;a criminal, comportamento eleitoral, viol&ecirc;ncia pol&iacute;tica e pol&iacute;tica subnacional na Am&eacute;rica Latina, com aten&ccedil;&atilde;o &agrave; seguran&ccedil;a p&uacute;blica e &agrave; desigualdade racial.",
     "Meu trabalho viveu dentro e fora da universidade. Fui pesquisador no Instituto Igarap&eacute;, atuando em seguran&ccedil;a p&uacute;blica e espa&ccedil;o c&iacute;vico, e assinei um relat&oacute;rio sobre mulheres defensoras do meio ambiente no Peru, apresentado na COP28. Tamb&eacute;m trabalhei no governo federal, onde liderei a estrat&eacute;gia do Minist&eacute;rio da Igualdade Racial para aprova&ccedil;&atilde;o da lei de cotas no ensino superior e coassinei cap&iacute;tulos no <em>Rep&uacute;blica em Notas</em>, semifinalista do Pr&ecirc;mio Jabuti, sobre o sistema de m&eacute;rito do servi&ccedil;o p&uacute;blico.",
     "A partir de 2026, integro o CEBRAP, em S&atilde;o Paulo, como pesquisador de p&oacute;s-doutorado. Sou bacharel e mestre em ci&ecirc;ncia pol&iacute;tica pela Universidade de Bras&iacute;lia, trabalho em portugu&ecirc;s, espanhol e ingl&ecirc;s.",
  ],
  "research_lead": "Minha pesquisa se concentra na governan&ccedil;a criminal e na pol&iacute;tica. Pergunto como grupos armados que governam o territ&oacute;rio, e ditam as regras da vida cotidiana ali, redefinem quem vota, quem pode se candidatar, quem vence e quem se machuca. O Rio de Janeiro &eacute; meu caso principal, e microdados administrativos georreferenciados s&atilde;o meu material principal.",
  "threads": [
     ("Governan&ccedil;a criminal e o voto", "Nem todo controle armado &eacute; igual. Onde mil&iacute;cias politicamente integradas governam, o comparecimento sobe e o registro se move com elas. Onde fac&ccedil;&otilde;es do tr&aacute;fico como o Comando Vermelho dominam, a participa&ccedil;&atilde;o cai. A assinatura espacial &eacute; a domin&acirc;ncia difusa. Candidatos ligados ao crime dominam localmente e se espalham fino pelo mapa, em vez de formar um &uacute;nico reduto."),
     ("O Estado redesenha o crime", "Quem o Estado nomeia para comandar um batalh&atilde;o reorganiza as fronteiras do controle criminal. Uso o timing da troca de comando para mostrar como uma decis&atilde;o formal de policiamento expande as fronteiras das mil&iacute;cias e eleva a letalidade policial. Trato o Estado como parte da ordem criminal, n&atilde;o como seu oposto."),
     ("Colapso e viol&ecirc;ncia de g&ecirc;nero", "Quando uma autoridade criminal, policial ou h&iacute;brida colapsa, a viol&ecirc;ncia que vem a seguir &eacute; a que a ordem anterior continha. Depois das rupturas de lideran&ccedil;a na Liga da Justi&ccedil;a, no Rio, a tentativa de feminic&iacute;dio sobe com for&ccedil;a, e a mesma l&oacute;gica aparece em Chicago ap&oacute;s o caso Laquan McDonald. O crime tamb&eacute;m estende sua autoridade &agrave; esfera dom&eacute;stica, virando juiz do conflito privado ao custo de substituir o Estado."),
     ("Ra&ccedil;a e viol&ecirc;ncia pol&iacute;tica", "Mapeio a viol&ecirc;ncia de motiva&ccedil;&atilde;o racial contra ativistas e lideran&ccedil;as pol&iacute;ticas negras no Rio, e como sua gram&aacute;tica muda da Baixada Fluminense &agrave; Zona Sul."),
  ],
  "groups": {"articles":"Artigos em peri&oacute;dico","chapters":"Cap&iacute;tulos de livro","reports":"Relat&oacute;rios t&eacute;cnicos","papers":"Working papers e preprints"},
  "writing_lead": "Escrevo para p&uacute;blicos amplos sobre crime, seguran&ccedil;a e democracia.",
  "map_caption": "Onde mora a popula&ccedil;&atilde;o negra em S&atilde;o Paulo, o &ocirc;nibus anda mais devagar. Velocidade do transporte por distrito, cruzada com ra&ccedil;a e renda. Elabora&ccedil;&atilde;o: Igor Novaes Lins.",
  "map_full": "Ver em tela cheia",
  "consulting": [
     "Levo trabalho de dados de n&iacute;vel acad&ecirc;mico a perguntas de interesse p&uacute;blico. Pego uma pergunta sobre uma cidade ou uma popula&ccedil;&atilde;o, encontro ou construo os dados para respond&ecirc;-la, cruzo com ra&ccedil;a, renda, g&ecirc;nero e territ&oacute;rio, e transformo isso em um mapa, um &iacute;ndice e uma nota t&eacute;cnica que uma organiza&ccedil;&atilde;o pode usar e auditar.",
     "Quando o registro oficial &eacute; raso, eu mesmo coleto o dado. Para S&atilde;o Paulo, constru&iacute; um coletor em tempo real da posi&ccedil;&atilde;o dos &ocirc;nibus da cidade que j&aacute; reuniu dezenas de milh&otilde;es de leituras de GPS, roda sozinho na nuvem e me avisa quando cai. Cruzando essa coleta com a composi&ccedil;&atilde;o racial de cada distrito, encontro que onde mora mais popula&ccedil;&atilde;o negra o &ocirc;nibus anda cerca de 16% mais devagar, e um morador negro alcan&ccedil;a de &ocirc;nibus cerca de 60% dos empregos que um morador branco alcan&ccedil;a na mesma hora.",
     "Todo n&uacute;mero que eu entrego vem de um script que rodou e est&aacute; registrado, ent&atilde;o o produto &eacute; reprodut&iacute;vel e audit&aacute;vel por quem o usa. Eu digo o que o dado n&atilde;o mostra, e leio ra&ccedil;a e territ&oacute;rio como coisas separadas, sem fundir as duas num r&oacute;tulo s&oacute;.",
     "Trabalho com observat&oacute;rios, ONGs, think tanks e &oacute;rg&atilde;os p&uacute;blicos que precisam desse tipo de evid&ecirc;ncia para incid&ecirc;ncia e pol&iacute;tica p&uacute;blica. As entregas incluem mapas interativos e est&aacute;ticos, notas t&eacute;cnicas e briefings espaciais, bases georreferenciadas abertas, dashboards e &iacute;ndices compostos, feitos em R com um pipeline documentado e reprodut&iacute;vel.",
  ],
},
"es": {
  "nav": [("index","Sobre m&iacute;"),("research","Investigaci&oacute;n"),("publications","Publicaciones"),("writing","Opini&oacute;n"),("consulting","Consultor&iacute;a")],
  "tagline": "Gobernanza criminal y pol&iacute;tica en Am&eacute;rica Latina",
  "kicker_index": "Cient&iacute;fico pol&iacute;tico",
  "current": "Doctorando, <strong>Universidad de Brasilia</strong> &middot; Investigador visitante, <strong>University of Illinois at Chicago</strong>",
  "footer": "&copy; 2026 Igor Novaes Lins",
  "skip_alt": "Igor Novaes Lins",
  "titles": {
     "index": "Igor Novaes Lins &mdash; Gobernanza criminal y pol&iacute;tica",
     "research": "Investigaci&oacute;n &mdash; Igor Novaes Lins",
     "publications": "Publicaciones &mdash; Igor Novaes Lins",
     "writing": "Opini&oacute;n &mdash; Igor Novaes Lins",
     "consulting": "Consultor&iacute;a &mdash; Igor Novaes Lins",
  },
  "desc": {
     "index": "Igor Novaes Lins estudia la gobernanza criminal y la política en América Latina — cómo los grupos criminales armados transforman la vida política, con Río de Janeiro como caso principal.",
     "research": "Investigación sobre gobernanza criminal y el voto, el Estado y el crimen, colapso y violencia de género, y violencia política racial en América Latina.",
     "publications": "Artículos, capítulos, informes y working papers de Igor Novaes Lins sobre gobernanza criminal, elecciones y violencia política.",
     "writing": "Artículos de opinión de Igor Novaes Lins sobre crimen, seguridad y democracia en Brasil.",
     "consulting": "Datos, mapas y análisis reproducible para organizaciones que trabajan con ciudades, seguridad y desigualdad en América Latina.",
  },
  "page_h1": {"index":"Sobre m&iacute;","research":"Investigaci&oacute;n","publications":"Publicaciones","writing":"Opini&oacute;n","consulting":"Investigaci&oacute;n y Consultor&iacute;a"},
  "about": [
     "Natural de S&atilde;o Paulo, soy cient&iacute;fico pol&iacute;tico, doctorando en la Universidad de Brasilia e investigador visitante en la Universidad de Illinois en Chicago. Estudio c&oacute;mo el crimen organizado y la violencia pol&iacute;tica moldean la vida pol&iacute;tica en las ciudades latinoamericanas, especialmente en Brasil, combinando m&eacute;todos cuantitativos y cualitativos.",
     "Mis intereses son la gobernanza criminal, el comportamiento electoral, la violencia pol&iacute;tica y la pol&iacute;tica subnacional en Am&eacute;rica Latina, con atenci&oacute;n a la seguridad p&uacute;blica y la desigualdad racial.",
     "Mi trabajo vivi&oacute; dentro y fuera de la universidad. Fui investigador en el Instituto Igarap&eacute;, trabajando en seguridad p&uacute;blica y espacio c&iacute;vico, y firm&eacute; un informe sobre mujeres defensoras del medio ambiente en Per&uacute;, presentado en la COP28. Tambi&eacute;n trabaj&eacute; en el gobierno federal, donde lider&eacute; la estrategia del Ministerio de Igualdad Racial para la aprobaci&oacute;n de la ley de cuotas en la educaci&oacute;n superior, y coescrib&iacute; cap&iacute;tulos en <em>Rep&uacute;blica em Notas</em>, semifinalista del Premio Jabuti, sobre el sistema de m&eacute;rito del servicio p&uacute;blico.",
     "Desde 2026 me incorporo al CEBRAP, en S&atilde;o Paulo, como investigador posdoctoral. Soy licenciado y mag&iacute;ster en ciencia pol&iacute;tica por la Universidad de Brasilia, y trabajo en portugu&eacute;s, espa&ntilde;ol e ingl&eacute;s.",
  ],
  "research_lead": "Mi investigaci&oacute;n se centra en la gobernanza criminal y la pol&iacute;tica. Pregunto c&oacute;mo los grupos armados que gobiernan el territorio, y dictan las reglas de la vida cotidiana all&iacute;, redefinen qui&eacute;n vota, qui&eacute;n puede postularse, qui&eacute;n gana y qui&eacute;n resulta herido. R&iacute;o de Janeiro es mi caso principal, y los microdatos administrativos georreferenciados son mi material principal.",
  "threads": [
     ("Gobernanza criminal y el voto", "No todo control armado es igual. Donde gobiernan milicias pol&iacute;ticamente integradas, la participaci&oacute;n sube y el registro se mueve con ellas. Donde dominan facciones del narcotr&aacute;fico como el Comando Vermelho, la participaci&oacute;n cae. La firma espacial es la dominancia difusa. Los candidatos ligados al crimen dominan localmente y se dispersan por el mapa, en vez de formar un &uacute;nico basti&oacute;n."),
     ("El Estado redibuja el crimen", "A qui&eacute;n nombra el Estado para comandar un batall&oacute;n reorganiza las fronteras del control criminal. Uso el momento del relevo de mando para mostrar c&oacute;mo una decisi&oacute;n formal de polic&iacute;a expande las fronteras de las milicias y eleva la letalidad policial. Trato al Estado como parte del orden criminal, no como su opuesto."),
     ("Colapso y violencia de g&eacute;nero", "Cuando una autoridad criminal, policial o h&iacute;brida colapsa, la violencia que sigue es la que el orden anterior conten&iacute;a. Tras las rupturas de liderazgo en la Liga da Justi&ccedil;a, en R&iacute;o, la tentativa de feminicidio sube con fuerza, y la misma l&oacute;gica aparece en Chicago tras el caso Laquan McDonald. El crimen tambi&eacute;n extiende su autoridad a la esfera dom&eacute;stica, volvi&eacute;ndose juez del conflicto privado al costo de sustituir al Estado."),
     ("Raza y violencia pol&iacute;tica", "Mapeo la violencia de motivaci&oacute;n racial contra activistas y liderazgos pol&iacute;ticos negros en R&iacute;o, y c&oacute;mo su gram&aacute;tica cambia de la Baixada Fluminense a la Zona Sur."),
  ],
  "groups": {"articles":"Art&iacute;culos en revistas","chapters":"Cap&iacute;tulos de libro","reports":"Informes t&eacute;cnicos","papers":"Working papers y preprints"},
  "writing_lead": "Escribo para p&uacute;blicos amplios sobre crimen, seguridad y democracia.",
  "map_caption": "Donde vive la poblaci&oacute;n negra en S&atilde;o Paulo, el autob&uacute;s anda m&aacute;s lento. Velocidad del transporte por distrito, cruzada con raza e ingreso. Elaboraci&oacute;n: Igor Novaes Lins.",
  "map_full": "Ver en pantalla completa",
  "consulting": [
     "Llevo trabajo de datos de nivel acad&eacute;mico a preguntas de inter&eacute;s p&uacute;blico. Tomo una pregunta sobre una ciudad o una poblaci&oacute;n, encuentro o construyo los datos para responderla, la cruzo con raza, ingreso, g&eacute;nero y territorio, y la convierto en un mapa, un &iacute;ndice y una nota t&eacute;cnica que una organizaci&oacute;n puede usar y auditar.",
     "Cuando el registro oficial es delgado, recojo el dato yo mismo. Para S&atilde;o Paulo constru&iacute; un colector en tiempo real de la posici&oacute;n de los autobuses de la ciudad que ya reuni&oacute; decenas de millones de lecturas de GPS, corre solo en la nube y me avisa cuando se cae. Cruzando esa recolecci&oacute;n con la composici&oacute;n racial de cada distrito, encuentro que donde vive m&aacute;s poblaci&oacute;n negra el autob&uacute;s anda cerca de 16% m&aacute;s lento, y un residente negro alcanza en transporte p&uacute;blico cerca del 60% de los empleos que un residente blanco alcanza en la misma hora.",
     "Cada n&uacute;mero que entrego viene de un script que corri&oacute; y est&aacute; registrado, as&iacute; que el producto es reproducible y auditable por quienes lo usan. Digo lo que el dato no muestra, y leo raza y territorio como cosas separadas, sin fundir ambas en una sola etiqueta.",
     "Trabajo con observatorios, ONG, think tanks y organismos p&uacute;blicos que necesitan este tipo de evidencia para incidencia y pol&iacute;tica p&uacute;blica. Las entregas incluyen mapas interactivos y est&aacute;ticos, notas t&eacute;cnicas y briefings espaciales, bases georreferenciadas abiertas, tableros e &iacute;ndices compuestos, hechos en R con un pipeline documentado y reproducible.",
  ],
},
}

def render_head(lang, page):
    t = T[lang]
    title = t["titles"][page]; desc = t["desc"][page]; canon = abs_url(lang, page)
    alts = "\n".join('<link rel="alternate" hreflang="%s" href="%s">' % (HREFLANG[l], abs_url(l, page)) for l in LANGS)
    alts += '\n<link rel="alternate" hreflang="x-default" href="%s">' % abs_url(DEFAULT, page)
    og_locale = {"en":"en_US","pt":"pt_BR","es":"es_ES"}[lang]
    return """<!DOCTYPE html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="author" content="Igor Novaes Lins">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="%s">
%s
<meta property="og:type" content="website">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s">
<meta property="og:locale" content="%s">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="%s">
<meta name="twitter:description" content="%s">
<meta name="twitter:image" content="%s">
<!-- ADD-GOOGLE-VERIFICATION-HERE: paste the tag Search Console gives you on the next line -->
<!-- <meta name="google-site-verification" content="PASTE_TOKEN_HERE"> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body>
""" % (lang, title, desc, canon, alts, t["titles"]["index"], desc, canon, OG_IMAGE, og_locale, t["titles"]["index"], desc, OG_IMAGE)

def render_sidebar(lang, page):
    t = T[lang]; home = page_url(lang, "index")
    if HAS_PHOTO:
        photo = '<a href="%s"><img class="portrait" src="/assets/portrait.jpg" alt="%s"></a>' % (home, t["skip_alt"])
    else:
        photo = '<a href="%s"><div class="monogram">IN</div></a>' % home
    navitems = "".join('<a href="%s"%s>%s</a>' % (page_url(lang,p), ' class="active"' if p==page else "", label) for p,label in t["nav"])
    langlinks = ['<a href="%s"%s>%s</a>' % (page_url(l,page), ' class="active"' if l==lang else "", l.upper()) for l in LANGS]
    langrow = "<span>&middot;</span>".join(langlinks)
    contacts = "".join('<a href="%s"%s>%s</a>' % (url, ("" if url.startswith("mailto:") else ' rel="me noopener" target="_blank"'), label) for label,url in CONTACTS)
    return """<aside class="sidebar">
  <div class="flag"></div>
  <div class="inner">
    %s
    <div class="brand">
      <a href="%s" class="namelink"><div class="name">Igor Novaes Lins</div></a>
      <p class="tagline">%s</p>
      <p class="current">%s</p>
    </div>
    <nav class="tabs">%s</nav>
    <div class="langs">%s</div>
    <div class="contact">%s</div>
  </div>
</aside>
""" % (photo, home, t["tagline"], t["current"], navitems, langrow, contacts)

def render_map(lang):
    t = T[lang]
    return """<figure class="mapwrap">
  <iframe class="map" src="%s" title="%s" loading="lazy" referrerpolicy="no-referrer"></iframe>
  <figcaption>%s <a href="%s" target="_blank" rel="noopener">%s &rarr;</a></figcaption>
</figure>
""" % (MAP_URL, t["skip_alt"], t["map_caption"], MAP_URL, t["map_full"])

def render_groups(lang):
    t = T[lang]; out = []
    for key, items in PUBS:
        lis = "".join("<li>%s</li>" % it for it in items)
        out.append('<div class="group"><h3>%s</h3><ol class="list">%s</ol></div>' % (t["groups"][key], lis))
    return "\n".join(out)

def render_main(lang, page):
    t = T[lang]; h1 = t["page_h1"][page]; inner = ""
    if page == "index":
        inner = "".join("<p>%s</p>" % p for p in t["about"])
    elif page == "research":
        inner = '<p class="lead">%s</p>' % t["research_lead"]
        for title, desc in t["threads"]:
            inner += '<div class="group"><h3>%s</h3><p>%s</p></div>' % (title, desc)
    elif page == "publications":
        inner = render_groups(lang)
    elif page == "writing":
        inner = '<p class="lead">%s</p>' % t["writing_lead"]
        inner += '<ol class="list">%s</ol>' % "".join("<li>%s</li>" % it for it in OPEDS)
    elif page == "consulting":
        paras = t["consulting"]
        inner = '<p class="lead">%s</p>' % paras[0]
        inner += "".join("<p>%s</p>" % p for p in paras[1:])
    jsonld = render_jsonld(lang) if page == "index" else ""
    kicker = '<p class="kicker">%s</p>\n  ' % t["kicker_index"] if page == "index" else ""
    return """<main>
  %s<h1>%s</h1>
  %s
  <footer>%s</footer>
</main>
%s
""" % (kicker, h1, inner, t["footer"], jsonld)

def render_jsonld(lang):
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Igor Novaes Lins",
  "givenName": "Igor",
  "familyName": "Novaes Lins",
  "url": "%s/",
  "identifier": "https://orcid.org/0000-0003-0510-8355",
  "email": "mailto:igornovaeslins@gmail.com",
  "jobTitle": "Political Scientist",
  "description": "Political scientist studying criminal governance and politics in Latin America.",
  "birthPlace": "Sao Paulo, Brazil",
  "alumniOf": {"@type": "CollegeOrUniversity", "name": "University of Brasilia"},
  "affiliation": [
    {"@type": "CollegeOrUniversity", "name": "University of Brasilia"},
    {"@type": "CollegeOrUniversity", "name": "University of Illinois at Chicago"},
    {"@type": "Organization", "name": "CEBRAP"}
  ],
  "knowsAbout": ["Criminal governance","Electoral behavior","Political violence","Organized crime","Public security","Spatial data analysis","Latin American politics","Brazilian politics"],
  "sameAs": [
    "https://scholar.google.com/citations?user=pD8sQZAAAAAJ&hl=en",
    "https://orcid.org/0000-0003-0510-8355",
    "https://unb.academia.edu/IgorNovaesLins",
    "https://www.linkedin.com/in/igornovaeslins"
  ]
}
</script>""" % SITE

def render_page(lang, page):
    return render_head(lang, page) + render_sidebar(lang, page) + render_main(lang, page) + "</body>\n</html>\n"

def write(path, content):
    full = os.path.join(ROOT, path); d = os.path.dirname(full)
    if d and not os.path.isdir(d): os.makedirs(d)
    with open(full, "w", encoding="utf-8") as f: f.write(content)
    return path

def main():
    written = []
    for lang in LANGS:
        sub = "" if lang == DEFAULT else lang + "/"
        for page in PAGES:
            fname = "index.html" if page == "index" else "%s.html" % page
            written.append(write(sub + fname, render_page(lang, page)))
    urls = []
    for lang in LANGS:
        for page in PAGES:
            urls.append("  <url><loc>%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>" % (abs_url(lang,page), "1.0" if page=="index" else "0.7"))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
    print("Wrote %d pages + sitemap + robots" % len(written))

if __name__ == "__main__":
    main()
