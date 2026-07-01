#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for igornovaeslins.github.io
Trilingual (EN / PT / ES), 5 pages, Economist-style sidebar layout.
Run:  python3 build.py
"""
import os, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://igornovaeslins.github.io"
LANGS = ["en", "pt", "es"]
DEFAULT = "en"
PAGES = ["index", "research", "writing", "consulting"]
HREFLANG = {"en": "en", "pt": "pt-BR", "es": "es"}
HAS_PHOTO = True
OG_IMAGE = SITE + "/assets/portrait.jpg"
MAP_URL = "https://igornovaeslins.github.io/mobilidade-raca-sp/mapa.html"
NAME = "Igor Novaes Lins"

def _css_ver():
    try:
        return hashlib.md5(open(os.path.join(ROOT, "style.css"), "rb").read()).hexdigest()[:8]
    except Exception:
        return "1"
CSS_VER = _css_ver()

def base(lang): return "/" if lang == DEFAULT else "/%s/" % lang
def page_url(lang, page):
    b = base(lang)
    return b if page == "index" else "%s%s.html" % (b, page)
def abs_url(lang, page): return SITE + page_url(lang, page)

CONTACTS = [
    ("Email", "mailto:igornovaeslins@gmail.com"),
    ("Google Scholar", "https://scholar.google.com/citations?user=pD8sQZAAAAAJ&hl=en"),
    ("ORCID", "https://orcid.org/0000-0003-0510-8355"),
    ("Lattes", "http://lattes.cnpq.br/1256551333741329"),
    ("LinkedIn", "https://www.linkedin.com/in/igornovaeslins"),
    ("GitHub", "https://github.com/igornovaeslins"),
]

# Research themes (anchors on the research page) and the short tag label per language.
THEME_IDS = ["t-governance", "t-state", "t-collapse", "t-race", "t-institutions"]
THEME_TAGS = {
    "en": {"t-governance": "criminal governance", "t-state": "the state &amp; crime", "t-collapse": "order &amp; violence", "t-race": "racial violence", "t-institutions": "institutions &amp; civic space"},
    "pt": {"t-governance": "governan&ccedil;a criminal", "t-state": "o Estado e o crime", "t-collapse": "ordem e viol&ecirc;ncia", "t-race": "viol&ecirc;ncia racial", "t-institutions": "institui&ccedil;&otilde;es e espa&ccedil;o c&iacute;vico"},
    "es": {"t-governance": "gobernanza criminal", "t-state": "el Estado y el crimen", "t-collapse": "orden y violencia", "t-race": "violencia racial", "t-institutions": "instituciones y espacio c&iacute;vico"},
}
# which theme(s) each publication belongs to (index-aligned with the lists below; same order in EN and PT).
PUB_TAGS = {
    "articles": [["t-governance"], ["t-governance"], ["t-race"], ["t-state"], ["t-institutions"]],
    "chapters": [["t-institutions"], ["t-institutions"]],
    "reports":  [["t-collapse"], ["t-governance", "t-collapse"]],
    "papers":   [["t-governance"], ["t-governance"], ["t-collapse"], ["t-governance"], ["t-state"], ["t-governance"], ["t-collapse"]],
}

PUBS_EN = [
    ("articles", [
        'Lins, I. N., &amp; Machado, C. A. M. (2024). The geography of militia voting in the city of Rio de Janeiro. <em>Teoria &amp; Pesquisa</em>, <span class="venue">33, 1&ndash;54.</span><br><a href="https://doi.org/10.14244/tp.v33i00.1083" rel="noopener" target="_blank">doi.org/10.14244/tp.v33i00.1083</a>',
        'Lins, I. N., &amp; Machado, C. A. M. (2023). Crime is political: theoretical elements for a neoinstitutionalist analysis of paramilitary groups in Rio de Janeiro. <em>Brazilian Journal of Political Science</em>.<br><a href="https://doi.org/10.1590/0103-3352.2023.42.271780" rel="noopener" target="_blank">doi.org/10.1590/0103-3352.2023.42.271780</a>',
        'Lins, I. N. (2023). From the Baixada to the South Zone: paths of racial political violence in Rio de Janeiro. <em>Brazilian Public Security Review</em>, <span class="venue">17, 188&ndash;207.</span><br><a href="https://doi.org/10.31060/rbsp.2023.v17.n1.1532" rel="noopener" target="_blank">doi.org/10.31060/rbsp.2023.v17.n1.1532</a>',
        'Lins, I. N., &amp; Ferreira, J. V. B. (2022). Penal populism in parliamentary discourse: the debate on police violence in the Brazilian Chamber of Deputies (2019&ndash;2021). <em>Revista Eletr&ocirc;nica de Ci&ecirc;ncia Pol&iacute;tica</em>, <span class="venue">13.</span><br><a href="https://doi.org/10.5380/recp.v13i1.82629" rel="noopener" target="_blank">doi.org/10.5380/recp.v13i1.82629</a>',
        'Parnes, H. R., Lins, I. N., &amp; Trindade, P. S. (2020). Engagement, identity, and networks: a case study of the School Without Party movement. <em>Revista Eletr&ocirc;nica Intera&ccedil;&otilde;es Sociais</em>, <span class="venue">4, 79&ndash;92.</span><br><a href="https://periodicos.furg.br/reis/article/view/11824" rel="noopener" target="_blank">periodicos.furg.br</a>',
    ]),
    ("chapters", [
        'Giannini, R., Lins, I. N., Cerqueira, M., &amp; Leite, R. (2023). The merit system in Brazil and worldwide. In G. Lotta &amp; V. Campagnac (Eds.), <em>Rep&uacute;blica em Notas</em> (Vol. 1, pp. 331&ndash;354). Rio de Janeiro: Cobog&oacute;. <span class="venue">(Jabuti Prize semifinalist)</span><br><a href="https://books.google.com/books/about/Rep%C3%BAblica_em_notas.html?id=gQ_iEAAAQBAJ" rel="noopener" target="_blank">books.google.com</a>',
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

# Original Portuguese titles for Brazilian-published works (shown on PT and ES pages).
PUBS_PT_ARTICLES = [
    'Lins, I. N., &amp; Machado, C. A. M. (2024). A geografia do voto das mil&iacute;cias na cidade do Rio de Janeiro. <em>Teoria &amp; Pesquisa</em>, <span class="venue">33, 1&ndash;54.</span><br><a href="https://doi.org/10.14244/tp.v33i00.1083" rel="noopener" target="_blank">doi.org/10.14244/tp.v33i00.1083</a>',
    'Lins, I. N., &amp; Machado, C. A. M. (2023). O crime &eacute; pol&iacute;tico: elementos te&oacute;ricos para uma an&aacute;lise neoinstitucionalista das mil&iacute;cias no Rio de Janeiro. <em>Revista Brasileira de Ci&ecirc;ncia Pol&iacute;tica</em>, <span class="venue">42.</span><br><a href="https://doi.org/10.1590/0103-3352.2023.42.271780" rel="noopener" target="_blank">doi.org/10.1590/0103-3352.2023.42.271780</a>',
    'Lins, I. N. (2023). Da baixada &agrave; zona sul: caminhos da viol&ecirc;ncia pol&iacute;tica de ra&ccedil;a no Rio de Janeiro. <em>Revista Brasileira de Seguran&ccedil;a P&uacute;blica</em>, <span class="venue">17, 188&ndash;207.</span><br><a href="https://doi.org/10.31060/rbsp.2023.v17.n1.1532" rel="noopener" target="_blank">doi.org/10.31060/rbsp.2023.v17.n1.1532</a>',
    'Lins, I. N., &amp; Ferreira, J. V. B. (2022). Populismo penal no discurso parlamentar: o debate da viol&ecirc;ncia policial na C&acirc;mara dos Deputados (2019&ndash;2021). <em>Revista Eletr&ocirc;nica de Ci&ecirc;ncia Pol&iacute;tica</em>, <span class="venue">13.</span><br><a href="https://doi.org/10.5380/recp.v13i1.82629" rel="noopener" target="_blank">doi.org/10.5380/recp.v13i1.82629</a>',
    'Parnes, H. R., Lins, I. N., &amp; Trindade, P. S. (2020). Engajamento, identidade e redes: um estudo de caso do Escola sem Partido. <em>Revista Eletr&ocirc;nica Intera&ccedil;&otilde;es Sociais</em>, <span class="venue">4, 79&ndash;92.</span><br><a href="https://periodicos.furg.br/reis/article/view/11824" rel="noopener" target="_blank">periodicos.furg.br</a>',
]
PUBS_PT_CHAPTERS = [
    'Giannini, R., Lins, I. N., Cerqueira, M., &amp; Leite, R. (2023). O sistema de m&eacute;rito no Brasil e no mundo. In G. Lotta &amp; V. Campagnac (Org.), <em>Rep&uacute;blica em Notas</em> (Vol. 1, pp. 331&ndash;354). Rio de Janeiro: Cobog&oacute;. <span class="venue">(semifinalista do Pr&ecirc;mio Jabuti)</span><br><a href="https://books.google.com/books/about/Rep%C3%BAblica_em_notas.html?id=gQ_iEAAAQBAJ" rel="noopener" target="_blank">books.google.com</a>',
    'Giannini, R., Lins, I. N., Cerqueira, M., &amp; Leite, R. (2023). Recomenda&ccedil;&otilde;es para fortalecer o sistema de m&eacute;rito do servi&ccedil;o p&uacute;blico. In G. Lotta &amp; V. Campagnac (Org.), <em>Rep&uacute;blica em Notas</em> (Vol. 1, pp. 355&ndash;365). Rio de Janeiro: Cobog&oacute;.',
]

def pubs_for(lang):
    if lang == "en":
        return PUBS_EN
    return [("articles", PUBS_PT_ARTICLES), ("chapters", PUBS_PT_CHAPTERS)] + [(k, v) for k, v in PUBS_EN if k in ("reports", "papers")]

OPEDS = {
  "pt": [
    'Lins, I. N. (2026). Redu&ccedil;&atilde;o da maioridade penal vai criar novo ex&eacute;rcito do PCC. <em>CartaCapital</em>. <a href="https://www.cartacapital.com.br/artigo/reducao-da-maioridade-penal-vai-criar-novo-exercito-do-pcc/" rel="noopener" target="_blank">cartacapital.com.br</a>',
    'Lins, I. N., &amp; Giannini, R. (2022). O medo n&atilde;o vencer&aacute; a democracia. <em>Correio Braziliense</em>.',
    'Lins, I. N. (2021). No Brasil, vidas negras n&atilde;o importam: discursos sobre a viol&ecirc;ncia policial na C&acirc;mara dos Deputados. <em>Boletim Lua Nova</em>.',
    'Lins, I. N. (2019). Supl&ecirc;ncia de deputados: parlamentar eleito depois das elei&ccedil;&otilde;es? <em>Politize!</em>',
  ],
  "en": [
    'Lins, I. N. (2026). Lowering the age of criminal responsibility will build a new army for the PCC. <em>CartaCapital</em>. <a href="https://www.cartacapital.com.br/artigo/reducao-da-maioridade-penal-vai-criar-novo-exercito-do-pcc/" rel="noopener" target="_blank">cartacapital.com.br</a>',
    'Lins, I. N., &amp; Giannini, R. (2022). Fear will not defeat democracy. <em>Correio Braziliense</em>.',
    'Lins, I. N. (2021). In Brazil, Black lives do not matter: discourse on police violence in the Chamber of Deputies. <em>Boletim Lua Nova</em>.',
    'Lins, I. N. (2019). Substitute deputies: a representative elected after the election? <em>Politize!</em>',
  ],
  "es": [
    'Lins, I. N. (2026). La reducci&oacute;n de la mayor&iacute;a de edad penal crear&aacute; un nuevo ej&eacute;rcito para el PCC. <em>CartaCapital</em>. <a href="https://www.cartacapital.com.br/artigo/reducao-da-maioridade-penal-vai-criar-novo-exercito-do-pcc/" rel="noopener" target="_blank">cartacapital.com.br</a>',
    'Lins, I. N., &amp; Giannini, R. (2022). El miedo no vencer&aacute; a la democracia. <em>Correio Braziliense</em>.',
    'Lins, I. N. (2021). En Brasil, las vidas negras no importan: discursos sobre la violencia policial en la C&aacute;mara de Diputados. <em>Boletim Lua Nova</em>.',
    'Lins, I. N. (2019). Suplencia de diputados: &iquest;un parlamentario electo despu&eacute;s de las elecciones? <em>Politize!</em>',
  ],
}
INTERVIEWS = {
  "pt": [
    'Lins, I. N. (2025). Entrevista &agrave; r&aacute;dio sueca sobre o PL do licenciamento ambiental (&ldquo;PL da devasta&ccedil;&atilde;o&rdquo;). <em>Sveriges Radio (Ekot)</em>.',
    'Lins, I. N. (2023). Chacinas comprometeram plano de seguran&ccedil;a de Dino. <em>Correio da Manh&atilde;</em>. <a href="https://correiodamanha.com.br/politica/2023/10/98656-chacinas-comprometeram-plano-de-seguranca-de-dino.html" rel="noopener" target="_blank">correiodamanha.com.br</a>',
    'Lins, I. N. (2022). Norte e Nordeste ser&atilde;o as &uacute;ltimas regi&otilde;es a darem in&iacute;cio &agrave; contagem de votos. <em>Correio Braziliense</em>. <a href="https://www.correiobraziliense.com.br/politica/2022/10/5047995-norte-e-nordeste-serao-as-ultimas-regioes-a-darem-inicio-a-contagem-de-votos.html" rel="noopener" target="_blank">correiobraziliense.com.br</a>',
    'Lins, I. N. (2022). Assassinato de petista por bolsonarista eleva tens&atilde;o &agrave;s v&eacute;speras da elei&ccedil;&atilde;o. <em>Correio Braziliense</em>. <a href="https://www.correiobraziliense.com.br/politica/2022/09/5035865-assassinato-de-petista-por-bolsonarista-eleva-tensao-as-vesperas-da-eleicao.html" rel="noopener" target="_blank">correiobraziliense.com.br</a>',
    'Lins, I. N., &amp; Paz, H. (2020). Persegui&ccedil;&atilde;o e viol&ecirc;ncia a ativistas e lideran&ccedil;as pol&iacute;ticas negras e perif&eacute;ricas. <span class="venue">Mesa redonda, r&aacute;dio/TV.</span>',
  ],
  "en": [
    'Lins, I. N. (2025). Interview on Brazil&rsquo;s environmental licensing bill (the &ldquo;devastation bill&rdquo;). <em>Sveriges Radio (Ekot)</em>.',
    'Lins, I. N. (2023). On how massacres undermined Justice Minister Dino&rsquo;s security plan. <em>Correio da Manh&atilde;</em>. <a href="https://correiodamanha.com.br/politica/2023/10/98656-chacinas-comprometeram-plano-de-seguranca-de-dino.html" rel="noopener" target="_blank">correiodamanha.com.br</a>',
    'Lins, I. N. (2022). On why the North and Northeast are the last regions to begin counting votes. <em>Correio Braziliense</em>. <a href="https://www.correiobraziliense.com.br/politica/2022/10/5047995-norte-e-nordeste-serao-as-ultimas-regioes-a-darem-inicio-a-contagem-de-votos.html" rel="noopener" target="_blank">correiobraziliense.com.br</a>',
    'Lins, I. N. (2022). On rising political tension before the election after the killing of a Workers&rsquo; Party supporter. <em>Correio Braziliense</em>. <a href="https://www.correiobraziliense.com.br/politica/2022/09/5035865-assassinato-de-petista-por-bolsonarista-eleva-tensao-as-vesperas-da-eleicao.html" rel="noopener" target="_blank">correiobraziliense.com.br</a>',
    'Lins, I. N., &amp; Paz, H. (2020). Round table on violence against Black and peripheral activists and political leaders. <span class="venue">Radio/TV.</span>',
  ],
  "es": [
    'Lins, I. N. (2025). Entrevista a la radio sueca sobre el proyecto de licenciamiento ambiental (la &ldquo;ley de la devastaci&oacute;n&rdquo;). <em>Sveriges Radio (Ekot)</em>.',
    'Lins, I. N. (2023). Sobre c&oacute;mo las masacres comprometieron el plan de seguridad del ministro Dino. <em>Correio da Manh&atilde;</em>. <a href="https://correiodamanha.com.br/politica/2023/10/98656-chacinas-comprometeram-plano-de-seguranca-de-dino.html" rel="noopener" target="_blank">correiodamanha.com.br</a>',
    'Lins, I. N. (2022). Sobre por qu&eacute; el Norte y el Nordeste son las &uacute;ltimas regiones en empezar el conteo de votos. <em>Correio Braziliense</em>. <a href="https://www.correiobraziliense.com.br/politica/2022/10/5047995-norte-e-nordeste-serao-as-ultimas-regioes-a-darem-inicio-a-contagem-de-votos.html" rel="noopener" target="_blank">correiobraziliense.com.br</a>',
    'Lins, I. N. (2022). Sobre la tensi&oacute;n pol&iacute;tica antes de la elecci&oacute;n tras el asesinato de un simpatizante del PT. <em>Correio Braziliense</em>. <a href="https://www.correiobraziliense.com.br/politica/2022/09/5035865-assassinato-de-petista-por-bolsonarista-eleva-tensao-as-vesperas-da-eleicao.html" rel="noopener" target="_blank">correiobraziliense.com.br</a>',
    'Lins, I. N., &amp; Paz, H. (2020). Mesa redonda sobre la violencia contra activistas y liderazgos pol&iacute;ticos negros y perif&eacute;ricos. <span class="venue">Radio/TV.</span>',
  ],
}
TALKS = {
  "pt": [
    'Audi&ecirc;ncia p&uacute;blica sobre publicidade ambiental enganosa (greenwashing). <span class="venue">C&acirc;mara dos Deputados, Comiss&atilde;o de Legisla&ccedil;&atilde;o Participativa, 2025.</span>',
    'Justi&ccedil;a clim&aacute;tica e sa&uacute;de nas periferias. <span class="venue">Pal&aacute;cio do Planalto, 2025.</span>',
    'Mudan&ccedil;as clim&aacute;ticas e seus impactos nas rela&ccedil;&otilde;es de trabalho. <span class="venue">Tribunal Superior do Trabalho, com OIT Brasil e MPT, 2025.</span>',
    'Ilegalismos e produ&ccedil;&atilde;o da cidade: grupos armados, viol&ecirc;ncia pol&iacute;tica e voto. <span class="venue">Observat&oacute;rio de Favelas e Defensoria P&uacute;blica do Rio de Janeiro, 2025.</span>',
    'Desafios da cultura organizacional militar frente ao ass&eacute;dio e ao abuso sexual. <span class="venue">Webinar, RESDAL, 2025.</span>',
  ],
  "en": [
    'Public hearing on misleading environmental advertising (greenwashing). <span class="venue">Chamber of Deputies, Committee on Participatory Legislation, 2025.</span>',
    'Climate justice and health in the urban periphery. <span class="venue">Planalto Palace, 2025.</span>',
    'Climate change and its impact on labour relations. <span class="venue">Superior Labour Court (TST), with ILO Brazil and the Labour Prosecutor&rsquo;s Office, 2025.</span>',
    'Illegalisms and the making of the city: armed groups, political violence, and the vote. <span class="venue">Observat&oacute;rio de Favelas and the Rio de Janeiro Public Defender&rsquo;s Office, 2025.</span>',
    'Challenges of military organizational culture in the face of harassment and sexual abuse. <span class="venue">Webinar, RESDAL, 2025.</span>',
  ],
  "es": [
    'Audiencia p&uacute;blica sobre publicidad ambiental enga&ntilde;osa (greenwashing). <span class="venue">C&aacute;mara de Diputados, Comisi&oacute;n de Legislaci&oacute;n Participativa, 2025.</span>',
    'Justicia clim&aacute;tica y salud en las periferias. <span class="venue">Palacio de Planalto, 2025.</span>',
    'Cambio clim&aacute;tico y sus impactos en las relaciones laborales. <span class="venue">Tribunal Superior del Trabajo, con la OIT Brasil y el MPT, 2025.</span>',
    'Ilegalismos y producci&oacute;n de la ciudad: grupos armados, violencia pol&iacute;tica y voto. <span class="venue">Observat&oacute;rio de Favelas y la Defensor&iacute;a P&uacute;blica de R&iacute;o de Janeiro, 2025.</span>',
    'Desaf&iacute;os de la cultura organizacional militar frente al acoso y abuso sexual. <span class="venue">Webinar, RESDAL, 2025.</span>',
  ],
}

T = {
"en": {
  "nav": [("index","About"),("research","Research"),("writing","Public engagement"),("consulting","Consulting")],
  "tagline": "Criminal governance and politics in Latin America",
  "kicker_index": "Political scientist",
  "current": "PhD candidate, <strong>University of Bras&iacute;lia</strong> &middot; Visiting researcher, <strong>University of Illinois at Chicago</strong>",
  "footer": "&copy; 2026 Igor Novaes Lins",
  "skip_alt": "Igor Novaes Lins",
  "titles": {
     "index": "Igor Novaes Lins &mdash; Criminal governance &amp; politics in Latin America",
     "research": "Research &mdash; Igor Novaes Lins",
     "publications": "Publications &mdash; Igor Novaes Lins",
     "writing": "Public engagement &mdash; Igor Novaes Lins",
     "consulting": "Consulting &mdash; Igor Novaes Lins",
  },
  "desc": {
     "index": "Igor Novaes Lins studies criminal governance and politics in Latin America — how armed criminal groups reshape political life, with Rio de Janeiro as the main case.",
     "research": "Research on criminal governance and the vote, the state and crime, collapse and gendered violence, and racial political violence in Latin America.",
     "publications": "Articles, book chapters, reports, and working papers by Igor Novaes Lins on criminal governance, elections, and political violence.",
     "writing": "Op-eds, interviews, and public engagement by Igor Novaes Lins on crime, security, climate, and democracy.",
     "consulting": "Data, maps, and reproducible analysis for organizations working on cities, security, and inequality in Latin America.",
  },
  "page_h1": {"index":"About","research":"Research","publications":"Publications","writing":"Public engagement","consulting":"Research &amp; consulting"},
  "about": [
     "Born in S&atilde;o Paulo, I am a political scientist, a doctoral candidate at the University of Bras&iacute;lia and a visiting researcher at the University of Illinois at Chicago. I study how organized crime and political violence shape political life in Latin American cities, especially in Brazil, combining quantitative and qualitative methods.",
     "My interests are criminal governance, electoral behavior, political violence, and subnational politics in Latin America, with attention to public security and racial inequality.",
     "My work has lived inside and outside the academy. I was a researcher at the Igarap&eacute; Institute, working on public security and civic space, and I authored a report on women environmental defenders in Peru, presented at COP28. I have also worked in the Brazilian federal government, where I led the Ministry of Racial Equality&rsquo;s strategy to pass the higher-education quota law, and I co-authored chapters in <em>Rep&uacute;blica em Notas</em>, a Jabuti Prize semifinalist, on the merit-based civil service.",
     "From 2026 I will be a postdoctoral researcher at CEBRAP, in S&atilde;o Paulo. I hold a Bachelor&rsquo;s and a Master&rsquo;s in political science from the University of Bras&iacute;lia, and I work in Portuguese, Spanish, and English.",
  ],
  "research_lead": "I study how organized crime reshapes political life. When armed groups govern a territory &mdash; setting the rules of daily life for the people who live there &mdash; they also change who votes, who can run for office, who wins, and who is exposed to violence. I work these questions out mainly in Rio de Janeiro, with georeferenced administrative microdata.",
  "threads": [
     ("Criminal governance and elections", "The political weight of an armed group depends on how deeply it is integrated into the political system, more than on how much territory it holds. Integrated groups build durable, reciprocal ties to parties and candidates and govern the people under them as a constituency; peripheral groups hold ground by force alone. Reading criminal governance as a question of political incorporation lets me explain why groups with similar territorial power move elections in opposite directions. I formalize this as a typology &mdash; integrated, peripheral, and hybrid governance &mdash; and trace it through turnout, voter registration, candidacy, and who wins."),
     ("The state and organized crime", "The state is part of the infrastructure of criminal order. Formal decisions, above all who is put in command of the local police, redraw the borders of criminal control and feed electoral capture. Policing is one of the levers through which the state reorganizes the order it claims to fight, and penal discourse in the legislature lends that order legitimacy."),
     ("Order, collapse, and gendered violence", "Order holds violence in check. When a governing authority breaks down &mdash; criminal, police, or hybrid &mdash; what surfaces is the violence it had been containing. Reading that violence means keeping two ledgers at once, the institutional record and the real one, because under criminal governance the two diverge systematically, and the gap between them is itself evidence of capture. The same logic runs through gender. Armed order at once restrains and produces violence against women."),
     ("Race and political violence", "Political violence in Brazil has a racial grammar. Who becomes a target in political life, and where, runs along two lines that I keep separate, one of race and one of territory. I also show how parliamentary discourse normalizes police lethality against Black citizens."),
     ("Democratic institutions and civic space", "Alongside crime, I work on the institutions of democracy and the space for civic life. I have studied the merit-based civil service and the patronage that wears it down, and the social movements that contest the boundaries of civic space. What ties this to my main agenda is capture, the takeover of public institutions by private interests."),
  ],
  "groups": {"articles":"Peer-reviewed articles","chapters":"Book chapters","reports":"Technical reports","papers":"Working papers &amp; preprints"},
  "writing_lead": "I take part in public debate on crime, security, climate, and democracy, through op-eds, the media, and public hearings.",
  "writing_groups": {"talks": "Talks &amp; public hearings", "media": "Interviews &amp; media", "opeds": "Op-eds"},
  "pubs_label": "publications",
  "map_caption": "Where Black residents live in S&atilde;o Paulo, the bus runs slower. Bus speed by district, crossed with race and income. By Igor Novaes Lins.",
  "map_full": "Open full screen",
  "consulting": [
     "I am a social scientist who works at the intersection of research and public policy. Organizations working on cities, security, and inequality often face questions the available evidence does not answer. I help them answer those questions, bringing the method each one calls for and a clear reading of the politics and institutions in play.",
     "I bring quantitative and qualitative evidence to the same problem &mdash; administrative and survey data, interviews and fieldwork, the analysis of discourse and documents, and maps when the answer is spatial. When the official record is thin, I build the data myself, including in real time, and look in it for the inequalities of race, income, gender, and territory that averages hide.",
     "My work is built to be trusted and checked. I document how I reach each result and stay explicit about what the evidence supports and what it leaves open.",
     "I work with observatories, NGOs, think tanks, and public agencies that need this kind of evidence for advocacy and policy. The work takes the form its question requires &mdash; a diagnosis, a technical note or evidence review, a map, an open dataset or indicator, or the strategy to carry a decision through.",
  ],
},
"pt": {
  "nav": [("index","Sobre"),("research","Pesquisa"),("writing","Atua&ccedil;&atilde;o p&uacute;blica"),("consulting","Consultoria")],
  "tagline": "Governan&ccedil;a criminal e pol&iacute;tica na Am&eacute;rica Latina",
  "kicker_index": "Cientista pol&iacute;tico",
  "current": "Doutorando, <strong>Universidade de Bras&iacute;lia</strong> &middot; Pesquisador visitante, <strong>University of Illinois at Chicago</strong>",
  "footer": "&copy; 2026 Igor Novaes Lins",
  "skip_alt": "Igor Novaes Lins",
  "titles": {
     "index": "Igor Novaes Lins &mdash; Governan&ccedil;a criminal e pol&iacute;tica",
     "research": "Pesquisa &mdash; Igor Novaes Lins",
     "publications": "Publica&ccedil;&otilde;es &mdash; Igor Novaes Lins",
     "writing": "Atua&ccedil;&atilde;o p&uacute;blica &mdash; Igor Novaes Lins",
     "consulting": "Consultoria &mdash; Igor Novaes Lins",
  },
  "desc": {
     "index": "Igor Novaes Lins estuda governança criminal e política na América Latina — como grupos criminais armados reconfiguram a vida política, tendo o Rio de Janeiro como caso principal.",
     "research": "Pesquisa sobre governança criminal e o voto, o Estado e o crime, colapso e violência de gênero, e violência política racial na América Latina.",
     "publications": "Artigos, capítulos, relatórios e working papers de Igor Novaes Lins sobre governança criminal, eleições e violência política.",
     "writing": "Artigos, entrevistas e atuação pública de Igor Novaes Lins sobre crime, segurança, clima e democracia.",
     "consulting": "Dados, mapas e análise reprodutível para organizações que trabalham com cidades, segurança e desigualdade na América Latina.",
  },
  "page_h1": {"index":"Sobre","research":"Pesquisa","publications":"Publica&ccedil;&otilde;es","writing":"Atua&ccedil;&atilde;o p&uacute;blica","consulting":"Pesquisa e consultoria"},
  "about": [
     "Natural de S&atilde;o Paulo, sou cientista pol&iacute;tico, doutorando na Universidade de Bras&iacute;lia e pesquisador visitante na Universidade de Illinois em Chicago. Estudo como o crime organizado e a viol&ecirc;ncia pol&iacute;tica moldam a vida pol&iacute;tica nas cidades latino-americanas, especialmente no Brasil, combinando m&eacute;todos quantitativos e qualitativos.",
     "Meus interesses s&atilde;o governan&ccedil;a criminal, comportamento eleitoral, viol&ecirc;ncia pol&iacute;tica e pol&iacute;tica subnacional na Am&eacute;rica Latina, com aten&ccedil;&atilde;o &agrave; seguran&ccedil;a p&uacute;blica e &agrave; desigualdade racial.",
     "Meu trabalho viveu dentro e fora da universidade. Fui pesquisador no Instituto Igarap&eacute;, atuando em seguran&ccedil;a p&uacute;blica e espa&ccedil;o c&iacute;vico, e assinei um relat&oacute;rio sobre mulheres defensoras do meio ambiente no Peru, apresentado na COP28. Tamb&eacute;m trabalhei no governo federal, onde liderei a estrat&eacute;gia do Minist&eacute;rio da Igualdade Racial para aprova&ccedil;&atilde;o da lei de cotas no ensino superior e coassinei cap&iacute;tulos no <em>Rep&uacute;blica em Notas</em>, semifinalista do Pr&ecirc;mio Jabuti, sobre o sistema de m&eacute;rito do servi&ccedil;o p&uacute;blico.",
     "A partir de 2026, integro o CEBRAP, em S&atilde;o Paulo, como pesquisador de p&oacute;s-doutorado. Sou bacharel e mestre em ci&ecirc;ncia pol&iacute;tica pela Universidade de Bras&iacute;lia, trabalho em portugu&ecirc;s, espanhol e ingl&ecirc;s.",
  ],
  "research_lead": "Estudo como o crime organizado reconfigura a vida pol&iacute;tica. Quando grupos armados governam um territ&oacute;rio &mdash; e ditam as regras do cotidiano de quem vive ali &mdash;, eles tamb&eacute;m mudam quem vota, quem pode se candidatar, quem vence e quem fica exposto &agrave; viol&ecirc;ncia. Trabalho essas perguntas sobretudo no Rio de Janeiro, com microdados administrativos georreferenciados.",
  "threads": [
     ("Governan&ccedil;a criminal e elei&ccedil;&otilde;es", "O peso pol&iacute;tico de um grupo armado depende de quanto ele est&aacute; integrado ao sistema pol&iacute;tico, mais do que da extens&atilde;o do territ&oacute;rio que domina. Grupos integrados constroem la&ccedil;os dur&aacute;veis e rec&iacute;procos com partidos e candidatos e governam quem vive sob eles como um eleitorado; grupos perif&eacute;ricos seguram o territ&oacute;rio apenas pela for&ccedil;a. Ler a governan&ccedil;a criminal como uma quest&atilde;o de incorpora&ccedil;&atilde;o pol&iacute;tica me permite explicar por que grupos com poder territorial parecido movem as elei&ccedil;&otilde;es em dire&ccedil;&otilde;es opostas. Formalizo isso como uma tipologia &mdash; governan&ccedil;a integrada, perif&eacute;rica e h&iacute;brida &mdash; e a acompanho no comparecimento, no alistamento eleitoral, na candidatura e em quem vence."),
     ("O Estado e o crime organizado", "O Estado &eacute; parte da infraestrutura da ordem criminal. Decis&otilde;es formais, sobretudo quem assume o comando da pol&iacute;cia local, redesenham as fronteiras do controle criminal e alimentam a captura eleitoral. O policiamento &eacute; uma das alavancas pelas quais o Estado reorganiza a ordem que diz combater, e o discurso penal no Legislativo confere legitimidade a essa ordem."),
     ("Ordem, colapso e viol&ecirc;ncia de g&ecirc;nero", "A ordem cont&eacute;m a viol&ecirc;ncia. Quando uma autoridade que governa entra em colapso &mdash; criminal, policial ou h&iacute;brida &mdash;, o que vem &agrave; tona &eacute; a viol&ecirc;ncia que ela vinha represando. Ler essa viol&ecirc;ncia exige manter dois registros ao mesmo tempo, o institucional e o real, porque sob governan&ccedil;a criminal os dois divergem de forma sistem&aacute;tica, e a dist&acirc;ncia entre eles &eacute;, ela pr&oacute;pria, evid&ecirc;ncia de captura. A mesma l&oacute;gica atravessa o g&ecirc;nero. A ordem armada ao mesmo tempo cont&eacute;m e produz a viol&ecirc;ncia contra a mulher."),
     ("Ra&ccedil;a e viol&ecirc;ncia pol&iacute;tica", "A viol&ecirc;ncia pol&iacute;tica no Brasil tem uma gram&aacute;tica racial. Quem vira alvo na vida pol&iacute;tica, e onde, corre por duas linhas que mantenho separadas, a de ra&ccedil;a e a de territ&oacute;rio. Mostro tamb&eacute;m como o discurso parlamentar normaliza a letalidade policial contra cidad&atilde;os negros."),
     ("Institui&ccedil;&otilde;es democr&aacute;ticas e espa&ccedil;o c&iacute;vico", "Al&eacute;m do crime, trabalho com as institui&ccedil;&otilde;es da democracia e com o espa&ccedil;o da vida c&iacute;vica. Estudei o sistema de m&eacute;rito do servi&ccedil;o p&uacute;blico e o clientelismo que o corr&oacute;i, e os movimentos sociais que disputam os limites do espa&ccedil;o c&iacute;vico. O que liga isso &agrave; minha agenda principal &eacute; a captura, a tomada de institui&ccedil;&otilde;es p&uacute;blicas por interesses privados."),
  ],
  "groups": {"articles":"Artigos em peri&oacute;dico","chapters":"Cap&iacute;tulos de livro","reports":"Relat&oacute;rios t&eacute;cnicos","papers":"Working papers e preprints"},
  "writing_lead": "Participo do debate p&uacute;blico sobre crime, seguran&ccedil;a, clima e democracia, em artigos, na m&iacute;dia e em audi&ecirc;ncias p&uacute;blicas.",
  "writing_groups": {"talks": "Palestras e audi&ecirc;ncias p&uacute;blicas", "media": "Entrevistas e m&iacute;dia", "opeds": "Artigos de opini&atilde;o"},
  "pubs_label": "publica&ccedil;&otilde;es",
  "map_caption": "Onde mora a popula&ccedil;&atilde;o negra em S&atilde;o Paulo, o &ocirc;nibus anda mais devagar. Velocidade do transporte por distrito, cruzada com ra&ccedil;a e renda. Elabora&ccedil;&atilde;o: Igor Novaes Lins.",
  "map_full": "Ver em tela cheia",
  "consulting": [
     "Sou cientista social e trabalho no cruzamento entre a pesquisa e a pol&iacute;tica p&uacute;blica. Organiza&ccedil;&otilde;es que atuam com cidades, seguran&ccedil;a e desigualdade muitas vezes enfrentam perguntas que a evid&ecirc;ncia dispon&iacute;vel n&atilde;o responde. Ajudo a respond&ecirc;-las com o m&eacute;todo que cada uma pede e com uma leitura clara da pol&iacute;tica e das institui&ccedil;&otilde;es em jogo.",
     "Levo evid&ecirc;ncia quantitativa e qualitativa ao mesmo problema &mdash; dados administrativos e de pesquisa amostral, entrevistas e trabalho de campo, an&aacute;lise de discurso e de documentos, e mapas quando a resposta &eacute; espacial. Quando o registro oficial &eacute; escasso, construo a base eu mesmo, inclusive em tempo real, e busco nela as desigualdades de ra&ccedil;a, renda, g&ecirc;nero e territ&oacute;rio que as m&eacute;dias escondem.",
     "Trabalho para que o resultado possa ser conferido por quem depende dele. Documento como chego a cada conclus&atilde;o e sou claro sobre o que a evid&ecirc;ncia sustenta e o que ela deixa em aberto.",
     "Trabalho com observat&oacute;rios, ONGs, institutos de pesquisa e &oacute;rg&atilde;os p&uacute;blicos que precisam desse tipo de evid&ecirc;ncia para incid&ecirc;ncia e pol&iacute;tica p&uacute;blica. O produto assume a forma que a pergunta exige &mdash; um diagn&oacute;stico, uma nota t&eacute;cnica ou uma s&iacute;ntese de evid&ecirc;ncias, um mapa, uma base de dados aberta, um indicador, ou a estrat&eacute;gia para levar uma decis&atilde;o adiante.",
  ],
},
"es": {
  "nav": [("index","Sobre m&iacute;"),("research","Investigaci&oacute;n"),("writing","Participaci&oacute;n p&uacute;blica"),("consulting","Consultor&iacute;a")],
  "tagline": "Gobernanza criminal y pol&iacute;tica en Am&eacute;rica Latina",
  "kicker_index": "Polit&oacute;logo",
  "current": "Doctorando, <strong>Universidad de Brasilia</strong> &middot; Investigador visitante, <strong>University of Illinois at Chicago</strong>",
  "footer": "&copy; 2026 Igor Novaes Lins",
  "skip_alt": "Igor Novaes Lins",
  "titles": {
     "index": "Igor Novaes Lins &mdash; Gobernanza criminal y pol&iacute;tica",
     "research": "Investigaci&oacute;n &mdash; Igor Novaes Lins",
     "publications": "Publicaciones &mdash; Igor Novaes Lins",
     "writing": "Participaci&oacute;n p&uacute;blica &mdash; Igor Novaes Lins",
     "consulting": "Consultor&iacute;a &mdash; Igor Novaes Lins",
  },
  "desc": {
     "index": "Igor Novaes Lins estudia la gobernanza criminal y la política en América Latina — cómo los grupos criminales armados transforman la vida política, con Río de Janeiro como caso principal.",
     "research": "Investigación sobre gobernanza criminal y el voto, el Estado y el crimen, colapso y violencia de género, y violencia política racial en América Latina.",
     "publications": "Artículos, capítulos, informes y working papers de Igor Novaes Lins sobre gobernanza criminal, elecciones y violencia política.",
     "writing": "Artículos, entrevistas y participación pública de Igor Novaes Lins sobre crimen, seguridad, clima y democracia.",
     "consulting": "Datos, mapas y análisis reproducible para organizaciones que trabajan con ciudades, seguridad y desigualdad en América Latina.",
  },
  "page_h1": {"index":"Sobre m&iacute;","research":"Investigaci&oacute;n","publications":"Publicaciones","writing":"Participaci&oacute;n p&uacute;blica","consulting":"Investigaci&oacute;n y consultor&iacute;a"},
  "about": [
     "Natural de S&atilde;o Paulo, soy polit&oacute;logo, doctorando en la Universidad de Brasilia e investigador visitante en la Universidad de Illinois en Chicago. Estudio c&oacute;mo el crimen organizado y la violencia pol&iacute;tica moldean la vida pol&iacute;tica en las ciudades latinoamericanas, especialmente en Brasil, combinando m&eacute;todos cuantitativos y cualitativos.",
     "Mis intereses son la gobernanza criminal, el comportamiento electoral, la violencia pol&iacute;tica y la pol&iacute;tica subnacional en Am&eacute;rica Latina, con atenci&oacute;n a la seguridad p&uacute;blica y la desigualdad racial.",
     "Mi trabajo vivi&oacute; dentro y fuera de la universidad. Fui investigador en el Instituto Igarap&eacute;, trabajando en seguridad p&uacute;blica y espacio c&iacute;vico, y firm&eacute; un informe sobre mujeres defensoras del medio ambiente en Per&uacute;, presentado en la COP28. Tambi&eacute;n trabaj&eacute; en el gobierno federal, donde lider&eacute; la estrategia del Ministerio de Igualdad Racial para la aprobaci&oacute;n de la ley de cuotas en la educaci&oacute;n superior, y coescrib&iacute; cap&iacute;tulos en <em>Rep&uacute;blica em Notas</em>, semifinalista del Premio Jabuti, sobre el sistema de m&eacute;rito del servicio p&uacute;blico.",
     "Desde 2026 me incorporo al CEBRAP, en S&atilde;o Paulo, como investigador posdoctoral. Soy licenciado y mag&iacute;ster en ciencia pol&iacute;tica por la Universidad de Brasilia, y trabajo en portugu&eacute;s, espa&ntilde;ol e ingl&eacute;s.",
  ],
  "research_lead": "Estudio c&oacute;mo el crimen organizado reconfigura la vida pol&iacute;tica. Cuando los grupos armados gobiernan un territorio &mdash; y dictan las reglas de la vida cotidiana de quienes viven all&iacute; &mdash;, tambi&eacute;n cambian qui&eacute;n vota, qui&eacute;n puede postularse, qui&eacute;n gana y qui&eacute;n queda expuesto a la violencia. Trabajo estas preguntas sobre todo en R&iacute;o de Janeiro, con microdatos administrativos georreferenciados.",
  "threads": [
     ("Gobernanza criminal y elecciones", "El peso pol&iacute;tico de un grupo armado depende de cu&aacute;n integrado est&eacute; al sistema pol&iacute;tico, m&aacute;s que de la extensi&oacute;n del territorio que domina. Los grupos integrados construyen v&iacute;nculos duraderos y rec&iacute;procos con partidos y candidatos, y gobiernan a quienes viven bajo ellos como un electorado; los grupos perif&eacute;ricos sostienen el territorio solo por la fuerza. Leer la gobernanza criminal como una cuesti&oacute;n de incorporaci&oacute;n pol&iacute;tica me permite explicar por qu&eacute; grupos con poder territorial parecido mueven las elecciones en direcciones opuestas. Lo formalizo como una tipolog&iacute;a &mdash; gobernanza integrada, perif&eacute;rica e h&iacute;brida &mdash; y la sigo en la participaci&oacute;n electoral, el registro de votantes, la candidatura y qui&eacute;n gana."),
     ("El Estado y el crimen organizado", "El Estado es parte de la infraestructura del orden criminal. Las decisiones formales, sobre todo qui&eacute;n asume el mando de la polic&iacute;a local, redibujan las fronteras del control criminal y alimentan la captura electoral. La actuaci&oacute;n policial es una de las palancas con que el Estado reorganiza el orden que dice combatir, y el discurso penal en el Legislativo le confiere legitimidad."),
     ("Orden, colapso y violencia de g&eacute;nero", "El orden mantiene la violencia bajo control. Cuando una autoridad que gobierna se derrumba &mdash; criminal, policial o h&iacute;brida &mdash;, lo que aflora es la violencia que ven&iacute;a conteniendo. Leer esa violencia exige mantener dos registros a la vez, el institucional y el real, porque bajo gobernanza criminal ambos divergen de forma sistem&aacute;tica, y la distancia entre ellos es, en s&iacute; misma, evidencia de captura. La misma l&oacute;gica atraviesa el g&eacute;nero. El orden armado a la vez contiene y produce la violencia contra las mujeres."),
     ("Raza y violencia pol&iacute;tica", "La violencia pol&iacute;tica en Brasil tiene una gram&aacute;tica racial. Qui&eacute;n se vuelve blanco en la vida pol&iacute;tica, y d&oacute;nde, corre por dos l&iacute;neas que mantengo separadas, la de raza y la de territorio. Muestro tambi&eacute;n c&oacute;mo el discurso parlamentario normaliza la letalidad policial contra los ciudadanos negros."),
     ("Instituciones democr&aacute;ticas y espacio c&iacute;vico", "M&aacute;s all&aacute; del crimen, trabajo con las instituciones de la democracia y con el espacio de la vida c&iacute;vica. Estudi&eacute; el sistema de m&eacute;rito del servicio p&uacute;blico y el clientelismo que lo desgasta, y los movimientos sociales que disputan los l&iacute;mites del espacio c&iacute;vico. Lo que liga esto con mi agenda principal es la captura, la toma de las instituciones p&uacute;blicas por intereses privados."),
  ],
  "groups": {"articles":"Art&iacute;culos en revistas","chapters":"Cap&iacute;tulos de libro","reports":"Informes t&eacute;cnicos","papers":"Working papers y preprints"},
  "writing_lead": "Participo en el debate p&uacute;blico sobre crimen, seguridad, clima y democracia, en art&iacute;culos, en los medios y en audiencias p&uacute;blicas.",
  "writing_groups": {"talks": "Charlas y audiencias p&uacute;blicas", "media": "Entrevistas y medios", "opeds": "Art&iacute;culos de opini&oacute;n"},
  "pubs_label": "publicaciones",
  "map_caption": "Donde vive la poblaci&oacute;n negra en S&atilde;o Paulo, el autob&uacute;s anda m&aacute;s lento. Velocidad del transporte por distrito, cruzada con raza e ingreso. Elaboraci&oacute;n: Igor Novaes Lins.",
  "map_full": "Ver en pantalla completa",
  "consulting": [
     "Soy cient&iacute;fico social y trabajo en el cruce entre la investigaci&oacute;n y la pol&iacute;tica p&uacute;blica. Las organizaciones que trabajan con ciudades, seguridad y desigualdad muchas veces enfrentan preguntas que la evidencia disponible no responde. Ayudo a responderlas con el m&eacute;todo que cada una pide y con una lectura clara de la pol&iacute;tica y las instituciones en juego.",
     "Llevo evidencia cuantitativa y cualitativa al mismo problema &mdash; datos administrativos y de encuesta, entrevistas y trabajo de campo, an&aacute;lisis de discurso y de documentos, y mapas cuando la respuesta es espacial. Cuando el registro oficial es escaso, construyo la base yo mismo, incluso en tiempo real, y busco en ella las desigualdades de raza, ingreso, g&eacute;nero y territorio que los promedios esconden.",
     "Trabajo para que el resultado pueda comprobarse por quien depende de &eacute;l. Documento c&oacute;mo llego a cada conclusi&oacute;n y soy claro sobre lo que la evidencia sostiene y lo que deja abierto.",
     "Trabajo con observatorios, ONG, institutos de investigaci&oacute;n y organismos p&uacute;blicos que necesitan este tipo de evidencia para incidencia y pol&iacute;tica p&uacute;blica. El producto toma la forma que la pregunta exige &mdash; un diagn&oacute;stico, una nota t&eacute;cnica o una s&iacute;ntesis de evidencia, un mapa, una base de datos abierta, un indicador, o la estrategia para llevar una decisi&oacute;n adelante.",
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

def contact_links():
    return "".join('<a href="%s"%s>%s</a>' % (url, ("" if url.startswith("mailto:") else ' rel="me noopener" target="_blank"'), label) for label, url in CONTACTS)

def render_sidebar(lang, page):
    t = T[lang]; home = page_url(lang, "index")
    if HAS_PHOTO:
        photo = '<a href="%s"><img class="portrait" src="/assets/portrait.jpg" alt="%s"></a>' % (home, t["skip_alt"])
    else:
        photo = '<a href="%s"><div class="monogram">IN</div></a>' % home
    navitems = "".join('<a href="%s"%s>%s</a>' % (page_url(lang,p), ' class="active"' if p==page else "", label) for p,label in t["nav"])
    langlinks = ['<a href="%s"%s>%s</a>' % (page_url(l,page), ' class="active"' if l==lang else "", l.upper()) for l in LANGS]
    langrow = "<span>&middot;</span>".join(langlinks)
    contacts = contact_links()
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
    for key, items in pubs_for(lang):
        tagsets = PUB_TAGS.get(key, [])
        lis = ""
        for i, it in enumerate(items):
            idlist = tagsets[i] if i < len(tagsets) else []
            chips = "".join('<a class="tag" href="#%s">%s</a>' % (tid, THEME_TAGS[lang][tid]) for tid in idlist)
            tagblock = '<div class="tags">%s</div>' % chips if chips else ""
            lis += "<li>%s%s</li>" % (it, tagblock)
        out.append('<div class="group"><h3>%s</h3><ol class="list">%s</ol></div>' % (t["groups"][key], lis))
    return "\n".join(out)

def render_main(lang, page):
    t = T[lang]; h1 = t["page_h1"][page]; inner = ""
    if page == "index":
        inner = "".join("<p>%s</p>" % p for p in t["about"])
    elif page == "research":
        inner = '<p class="lead">%s</p>' % t["research_lead"]
        for i, (title, desc) in enumerate(t["threads"]):
            inner += '<div class="group" id="%s"><h3>%s</h3><p>%s</p></div>' % (THEME_IDS[i], title, desc)
        inner += '<h2 class="sub">%s</h2>' % t["pubs_label"]
        inner += render_groups(lang)
    elif page == "writing":
        inner = '<p class="lead">%s</p>' % t["writing_lead"]
        wg = t["writing_groups"]
        inner += '<div class="group"><h3>%s</h3><ol class="list">%s</ol></div>' % (wg["talks"], "".join("<li>%s</li>" % it for it in TALKS[lang]))
        inner += '<div class="group"><h3>%s</h3><ol class="list">%s</ol></div>' % (wg["media"], "".join("<li>%s</li>" % it for it in INTERVIEWS[lang]))
        inner += '<div class="group"><h3>%s</h3><ol class="list">%s</ol></div>' % (wg["opeds"], "".join("<li>%s</li>" % it for it in OPEDS[lang]))
    elif page == "consulting":
        paras = t["consulting"]
        inner = '<p class="lead">%s</p>' % paras[0]
        inner += "".join("<p>%s</p>" % p for p in paras[1:])
    jsonld = render_jsonld(lang) if page == "index" else ""
    kicker = '<p class="kicker">%s</p>\n  ' % t["kicker_index"] if page == "index" else ""
    return """<main>
  %s<h1>%s</h1>
  %s
  <footer><div class="contact-foot">%s</div>%s</footer>
</main>
%s
""" % (kicker, h1, inner, contact_links(), t["footer"], jsonld)

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
    "http://lattes.cnpq.br/1256551333741329",
    "https://www.linkedin.com/in/igornovaeslins",
    "https://github.com/igornovaeslins"
  ]
}
</script>""" % SITE

def render_page(lang, page):
    html = render_head(lang, page) + render_sidebar(lang, page) + render_main(lang, page) + "</body>\n</html>\n"
    return html.replace('href="/style.css"', 'href="/style.css?v=%s"' % CSS_VER)

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
