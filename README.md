# CV LaTeX multi-version

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
