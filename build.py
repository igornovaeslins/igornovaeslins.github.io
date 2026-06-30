#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for igornovaeslins.github.io
Trilingual (EN / PT / ES), 5 pages, shared sidebar layout.
Run:  python3 build.py
Outputs HTML into the repo root (and /pt, /es) plus sitemap.xml + robots.txt.
Edit the CONTENT dicts below and re-run to update the site.
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

NAME = "Igor Novaes Lins"

# ---------------------------------------------------------------- url helpers
def base(lang):
    return "/" if lang == DEFAULT else "/%s/" % lang

def page_url(lang, page):
    b = base(lang)
    return b if page == "index" else "%s%s.html" % (b, page)

def abs_url(lang, page):
    return SITE + page_url(lang, page)

# ---------------------------------------------------------------- shared data
CONTACTS = [
    ("Email", "mailto:igornovaeslins@gmail.com"),
    ("Google Scholar", "https://scholar.google.com/citations?user=pD8sQZAAAAAJ&hl=en"),
    ("ORCID", "https://orcid.org/0000-0003-0510-8355"),
    ("Academia.edu", "https://unb.academia.edu/IgorNovaesLins"),
    ("LinkedIn", "https://www.linkedin.com/in/igornovaeslins"),
]

# Publications — citations are language-independent; only group labels translate.
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
        'Lins, I. N. (2026). Voting under criminal governance: election mobilization by criminal organizations. <em>Research Square</em>. <span class="tag">under review</span><br><a href="https://doi.org/10.21203/rs.3.rs-9534248/v1" rel="noopener" target="_blank">doi.org/10.21203/rs.3.rs-9534248/v1</a>',
        'Lins, I. N. (2026). Who can compete under criminal governments? Political selection in local elections. <em>SSRN</em>.<br><a href="https://ssrn.com/abstract=6849338" rel="noopener" target="_blank">ssrn.com/abstract=6849338</a>',
        'Lins, I. N. (2026). Criminal order and gendered violence: gang control, state repression, and violence against women in Chicago. <em>SocArXiv</em>.<br><a href="https://doi.org/10.31235/osf.io/6yrka_v1" rel="noopener" target="_blank">doi.org/10.31235/osf.io/6yrka_v1</a>',
    ]),
]

OPEDS = [
    'Lins, I. N. (2026). Redu&ccedil;&atilde;o da maioridade penal vai criar novo ex&eacute;rcito do PCC. <em>CartaCapital</em>. <a href="https://www.cartacapital.com.br/artigo/reducao-da-maioridade-penal-vai-criar-novo-exercito-do-pcc/" rel="noopener" target="_blank">cartacapital.com.br</a>',
    'Lins, I. N., &amp; Giannini, R. (2022). O medo n&atilde;o vencer&aacute; a democracia. <em>Correio Braziliense</em>.',
    'Lins, I. N. (2021). No Brasil, vidas negras n&atilde;o importam: discursos sobre a viol&ecirc;ncia policial na C&acirc;mara dos Deputados. <em>Boletim Lua Nova</em>.',
]

# ---------------------------------------------------------------- translatable
T = {
"en": {
  "nav": [("index","About"),("research","Research"),("publications","Publications"),("writing","Writing"),("consulting","Consulting")],
  "tagline": "Criminal governance and politics in Latin America",
  "kicker_index": "Political Scientist",
  "current": "PhD candidate, <strong>University of Bras&iacute;lia</strong> &middot; Visiting scholar, <strong>University of Illinois at Chicago</strong>",
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
     "research": "Research on criminal governance and the vote, race and political violence, gender and state repression, and public security in Latin America.",
     "publications": "Articles, book chapters, reports, and working papers by Igor Novaes Lins on criminal governance, elections, and political violence.",
     "writing": "Op-eds and public writing by Igor Novaes Lins on crime, security, and democracy in Brazil.",
     "consulting": "Strategic political analysis and research consulting on security, organized crime, and elections in Latin America.",
  },
  "page_h1": {"index":"About","research":"Research","publications":"Publications","writing":"Writing","consulting":"Research &amp; Consulting"},
  "about": [
     "I am a political scientist working on criminal governance and politics &mdash; how armed criminal groups that rule territory, rather than seek to topple the state, reshape political life in Latin America. My main case is Rio de Janeiro, where my dissertation traces how criminal rule reaches the vote. The same question runs through the racial geography of political violence, gender and state repression under criminal order, and public-security policy. I work with spatial and quantitative methods and first-hand field knowledge of Brazilian cities.",
     "I am a doctoral candidate in Political Science at the University of Bras&iacute;lia and a visiting scholar at the University of Illinois at Chicago; from 2026 I will be a postdoctoral researcher at CEBRAP, in S&atilde;o Paulo. I am a researcher at RESDAL, affiliated with GEMAA (IESP-UERJ), and serve on the editorial board of the <em>Brazilian Journal of Political Science</em>. In 2024 I was selected for the British Academy Writing Academy. I hold Bachelor&rsquo;s and Master&rsquo;s degrees in Political Science from the University of Bras&iacute;lia, work in Portuguese, Spanish, and English, and was born in S&atilde;o Paulo.",
  ],
  "research_lead": "My research centers on <strong>criminal governance and politics</strong>: how armed groups that rule territory, and set the terms of daily life there, reshape democratic life in Latin America. My dissertation takes this to the ballot box in Rio de Janeiro, following armed order into turnout, candidacy, and the vote with spatial data, electoral and administrative records, and fieldwork; related work asks who can compete under criminal governments and how militias build their own electoral geographies. The same question runs along three further fronts.",
  "threads": [
     ("Race and political violence", "Who is targeted in political life, and where. I map the racial geography of political violence in Rio &mdash; from the Baixada to the South Zone &mdash; and the parliamentary discourse that normalizes police lethality."),
     ("Gender, criminal order, and state repression", "How armed governance and policing fall unevenly on women. Comparative work on gang control, state repression, and violence against women, including a study set in Chicago, and the women, peace and security agenda."),
     ("Public security, institutions, and policy", "How security institutions are built, captured, and reformed &mdash; from police governance to the design of public-security policy across Latin America."),
  ],
  "groups": {"articles":"Peer-reviewed articles","chapters":"Book chapters","reports":"Technical reports","papers":"Working papers &amp; preprints"},
  "writing_lead": "Writing for broader audiences on crime, security, and democracy.",
  "consulting_lead": "I bring this research into applied settings, offering strategic political analysis for complex Latin American contexts &mdash; bridging academic rigor and decision-making. Areas of work:",
  "areas": ["Political risk and institutional dynamics","Defense, public security, and organized crime","Human rights, gender and racial inequalities","Electoral landscapes and democratic trends","Policy evaluation and governance structures"],
  "consulting_close": "I work with research centers and universities, NGOs and international cooperation agencies, and private-sector organizations across Latin America, integrating qualitative and quantitative methods &mdash; including spatial data analysis, institutional mapping, and strategic briefings.",
},
"pt": {
  "nav": [("index","Sobre"),("research","Pesquisa"),("publications","Publica&ccedil;&otilde;es"),("writing","Textos"),("consulting","Consultoria")],
  "tagline": "Governan&ccedil;a criminal e pol&iacute;tica na Am&eacute;rica Latina",
  "kicker_index": "Cientista pol&iacute;tico",
  "current": "Doutorando, <strong>Universidade de Bras&iacute;lia</strong> &middot; Pesquisador visitante, <strong>University of Illinois at Chicago</strong>",
  "footer": "&copy; 2026 Igor Novaes Lins",
  "skip_alt": "Igor Novaes Lins",
  "titles": {
     "index": "Igor Novaes Lins &mdash; Governan&ccedil;a criminal e pol&iacute;tica",
     "research": "Pesquisa &mdash; Igor Novaes Lins",
     "publications": "Publica&ccedil;&otilde;es &mdash; Igor Novaes Lins",
     "writing": "Textos &mdash; Igor Novaes Lins",
     "consulting": "Consultoria &mdash; Igor Novaes Lins",
  },
  "desc": {
     "index": "Igor Novaes Lins estuda governança criminal e política na América Latina — como grupos criminais armados reconfiguram a vida política, tendo o Rio de Janeiro como caso principal.",
     "research": "Pesquisa sobre governança criminal e o voto, raça e violência política, gênero e repressão estatal, e segurança pública na América Latina.",
     "publications": "Artigos, capítulos, relatórios e working papers de Igor Novaes Lins sobre governança criminal, eleições e violência política.",
     "writing": "Artigos de opinião e textos de divulgação de Igor Novaes Lins sobre crime, segurança e democracia no Brasil.",
     "consulting": "Análise política estratégica e consultoria de pesquisa sobre segurança, crime organizado e eleições na América Latina.",
  },
  "page_h1": {"index":"Sobre","research":"Pesquisa","publications":"Publica&ccedil;&otilde;es","writing":"Textos","consulting":"Pesquisa e Consultoria"},
  "about": [
     "Sou cientista pol&iacute;tico e trabalho com governan&ccedil;a criminal e pol&iacute;tica &mdash; como grupos criminais armados que governam o territ&oacute;rio, em vez de tentar derrubar o Estado, reconfiguram a vida pol&iacute;tica na Am&eacute;rica Latina. Meu caso principal &eacute; o Rio de Janeiro, onde minha tese acompanha como o dom&iacute;nio armado chega ao voto. A mesma pergunta atravessa a geografia racial da viol&ecirc;ncia pol&iacute;tica, g&ecirc;nero e repress&atilde;o estatal sob ordem criminal, e a pol&iacute;tica de seguran&ccedil;a p&uacute;blica. Trabalho com m&eacute;todos espaciais e quantitativos e com conhecimento de campo de primeira m&atilde;o das cidades brasileiras.",
     "Sou doutorando em Ci&ecirc;ncia Pol&iacute;tica na Universidade de Bras&iacute;lia e pesquisador visitante na University of Illinois at Chicago; a partir de 2026, serei pesquisador de p&oacute;s-doutorado no CEBRAP, em S&atilde;o Paulo. Sou pesquisador da RESDAL, associado ao GEMAA (IESP-UERJ) e integro o corpo editorial da <em>Revista Brasileira de Ci&ecirc;ncia Pol&iacute;tica</em>. Em 2024, fui selecionado para a Writing Academy da British Academy. Sou bacharel e mestre em Ci&ecirc;ncia Pol&iacute;tica pela Universidade de Bras&iacute;lia, trabalho em portugu&ecirc;s, espanhol e ingl&ecirc;s, e nasci em S&atilde;o Paulo.",
  ],
  "research_lead": "Minha pesquisa se concentra na <strong>governan&ccedil;a criminal e na pol&iacute;tica</strong>: como grupos armados que governam o territ&oacute;rio, e ditam as regras da vida cotidiana ali, reconfiguram a vida democr&aacute;tica na Am&eacute;rica Latina. Minha tese leva isso &agrave;s urnas no Rio de Janeiro, seguindo a ordem armada at&eacute; o comparecimento, a candidatura e o voto, com dados espaciais, registros eleitorais e administrativos e trabalho de campo; trabalhos relacionados perguntam quem pode competir sob governos criminais e como as mil&iacute;cias constroem suas pr&oacute;prias geografias eleitorais. A mesma pergunta se estende por tr&ecirc;s outras frentes.",
  "threads": [
     ("Ra&ccedil;a e viol&ecirc;ncia pol&iacute;tica", "Quem &eacute; alvo na vida pol&iacute;tica, e onde. Mapeio a geografia racial da viol&ecirc;ncia pol&iacute;tica no Rio &mdash; da Baixada &agrave; Zona Sul &mdash; e o discurso parlamentar que normaliza a letalidade policial."),
     ("G&ecirc;nero, ordem criminal e repress&atilde;o estatal", "Como a governan&ccedil;a armada e o policiamento recaem de forma desigual sobre as mulheres. Trabalho comparado sobre controle de fac&ccedil;&otilde;es, repress&atilde;o estatal e viol&ecirc;ncia contra a mulher, incluindo um estudo em Chicago, e a agenda mulheres, paz e seguran&ccedil;a."),
     ("Seguran&ccedil;a p&uacute;blica, institui&ccedil;&otilde;es e pol&iacute;tica", "Como as institui&ccedil;&otilde;es de seguran&ccedil;a s&atilde;o constru&iacute;das, capturadas e reformadas &mdash; da governan&ccedil;a policial ao desenho da pol&iacute;tica de seguran&ccedil;a p&uacute;blica na Am&eacute;rica Latina."),
  ],
  "groups": {"articles":"Artigos em peri&oacute;dico","chapters":"Cap&iacute;tulos de livro","reports":"Relat&oacute;rios t&eacute;cnicos","papers":"Working papers e preprints"},
  "writing_lead": "Escrevendo para p&uacute;blicos amplos sobre crime, seguran&ccedil;a e democracia.",
  "consulting_lead": "Levo essa pesquisa para o terreno aplicado, oferecendo an&aacute;lise pol&iacute;tica estrat&eacute;gica para contextos latino-americanos complexos &mdash; unindo rigor acad&ecirc;mico e apoio &agrave; decis&atilde;o. &Aacute;reas de atua&ccedil;&atilde;o:",
  "areas": ["Risco pol&iacute;tico e din&acirc;micas institucionais","Defesa, seguran&ccedil;a p&uacute;blica e crime organizado","Direitos humanos e desigualdades de g&ecirc;nero e ra&ccedil;a","Cen&aacute;rios eleitorais e tend&ecirc;ncias democr&aacute;ticas","Avalia&ccedil;&atilde;o de pol&iacute;ticas e estruturas de governan&ccedil;a"],
  "consulting_close": "Trabalho com centros de pesquisa e universidades, ONGs e ag&ecirc;ncias de coopera&ccedil;&atilde;o internacional, e organiza&ccedil;&otilde;es do setor privado na Am&eacute;rica Latina, integrando m&eacute;todos qualitativos e quantitativos &mdash; incluindo an&aacute;lise de dados espaciais, mapeamento institucional e briefings estrat&eacute;gicos.",
},
"es": {
  "nav": [("index","Perfil"),("research","Investigaci&oacute;n"),("publications","Publicaciones"),("writing","Textos"),("consulting","Consultor&iacute;a")],
  "tagline": "Gobernanza criminal y pol&iacute;tica en Am&eacute;rica Latina",
  "kicker_index": "Cient&iacute;fico pol&iacute;tico",
  "current": "Doctorando, <strong>Universidad de Brasilia</strong> &middot; Investigador visitante, <strong>University of Illinois at Chicago</strong>",
  "footer": "&copy; 2026 Igor Novaes Lins",
  "skip_alt": "Igor Novaes Lins",
  "titles": {
     "index": "Igor Novaes Lins &mdash; Gobernanza criminal y pol&iacute;tica",
     "research": "Investigaci&oacute;n &mdash; Igor Novaes Lins",
     "publications": "Publicaciones &mdash; Igor Novaes Lins",
     "writing": "Textos &mdash; Igor Novaes Lins",
     "consulting": "Consultor&iacute;a &mdash; Igor Novaes Lins",
  },
  "desc": {
     "index": "Igor Novaes Lins estudia la gobernanza criminal y la política en América Latina — cómo los grupos criminales armados transforman la vida política, con Río de Janeiro como caso principal.",
     "research": "Investigación sobre gobernanza criminal y el voto, raza y violencia política, género y represión estatal, y seguridad pública en América Latina.",
     "publications": "Artículos, capítulos, informes y working papers de Igor Novaes Lins sobre gobernanza criminal, elecciones y violencia política.",
     "writing": "Artículos de opinión de Igor Novaes Lins sobre crimen, seguridad y democracia en Brasil.",
     "consulting": "Análisis político estratégico y consultoría de investigación sobre seguridad, crimen organizado y elecciones en América Latina.",
  },
  "page_h1": {"index":"Perfil","research":"Investigaci&oacute;n","publications":"Publicaciones","writing":"Textos","consulting":"Investigaci&oacute;n y Consultor&iacute;a"},
  "about": [
     "Soy cient&iacute;fico pol&iacute;tico y trabajo sobre gobernanza criminal y pol&iacute;tica &mdash; c&oacute;mo los grupos criminales armados que gobiernan el territorio, en lugar de buscar derrocar al Estado, transforman la vida pol&iacute;tica en Am&eacute;rica Latina. Mi caso principal es R&iacute;o de Janeiro, donde mi tesis sigue c&oacute;mo el dominio criminal llega al voto. La misma pregunta atraviesa la geograf&iacute;a racial de la violencia pol&iacute;tica, g&eacute;nero y represi&oacute;n estatal bajo el orden criminal, y la pol&iacute;tica de seguridad p&uacute;blica. Trabajo con m&eacute;todos espaciales y cuantitativos y con conocimiento de campo de primera mano de las ciudades brasile&ntilde;as.",
     "Soy doctorando en Ciencia Pol&iacute;tica en la Universidad de Brasilia e investigador visitante en la University of Illinois at Chicago; a partir de 2026 ser&eacute; investigador posdoctoral en el CEBRAP, en S&atilde;o Paulo. Soy investigador de la RESDAL, miembro del GEMAA (IESP-UERJ) e integro el consejo editorial de la <em>Revista Brasile&ntilde;a de Ciencia Pol&iacute;tica</em>. En 2024 fui seleccionado para la Writing Academy de la British Academy. Soy licenciado y mag&iacute;ster en Ciencia Pol&iacute;tica por la Universidad de Brasilia, trabajo en portugu&eacute;s, espa&ntilde;ol e ingl&eacute;s, y nac&iacute; en S&atilde;o Paulo.",
  ],
  "research_lead": "Mi investigaci&oacute;n se centra en la <strong>gobernanza criminal y la pol&iacute;tica</strong>: c&oacute;mo los grupos armados que gobiernan el territorio, y dictan las reglas de la vida cotidiana all&iacute;, transforman la vida democr&aacute;tica en Am&eacute;rica Latina. Mi tesis lo lleva a las urnas en R&iacute;o de Janeiro, siguiendo el orden armado hasta la participaci&oacute;n, la candidatura y el voto, con datos espaciales, registros electorales y administrativos y trabajo de campo; trabajos relacionados preguntan qui&eacute;n puede competir bajo gobiernos criminales y c&oacute;mo las milicias construyen sus propias geograf&iacute;as electorales. La misma pregunta se extiende por tres frentes m&aacute;s.",
  "threads": [
     ("Raza y violencia pol&iacute;tica", "Qui&eacute;n es blanco en la vida pol&iacute;tica, y d&oacute;nde. Mapeo la geograf&iacute;a racial de la violencia pol&iacute;tica en R&iacute;o &mdash; de la Baixada a la Zona Sur &mdash; y el discurso parlamentario que normaliza la letalidad policial."),
     ("G&eacute;nero, orden criminal y represi&oacute;n estatal", "C&oacute;mo la gobernanza armada y la actuaci&oacute;n policial recaen de forma desigual sobre las mujeres. Trabajo comparado sobre control de pandillas, represi&oacute;n estatal y violencia contra las mujeres, incluido un estudio en Chicago, y la agenda mujeres, paz y seguridad."),
     ("Seguridad p&uacute;blica, instituciones y pol&iacute;tica", "C&oacute;mo se construyen, capturan y reforman las instituciones de seguridad &mdash; de la gobernanza policial al dise&ntilde;o de la pol&iacute;tica de seguridad p&uacute;blica en Am&eacute;rica Latina."),
  ],
  "groups": {"articles":"Art&iacute;culos en revistas","chapters":"Cap&iacute;tulos de libro","reports":"Informes t&eacute;cnicos","papers":"Working papers y preprints"},
  "writing_lead": "Escribiendo para p&uacute;blicos amplios sobre crimen, seguridad y democracia.",
  "consulting_lead": "Llevo esta investigaci&oacute;n al terreno aplicado, ofreciendo an&aacute;lisis pol&iacute;tico estrat&eacute;gico para contextos latinoamericanos complejos &mdash; uniendo rigor acad&eacute;mico y apoyo a la toma de decisiones. &Aacute;reas de trabajo:",
  "areas": ["Riesgo pol&iacute;tico y din&aacute;micas institucionales","Defensa, seguridad p&uacute;blica y crimen organizado","Derechos humanos y desigualdades de g&eacute;nero y raza","Escenarios electorales y tendencias democr&aacute;ticas","Evaluaci&oacute;n de pol&iacute;ticas y estructuras de gobernanza"],
  "consulting_close": "Trabajo con centros de investigaci&oacute;n y universidades, ONG y agencias de cooperaci&oacute;n internacional, y organizaciones del sector privado en Am&eacute;rica Latina, integrando m&eacute;todos cualitativos y cuantitativos &mdash; incluyendo an&aacute;lisis de datos espaciales, mapeo institucional e informes estrat&eacute;gicos.",
},
}

# ---------------------------------------------------------------- render parts
def render_head(lang, page):
    t = T[lang]
    title = t["titles"][page]
    desc = t["desc"][page]
    canon = abs_url(lang, page)
    alts = "\n".join(
        '<link rel="alternate" hreflang="%s" href="%s">' % (HREFLANG[l], abs_url(l, page))
        for l in LANGS
    )
    alts += '\n<link rel="alternate" hreflang="x-default" href="%s">' % abs_url(DEFAULT, page)
    og_locale = {"en": "en_US", "pt": "pt_BR", "es": "es_ES"}[lang]
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
    t = T[lang]
    home = page_url(lang, "index")
    if HAS_PHOTO:
        photo = '<a href="%s"><img class="portrait" src="/assets/portrait.jpg" alt="%s"></a>' % (home, t["skip_alt"])
    else:
        photo = '<a href="%s"><div class="monogram">IN</div></a>' % home
    navitems = "".join(
        '<a href="%s"%s>%s</a>' % (
            page_url(lang, p),
            ' class="active"' if p == page else "",
            label,
        )
        for p, label in t["nav"]
    )
    langlinks = []
    for i, l in enumerate(LANGS):
        cls = ' class="active"' if l == lang else ""
        langlinks.append('<a href="%s"%s>%s</a>' % (page_url(l, page), cls, l.upper()))
    langrow = "<span>&middot;</span>".join(langlinks)
    contacts = "".join(
        '<a href="%s"%s>%s</a>' % (
            url, ("" if url.startswith("mailto:") else ' rel="me noopener" target="_blank"'), label
        )
        for label, url in CONTACTS
    )
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

def render_groups(lang):
    t = T[lang]
    out = []
    for key, items in PUBS:
        lis = "".join("<li>%s</li>" % it for it in items)
        out.append('<div class="group"><h3>%s</h3><ol class="list">%s</ol></div>' % (t["groups"][key], lis))
    return "\n".join(out)

def render_main(lang, page):
    t = T[lang]
    h1 = t["page_h1"][page]
    inner = ""
    if page == "index":
        inner = "".join('<p class="lead">%s</p>' % p if i == 0 else "<p>%s</p>" % p
                        for i, p in enumerate(t["about"]))
    elif page == "research":
        inner = '<p class="lead">%s</p>' % t["research_lead"]
        for title, desc in t["threads"]:
            inner += '<div class="group"><h3>%s</h3><p>%s</p></div>' % (title, desc)
    elif page == "publications":
        inner = render_groups(lang)
    elif page == "writing":
        inner = '<p class="lead">%s</p>' % t["writing_lead"]
        lis = "".join("<li>%s</li>" % it for it in OPEDS)
        inner += '<ol class="list">%s</ol>' % lis
    elif page == "consulting":
        inner = '<p class="lead">%s</p>' % t["consulting_lead"]
        inner += '<ul class="areas">%s</ul>' % "".join("<li>%s</li>" % a for a in t["areas"])
        inner += "<p>%s</p>" % t["consulting_close"]
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
  "knowsAbout": ["Criminal governance","Electoral behavior","Political violence","Organized crime","Public security","Latin American politics","Brazilian politics"],
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

# ---------------------------------------------------------------- write files
def write(path, content):
    full = os.path.join(ROOT, path)
    d = os.path.dirname(full)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def main():
    written = []
    for lang in LANGS:
        sub = "" if lang == DEFAULT else lang + "/"
        for page in PAGES:
            fname = "index.html" if page == "index" else "%s.html" % page
            written.append(write(sub + fname, render_page(lang, page)))

    # sitemap
    urls = []
    for lang in LANGS:
        for page in PAGES:
            urls.append("  <url><loc>%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>"
                        % (abs_url(lang, page), "1.0" if page == "index" else "0.7"))
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    written.append(write("sitemap.xml", sitemap))

    robots = "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE
    written.append(write("robots.txt", robots))

    print("Wrote %d files:" % len(written))
    for w in written:
        print("  " + w)

if __name__ == "__main__":
    main()
