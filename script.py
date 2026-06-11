from pathlib import Path
base = Path('output/cv_github_final')
for p in [base/'content', base/'style', base/'.github/workflows', base/'assets/logos', base/'build']:
    p.mkdir(parents=True, exist_ok=True)

files = {
'latexmkrc': r'''$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$pdf_mode = 1;
$out_dir = 'build';
''',
'.gitignore': r'''build/
*.aux
*.log
*.out
*.toc
*.fls
*.fdb_latexmk
*.synctex.gz
''',
'README.md': r'''# CV LaTeX multi-version

Build locally:
```bash
latexmk -pdf main.tex
```

Build variants:
```bash
latexmk -pdf -jobname=cv-fr-exec "\def\Lang{fr}\def\Mode{exec}\input{main.tex}"
latexmk -pdf -jobname=cv-fr-op "\def\Lang{fr}\def\Mode{op}\input{main.tex}"
latexmk -pdf -jobname=cv-en-exec "\def\Lang{en}\def\Mode{exec}\input{main.tex}"
latexmk -pdf -jobname=cv-en-op "\def\Lang{en}\def\Mode{op}\input{main.tex}"
```
''',
'main.tex': r'''\documentclass[11pt,a4paper]{article}
\def\Lang{fr}
\def\Mode{exec}
\input{style/preamble}
\begin{document}
\input{style/header}
\input{content/body}
\end{document}
''',
'style/preamble.tex': r'''\usepackage[a4paper,margin=1.15cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[french,english]{babel}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{fontawesome5}
\usepackage{enumitem}
\usepackage{tabularx}
\usepackage{array}
\usepackage{titlesec}
\usepackage{hyperref}
\usepackage{ifthen}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\definecolor{primary}{HTML}{214D3A}
\definecolor{secondary}{HTML}{6B8F71}
\definecolor{light}{HTML}{F4F7F4}
\definecolor{text}{HTML}{1F1F1F}
\hypersetup{colorlinks=true,urlcolor=primary,linkcolor=primary}
\titleformat{\section}{\Large\bfseries\color{primary}}{}{0pt}{}[\vspace{-0.4em}\titlerule]
\titlespacing*{\section}{0pt}{0.8em}{0.35em}
\newcommand{\cvsub}[1]{\textit{\color{secondary}#1}}
\newcommand{\entry}[4]{\textbf{#1} \hfill #2\\#3\\\textit{#4}\vspace{0.2em}}
\newcommand{\entrytwo}[4]{\textbf{#1} \hfill #2\\#3\\#4\vspace{0.2em}}
\newcommand{\contact}[3]{\faEnvelope~\href{mailto:#1}{#1}\hspace{1em}\faPhone~#2\hspace{1em}\faMapMarker*~#3}
\newcommand{\Fr}[1]{\ifthenelse{\equal{\Lang}{fr}}{#1}{}}
\newcommand{\En}[1]{\ifthenelse{\equal{\Lang}{en}}{#1}{}}
\newcommand{\Exec}[1]{\ifthenelse{\equal{\Mode}{exec}}{#1}{}}
\newcommand{\Op}[1]{\ifthenelse{\equal{\Mode}{op}}{#1}{}}
''',
'style/header.tex': r'''\begin{center}
{\Huge\bfseries\color{primary} Bastien Grand}\\
{\large\cvsub{\Fr{Leader des opérations et de l’ingénierie}\En{Operations and engineering leader}}}\\[0.4em]
\contact{Bastien.Grand@swissgrid.ch}{+41 79 276 37 81}{Sion, Valais, CH}
\end{center}
\vspace{0.3em}
''',
'content/body.tex': r'''\section*{\Fr{Profil}\En{Profile}}
\Exec{\Fr{Leader dans les opérations système et l’ingénierie, j’évolue dans des environnements complexes où la qualité de l’exécution, la coordination transverse et la prise de décision rapide sont essentielles. Mon parcours m’a amené à structurer des équipes, conduire des améliorations organisationnelles et contribuer à des sujets stratégiques à l’interface entre technologie, performance et gouvernance.}\En{Leader in system operations and engineering, I work in complex environments where execution quality, cross-functional coordination, and fast decision-making are essential. My background combines team leadership, organizational improvement, and strategic contribution at the intersection of technology, performance, and governance.}}
\Op{\Fr{Leader opérationnel avec une solide base d’ingénierie, je transforme des contextes complexes en décisions claires, en équipes alignées et en résultats mesurables. Mon parcours combine excellence technique, pilotage d’équipes et contribution à des enjeux de transformation et de performance.}\En{An operations leader with a strong engineering foundation, I turn complex environments into clear decisions, aligned teams, and measurable outcomes. My background combines technical excellence, team leadership, and contribution to transformation and performance initiatives.}}

\section*{\Fr{Expérience}\En{Experience}}
\entry{Swissgrid --- Head of System Operations}{2023 -- aujourd'hui}{\Fr{Responsable des opérations système et de la coordination transverse sur des activités critiques. Pilotage d’équipes et contribution à l’évolution des processus, de l’organisation et des priorités opérationnelles.}{Leadership, transformation, gouvernance}\En{Responsible for system operations and cross-functional coordination in critical activities. Led teams and contributed to process evolution, organizational design, and operational priorities.}{Leadership, transformation, governance}}
\entry{Swissgrid --- Head of Team System Operations}{2018 -- 2023}{\Fr{Constitution et développement d’équipes spécialisées; structuration de processus clés et amélioration de la performance opérationnelle; contribution à la stratégie et à la vision future de l’organisation.}{Management, structuration, performance}\En{Built and developed specialist teams; structured key processes and improved operational performance; contributed to strategy and the organization’s future vision.}{Management, structuring, performance}}
\entry{Alpiq / Swissgrid --- Deputy Head of Dispatching Center}{2012 -- 2018}{\Fr{Coordination d’équipes dans des environnements temps réel; gestion de transitions organisationnelles sensibles; contribution au renforcement des capacités internes et à la montée en compétence des équipes.}{Execution, continuity, scaling}\En{Coordinated teams in real-time environments; managed sensitive organizational transitions; contributed to capability building and team development.}{Execution, continuity, scaling}}
\entry{EOS / Alpiq --- Operations Engineer / System Operator}{2008 -- 2012}{\Fr{Expérience fondatrice au contact direct de la sûreté système. Prise de décision sous contrainte et gestion de situations critiques.}{Sûreté, décisions critiques}\En{Foundational experience in direct contact with system security. Decision-making under pressure and handling critical situations.}{Security, critical decisions}}

\section*{\Fr{Formation}\En{Education}}
\entrytwo{HEIA Fribourg}{2004 -- 2007}{\Fr{Diplôme d’ingénieur électricien.}\En{Electrical engineering diploma.}}{\Fr{Base technique}\En{Technical foundation}}
\entrytwo{Université de Saint-Gall}{2020 -- 2021}{\Fr{Leadership et management.}\En{Leadership and management.}}{\Fr{Développement managérial}\En{Managerial development}}

\section*{\Fr{Compétences}\En{Skills}}
\Fr{Pilotage d’équipes • opérations système • coordination transverse • gestion de crise • amélioration continue • communication avec parties prenantes • Python • VBA • anglais C1 • allemand C1 • français natif}
\En{Team leadership • system operations • cross-functional coordination • crisis management • continuous improvement • stakeholder communication • Python • VBA • English C1 • German C1 • native French}
''',
'.github/workflows/build.yml': r'''name: build-cv

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          - jobname: cv-fr-exec
            def_lang: '\\def\\Lang{fr}\\def\\Mode{exec}'
          - jobname: cv-fr-op
            def_lang: '\\def\\Lang{fr}\\def\\Mode{op}'
          - jobname: cv-en-exec
            def_lang: '\\def\\Lang{en}\\def\\Mode{exec}'
          - jobname: cv-en-op
            def_lang: '\\def\\Lang{en}\\def\\Mode{op}'
    steps:
      - uses: actions/checkout@v4
      - uses: xu-cheng/latex-action@v3
        with:
          root_file: main.tex
          pre_compile: |
            sed -i "1i${{ matrix.def_lang }}" main.tex
          args: -pdf -jobname=${{ matrix.jobname }} -interaction=nonstopmode -halt-on-error -file-line-error
      - uses: actions/upload-artifact@v4
        with:
          name: ${{ matrix.jobname }}
          path: build/${{ matrix.jobname }}.pdf
'''
}
for rel, content in files.items():
    p = base / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

print(base)
print('done')