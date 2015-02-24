% CSE/IT 107: Introduction to Programming
% New Mexico Tech
%
% Prepared by Cynthia Veitch, William Kwan, Scott Chadde, Kaley Goatcher,
% Russell White, and Christopher Koch

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cselabheader}
\def\@@ptsize{11pt}
\DeclareOption{10pt}{\def\@@ptsize{10pt}}
\DeclareOption{11pt}{\def\@@ptsize{11pt}}
\DeclareOption{12pt}{\def\@@ptsize{12pt}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[\@@ptsize]{article}

% Allows for bold tele-type
\DeclareFontShape{OT1}{cmtt}{bx}{n}{
  <5><6><7><8><9><10><10.95><12><14.4><17.28><20.74><24.88>cmttb10}{}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{mathpazo}
% AMS math formatting
\usepackage{amsmath,nicefrac}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{textcomp}
\usepackage{IEEEtrantools}
% Indention formatting
\setlength{\parindent}{0.0in}
\setlength{\parskip}{0.04in}

% Margin support
\usepackage[margin=1in]{geometry}
\usepackage{float}
\usepackage{hyperref}

\usepackage{minted}
\usepackage[format=plain,font=small,labelfont=bf]{caption}
\usepackage{wrapfig}
% Header/footer support
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead{}
\fancyhead[L]{CSE/IT 107}

% Color support
\usepackage{color}
\usepackage[dvipsnames]{xcolor}
\definecolor{light-gray}{gray}{0.9}
\definecolor{green}{RGB}{0,127,0}
\definecolor{dred}{rgb}{0.6,0,0}
\definecolor{maroon}{rgb}{0.35,0,0}
\definecolor{dkbrown}{RGB}{92,51,23}
\definecolor{lightgray}{rgb}{0.93,0.93,0.93}
\definecolor{anothergray}{rgb}{0.95,0.95,0.99}
% Outline support
%\usepackage{outlines}
% URL formatting
\usepackage{}\usepackage{url}
% Image/graphic support
\usepackage{graphicx}
% Supports in-document hyperlinks
\usepackage[numbered]{bookmark}
% List compression
\usepackage{mdwlist}
\usepackage{enumerate}
% Support long tables across pages
\usepackage{longtable}
\setlength{\LTcapwidth}{6in}
\usepackage{array}
\usepackage{multirow}
\usepackage{multicol}
% better table formatting
\usepackage{booktabs}
% Supports code formatting/highlighting
\usepackage{listings}

\usepackage{MnSymbol}
\lstdefinestyle{python}{
  language=Python,
  basicstyle=\small\ttfamily,
  frame=single,
  prebreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\rhookswarrow}},
  postbreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\rcurvearrowse\space}}
  breaklines=true,
  breakatwhitespace=true,
  numbers=left,
  numberstyle=\scriptsize,
  morekeywords={True,False},
  identifierstyle=\color{black},
}
\lstset{
  style=python,
  basicstyle=\small\ttfamily,
  keywordstyle=\color{blue},
  stringstyle=\color{Maroon},
  commentstyle=\color{green},
  showstringspaces=false,
  captionpos=b,
}
% interpreted python -- with gray background.
\lstdefinestyle{ipython}{
  backgroundcolor=\color{light-gray},
  language=Python,
  basicstyle=\small\ttfamily,
  frame=single,
  prebreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\rhookswarrow}},
  postbreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\rcurvearrowse\space}}
  breaklines=true,
  breakatwhitespace=true,
  numbers=left,
  numberstyle=\scriptsize,
  morekeywords={True,False},
  identifierstyle=\color{black},
}
\lstdefinestyle{bash}{
  language=bash,
  basicstyle=\small\ttfamily,
  identifierstyle=,
  keywordstyle=,
  backgroundcolor=\color{light-gray}
}

% I wanted bash to have the breaklines stuff, too, but the typesetting is having
% problems with my prebreak and postbreak symbols and boxes. I have to
% investigate (it always worked in the C labs..) -Chris
\lstdefinestyle{c}{
  language=C,
  basicstyle=\small\ttfamily,
  frame=single,
  prebreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\rhookswarrow}},
  postbreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\rcurvearrowse\space}}
  breaklines=true,
  breakatwhitespace=true,
  numbers=left,
  numberstyle=\scriptsize
}

% caption formatting
\usepackage[toc,page]{appendix}
\usepackage{tikz}
\usetikzlibrary{trees}


\usemintedstyle{tango} % friendly, colorful
\newminted{python3}{fontsize=\small,
  mathescape,linenos,numbersep=5pt,frame=single,framesep=2mm,autogobble}
\newminted{pycon}{fontsize=\small,
  mathescape,linenos,numbersep=5pt,frame=single,framesep=2mm,python3,autogobble}
\newminted[bashcode]{console}{fontsize=\small,autogobble,
  mathescape,linenos,numbersep=5pt,framesep=2mm,frame=lines,bgcolor=lightgray}
\newminted[verbatimcode]{text}{fontsize=\small,autogobble,
  mathescape,linenos,numbersep=5pt,framesep=2mm,frame=lines,bgcolor=lightgray}
\newmintinline{python}{mathescape}
\newmintinline{bash}{mathescape}
\newmintinline{pycon}{python3,mathescape}

\usepackage{mdframed}

\newenvironment{warningbox}[1]{
  \mdfsetup{%
    frametitle={%
      \tikz[baseline=(current bounding box.east),outer sep=0pt]
      \node[anchor=east,rectangle,fill=red!20]
           {\strut #1};}}
  \mdfsetup{innertopmargin=10pt, linecolor=red!20, linewidth=2pt, topline=true,
    frametitleaboveskip=\dimexpr-\ht\strutbox\relax,}
  \begin{mdframed}[]\relax
}{\end{mdframed}}

\newenvironment{infobox}[1]{
  \mdfsetup{%
    frametitle={%
      \tikz[baseline=(current bounding box.east),outer sep=0pt]
      \node[anchor=east,rectangle,fill=green!20]
           {\strut #1};}}
  \mdfsetup{innertopmargin=10pt, linecolor=green!20, linewidth=2pt, topline=true,
    frametitleaboveskip=\dimexpr-\ht\strutbox\relax,}
  \begin{mdframed}[]\relax
}{\end{mdframed}}

\usepackage{amsmath} % MATH

\usepackage{amsthm, thmtools}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{mathtools} % matrix alignment
\usepackage{dsfont}
\usepackage{IEEEtrantools} % nice equations

\theoremstyle{definition}
\declaretheoremstyle[
  headfont=\color{maroon}\sffamily\bfseries,
  notebraces={(}{)},
  notefont=\mdseries,
  bodyfont=\normalfont,
  headpunct={.},
  postheadspace=\newline,
  spacebelow=\parsep,
  spaceabove=\parsep,
  headindent=0pt,
  mdframed={
    %linecolor=black,
    %backgroundcolor=black!20,
    topline=false,
    rightline=false,
    leftline=false,
    bottomline=false,
    backgroundcolor=anothergray,
    innertopmargin=7pt,
    innerrightmargin=10pt,
    innerleftmargin=10pt,
    innerbottommargin=7pt,
    skipabove=\parsep,
    skipbelow=\parsep
  }
]{exercises}
\declaretheorem[style=exercises,name=Exercise,refname={exercise,exercises},Refname={Exercise,Exercises},numberwithin=section]{ex}
\renewcommand{\listtheoremname}{List of Files to Submit}
\declaretheorem[style=exercises,name=Problem,refname={problem,problems},Refname={Problem,Problems}]{prob}

%\makeatletter
%\AtBeginEnvironment{ex}{%
%  \patchcmd\@ex
%    {\trivlist}
%    {\list{}{\leftmargin2.5em\itemindent-5em}}
%    {}{}%
%  \patchcmd\thmt@original@endex{\endtrivlist}{\endlist}{}{}%
%}
%\makeatother

\usepackage{bm}

\setlength{\itemsep}{0in}

\def\Version#1{\def\version{#1}}

\author{CSE/IT 107}
\date{NMT Department of Computer Science and Engineering}

\hypersetup{hidelinks}
