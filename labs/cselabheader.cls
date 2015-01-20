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
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{textcomp}
\usepackage{IEEEtrantools}
% Indention formatting
\setlength{\parindent}{0.0in}
\setlength{\parskip}{0.05in}


% Margin support
\usepackage[margin=1in]{geometry}

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
\definecolor{dkbrown}{RGB}{92,51,23}
\definecolor{lightgray}{rgb}{0.96,0.96,0.96}
% Outline support
%\usepackage{outlines}
% URL formatting
\usepackage{}\usepackage{url}
% Image/graphic support
\usepackage{graphicx}
% Supports in-document hyperlinks
\usepackage[hidelinks,pdfborder=0in,bookmarks=true]{hyperref}
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
\usepackage[format=plain,font=small,labelfont=bf]{caption}
\usepackage[toc,page]{appendix}
\usepackage{tikz}
\usetikzlibrary{trees}

\usepackage{minted}

\usemintedstyle{tango} % friendly, colorful
\newminted{python3}{fontsize=\small,
  mathescape,linenos,numbersep=5pt,frame=single,framesep=2mm}
\newminted{pycon}{fontsize=\small,
  mathescape,linenos,numbersep=5pt,frame=single,framesep=2mm,python3}
\newminted[bashcode]{console}{fontsize=\small,
  mathescape,linenos,numbersep=5pt,framesep=2mm,frame=lines,bgcolor=lightgray}
\newminted[verbatimcode]{html}{fontsize=\small,
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

\def\Version#1{\def\version{#1}}

\author{CSE/IT 107}
\date{NMT Computer Science}

