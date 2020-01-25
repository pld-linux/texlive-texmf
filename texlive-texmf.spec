# TODO:
# - unpackaged-files in CVS tree, please use this!
# - latex subpackage (maybe rename latex-base and texlive-latex requires latex-base)
# - maybe tex4ht-data splitting

# Conditional build:
%bcond_with	bootstrap	# bootstrap build

%define		shortname	texlive
%define		year		2013
%define		monthday	0530

Summary:	TeX typesetting system and MetaFont font formatter
Summary(de.UTF-8):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(es.UTF-8):	Sistema de typesetting TeX y formateador de fuentes MetaFont
Summary(fr.UTF-8):	Systéme de compostion TeX et formatteur de MetaFontes
Summary(hu.UTF-8):	TeX szövegszedő rendszer és MetaFont font formázó
Summary(pl.UTF-8):	System składu publikacji TeX oraz formater fontów MetaFont
Summary(pt_BR.UTF-8):	Sistema de typesetting TeX e formatador de fontes MetaFont
Summary(tr.UTF-8):	TeX dizgi sistemi ve MetaFont yazıtipi biçimlendiricisi
Name:		texlive-texmf
Version:	%{year}%{monthday}
Release:	0.1.mf
Epoch:		1
License:	distributable
Group:		Applications/Publishing/TeX
Source0:	ftp://tug.org/texlive/historic/%{year}/texlive-%{version}-texmf.tar.xz
# Source0-md5:	a66ff4d09727af68a5368dddf297cbcb
URL:		http://www.tug.org/texlive/
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
%if %{without bootstrap}
### BuildRequires:	%{shortname}-context
### BuildRequires:	%{shortname}-csplain
### BuildRequires:	%{shortname}-fonts-cmsuper
### BuildRequires:	%{shortname}-format-eplain
### BuildRequires:	%{shortname}-format-mex
### BuildRequires:	%{shortname}-format-pdflatex
### BuildRequires:	%{shortname}-latex
### BuildRequires:	%{shortname}-latex-ams
### BuildRequires:	%{shortname}-latex-cyrillic
### BuildRequires:	%{shortname}-latex-extend
### BuildRequires:	%{shortname}-latex-wasysym
### BuildRequires:	%{shortname}-metapost
### BuildRequires:	%{shortname}-mex
### BuildRequires:	%{shortname}-omega
### BuildRequires:	%{shortname}-other-utils
### BuildRequires:	%{shortname}-pdftex
### BuildRequires:	%{shortname}-phyzzx
### BuildRequires:	%{shortname}-plain
### BuildRequires:	%{shortname}-tex-babel
### BuildRequires:	%{shortname}-tex-physe
### BuildRequires:	%{shortname}-xetex
### BuildRequires:	%{shortname}-xmltex
### BuildRequires:	/usr/bin/latex
%endif
BuildRequires:	unzip
Requires:	%{shortname}-dirs-fonts
Requires:	%{shortname}-fonts-cm
Requires:	%{shortname}-fonts-misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texmf	%{_datadir}/texmf
%define		texmfdist %{texmf}-dist
%define		texmfdoc %{texmf}-doc
%define		fmtdir	/var/lib/texmf/web2c
%define		texhash	umask 022; [ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2;
%define		_localstatedir	/var/lib/texmf
%define		fixinfodir [ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 ;
%define		fmtutil(f:) [ ! \\\( -f %{_localstatedir}/web2c/%{-f*}.fmt.rpmnew -o -f %{_localstatedir}/web2c/%{-f*}.efmt.rpmnew \\\) ] || %{_bindir}/fmtutil-sys --byfmt %{-f*} >/dev/null 2>/dev/null || echo "Regenerating %{-f*} failed. See %{_localstatedir}/web2c/%{-f*}.log for details" 1>&2 && exit 0 ;

%define		_noautoreq 'perl(path_tre)'

%description
TeXLive is an implementation of TeX for Linux or UNIX systems. TeX
takes a text file and a set of formatting commands as input and
creates a typesetter independent .dvi (DeVice Independent) file as
output. Usually, TeX is used in conjunction with a higher level
formatting package like LaTeX or PlainTeX, since TeX by itself is not
very user-friendly.

%description -l es.UTF-8
Tex formata archivos de texto y órdenes para una salida independiente
de dispositivo (que se llama DVI - DeVice Independent). En The TeXbook
de Knut se describen las capacidades y el lenguaje TeX.

%description -l de.UTF-8
TeX formatiert eine Datei, die abwechselnd Text und Befehle enthält
und gibt eine geräteunabhängige Datei aus (DVI genannt, Abk. für
DeVice Independent). Die Funktionen und Sprache von TeX werden in The
TeXbook von Knuth beschrieben.

%description -l fr.UTF-8
TeX formate un fichier de commandes et de texte mélandés, et produit
un fichier de indépendant de toute plate-forme (appelé DVI, qui est un
raccourci pour Device Independant). Les possibilités de TeX et son
langage sont décrites dans l'ouvrage TeXbook, de Knuth.

%description -l hu.UTF-8
TeXLive a TeX egy implementációja Linux és UNIX rendszerekre. TeX egy
egyszerű szövegfájlt fogad bemenetként, és formázó parancsok
segítségével a szövegszedő egy független .dvi (DeVice Independent)
fájlt készít. A TeX-et leginkább magasabb szintű formázó parancsokkal
kiegészítve használják, mint pl. LaTeX-hel vagy PlainTeX-hel, mivel a
TeX önmaga nem túlzottan "felhasználóbarát".

%description -l pl.UTF-8
TeX formatuje przygotowany tekst oraz komendy i produkuje niezależny
od urządzenia plik wynikowy (tzw. DVI -- skrót od DeVice Independent).
Możliwości TeXa, oraz jego język zostały opisane w ,,The TeXbook''
Donalda E. Knutha.

%description -l pt_BR.UTF-8
Tex formata arquivos de texto e comandos para uma saída independente
de dispositivo (chamado DVI - DeVice Independent). As capacidades e a
linguagem TeX são descritas no The TeXbook, de Knuth.

%description -l tr.UTF-8
TeX, içinde metin ve komutların yer aldığı bir dosyayı okur ve dizgi
aygıtından bağımsız bir çıktı (DeVice Independent - DVI) oluşturur.
TeX'in becerileri ve dizgi dili, dili geliştiren Knuth'un 'The
TeXbook' başlıklı kitabında anlatılmaktadır.

%package -n texlive-dirs-fonts
Summary:	TeX font directories
Summary(pl.UTF-8):	Katalogi fontów TeXa
Group:		Fonts
Provides:	tetex-dirs-fonts
Obsoletes:	tetex-dirs-fonts

%description -n texlive-dirs-fonts
TeX font directories.

%description -n texlive-dirs-fonts -l pl.UTF-8
Katalogi fontów TeXa.

%package -n texlive-doc
Summary:	Documentation for TeX Live
Group:		Documentation

%description -n texlive-doc
Assorted useful documentation for TeX Live.

%package -n texlive-doc-knuth
Summary:	Knuth's documentation
Group:		Documentation

%description -n texlive-doc-knuth
Knuth's documentation.

%package -n texlive-doc-bg
Summary:	Bulgarian documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-bg
Assorted useful Bulgarian documentation for TeX Live.

%package -n texlive-doc-cs
Summary:	Czech documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-cs
Assorted useful Czech documentation for TeX Live.

%package -n texlive-doc-de
Summary:	German documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-de
Assorted useful German documentation for TeX Live.

%package -n texlive-doc-el
Summary:	Greek documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-el
Assorted useful Greek documentation for TeX Live.

%package -n texlive-doc-es
Summary:	Spanish documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-es
Assorted useful Spanish documentation for TeX Live.

%package -n texlive-doc-fi
Summary:	Finnish documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-fi
Assorted useful Finnish documentation for TeX Live.

%package -n texlive-doc-fr
Summary:	French documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-fr
Assorted useful French documentation for TeX Live.

%package -n texlive-doc-it
Summary:	Italian documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-it
Assorted useful Italian documentation for TeX Live.

%package -n texlive-doc-ja
Summary:	Japanese documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-ja
Assorted useful Japanese documentation for TeX Live.

%package -n texlive-doc-ko
Summary:	Korean documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-ko
Assorted useful Korean documentation for TeX Live.

%package -n texlive-doc-mn
Summary:	Mongolian documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-mn
Assorted useful Mongolian documentation for TeX Live.

%package -n texlive-doc-nl
Summary:	Dutch documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-nl
Assorted useful Dutch documentation for TeX Live.

%package -n texlive-doc-pl
Summary:	Polish documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-pl
Assorted useful Polish documentation for TeX Live.

%package -n texlive-doc-pt
Summary:	Portuguese documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-pt
Assorted useful Portuguese documentation for TeX Live.

%package -n texlive-doc-ru
Summary:	Russian documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-ru
Assorted useful Russian documentation for TeX Live.

%package -n texlive-doc-sk
Summary:	Slovak documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-sk
Assorted useful Slovak documentation for TeX Live.

%package -n texlive-doc-sl
Summary:	Slovenian documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-sl
Assorted useful Slovenian documentation for TeX Live.

%package -n texlive-doc-th
Summary:	Thai documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-th
Assorted useful Thai documentation for TeX Live.

%package -n texlive-doc-tr
Summary:	Turkish documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-tr
Assorted useful Turkish documentation for TeX Live.

%package -n texlive-doc-uk
Summary:	Ukrainian documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-uk
Assorted useful Ukrainian documentation for TeX Live.

%package -n texlive-doc-vi
Summary:	Vietnamese documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-vi
Assorted useful Vietnamese documentation for TeX Live.

%package -n texlive-doc-zh_CN
Summary:	Chinese documentation for TeX Live
Group:		Documentation

%description -n texlive-doc-zh_CN
Assorted useful Chinese documentation for TeX Live.

%package -n texlive-doc-latex
Summary:	Basic LaTeX packages documentation
Summary(hu.UTF-8):	Az alap LaTeX csomagok dokumentációja
Summary(pl.UTF-8):	Podstawowa dokumentacja do pakietów LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-doc-latex

%description -n texlive-doc-latex
Basic LaTeX packages documentation.

%description -n texlive-doc-latex -l hu.UTF-8
Az alap LaTeX csomagok dokumentációja

%description -n texlive-doc-latex -l pl.UTF-8
Podstawowa dokumentacja do pakietów LaTeXa.

%package -n texlive-jadetex
Summary:	LaTeX macros for converting Jade TeX output into DVI/PS/PDF
Summary(pl.UTF-8):	Makra LaTeXa do konwersji Jade TeXa do DVI/PS/PDF
Group:		Applications/Publishing/TeX
Requires:	%{shortname} = %{epoch}:%{version}-%{release}
Requires:	%{shortname}-latex = %{epoch}:%{version}-%{release}
Requires:	%{shortname}-pdftex = %{epoch}:%{version}-%{release}
Provides:	jadetex = %{epoch}:%{version}-%{release}
Obsoletes:	jadetex

%description -n texlive-jadetex
JadeTeX contains the additional LaTeX macros necessary for taking Jade
TeX output files and processing them as LaTeX files.

%description -n texlive-jadetex -l pl.UTF-8
JadeTeX zawiera dodatkowe makra LaTeXa potrzebne do konwersji plików
otrzymanych z Jade TeXa i przetworzenia ich jako plików LaTeXa.

%package -n texlive-tex4ht-data
Summary:	Fonts and other datas to tex4ht
Group:		Applications/Publishing/TeX

%description -n texlive-tex4ht-data
Fonts and other datas to tex4ht.

%package -n texlive-xetex-data
Summary:	Files for xetex/xelatex
Group:		Applications/Publishing/TeX

%description -n texlive-xetex-data
Files for xetex/xelatex.

%package -n texlive-tex-arrayjob
Summary:	Array data structures for (La)TeX
Summary(hu.UTF-8):	Tömb adatstruktúra (La)TeX-hez
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-arrayjob
Array data structures for (La)TeX.

%description -n texlive-tex-arrayjob -l hu.UTF-8
Tömb adatstruktúra (La)TeX-hez.

%package -n texlive-tex-mathdots
Summary:	Commands to produce dots in math that respect font size
Summary(hu.UTF-8):	Pontok előállítása matematikai módban a font méret figyelmbevételével
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-mathdots
Commands to produce dots in math that respect font size.

%description -n texlive-tex-mathdots -l hu.UTF-8
Pontok előállítása matematikai módban a font méret figyelmbevételével.

%package -n texlive-tex-midnight
Summary:	A set of useful macro tools
Summary(hu.UTF-8):	Hasznos makrók gyűjteménye
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-midnight
A set of useful macro tools.

%description -n texlive-tex-midnight -l hu.UTF-8
Hasznos makrók gyűjteménye.

%package -n texlive-tex-kastrup
Summary:	Convert numbers into binary, octal and hexadecimal
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-kastrup
Convert numbers into binary, octal and hexadecimal.

%package -n texlive-tex-ofs
Summary:	Olsak's Font System
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-ofs
Olsak's Font System.

%package -n texlive-tex-physe
Summary:	The PHYSE format
Summary(hu.UTF-8):	PHYSE formátum
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-physe
The PHYSE format.

%description -n texlive-tex-physe -l hu.UTF-8
PHYSE formátum.

%package -n texlive-phyzzx
Summary:        A TeX format for physicists
Summary(hu.UTF-8):      TeX formátum fizikusoknak
Group:          Applications/Publishing/TeX
Requires(post,postun):  %{_bindir}/texhash
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n texlive-phyzzx
A TeX format for physicists.

%description -n texlive-phyzzx -l hu.UTF-8
TeX formátum fizikusoknak.


%package -n texlive-tex-velthuis
Summary:	This package provides support for typesetting texts in Devanagari script (Sanskrit and Hindi)
Summary(hu.UTF-8):	Ezzel a csomaggal lehetőséged nyílik Devanagari szövegek szedésére (Sanskrit és Hindi)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-velthuis
This package provides support for typesetting texts in Devanagari
script (Sanskrit and Hindi).

%description -n texlive-tex-velthuis -l hu.UTF-8
Ezzel a csomaggal lehetőséged nyílik Devanagari szövegek szedésére
(Sanskrit és Hindi).

%package -n texlive-tex-ytex
Summary:	Macro package developed at MIT
Summary(hu.UTF-8):	MIT-en fejlesztett makrócsomag
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-ytex
Macro package developed at MIT.

%description -n texlive-tex-ytex -l hu.UTF-8
MIT-en fejlesztett makrócsomag.

%package -n texlive-makeindex-data
Summary:	Texmf files needed for texlive-makeindex
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-makeindex-data
Texmf files needed for texlive-makeindex.

%package -n texlive-metapost-data
Summary:	Texmf files needed for texlive-metapost
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Provides:	texlive-metapost-other
Obsoletes:	texlive-metapost-other

%description -n texlive-metapost-data
Texmf files needed for texlive-metapost.

%package -n xindy-data
Summary:	Xindy data files
Group:		Applications/Publishing/TeX

%description -n xindy-data
Xindy data files.

%package -n xindy-albanian
Summary:	Xindy albanian language
Summary(hu.UTF-8):	Xindy albán nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-albanian
Xindy albanian language

%description -n xindy-albanian -l hu.UTF-8
Xindy albán nyelv

%package -n xindy-belarusian
Summary:	Xindy belarusian language
Summary(hu.UTF-8):	Xindy belorusz nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-belarusian
Xindy belarusian language

%description -n xindy-belarusian -l hu.UTF-8
Xindy belorusz nyelv

%package -n xindy-bulgarian
Summary:	Xindy bulgarian language
Summary(hu.UTF-8):	Xindy bolgár nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-bulgarian
Xindy bulgarian language

%description -n xindy-bulgarian -l hu.UTF-8
Xindy bolgár nyelv

%package -n xindy-croatian
Summary:	Xindy croatian language
Summary(hu.UTF-8):	Xindy horvát nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-croatian
Xindy croatian language

%description -n xindy-croatian -l hu.UTF-8
Xindy horvát nyelv

%package -n xindy-czech
Summary:	Xindy czech language
Summary(hu.UTF-8):	Xindy cseh nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-czech
Xindy czech language

%description -n xindy-czech -l hu.UTF-8
Xindy cseh nyelv

%package -n xindy-danish
Summary:	Xindy danish language
Summary(hu.UTF-8):	Xindy dán nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-danish
Xindy danish language

%description -n xindy-danish -l hu.UTF-8
Xindy dán nyelv

%package -n xindy-dutch
Summary:	Xindy dutch language
Summary(hu.UTF-8):	Xindy holland nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-dutch
Xindy dutch language

%description -n xindy-dutch -l hu.UTF-8
Xindy holland nyelv

%package -n xindy-english
Summary:	Xindy english language
Summary(hu.UTF-8):	Xindy angol nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-english
Xindy english language

%description -n xindy-english -l hu.UTF-8
Xindy angol nyelv

%package -n xindy-esperanto
Summary:	Xindy esperanto language
Summary(hu.UTF-8):	Xindy eszperantó nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-esperanto
Xindy esperanto language

%description -n xindy-esperanto -l hu.UTF-8
Xindy eszperantó nyelv

%package -n xindy-estonian
Summary:	Xindy estonian language
Summary(hu.UTF-8):	Xindy észt nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-estonian
Xindy estonian language

%description -n xindy-estonian -l hu.UTF-8
Xindy észt nyelv

%package -n xindy-finnish
Summary:	Xindy finnish language
Summary(hu.UTF-8):	Xindy finn nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-finnish
Xindy finnish language

%description -n xindy-finnish -l hu.UTF-8
Xindy finn nyelv

%package -n xindy-french
Summary:	Xindy french language
Summary(hu.UTF-8):	Xindy francia nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-french
Xindy french language

%description -n xindy-french -l hu.UTF-8
Xindy francia nyelv

%package -n xindy-general
Summary:	Xindy general language
Summary(hu.UTF-8):	Xindy általános nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-general
Xindy general language

%description -n xindy-general -l hu.UTF-8
Xindy általános nyelv

%package -n xindy-georgian
Summary:	Xindy georgian language
Summary(hu.UTF-8):	Xindy georgian nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-georgian
Xindy georgian language

%description -n xindy-georgian -l hu.UTF-8
Xindy georgian nyelv

%package -n xindy-german
Summary:	Xindy german language
Summary(hu.UTF-8):	Xindy német nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-german
Xindy german language

%description -n xindy-german -l hu.UTF-8
Xindy német nyelv

%package -n xindy-greek
Summary:	Xindy greek language
Summary(hu.UTF-8):	Xindy görög nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-greek
Xindy greek language

%description -n xindy-greek -l hu.UTF-8
Xindy görög nyelv

%package -n xindy-gypsy
Summary:	Xindy gypsy language
Summary(hu.UTF-8):	Xindy cigány nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-gypsy
Xindy gypsy language

%description -n xindy-gypsy -l hu.UTF-8
Xindy cigány nyelv

%package -n xindy-hausa
Summary:	Xindy hausa language
Summary(hu.UTF-8):	Xindy hausa nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-hausa
Xindy hausa language

%description -n xindy-hausa -l hu.UTF-8
Xindy hausa nyelv

%package -n xindy-hebrew
Summary:	Xindy hebrew language
Summary(hu.UTF-8):	Xindy héber nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-hebrew
Xindy hebrew language

%description -n xindy-hebrew -l hu.UTF-8
Xindy héber nyelv

%package -n xindy-hungarian
Summary:	Xindy hungarian language
Summary(hu.UTF-8):	Xindy magyar nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-hungarian
Xindy hungarian language

%description -n xindy-hungarian -l hu.UTF-8
Xindy magyar nyelv

%package -n xindy-icelandic
Summary:	Xindy icelandic language
Summary(hu.UTF-8):	Xindy izlandi nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-icelandic
Xindy icelandic language

%description -n xindy-icelandic -l hu.UTF-8
Xindy izlandi nyelv

%package -n xindy-italian
Summary:	Xindy italian language
Summary(hu.UTF-8):	Xindy olasz nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-italian
Xindy italian language

%description -n xindy-italian -l hu.UTF-8
Xindy olasz nyelv

%package -n xindy-klingon
Summary:	Xindy klingon language
Summary(hu.UTF-8):	Xindy klingon nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-klingon
Xindy klingon language

%description -n xindy-klingon -l hu.UTF-8
Xindy klingon nyelv

%package -n xindy-kurdish
Summary:	Xindy kurdish language
Summary(hu.UTF-8):	Xindy kurd nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-kurdish
Xindy kurdish language

%description -n xindy-kurdish -l hu.UTF-8
Xindy kurd nyelv

%package -n xindy-latin
Summary:	Xindy latin language
Summary(hu.UTF-8):	Xindy latin nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-latin
Xindy latin language

%description -n xindy-latin -l hu.UTF-8
Xindy latin nyelv

%package -n xindy-latvian
Summary:	Xindy latvian language
Summary(hu.UTF-8):	Xindy lett nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-latvian
Xindy latvian language

%description -n xindy-latvian -l hu.UTF-8
Xindy lett nyelv

%package -n xindy-lithuanian
Summary:	Xindy lithuanian language
Summary(hu.UTF-8):	Xindy litván nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-lithuanian
Xindy lithuanian language

%description -n xindy-lithuanian -l hu.UTF-8
Xindy litván nyelv

%package -n xindy-lower-sorbian
Summary:	Xindy lower-sorbian language
Summary(hu.UTF-8):	Xindy lower-sorbian nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-lower-sorbian
Xindy lower-sorbian language

%description -n xindy-lower-sorbian -l hu.UTF-8
Xindy lower-sorbian nyelv

%package -n xindy-macedonian
Summary:	Xindy macedonian language
Summary(hu.UTF-8):	Xindy macedón nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-macedonian
Xindy macedonian language

%description -n xindy-macedonian -l hu.UTF-8
Xindy macedón nyelv

%package -n xindy-mongolian
Summary:	Xindy mongolian language
Summary(hu.UTF-8):	Xindy mongol nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-mongolian
Xindy mongolian language

%description -n xindy-mongolian -l hu.UTF-8
Xindy mongol nyelv

%package -n xindy-norwegian
Summary:	Xindy norwegian language
Summary(hu.UTF-8):	Xindy norvég nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-norwegian
Xindy norwegian language

%description -n xindy-norwegian -l hu.UTF-8
Xindy norvég nyelv

%package -n xindy-polish
Summary:	Xindy polish language
Summary(hu.UTF-8):	Xindy lengyel nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-polish
Xindy polish language

%description -n xindy-polish -l hu.UTF-8
Xindy lengyel nyelv

%package -n xindy-portuguese
Summary:	Xindy portuguese language
Summary(hu.UTF-8):	Xindy portugál nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-portuguese
Xindy portuguese language

%description -n xindy-portuguese -l hu.UTF-8
Xindy portugál nyelv

%package -n xindy-romanian
Summary:	Xindy romanian language
Summary(hu.UTF-8):	Xindy román nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-romanian
Xindy romanian language

%description -n xindy-romanian -l hu.UTF-8
Xindy román nyelv

%package -n xindy-russian
Summary:	Xindy russian language
Summary(hu.UTF-8):	Xindy orosz nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-russian
Xindy russian language

%description -n xindy-russian -l hu.UTF-8
Xindy orosz nyelv

%package -n xindy-serbian
Summary:	Xindy serbian language
Summary(hu.UTF-8):	Xindy szerb nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-serbian
Xindy serbian language

%description -n xindy-serbian -l hu.UTF-8
Xindy szerb nyelv

%package -n xindy-slovak
Summary:	Xindy slovak language
Summary(hu.UTF-8):	Xindy szlovák nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-slovak
Xindy slovak language

%description -n xindy-slovak -l hu.UTF-8
Xindy szlovák nyelv

%package -n xindy-slovenian
Summary:	Xindy slovenian language
Summary(hu.UTF-8):	Xindy szlovén nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-slovenian
Xindy slovenian language

%description -n xindy-slovenian -l hu.UTF-8
Xindy szlovén nyelv

%package -n xindy-spanish
Summary:	Xindy spanish language
Summary(hu.UTF-8):	Xindy spanyol nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-spanish
Xindy spanish language

%description -n xindy-spanish -l hu.UTF-8
Xindy spanyol nyelv

%package -n xindy-swedish
Summary:	Xindy swedish language
Summary(hu.UTF-8):	Xindy svéd nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-swedish
Xindy swedish language

%description -n xindy-swedish -l hu.UTF-8
Xindy svéd nyelv

%package -n xindy-turkish
Summary:	Xindy turkish language
Summary(hu.UTF-8):	Xindy török nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-turkish
Xindy turkish language

%description -n xindy-turkish -l hu.UTF-8
Xindy török nyelv

%package -n xindy-ukrainian
Summary:	Xindy ukrainian language
Summary(hu.UTF-8):	Xindy ukrán nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-ukrainian
Xindy ukrainian language

%description -n xindy-ukrainian -l hu.UTF-8
Xindy ukrán nyelv

%package -n xindy-upper-sorbian
Summary:	Xindy upper-sorbian language
Summary(hu.UTF-8):	Xindy upper-sorbian nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-upper-sorbian
Xindy upper-sorbian language

%description -n xindy-upper-sorbian -l hu.UTF-8
Xindy upper-sorbian nyelv

%package -n xindy-vietnamese
Summary:	Xindy vietnamese language
Summary(hu.UTF-8):	Xindy vietnámi nyelv
Group:		Applications/Publishing/TeX

%description -n xindy-vietnamese
Xindy vietnamese language

%description -n xindy-vietnamese -l hu.UTF-8
Xindy vietnám nyelv

%package -n texlive-dvips
Summary:	Texmf files needed for texlive-dvips
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	texlive-dvips-basic >= %{texlive_version}

%description -n texlive-dvips
The program dvips takes a DVI file file[.dvi] produced by TeX (or by
some other processor such as GFtoDVI) and converts it to PostScript,
normally sending the result directly to the laserprinter.

%description -n texlive-dvips -l de.UTF-8
Das dvips-Programm nimmt eine dvi-Datei ([.dvi]), die von TeX bzw.
durch einen anderen Prozessor wie GFtoDVI) erzeugt wurde, und
konvertiert diese in PostScript, wobei das Ergebnis in der Regel
direkt an einen Laserdrucker gesandt wird.

%description -n texlive-dvips -l es.UTF-8
El programa dvips coge un archivo DVI (.dvi) producido por TeX (o por
otro procesador como GFtoDVI) y lo convierte a PostScript, normalmente
enviando el resultado directamente a la impresora láser.

%description -n texlive-dvips -l fr.UTF-8
Le programme dvips convertit les fichiers DVI en PostScript, en
envoyant normalement le résultat directement sur une imprimante Laser.

%description -n texlive-dvips -l hu.UTF-8
A dvips program egy TeX által készített DVI-fájlból PostScript
állományt készít, amelyet a legtöbb esetben közvetlenül a
lézernyomtatóra küldhetsz.

%description -n texlive-dvips -l pl.UTF-8
Program dvips bierze plik DVI wygenerowany przez TeXa (lub jakiś inny
program, jak na przykład GFtoDVI) i konwertuje go do PostScriptu.
Domyślnie wynik jest wysyłany bezpośrednio do drukarki.

%description -n texlive-dvips -l pt_BR.UTF-8
O programa dvips toma um arquivo DVI (.dvi) produzido pelo TeX (ou por
outro processador como o GFtoDVI) e o converte para PostScript,
normalmente enviando o resultado diretamente para a impressora laser.

%description -n texlive-dvips -l tr.UTF-8
dvips programı, dvi biçiminde bir girdi dosyası alır ve onu
PostScript'e dönüştürür. Kaynak dosya TeX tarafından oluşturulmuş
olabileceği gibi başka işleyiciler tarafından da (GFtoDVI gibi)
üretilmiş olabilir.

%package -n texlive-omega
Summary:	Texmf files needed for texlive-omega
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	texlive-omega-basic >= %{texlive_version}
Requires:	%{name}-fonts-omega >= %{epoch}:%{version}-%{release}
Requires:	%{name}-plain >= %{epoch}:%{version}-%{release}

%description -n texlive-omega
Omega is a version of the TeX program modified for multilingual
typesetting. It uses unicode, and has additional primitives for (among
other things) bidirectional typesetting.

%description -n texlive-omega -l pl.UTF-8
Omega to wersja TeXa zmodyfikowana dla potrzeb składu wielojęzycznego.
Używa unikodu i ma dodatkowe prymitywy do (między innymi) składania
tekstu pisanego w obu kierunkach.

%package -n texlive-scripts-extra
Summary:	Various scripts
Summary(hu.UTF-8):	Néhány szkript
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-scripts-extra
Various scripts.

%description -n texlive-scripts-extra -l hu.UTF-8
Néhány szkript.

# # formats #

# Plain format.

%package -n texlive-plain
Summary:	Plain TeX format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Provides:	tetex-format-plain
Provides:	tetex-plain
Obsoletes:	tetex-cyrplain
Obsoletes:	tetex-format-cyrplain
Obsoletes:	tetex-format-plain
Obsoletes:	tetex-plain

%description -n texlive-plain
Plain TeX format basic files.

%description -n texlive-plain -l pl.UTF-8
Podstawowe pliki dla formatu Plain TeX.

# MeX Plain format

%package -n texlive-mex
Summary:	MeX Plain Format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla format MeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Requires:	texlive-fonts-pl
Requires:	texlive-plain
Obsoletes:	tetex-mex

%description -n texlive-mex
MeX Plain Format basic files.

%description -n texlive-mex -l pl.UTF-8
Podstawowe pliki dla formatu MeX Plain.

# AMS TeX format

%package -n texlive-amstex
Summary:	AMS macros for Plain TeX basic files
Summary(pl.UTF-8):	Podstawowe pliki makr AMS dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-ams
Requires:	%{shortname}-format-amstex
Requires:	%{shortname}-plain
Provides:	tetex-ams
Obsoletes:	tetex-ams
Obsoletes:	tetex-amstex
Obsoletes:	tetex-plain-amsfonts

%description -n texlive-amstex
American Mathematical Society macros for Plain TeX basic files.

%description -n texlive-amstex -l pl.UTF-8
Podstawowe pliki makr AMS (American Mathematical Society) dla formatu
Plain TeX.

# CSPlain format

%package -n texlive-format-csplain
Summary:	TeX CSPlain format
Summary(pl.UTF-8):	Format TeX CSPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-csplain
Obsoletes:	tetex-format-csplain

%description -n texlive-format-csplain
TeX CSPlain format.

%description -n texlive-format-csplain -l pl.UTF-8
Format TeX CSPlain.

# CSLaTeX format

%package -n texlive-cslatex
Summary:	CSLaTeX format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu CSLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-cs
Requires:	%{shortname}-plain
Provides:	tetex-cslatex
Obsoletes:	tetex-cslatex

%description -n texlive-cslatex
CSLaTeX format basic files.

%description -n texlive-cslatex -l pl.UTF-8
Podstawowe pliki dla formatu CSLaTeX.


%package -n texlive-enctex
Summary:	TeX extension that translates input on its way into TeX.
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-enctex
A TeX extension that translates input on its way into TeX.

# EPlain format

%package -n texlive-eplain
Summary:	EPlain format basic files
Summary(pl.UTF-8):	Podstawowe pliki dla formatu EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-plain
Obsoletes:	tetex-eplain
Obsoletes:	tetex-etex

%description -n texlive-eplain
EPlain format basic files.

%description -n texlive-eplain -l pl.UTF-8
Podstawowe pliki dla formatu EPlain.

# ConTeXt format.

%define		_noautoreq	'perl(path_tre)'

%package -n texlive-context-data
Summary:	Files for ConTeXt
Summary(pl.UTF-8):	Pliki dla ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-context-data
Files for ConTeXt.

%description -n texlive-context-data -l pl.UTF-8
Pliki dla ConTeXt.

%package -n texlive-format-context-de
Summary:	German ConTeXt format
Summary(pl.UTF-8):	Niemiecka wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-context
Obsoletes:	tetex-format-context-de

%description -n texlive-format-context-de
German ConTeXt format.

%description -n texlive-format-context-de -l pl.UTF-8
Niemiecka wersja formatu ConTeXt.

%package -n texlive-format-context-en
Summary:	English ConTeXt format
Summary(pl.UTF-8):	Angielska wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-context
Obsoletes:	tetex-format-context-en

%description -n texlive-format-context-en
English ConTeXt format.

%description -n texlive-format-context-en -l pl.UTF-8
Angielska wersja formatu ConTeXt.

%package -n texlive-format-context-nl
Summary:	Dutch ConTeXt format
Summary(pl.UTF-8):	Holenderska wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-context
Obsoletes:	tetex-format-context-nl

%description -n texlive-format-context-nl
Dutch ConTeXt format.

%description -n texlive-format-context-nl -l pl.UTF-8
Holenderska wersja formatu ConTeXt.

# LaTeX format.

%package -n texlive-latex-data
Summary:	LaTeX macro package basic files
Summary(pl.UTF-8):	Podstawowe pliki pakietu makr LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Requires:	%{shortname}-fonts-latex
Requires:	%{shortname}-tex-ruhyphen
Requires:	%{shortname}-tex-ukrhyph
# for misc/eurosym:
Requires:	%{shortname}-fonts-eurosym
Requires:	%{shortname}-pdftex
Requires:	%{shortname}-tex-babel
Requires:	%{shortname}-tex-pstricks
Suggests:	%{shortname}-fonts-jknappen
Suggests:	%{shortname}-latex-ucs = %{epoch}:%{version}-%{release}
Provides:	tetex-format-latex = %{epoch}:%{version}-%{release}
Provides:	tetex-latex = %{epoch}:%{version}-%{release}
Obsoletes:	tetex-bibtex-koma-script
Obsoletes:	tetex-format-latex
Obsoletes:	tetex-latex
Obsoletes:	tetex-latex-SIunits
Obsoletes:	tetex-latex-caption
Obsoletes:	tetex-latex-curves
Obsoletes:	tetex-latex-dinbrief
Obsoletes:	tetex-latex-draftcopy
Obsoletes:	tetex-latex-dstroke
Obsoletes:	tetex-latex-dvilj
Obsoletes:	tetex-latex-eepic
Obsoletes:	tetex-latex-endfloat
Obsoletes:	tetex-latex-fancyhdr
Obsoletes:	tetex-latex-fancyheadings
Obsoletes:	tetex-latex-fancyvrb
Obsoletes:	tetex-latex-fp
Obsoletes:	tetex-latex-graphics
Obsoletes:	tetex-latex-hyperref
Obsoletes:	tetex-latex-koma-script
Obsoletes:	tetex-latex-labels
Obsoletes:	tetex-latex-listings
Obsoletes:	tetex-latex-misc
Obsoletes:	tetex-latex-ms
Obsoletes:	tetex-latex-multirow
Obsoletes:	tetex-latex-mwcls
Obsoletes:	tetex-latex-mwdtools
Obsoletes:	tetex-latex-natbib
Obsoletes:	tetex-latex-ntgclass
Obsoletes:	tetex-latex-oberdiek
Obsoletes:	tetex-latex-pb-diagram
Obsoletes:	tetex-latex-pstricks
Obsoletes:	tetex-latex-qfonts
Obsoletes:	tetex-latex-revtex4
Obsoletes:	tetex-latex-seminar
Obsoletes:	tetex-latex-t2
Obsoletes:	tetex-latex-titlesec
Obsoletes:	tetex-latex-tools
Obsoletes:	tetex-latex-units
Obsoletes:	tetex-mwcls
Obsoletes:	tetex-revtex4

%description -n texlive-latex-data
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains basic files.

%description -n texlive-latex-data -l pl.UTF-8
LaTeX jest frontendem do systemu formatującego tekst TeX. Jest
łatwiejszy w użyciu niż TeX. Jest właściwie zestawem makr TeXowych,
dających użytkownikom wygodne, predefiniowane formaty dokumentów.

Ten pakiet zawiera podstawowe pliki.

%package -n texlive-latex-colortab
Summary:	Shade cells of tables and halign
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-colortab
Shade cells of tables and halign.

%package -n texlive-latex-ctex
Summary:	LaTeX classes and packages for Chinese typesetting
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-latex-ctex
LaTeX classes and packages for Chinese typesetting.

%package -n texlive-ptex
Summary:	A TeX system for publishing in Japanese
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-ptex
A TeX system for publishing in Japanese. 

%package -n texlive-latex-12many
Summary:	Generalising mathematical index sets
Summary(hu.UTF-8):	A matematikai halmazok indexelésének általánosítása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-12many
Generalising mathematical index sets.

%description -n texlive-latex-12many -l hu.UTF-8
A matematikai halmazok indexelésének általánosítása.

%package -n texlive-latex-abstract
Summary:	Control the typesetting of the abstract environment
Summary(hu.UTF-8):	Az "abstract" környezet szedésének irányítása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-abstract
Control the typesetting of the abstract environment.

%description -n texlive-latex-abstract -l hu.UTF-8
Az "abstract" környezet szedésének irányítása.

%package -n texlive-latex-accfonts
Summary:	Utilities to derive new fonts from existing ones
Summary(hu.UTF-8):	Eszközök új betűtípusok származtatására már létezőkből
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-latex-accfonts
Utilities to derive new fonts from existing ones.

%description -n texlive-latex-accfonts -l hu.UTF-8
Eszközök új betűtípusok származtatására már létezőkből.

%package -n texlive-latex-adrconv
Summary:	BibTeX styles to implement an address database
Summary(hu.UTF-8):	BibTeX stílusok cím-adatbázis megvalósításához
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-adrconv
BibTeX styles to implement an address database.

%description -n texlive-latex-adrconv -l hu.UTF-8
BibTeX stílusok cím-adatbázis megvalósításához.

%package -n texlive-latex-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl.UTF-8):	Wirtualne fonty dla plików PDF z fontami CMR o kodowaniu T1
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-ae
Requires:	%{shortname}-latex
Provides:	tetex-latex-ae
Obsoletes:	tetex-latex-ae

%description -n texlive-latex-ae
A set of virtual fonts which emulates T1 coded fonts using the
standard CM fonts. The package is called AE fonts (for Almost
European). The main use of the package is to produce PDF files using
versions of the CM fonts instead of the bitmapped EC fonts.

%description -n texlive-latex-ae -l pl.UTF-8
Zestaw wirtualnych fontów emulujących fonty o kodowaniu T1 przy użyciu
standardowych fontów CM. Ten pakiet został nazwany AE (Almost European
- prawie europejskie). Głównym przeznaczeniem tego pakietu jest
  produkowanie plików PDF przy użyciu wersji fontów CM zamiast
  bitmapowych fontów EC.

%package -n texlive-latex-algorithms
Summary:	Floating algorithm environment
Summary(pl.UTF-8):	Pływające środowisko dla algorytmów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-algorith
Obsoletes:	tetex-latex-algorithms

%description -n texlive-latex-algorithms
Defines a floating algorithm environment designed to work with the
algorithmic package.

%description -n texlive-latex-algorithms -l pl.UTF-8
Pakiet definiujący pływające środowisko dla algorytmów zaprojektowane
do pracy z pakietem algorithmic.

%package -n texlive-latex-ams
Summary:	AMS math facilities for LaTeX
Summary(pl.UTF-8):	Udogodnienia matematyczne AMS dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-ams
Requires:	%{shortname}-latex
Provides:	tetex-latex-ams
Obsoletes:	tetex-latex-ams
Obsoletes:	tetex-latex-amscls
Obsoletes:	tetex-latex-amsfonts
Obsoletes:	tetex-latex-amsmath

%description -n texlive-latex-ams
This package is the principal package in the AMS-LaTeX distribution.
It adapts for use in LaTeX most of the mathematical features found in
AMS-TeX.

%description -n texlive-latex-ams -l pl.UTF-8
To jest główny pakiet dystrybucji AMS-LaTeX. Jest adaptacją większości
możliwości matematycznych AMS-TeXa do używania w LaTeXu.

%package -n texlive-latex-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych czcionek polskich jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-antp
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-antp

%description -n texlive-latex-antp
A replica of Antykwa Poltawskiego font in PostScript Type 1 format
- -- preliminary version. This font was designed in the 'twenties and
  the 'thirties of XX century by a Polish graphic artist and a
  typographer Adam Poltawski. It was widely used by Polish printing
  houses as long as metal types were in use (until ca the 'sixties).
  Perhaps the first complete font family programmed and parametrized in
  METAPOST.

%description -n texlive-latex-antp -l pl.UTF-8
Wstępna wersja repliki kroju Antykwa Półtawskiego w formacie
PostScript Type 1. Ten krój został opracowany w latach 30-tych i
40-tych XX wieku przez polskiego grafika i typografa Adama
Półtawskiego. Była szeroko używana przez polskie drukarnie dopóki
używano metalowych czcionek (do lat 60-tych). Prawdopodobnie pierwsza
kompletna rodzina fontów zaprogramowana i zparametryzowana w
METAPOSCIE.

%package -n texlive-latex-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl.UTF-8):	Antykwa Turuńska - rodzina tradycyjnych czcionek polskich jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-antt
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-antt

%description -n texlive-latex-antt
Antykwa Torunska is a serif font designed by the late Polish
typographer Zygfryd Gardzielewski, reconstructed and digitized as Type
1.

%description -n texlive-latex-antt -l pl.UTF-8
Antykwa Toruńska to krój szeryfowy opracowany niedawno przez polskiego
typografa Zygfryda Gardzielewskiego, zrekonstruowany i przerobiony na
postać cyfrową jako Type 1.

%package -n texlive-latex-appendix
Summary:	Extra control of appendices
Summary(hu.UTF-8):	Az appendixek nagyobb irányítása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-appendix
Extra control of appendices.

%description -n texlive-latex-appendix -l hu.UTF-8
Az appendixek nagyobb irányítása.

%package -n texlive-latex-asyfig
Summary:	Commands for using Asymptote figures
Summary(hu.UTF-8):	Parancsok Asymptote alakzatok használatához
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Requires:	asymptote

%description -n texlive-latex-asyfig
Commands for using Asymptote figures.

%description -n texlive-latex-asyfig -l hu.UTF-8
Parancsok Asymptote alakzatok használatához.

%package -n texlive-latex-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl.UTF-8):	Tablicowy wariant fontów Computer Modern z obsługą LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-bbm
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-bbm

%description -n texlive-latex-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description -n texlive-latex-bbm -l pl.UTF-8
Tablicowy wariant fontów Computer Modern z obsługą LaTeXa.

%package -n texlive-latex-bardiag
Summary:	LateX package for drawing bar diagrams
Summary(pl.UTF-8):	LaTeX csomag oszlopdiagramok rajzolására
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-latex-bardiag
LateX package for drawing bar diagrams.

%description -n texlive-latex-bardiag -l hu.UTF-8
LaTeX csomag oszlopdiagramok rajzolására.

%package -n texlive-latex-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl.UTF-8):	Tablicowy tłusty font sans serif dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-bbold
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-bbold

%description -n texlive-latex-bbold
A geometric sans serif blackboard bold font, for use in mathematics.

%description -n texlive-latex-bbold -l pl.UTF-8
Geometryczny tablicowy tłusty font sans serif, do używania w
matematyce.

%package -n texlive-latex-beamer
Summary:	A LaTeX class for producing presentations and slides
Summary(hu.UTF-8):	LaTeX dokumentumosztály prezentációk és fóliák készítéséhez
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-beamer

%description -n texlive-latex-beamer
A LaTeX class for producing presentations and slides.

%description -n texlive-latex-beamer -l hu.UTF-8
LaTeX dokumentumosztály prezentációk és fóliák készítéséhez.

%package -n texlive-latex-bezos
Summary:	Packages by Javier Bezos (additional math tools)
Summary(hu.UTF-8):	Javier Bezos csomagjai (további matematikai eszközök)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-bezos
Packages by Javier Bezos (additional math tools).

%description -n texlive-latex-bezos -l hu.UTF-8
Javier Bezos csomagjai (további matematikai eszközök).

%package -n texlive-latex-bibtex-data
Summary:	Main BibTeX files
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-latex-bibtex-data
Main BibTeX files.

%package -n texlive-latex-bibtex-ams
Summary:	BibTeX style files for American Mathematical Society publications
Summary(pl.UTF-8):	Pliki stylów BibTeXa do publikacji American Mathematical Society
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex-ams
Requires:	%{shortname}-latex-bibtex
Obsoletes:	tetex-bibtex-ams
Obsoletes:	tetex-latex-bibtex-ams

%description -n texlive-latex-bibtex-ams
BibTeX style files for American Mathematical Society publications.

%description -n texlive-latex-bibtex-ams -l pl.UTF-8
Pliki stylów BibTeXa do publikacji American Mathematical Society.

%package -n texlive-latex-bibtex-dk
Summary:	Danish variants of the standard BibTeX styles
Summary(pl.UTF-8):	Duńskie warianty standardowych stylów BibTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex-bibtex
Obsoletes:	tetex-latex-bibtex-dk


%description -n texlive-latex-bibtex-dk
Dk-bib is a translation of the four standard BibTeX style files
(abbrv, alpha, plain and unsrt) into Danish. The files have been
extended with ISBN, ISSN and URL fields which can be enabled through a
LaTeX style file.

%description -n texlive-latex-bibtex-dk -l pl.UTF-8
Dk-bib to tłumaczenie czterech standardowych plików stylów BibTeXa
(abbrv, alpha, plain i unsrt) na język duński. Pliki zostały
rozszerzone o pola ISBN, ISSN i URL, które można włączyć poprzez plik
stylu LaTeXa.

%package -n texlive-latex-bibtex-pl
Summary:	Polish bibliography management for LaTeX
Summary(pl.UTF-8):	Polska wersja zarządzania bibliografią dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex-bibtex
Obsoletes:	tetex-bibtex-plbib
Obsoletes:	tetex-latex-bibtex-pl

%description -n texlive-latex-bibtex-pl
Polish bibliography management for LaTeX.

%description -n texlive-latex-bibtex-pl -l pl.UTF-8
Polska wersja zarządzania bibliografią dla LaTeXa.

%package -n texlive-latex-bibtex-german
Summary:	German variants of standard BibTeX styles
Summary(pl.UTF-8):	Niemieckie wersje standardowych stylów BibTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex-bibtex
Obsoletes:	tetex-bibtex-germbib
Obsoletes:	tetex-latex-bibtex-german

%description -n texlive-latex-bibtex-german
German variants of standard BibTeX styles.

%description -n texlive-latex-bibtex-german -l pl.UTF-8
Niemieckie wersje standardowych stylów BibTeXa.

%package -n texlive-latex-bibtex-revtex4
Summary:	BibTeX styles for REVTeX4
Summary(pl.UTF-8):	Style BibTeXa dla REVTeX4
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-bibtex-revtex4
Obsoletes:	tetex-latex-bibtex-revtex4

%description -n texlive-latex-bibtex-revtex4
BibTeX styles for REVTeX4.

%description -n texlive-latex-bibtex-revtex4 -l pl.UTF-8
Style BibTeXa dla REVTeX4.

%package -n texlive-latex-bibtex-jurabib
Summary:	Extended BibTeX citation support for the humanities and legal texts
Summary(pl.UTF-8):	Rozszerzona obsługa cytowania BibTeXa do tekstów humanistycznych i prawniczych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-bibtex-jurabib
Obsoletes:	tetex-latex-bibtex-jurabib

%description -n texlive-latex-bibtex-jurabib
Extended BibTeX citation support for the humanities and legal texts.

%description -n texlive-latex-bibtex-jurabib -l pl.UTF-8
Rozszerzona obsługa cytowania BibTeXa do tekstów humanistycznych i
prawniczych.

%package -n texlive-latex-bibtex-styles
Summary:	Various BibTeX styles
Summary(hu.UTF-8):	Vegyes BibTeX stílusok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex-bibtex

%description -n texlive-latex-bibtex-styles
Various BibTeX styles.

%description -n texlive-latex-bibtex-styles -l hu.UTF-8
Vegyes BibTeX stílusok.

%package -n texlive-latex-bibtex-vancouver
Summary:	Bibliographic style file for Biomedical Journals
Summary(hu.UTF-8):	Irodalomjegyzék-stílus a Biomedical Journal-hoz
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex-bibtex

%description -n texlive-latex-bibtex-vancouver
Bibliographic style file for Biomedical Journals.

%description -n texlive-latex-bibtex-vancouver -l hu.UTF-8
Irodalomjegyzék-stílus a Biomedical Journal-hoz.

%package -n texlive-latex-booktabs
Summary:	Publication quality tables in LaTeX
Summary(hu.UTF-8):	Nyomdai minőségű táblázatok LaTeX-ben
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-booktabs
Publication quality tables in LaTeX.

%description -n texlive-latex-booktabs -l hu.UTF-8
Nyomdai minőségű táblázatok LaTeX-ben.

%package -n texlive-latex-bosisio
Summary:	A collection of packages by Francesco Bosisio
Summary(hu.UTF-8):	Francesco Bosisio csomaggyűjteménye
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-bosisio
A collection of packages by Francesco Bosisio.

%description -n texlive-latex-bosisio -l hu.UTF-8
Francesco Bosisio csomaggyűjteménye.

%package -n texlive-latex-caption
Summary:	Customising captions in floating environments
Summary(hu.UTF-8):	Feliratok testreszabása úszó környezetekben
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-caption
Customising captions in floating environments.

%description -n texlive-latex-caption -l hu.UTF-8
Feliratok testreszabása úszó környezetekben.

%package -n texlive-latex-carlisle
Summary:	Miscellaneous small packages by David Carlisle
Summary(pl.UTF-8):	Różne małe pakiety autorstwa Davida Carlisle
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Provides:	tetex-latex-carlisle
Obsoletes:	tetex-latex-carlisle

%description -n texlive-latex-carlisle
Miscellaneous small packages by David Carlisle.

%description -n texlive-latex-carlisle -l pl.UTF-8
Różne małe pakiety autorstwa Davida Carlisle.

%package -n texlive-latex-ccfonts
Summary:	Support for Concrete text and math fonts in LaTeX
Summary(pl.UTF-8):	Obsługa fontów tekstowych i matematycznych Concrete w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-ccfonts

%description -n texlive-latex-ccfonts
LaTeX font definition files for the Concrete fonts and a LaTeX package
for typesetting documents using Concrete as the default font family.
The files support OT1, T1, TS1, and Concrete math including AMS fonts
(Ulrik Vieth's concmath).

%description -n texlive-latex-ccfonts -l pl.UTF-8
Pliki definicji fontów LaTeXowych dla fontów Concrete oraz pakiet
LaTeXa do składania dokumentów przy użyciu Concrete jako domyślnej
rodziny fontów. Pliki obsługują fonty OT1, T1, TS1 oraz matematyczny
Concrete wraz z AMS (concmath Ulrika Vietha).

%package -n texlive-latex-cite
Summary:	Supports compressed, sorted lists of numerical citations
Summary(pl.UTF-8):	Obsługa kompresowanych, sortowanych list numerowanych cytatów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-cite

%description -n texlive-latex-cite
Supports compressed, sorted lists of numerical citations.

%description -n texlive-latex-cite -l pl.UTF-8
Obsługa kompresowanych, sortowanych list numerowanych cytatów.

%package -n texlive-latex-cmbright
Summary:	Support for CM Bright fonts in LaTeX
Summary(pl.UTF-8):	Obsługa fontów CM Bright w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-cmbright
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-cmbright

%description -n texlive-latex-cmbright
A family of sans serif fonts for TeX and LaTeX, based on Donald
Knuth's CM fonts. It comprises OT1, T1 and TS1 encoded text fonts of
various shapes as well as all the fonts necessary for mathematical
typesetting, incl. AMS symbols. This collection provides all the
necessary files for using the fonts with LaTeX.

%description -n texlive-latex-cmbright -l pl.UTF-8
Rodzina fontów sans serif dla TeXa i LaTeXa, oparta na fontach CM
Donalda Knutha. Obejmuje fonty dla kodowań OT1, T1 i TS1 różnych
kształtów oraz fonty niezbędne do składu matematycznego, włącznie z
symbolami AMS. Ten zestaw dostarcza wszystkie niezbędne pliki do
używania fontów w LaTeXu.

%package -n texlive-latex-comment
Summary:	Selectively include/excludes portions of text
Summary(hu.UTF-8):	A szöveg részeinek beillesztése/kihagyása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-comment
Selectively include/excludes portions of text.

%description -n texlive-latex-comment -l hu.UTF-8
A szöveg részeinek beillesztése/kihagyása.

%package -n texlive-latex-concmath
Summary:	LaTeX package and font definition files to access the Concrete math fonts
Summary(pl.UTF-8):	Pakiet LaTeXa i pliki definicji fontów udostępniające fonty matematyczne Concrete
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-concmath
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-concmath

%description -n texlive-latex-concmath
LaTeX package and font definition files to access the Concrete math
fonts, which were derived from Computer Modern math fonts using
parameters from Concrete Roman text fonts.

%description -n texlive-latex-concmath -l pl.UTF-8
Pakiet LaTeXa i pliki definicji fontów udostępniające fonty
matematyczne Concrete wywodzące się z fontów matematycznych Computer
Modern poprzez zastosowanie parametrów fontów tekstowych Concrete
Roman.

%package -n texlive-latex-currvita
Summary:	Typeset a curriculum vitae
Summary(hu.UTF-8):	Önéletrajzok írása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-currvita
Typeset a curriculum vitae.

%description -n texlive-latex-currvita -l hu.UTF-8
Önéletrajzok írása.

%package -n texlive-latex-curves
Summary:	Curves for LaTeX picture environment
Summary(hu.UTF-8):	Görbék LaTeX picture környezetébe
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-curves
Curves for LaTeX picture environment.

%description -n texlive-latex-curves -l hu.UTF-8
Görbék LaTeX picture környezetébe.

%package -n texlive-latex-custom-bib
Summary:	Customized BibTeX styles for LaTeX
Summary(pl.UTF-8):	Dostosowywanie stylów BibTeXa dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-custom-bib

%description -n texlive-latex-custom-bib
Package generating customized BibTeX bibliography styles from a
generic file using docstrip. Includes support for the Harvard style.

%description -n texlive-latex-custom-bib -l pl.UTF-8
Pakiet generujący dostosowane style bibliografii BibTeXa z ogólnego
pliki przy użyciu docstrip. Zawiera obsługę stylu Harvard.

%package -n texlive-latex-cyrillic
Summary:	LaTeX Cyrillic support
Summary(pl.UTF-8):	Obsługa cyrylicy dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Provides:	tetex-latex-cyrillic
Obsoletes:	tetex-latex-cyrillic

%description -n texlive-latex-cyrillic
LaTeX Cyrillic support.

%description -n texlive-latex-cyrillic -l pl.UTF-8
Obsługa cyrylicy dla LaTeXa.

%package -n texlive-latex-enumitem
Summary:	A package to customize the three basic lists
Summary(hu.UTF-8):	Egy csomag, amivel testreszabhatod a három alapvető listát
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-enumitem
A package to customize the three basic lists (enumerate, itemize and
description).

%description -n texlive-latex-enumitem -l hu.UTF-8
Egy csomag, amivel testreszabhatod a három alapvető listakörnyezetet
(enumerate, itemize, description).

%package -n texlive-latex-exams
Summary:	Various document classes to typeset exams
Summary(hu.UTF-8):	Különböző dokumentumosztályok vizsgák, feladatsorok szedésére
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex-ams

%description -n texlive-latex-exams
Various document classes to typeset exams.

%description -n texlive-latex-exams -l hu.UTF-8
Különböző dokumentumosztályok vizsgák, feladatsorok szedésére.

%package -n texlive-latex-float
Summary:	Tools to manipulate float objects
Summary(hu.UTF-8):	Eszközök úszó objektuomok kezeléséhez
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-float
Tools to manipulate float objects.

%description -n texlive-latex-float -l hu.UTF-8
Eszközök úszó objektuomok kezeléséhez.

%package -n texlive-latex-foiltex
Summary:	The FoilTeX is a collection of LaTeX files for making foils
Summary(hu.UTF-8):	A FoilTeX a LaTeX fájlok gyűjteménye fóliák készítéséhez
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-foiltex
The FoilTeX is a collection of LaTeX files for making foils.

%description -n texlive-latex-foiltex -l hu.UTF-8
A FoilTeX a LaTeX fájlok gyűjteménye fóliák készítéséhez.

%package -n texlive-latex-formlett
Summary:	Letters to multiple recipients
Summary(hu.UTF-8):	Levél több címzettnek ("körlevél")
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-formlett
Letters to multiple recipients.

%description -n texlive-latex-formlett -l hu.UTF-8
Levél több címzettnek ("körlevél").

%package -n texlive-latex-formular
Summary:	Create forms containing field for manual entry
Summary(hu.UTF-8):	Kézzel kitöltendő űrlapok készítése
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-formular
Create forms containing field for manual entry.

%description -n texlive-latex-formular -l hu.UTF-8
Kézzel kitöltendő űrlapok készítése.

%package -n texlive-latex-gbrief
Summary:	Letter document class
Summary(hu.UTF-8):	Levél dokumentumosztály
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-gbrief
Letter document class.

%description -n texlive-latex-gbrief -l hu.UTF-8
Levél dokumentumosztály.

%package -n texlive-latex-keystroke
Summary:	Graphical representation of keys on keyboard
Summary(hu.UTF-8):	A billentyűk grafikus megjelenítése
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-keystroke
Graphical representation of keys on keyboard.

%description -n texlive-latex-keystroke -l hu.UTF-8
A billentyűk grafikus megjelenítése.

%package -n texlive-latex-labbook
Summary:	Typeset laboratory journals
Summary(hu.UTF-8):	Laborjegyzőkönyvek szedése
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-labbook
Typeset laboratory journals.

%description -n texlive-latex-labbook -l hu.UTF-8
Laborjegyzőkönyvek szedése.

%package -n texlive-latex-lcd
Summary:	Alphanumerical LCD-style displays
Summary(hu.UTF-8):	Alfanumerikus LCD-szerű kijelzés
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-lcd
Alphanumerical LCD-style displays.

%description -n texlive-latex-lcd -l hu.UTF-8
Alfanumerikus LCD-szerű kijelzés.

%package -n texlive-latex-leaflet
Summary:	Create small handouts (flyers)
Summary(hu.UTF-8):	Kis "kézikönyvek" készítése (brossúrák)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-leaflet
Create small handouts (flyers).

%description -n texlive-latex-leaflet -l hu.UTF-8
Kis "kézikönyvek" készítése (brossúrák).

%package -n texlive-latex-leftidx
Summary:	Left and right subscripts and superscripts in math mode
Summary(hu.UTF-8):	Bal és jobboldali alsó és felső indexek matematikai módban
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-leftidx
Left and right subscripts and superscripts in math mode.

%description -n texlive-latex-leftidx -l hu.UTF-8
Bal és jobboldali alsó és felső indexek matematikai módban.

%package -n texlive-latex-lewis
Summary:	Draw Lewis structures (chemistry)
Summary(hu.UTF-8):	Lewis struktúrák készítése (kémia)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-lewis
Draw Lewis structures (chemistry).

%description -n texlive-latex-lewis -l hu.UTF-8
Lewis struktúrák készítése (kémia).

%package -n texlive-latex-lm
Summary:	LaTeX styles for Latin Modern family fonts
Summary(pl.UTF-8):	Style LaTeXa dla fontów z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-fonts-lm
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-lm
Obsoletes:	texlive-fonts-type1-lm

%description -n texlive-latex-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%description -n texlive-latex-lm -l pl.UTF-8
Rodzina fontów Latin Modern, oparta na fontach Computer Modern
przekazanych do domeny publicznej przez AMS (copyright (C) 1997 AMS).
Zawiera wiele dodatkowych znaków, głównie z akcentami, ale nie tylko.
Jest jeden zbiór fontów postscriptowych oraz cztery zbiory plików TeX
Font Metric, odpowiadających: kodowaniu Cork (cork-*.tfm); kodowaniu
QX (qx-*.tfm); kodowaniu TeX'n'ANSI zwanemu także LY1
(texnansi-*.tfm); oraz Text Companion dla fontów EC zwanemu także TS1
(ts1-*.tfm). Zakłada się, że potencjalny użytkownik wie, co zrobić z
tymi wszystkimi plikami. Autorem jest Bogusław Jackowski.

%package -n texlive-latex-lastpage
Summary:	Reference last page for "Page N of M" type footers
Summary(hu.UTF-8):	Az utolsó oldalra hivatkozás "N/M. oldal" típusú lábfejekhez
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-latex-lastpage
Reference last page for Page N of M type footers.

%description -n texlive-latex-lastpage -l hu.UTF-8
Az utolsó oldalra hivatkozás "N/M. oldal" típusú lábfejekhez.

%package -n texlive-latex-lineno
Summary:	Line numbers on paragraphs
Summary(pl.UTF-8):	Numery linii dla paragrafów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-lineno

%description -n texlive-latex-lineno
The LaTeX package lineno.sty provides line numbers on paragraphs.
After TeX has broken a paragraph into lines there will be line numbers
attached to them, with the possibility to make references through the
LaTeX \ref, \pageref cross reference mechanism.

%description -n texlive-latex-lineno -l pl.UTF-8
Pakiet LaTeXa lineno.sty daje numery linii dla paragrafów. Po podziale
paragrafu na linie przez TeXa do linii dołączane są ich numery z
możliwością tworzenia odnośników poprzez mechanizm odnośników LaTeXa
\ref i \pageref.

%package -n texlive-latex-metre
Summary:	Support for the work of classicists
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-metre
Support for the work of classicists.

%package -n texlive-latex-games
Summary:	Packages for typesetting games
Summary(hu.UTF-8):	Játékok szedése
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-games
Chess, chinese chess, crosswords, go, backgammon and more.

%description -n texlive-latex-games -l hu.UTF-8
Sakk, kínai sakk, keresztrejtvények, go, backgammon és még sok más.

%package -n texlive-latex-extend
Summary:	Extensions, patches, improvements of main LaTeX styles, environments
Summary(hu.UTF-8):	Az alap LaTeX stílusok, környezetek, stb. bővítései, foltjai
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Provides:	tetex-latex-ltablex
Obsoletes:	tetex-latex-ltablex

%description -n texlive-latex-extend
This package contains:
- a4wide: "Wide" a4 layout.
- a5comb: Support for a5 paper sizes.
- addlines: a user-friendly wrapper around \enlargethispage.
- alnumsec: alphanumeric section numbering.
- anonchap: Make chapters be typeset like sections.
- arydshln: horizontal and vertical dashed lines in arrays and
  tabulars
- authoraftertitle: Make author, etc., available after \maketitle.
- babelbib: multilingual bibliographies.
- bibtopicprefix: prefix references to bibliographies produced by
  bibtopic.
- blkarray: Extended array and tabular.
- block: A block letter style for the letter class.
- boites: boxes that may break across pages
- booklet: aids for printing simple booklets.
- bullcntr: display list item counter as regular pattern of bullets.
- ccicons: LaTeX support for Creative Commons icons.
- chappg: page numbering by chapter.
- cjw: a bundle of packages and classes.
- clefval: key/value support with a hash.
- collref: Collect blocks of references into a single reference.
- colortbl: add colour to LaTeX tables.
- combine: bundle individual documents into a single document.
- combinedgraphics: Include graphic (EPS or PDF)/LaTeX combinations.
- contour: print a coloured contour around text.
- ctable: easily typeset centered tables.
- curve2e: extensions for package pict2e.
- dashbox: draw dashed boxes.
- dashline: draw dashed rules.
- docmute: Input files ignoring LaTeX preamble, etc.
- dox: Extend the doc package.
- emptypage: Make empty pages really empty.
- easylist: Lists using a single active character.
- esk: Package to encapsulate Sketch files in LaTeX sources.
- etaremune: reverse-counting enumerate environment.
- expdlist: expanded description environments.
- fix2col: Fix miscellaneous two column mode features.
- fltpage: Place caption on an adjacent page.
- fncylab: Alter the format of \label references.
- ftcap: Allows \caption at the beginning of a table-environment.
- ftnxtra: Extends the applicability of the \footnote command.
- HA-prosper: patches and improvements for prosper.
- import: Establish input relative to a directory.
- layaureo: A package to improve the A4 page layout.
- leading: define leading with a length.
- librarian: Tools to create bibliographies in TeX.
- listbib: Lists contents of BibTeX files.
- listliketab: typeset lists as tables.
- ltablex: table package extensions.
- makebox: defines a \makebox* command.
- makecell: tabular column heads and multilined cells.
- marginnote: notes in the margin, even where \marginpar fails
- mcaption: put captions in the margin.
- mcite: multiple items in a single citation.
- mciteplus: enhanced multiple citations.
- minipage-marginpar: minipages with marginal notes.
- miniplot: a package for easy figure arrangement.
- modref: Customisation of cross-references in LaTeX.
- multicap: format captions inside multicols
- newvbtm: define your own verbatim-like environment.
- nextpage: Generalisations of the page advance commands.
- nopageno: No page numbers in LaTeX documents.
- notes2bib: integrating notes into the bibliography.
- notoccite: Prevent trouble from citations in table of contents, etc.
- ntabbing: simple tabbing extension for automatic line numbering.
- numline: LaTeX macros for numbering lines.
- pagecont: Page numbering that continues between documents.
- pagerange: Flexible and configurable page range typesetting.
- pbox: a variable-width \parbox command.
- pinlabel: a TeX labelling package.
- polytable: tabular-like environments with named columns.
- rccol: decimal-centered optionally rounded numbers in tabular.
- romannum: generate roman numerals instead of arabic digits.
- schedule: weekly schedules.
- spreadtab: Spreadsheet features for LaTeX tabular environments.
- subfloat: sub-numbering for figures and tables.
- thmbox: Decorate theorem statements.
- titlepic: Add picture to title page of a document.
- twoinone: Print two pages on a single page.
- umoline: underline text allowing line breaking.
- umrand: package for fancy box frames.
- underlin: underlined running heads.
- underscore: Control the behaviour of "_" in text.
- undolabl: Override existing labels.
- ushort: shorter (and longer) underlines and underbars.
- widetable: An environment for typesetting tables of specified width
- zwpagelayout: Page layout and crop-marks.

%description -n texlive-latex-extend -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- a4wide: "Wide" a4 layout.
- a5comb: Support for a5 paper sizes.
- addlines: felhasználóbarát wrapper \enlargethispage-hez
- alnumsec: alfanumerikus section számozás
- anonchap: Make chapters be typeset like sections.
- arydshln: vízszintes és függőleges pontozott vonalak array és
  tabular környezetkben
- authoraftertitle: Make author, etc., available after \maketitle.
- babelbib: többnyelvű bibliográfiák
- bibtopicprefix: prefix hivatkozás bibtopic által készített
  bibliográfiára
- blkarray: Extended array and tabular.
- block: A block letter style for the letter class.
- boites: dobozok, amelyek törhetők oldalak között
- booklet: booklet formátumban történő nyomtatás
- bullcntr: lista elemek számlálójának megjelenítése mint...
- ccicons: LaTeX support for Creative Commons icons.
- chappg: oldalszámozás chapter alapján
- cjw: csomagok és osztályok tömkelege
- clefval: kulcs/érték párok hash-sel
- collref: Collect blocks of references into a single reference.
- colortbl: színek LaTeX táblázatokban
- combine: külön dokumentumok eggyé fűzése
- combinedgraphics: Include graphic (EPS or PDF)/LaTeX combinations.
- contour: színes kontúr nyomtatása szöveg körül
- ctable: középre igazított táblázatok szedése
- curve2e: pict2e csomaghoz kiegészítések
- dashbox: pontozott dobozok
- dashline: pontozott vonalak
- docmute: Input files ignoring LaTeX preamble, etc.
- dox: Extend the doc package.
- easylist: Lists using a single active character.
- emptypage: Make empty pages really empty.
- esk: Package to encapsulate Sketch files in LaTeX sources.
- etaremune: visszafele sorszámazó enumerate környezet
- expdlist: kibővített description környezetek
- fix2col: Fix miscellaneous two column mode features.
- fltpage: Place caption on an adjacent page.
- fncylab: Alter the format of \label references.
- ftcap: Allows \caption at the beginning of a table-environment.
- ftnxtra: Extends the applicability of the \footnote command.
- HA-prosper: foltok és bővítések a prosper-hez
- import: Establish input relative to a directory.
- layaureo: A package to improve the A4 page layout.
- leading: sorközök definiálása hosszal
- librarian: Tools to create bibliographies in TeX.
- listbib: Lists contents of BibTeX files.
- listliketab: listák táblázatként szedése
- ltablex: table csomag kiegészítése
- makebox: egy \makebox* parancs definiálása
- makecell: táblázat címsorral és többsoros cellákkal
- marginnote: széljegyzetek, ott is, ahol a \marginpar hibázik
- mcaption: címkék a margóra
- mcite: több elem egy hivatkozásban
- mciteplus: kibővített többszörös hivatkozás
- minipage-marginpar: minipage-ek széljegyzetekkel
- miniplot: egy csomag ábrák könnyű elhelyezéséhez
- modref: Customisation of cross-references in LaTeX.
- multicap: formázott cimkék multicols környezetben
- newvbtm: saját verbatim-szerű környezetek
- nextpage: Generalisations of the page advance commands.
- nopageno: No page numbers in LaTeX documents.
- notes2bib: megjegyzések elhelyezése bibliográfiába
- notoccite: Prevent trouble from citations in table of contents, etc.
- ntabbing: tabbing környezet automatikus sorszámozással
- numline: LaTeX makrók sorok számozására
- pagecont: Page numbering that continues between documents.
- pagerange: Flexible and configurable page range typesetting.
- pbox: változtatható szélességű \parbox
- pinlabel: a TeX labelling package.
- polytable: tabular-like environments with named columns.
- rccol: decimal-centered optionally rounded numbers in tabular.
- romannum: generate roman numerals instead of arabic digits.
- schedule: heti időbeosztás (órarend)
- spreadtab: Spreadsheet features for LaTeX tabular environments.
- subfloat: sub-numbering for figures and tables.
- thmbox: Decorate theorem statements.
- titlepic: Add picture to title page of a document.
- twoinone: Print two pages on a single page.
- umoline: aláhúzott szövegben sortörés engedélyezése
- umrand: package for fancy box frames.
- underlin: aláhúzott élőfej
- underscore: Control the behaviour of "_" in text.
- undolabl: Override existing labels.
- ushort: shorter (and longer) underlines and underbars.
- widetable: An environment for typesetting tables of specified width
- zwpagelayout: Page layout and crop-marks.

%package -n texlive-latex-effects
Summary:	Additional effects to fonts, texts
Summary(hu.UTF-8):	További effektek betűkhöz, szövegekhez,...
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-effects
This package contains:
- arcs: draw arcs over and under text
- background: Placement of background material on pages of a document.
- bclogo: Creating colourful boxes with logos.
- blowup: upscale or downscale all pages of a document.
- boxedminipage: A package for producing framed minipages.
- changebar: generate changebars in LaTeX documents.
- capt-of: captions on more than floats.
- changebar: generate changebars in LaTeX documents.
- changelayout: Change the layout of individual pages and their text.
- censor: facilities for controlling restricted text in a document.
- combelow: Typeset "comma-below" letters, as in Romanian.
- comma: Formats a number by inserting commas.
- dashundergaps: Underline with dotted or dashed lines.
- dblfloatfix: Fixes for twocolumn floats.
- draftwatermark: put a grey textual watermark on document pages.
- endnotes: Place footnotes at the end.
- fancypar: Decoration of individual paragraphs.
- flippdf: horizontal flipping of pages with pdfLaTeX.
- flowfram: create text frames for posters, brochures or magazines.
- framed: Framed or shaded regions that can break across pages.
- grid: Grid typesetting in LaTeX.
- isorot: rotation of document elements.
- lettrine: typeset dropped capitals.
- mdframed: Framed environments that can split at page boundaries.
- midpage: Environment for vertical centring.
- multibox: Multiple boxes and frames for the picture environment.
- niceframe: support for fancy frames.
- nolbreaks: No line breaks in text.
- notes: mark sections of a document.
- objectz: macros for typesetting Object Z.
- pageslts: Variants of last page labels.
- parallel: typeset parallel texts.
- quotchap: decorative chapter headings.
- rotpages: typeset sets of pages upside-down and backwards.
- rlepsf: Rewrite labels in EPS graphics.
- roundbox: Round boxes in LaTeX.
- sectionbox: create fancy boxed ((sub)sub)sections.
- shade: Shade pieces of text.
- shadethm: theorem environments that are shaded
- tablenotes: Notes in tables at end document.
- ulem: Package for underlining.
- xwatermark: Graphics and text watermarks on selected pages.

%description -n texlive-latex-effects -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- arcs: ívek rajzolása szöveg fölé és alá
- background: Placement of background material on pages of a document.
- bclogo: Creating colourful boxes with logos.
- blowup: a dokumentum összes oldalának nagyítása vagy kicsinyítése
- boxedminipage: A package for producing framed minipages.
- capt-of: Captions on more than floats.
- censor: facilities for controlling restricted text in a document.
- changebar: oldalsávok készítése LaTeX dokumentumokban
- changelayout: Change the layout of individual pages and their text.
- combelow: Typeset "comma-below" letters, as in Romanian.
- comma: Formats a number by inserting commas.
- dashundergaps: Underline with dotted or dashed lines.
- dblfloatfix: Fixes for twocolumn floats.
- draftwatermark: szürke szöveges vízjel a dokumentum oldalaira
- endnotes: Place footnotes at the end.
- fancypar: Decoration of individual paragraphs.
- flippdf: oldalak vízszintes tükrözése pdfLaTeX-hel
- flowfram: szövegkeretek poszterekhez, brossúrákhoz vagy magazinokhoz
- framed: Framed or shaded regions that can break across pages.
- grid: Grid typesetting in LaTeX.
- isorot: dokumentum-elemek forgatása
- lettrine: ejtett kapitálisok szedése
- mdframed: Framed environments that can split at page boundaries.
- midpage: Environment for vertical centring.
- multibox: Multiple boxes and frames for the picture environment.
- niceframe: különféle keretek
- nolbreaks: No line breaks in text.
- notes: dokumentum részeinek kiemelése, megjelölése
- objectz: Object Z objektumok szedése
- pageslts: Variants of last page labels.
- parallel: párhuzamos szövegek szedése
- quotchap: decorative chapter headings.
- rlepsf: Rewrite labels in EPS graphics.
- rotpages: typeset sets of pages upside-down and backwards.
- shade: Shade pieces of text.
- sectionbox: create fancy boxed ((sub)sub)sections.
- shadethm: theorem environments that are shaded
- tablenotes: Notes in tables at end document.
- ulem: Package for underlining.
- xwatermark: Graphics and text watermarks on selected pages.

%package -n texlive-latex-math-sources
Summary:	Sources of latex-math
Summary(hu.UTF-8):	A latex-math forrása
Group:		Applications/Publishing/TeX

%description -n texlive-latex-math-sources
Sources of latex-math.

%description -n texlive-latex-math-sources -l hu.UTF-8
A latex-math forrása.

%package -n texlive-latex-math
Summary:	Mathematical packages
Summary(hu.UTF-8):	Matematikai csomagok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-bbm
Requires:	%{shortname}-fonts-stmaryrd
Requires:	%{shortname}-latex
Requires:	%{shortname}-latex-ams
Requires:	%{shortname}-latex-carlisle
Requires:	%{shortname}-latex-psnfss
Requires:	%{shortname}-latex-pst-3dplot
Requires:	%{shortname}-latex-wasysym
Requires:	%{shortname}-tex-pstricks
Requires:	%{shortname}-tex-xkeyval
Requires:	%{shortname}-tex-xypic
# gnuplottex needs gnuplot
Requires:	gnuplot

%description -n texlive-latex-math
This package contains:
- bez123: support for Bezier curves.
- binomexp: calculate Pascal's triangle
- bigints: Writing big integrals.
- cases: numbered cases environment
- circle: Maths mode circles for temporal logic.
- cmll: symbols for linear logic.
- constants: automatic numbering of constants.
- coordsys: draw cartesian coordinate systems.
- dcpic: Commutative diagrams in a LaTeX and TeX documents.
- diagmac2: Diagram macros, using pict2e
- dot2texi: Create graphs within LaTeX using the dot2tex tool.
- dotseqn: flush left equations with dotted leaders to the numbers.
- egplot: encapsulate Gnuplot sources in LaTeX documents.
- eqlist: description lists with equal indentation.
- esdiff: simplify typesetting of derivatives.
- esvect: vector arrows.
- extpfeil: extensible arrows in mathematics
- faktor: typeset quotient structures with LaTeX.
- fouridx: left sub- and superscripts in maths mode.
- functan: macros for functional analysis and PDE theory
- galois: typeset Galois connections.
- gene-logic: typeset logic formulae, etc.
- gnuplottex: embed Gnuplot commands in LaTeX documents.
- hhtensor: print vectors, matrices, and tensors.
- ionumbers: Restyle numbers in maths mode.
- isomath: Mathematics conformant to ISO 31.
- isonums: Display numbers in maths mode according to ISO 31-0.
- logpap: generate logarithmic graph paper with LaTeX.
- makeplot: easy plots from Matlab in LaTeX.
- mathcomp: Text symbols in maths mode.
- maybemath: make math bold or italic according to context.
- mfpic4ode: macros to draw direction fields and solutions of ODEs.
- mhequ: multicolumn equations, tags, labels, sub-numbering.
- mhs: historical mathematics.
- mlist: logical markup for lists.
- nath: natural mathematics notation.
- noitcrul: improved underlines in mathematics.
- numprint: print numbers with separators and exponent if necessary.
- oubraces: braces over and under a formula.
- permute: support for symmetric groups.
- qsymbols: maths symbol abbreviations.
- qtree: draw tree structures.
- sdrt: macros for Segmented Discourse Representation Theory.
- semantic: help for writing programming language semantics.
- simplewick: simple Wick contractions.
- sseq: spectral sequence diagrams.
- subdepth: unify maths subscript height.
- subeqn: package for subequation numbering.
- subeqnarray: equation array with sub numbering.
- subsupscripts: A range of sub- and superscript commands.
- tikz-3dplot: Coordinate transformation styles for 3d plotting in TikZ.
- tree-dvips: trees and other linguists' macros.
- tkz-linknodes: Link nodes in mathematical environments.
- trfsigns: typeset transform signs.
- trsym: symbols for transformations.

%description -n texlive-latex-math -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- bez123: Bezier-görbék
- bigints: Writing big integrals.
- binomexp: Pascal-háromszög számítása
- cases: számozott esetszétválasztás
- circle: Maths mode circles for temporal logic.
- cmll: szimbólumok lineáris logikához
- constants: változók automatikus sorszámozása
- coordsys: Descartes-féle koordinátarendszerek rajzolása
- dcpic: Commutative diagrams in a LaTeX and TeX documents.
- diagmac2: Diagram macros, using pict2e
- dot2texi: Create graphs within LaTeX using the dot2tex tool.
- dotseqn: TODO
- egplot: Gnuplot források LaTeX dokumentumokba ágyazása
- eqlist: leíró lista egyenlő behúzással
- esdiff: deriváltak bevitele
- esvect: vektornyilak
- extpfeil: bővíthető nyilak matematikában
- faktor: hányados struktúrák LaTeX-hel
- fouridx: alsó és felső indexek bal oldalon matematikai módban
- functan: funkcionálanalízés és PDE elmélethez makrók
- galois: Galois kapcsolatok szedése
- gene-logic: logikai formulák
- gnuplottex: Gnuplot parancsok beágyazása LaTeX dokumentumokba
- hhtensor: vetkorok, mátrixok és tenzorok nyomtatása
- ionumbers: Restyle numbers in maths mode.
- isomath: Mathematics conformant to ISO 31.
- isonums: Display numbers in maths mode according to ISO 31-0.
- logpap: logaritmikus grafikonok
- makeplot: könnyű ábrázolások Matlab-ból LaTeX-be
- mathcomp: Text symbols in maths mode.
- maybemath: matematikai félkövér ill. dőlt szöveg környezettől
  függően
- mfpic4ode: differenciálegyenletek megoldásainak ábrázolása
- mhequ: többoszlopos egyenletek, cimkék, al-sorszámozás
- mhs: történelmi matematika
- mlist: listák logikus jelölése
- nath: természetes matematikai jelölés
- noitcrul: kibővített aláhúzások matematikában
- numprint: számok írása elválasztókkal és kitevőkkel, ha szükséges
- oubraces: braces over and under a formula.
- permute: szimmetriacsoportok
- petri-nets: A set TeX/LaTeX packages for drawing Petri nets.
- qsymbols: matematikai szimbólumok rövidítése
- qtree: fastruktúrák rajzolása
- sdrt: macros for Segmented Discourse Representation Theory.
- semantic: help for writing programming language semantics.
- simplewick: simple Wick contractions.
- sseq: spectral sequence diagrams.
- subdepth: matematikai indexek méretének egységesítése
- subeqn: alegyenletek sorszámozása
- subeqnarray: egyenletek al-sorszámozása
- subsupscripts: A range of sub- and superscript commands.
- tikz-3dplot: Coordinate transformation styles for 3d plotting in TikZ.
- tkz-linknodes: Link nodes in mathematical environments.
- tree-dvips: trees and other linguists' macros
- trfsigns: transzformációs jelek szedése
- trsym: szimbólumok transzformációkhoz
- ulsy: extra matematikai karakterek

%package -n texlive-latex-misc
Summary:	Misc packages
Summary(hu.UTF-8):	Vegyes csomagok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-misc
This packages contains:
- advdate: Print a date relative to "today".
- chronology: Provides a horizontal timeline.
- cooking: typeset recipes.
- cuisine: typeset recipes.
- envbig: Printing addresses on envelopes.
- fixme: insert "fixme" notes into draft documents.
- fn2end: Convert footnotes to endnotes.
- fnpara: Footnotes in paragraphs.
- fwlw: Get first and last words of a page.
- hyper: Hypertext cross referencing.
- knittingpattern: Create knitting patterns.
- liturg: Support for typesetting Catholic liturgical texts.
- mailmerge: Repeating text field substitution.
- menu: Typesetting menus.
- nicetext: Minimal markup for simple text (Wikipedia style) and
- ot-tableau: Optimality Theory tableaux in LaTeX.
- papermas: Compute the mass of a printed version of a document.
- plantslabels: Write labels for plants.
- recipe: A LaTeX class to typeset recipes.
- recipecard: typeset recipes in note-card-sized boxes.
- simplecd: Simple CD, DVD covers for printing.
- termcal: Print a class calendar.
- thumby: Create thumb indexes for printed books.
- tkz-tab: Tables of signs and variations using PGF/TikZ.
- todo: make a to-do list for a document.
- todonotes: Marking things to do in a LaTeX document.
- truncate: Truncate text to a specified width.
- typehtml: Typeset HTML directly from LaTeX.
- vruler: Numbering text.
- wordlike: Simulating word processor layout.
- xcomment: Allows selected environments to be included/excluded.

%description -n texlive-latex-misc -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- advdate: Print a date relative to "today".
- chronology: Provides a horizontal timeline.
- cooking: receptek szedése
- cookybooky: receptek szedése
- cuisine: receptek szedése
- envbig: Printing addresses on envelopes.
- fixme: "fixme" megjegyzések elhelyezése
- fn2end: Convert footnotes to endnotes.
- fnpara: Footnotes in paragraphs.
- fwlw: Get first and last words of a page.
- hyper: Hypertext cross referencing.
- knittingpattern: kötésminták
- liturg: Support for typesetting Catholic liturgical texts.
- mailmerge: Repeating text field substitution.
- menu: Typesetting menus.
- nicetext: Minimal markup for simple text (Wikipedia style) and
- ot-tableau: Optimality Theory tableaux in LaTeX.
- papermas: Compute the mass of a printed version of a document.
- plantslabels: Write labels for plants.
- recipe: A LaTeX class to typeset recipes.
- recipecard: receptek szedése jegyzet-méretű dobozokba
- simplecd: Simple CD, DVD covers for printing.
- termcal: Print a class calendar.
- thumby: Create thumb indexes for printed books.
- tkz-tab: Tables of signs and variations using PGF/TikZ.
- todo: dokumentumok teendőinek listája
- todonotes: Marking things to do in a LaTeX document.
- truncate: Truncate text to a specified width.
- typehtml: Typeset HTML directly from LaTeX.
- vruler: Numbering text.
- wordlike: Simulating word processor layout.
- xcomment: Allows selected environments to be included/excluded.

%package -n texlive-latex-music
Summary:	Musical packages
Summary(hu.UTF-8):	Zenei csomagok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-music
This package contains:
- abc: support ABC music notation in LaTeX.
- gchords: typeset guitar chords.
- guitar: guitar chords and song texts.
- songbook: package for typesetting song lyrics and chord books.

%description -n texlive-latex-music -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- abc: ABC hangjegyzések LaTeX-ben
- gchords: gitár akkordok szedése
- guitar: gitárkották és dalszövegek
- songbook: dalszövegek és akkordkönyvek szedése

%package -n texlive-latex-physics
Summary:	Physical packages
Summary(hu.UTF-8):	Fizikai csomagok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Suggests:	%{shortname}-latex-SIstyle
Suggests:	%{shortname}-latex-SIunits
Suggests:	%{shortname}-latex-siunitx

%description -n texlive-latex-physics
This package contains:
- braket: Dirac bra-ket and set notations.
- circ: macros for typesetting circuit diagrams.
- circuitikz: draw electrical networks with TikZ.
- colorwav: colours by wavelength of visible light.
- dyntree: construct Dynkin tree diagrams.
- eltex: Simple circuit diagrams in LaTeX picture mode.
- engtlc: Support for users in Telecommunications Engineering.
- feynmf: macros and fonts for creating Feynman (and other) diagrams.
- formula: typesetting physical units.
- isotope: a package for type setting isotopes
- listofsymbols: create and manipulate lists of symbols
- miller: typeset miller indices.
- pst-electricfield: Draw electric field and equipotential lines with PStricks.
- pst-magneticfield: Plotting a magnetic field with PSTricks.
- susy: macros for SuperSymmetry-related work.

%description -n texlive-latex-physics -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- braket: Dirac bra-ket és halmaz jelölés
- circ: áramkörök szedése
- circuitikz: elektromos hálózatok TikZ segítségével
- colorwav: a látható fény színei hullámhossz szerint
- dyntree: Dynkin fadiagramok készítése
- eltex: Simple circuit diagrams in LaTeX picture mode.
- engtlc: Support for users in Telecommunications Engineering.
- feynmf: makrók és fontok Feynman (és más) diagramok készítésére
- formula: fizikai egységek szedése
- isotope: izotópok szedése
- listofsymbols: szimbólumok listájának létrehozása és kezelése
- miller: miller indexek szedése
- pst-electricfield: Draw electric field and equipotential lines with PStricks.
- pst-magneticfield: Plotting a magnetic field with PSTricks.
- susy: Szuper-Szimmetria elmélettel kapcsolatos munkákhoz makrók

%package -n texlive-latex-bidi
Summary:	Support for bidirectional typesetting in plain TeX and LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-latex-bidi
Support for bidirectional typesetting in plain TeX and LaTeX.

%package -n texlive-latex-biology
Summary:	Biological packages
Summary(hu.UTF-8):	Biológiai csomagok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Requires:	%{shortname}-xetex

%description -n texlive-latex-biology
This package contains:
- biocon: typesetting biological species names
- dnaseq: format DNA base sequences.

%description -n texlive-latex-biology -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- biocon: biológiai fajnevek szedése
- dnaseq: DNS szekvenciák szedése

%package -n texlive-latex-presentation
Summary:	Presentations in LaTeX
Summary(hu.UTF-8):	Prezentációk LaTeX-ben
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex-foiltex
Suggests:	%{shortname}-latex-prosper = %{epoch}:%{version}-%{release}

%description -n texlive-latex-presentation
This package contains:
- powerdot: a presentation class.
- ppower4: a postprocessor for PDF presentations.
- sciposter: make posters of ISO A3 size and larger.
- tpslifonts: a LaTeX package for configuring presentation fonts.

%description -n texlive-latex-presentation -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- powerdot: egy prezentáció osztály
- ppower4: egy postprocesszor PDF prezentációkhoz
- sciposter: poszterek készítése A3-as és nagyobb méretben
- tpslifonts: a LaTeX package for configuring presentation fonts.

%package -n texlive-latex-chem
Summary:	Chemical packages
Summary(hu.UTF-8):	Kémiai csomagok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Suggests:	%{shortname}-latex-lewis

%description -n texlive-latex-chem
This package contains:
- achemso: support for American Chemical Society journal submissions.
- bpchem: typeset chemical names, formulae, etc.
- chemarrow: arrows for use in chemistry.
- chemcompounds: simple consecutive numbering of chemical compounds.
- chemcono: support for compound numbers in chemistry documents.
- chemstyle: writing chemistry with style.
- mhchem: typeset chemical formulae/equations and Risk and Safety
  phrases

%description -n texlive-latex-chem -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- achemso: American Chemical Society formátuma
- bpchem: kémiai nevek, formulák, stb. szedése
- chemarrow: kémiában használatos nyilak
- chemcompounds: kémiai vegyületek számozása
- chemcono: kémiai vegyületek kémiai dokumentumokbam
- chemstyle: kémiai dokumentum írása
- mhchem: kémiai formulák/egyenletek szedése

%package -n texlive-latex-informatic
Summary:	Informatical packages
Summary(hu.UTF-8):	Informatikai csomagok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-informatic
This package contains:
- alg: LaTeX environments for typesetting algorithms.
- bytefield: Create illustrations for network protocol specifications.
- colordoc: Coloured syntax highlights in documentation.
- dirtree: Display trees in the style of windows explorer.
- drs: Typeset Discourse Representation Structures (DRS).
- lsc: typesetting Live Sequence Charts.
- method: typeset method and variable declarations.
- minted: highlighted source code for LaTeX.
- msc: draw MSC diagrams.
- multiobjective: Symbols for multibojective optimisation etc.
- nag: detecting and warning about obsolete LaTeX commands
- register: typeset programmable elements in digital hardware
  (registers).
- uml: UML diagrams in LaTeX.
- vaucanson-g: PSTricks macros for drawing automata

%description -n texlive-latex-informatic -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- alg: LaTeX környezetek algoritmusok szedésére
- bytefield: hálózati protokoll specifikációk szemléltetése
- colordoc: Coloured syntax highlights in documentation.
- dirtree: Display trees in the style of windows explorer.
- drs: Typeset Discourse Representation Structures (DRS).
- lsc: Live Sequence Charts
- method: eljárások és változók deklarációjának szedése
- minted: highlighted source code for LaTeX.
- msc: MSC diagramok
- multiobjective: Symbols for multibojective optimisation etc.
- nag: elavult LaTeX parancsok detektálása és figyelmeztetés
- register: programozható elemek (regiszterek) szedése
- uml: UML diagramok LaTeX-ben
- vaucanson-g: PSTricks macros for drawing automata

%package -n texlive-latex-pdftools
Summary:	Various tools to pdf output
Summary(hu.UTF-8):	Különböző eszközök pdf output-hoz
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-pdftools
This package contains:
- attachfile: attach arbitrary files to a PDF document
- cooltooltips: associate a pop-up window and tooltip with PDF
  hyperlinks
- flashmovie: Directly embed flash movies into PDF files.
- movie15: multimedia inclusion package.
- pax: Extract and reinsert PDF annotations with pdfTeX.
- pdf14: Restore PDF 1.4 to a TeX live 2010 format.
- pdfcomment: A user-friendly interface to pdf annotations.
- pdfcprot: activating and setting of character protruding using
  pdflatex.
- pdfmarginpar: Generate marginpar-equivalent PDF annotations.
- pdfsync: provide links between source and PDF.
- pdftricks: support for pstricks in pdfTeX. . pdfscreen: support
  screen-based document design.
- tdclock: A ticking digital clock package for PDF output.

%description -n texlive-latex-pdftools -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- attachfile: fájlok csatolása PDF dokumentumokba
- cooltooltips: felugró ablakok és súgók társítása PDF linkekhez
- flashmovie: Directly embed flash movies into PDF files.
- movie15: multimédia beillesztése
- pax: Extract and reinsert PDF annotations with pdfTeX.
- pdf14: Restore PDF 1.4 to a TeX live 2010 format.
- pdfcomment: A user-friendly interface to pdf annotations.
- pdfcprot: activating and setting of character protruding using
  pdflatex.
- pdfmarginpar: Generate marginpar-equivalent PDF annotations.
- pdfsync: provide links between source and PDF.
- pdfscreen: képernyő alapú dokumentumok
- pdftricks: pstricks támogatás pdfTeX-ben
- tdclock: A ticking digital clock package for PDF output.

%package -n texlive-latex-microtype
Summary:	An interface to the micro-typographic extensions of pdfTeX
Summary(pl.UTF-8):	Interfejs do rozszerzeń mikrotypograficznych pdfTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-microtype

%description -n texlive-latex-microtype
The `microtype' package provides a LaTeX interface to pdfTeX's
micro-typographic extensions: character protrusion and font expansion.
It allows to restrict character protrusion and/or font expansion to a
definable set of fonts, and to configure micro-typographic aspects of
the fonts in a straight-forward and flexible way. Settings for various
fonts are provided.

%description -n texlive-latex-microtype -l pl.UTF-8
Pakiet microtype dodaje do LaTeXa mechanizm do rozszerzeń
mikrotypograficznych pdfTeXa: wysuwania znaków i rozszerzania fontów.
Pozwala ograniczyć wysuwanie znaku i/lub rozszerzanie fontu do
określonego zbioru fontów oraz skonfigurować mikrotypograficzne
aspekty fontów w prosty i elastyczny sposób. Dostarczone są ustawienia
dla różnych fontów.

%package -n texlive-latex-musictex
Summary:	Typesetting music with TeX
Summary(hu.UTF-8):	Zenék szedése TeX-hel
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-musictex
Typesetting music with TeX.

%description -n texlive-latex-musictex -l hu.UTF-8
Zenék szedése TeX-hel.

%package -n texlive-latex-lucidabr
Summary:	Package to make Lucida Bright fonts usable with LaTeX
Summary(pl.UTF-8):	Pakiet umożliwiający używanie fontów Lucida Bright w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-lucidabr

%description -n texlive-latex-lucidabr
Package to make Lucida Bright fonts usable with LaTeX.

%description -n texlive-latex-lucidabr -l pl.UTF-8
Pakiet umożliwiający używanie fontów Lucida Bright w LaTeXu.

%package -n texlive-latex-marvosym
Summary:	Styles for Martin Vogel's Symbol (marvosym) font
Summary(pl.UTF-8):	Style dla fontu Symbol Martina Vogela (marvosym)
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-fonts-marvosym
Requires:	%{shortname}-latex
Provides:	tetex-latex-marvosym
Obsoletes:	tetex-latex-marvosym

%description -n texlive-latex-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%description -n texlive-latex-marvosym -l pl.UTF-8
Font Martin Vogel's Symbol (marvosym) to font zawierający: symbol
waluty Euro zdefiniowany przez Komisję Europejską; symbole Euro w
krojach Times, Helvetica i Courier; symbole do inżynierii
strukturalnej; symbole do przekrojów stalowych; znaki astronomiczne
(Słońce, Księżyc, planety); 12 znaków Zodiaku; symbole nożyczek; znak
CE i inne.

%package -n texlive-latex-mflogo
Summary:	LaTeX support for MetaFont and logo fonts
Summary(pl.UTF-8):	Obsługa LaTeXa dla MetaFonta i fontów logo
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-mflogo
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-mflogo

%description -n texlive-latex-mflogo
LaTeX package and font definition file to access the Knuthian `logo'
fonts described in `The MetaFontbook' and the MetaFont and logos in
LaTeX documents.

%description -n texlive-latex-mflogo -l pl.UTF-8
Pakiet LaTeXa i plik definicji fontów udostępniający fonty logo Knutha
opisane w "The MetaFontbook" oraz MetaFont i loga w dokumentach
LaTeXa.

%package -n texlive-latex-mfnfss
Summary:	Font description files to use extra fonts like yinit and ygoth
Summary(pl.UTF-8):	Pliki opisów fontów udostępniające dodatkowe fonty, jak yinit i ygoth
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-mfnfss

%description -n texlive-latex-mfnfss
Font description files to use extra fonts like yinit and ygoth.

%description -n texlive-latex-mfnfss -l pl.UTF-8
Pliki opisów fontów udostępniające dodatkowe fonty, jak yinit i ygoth.

%package -n texlive-latex-minitoc
Summary:	Produce a table of contents for each chapter
Summary(pl.UTF-8):	Tworzenie spisów treści dla każdego rozdziału
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-minitoc

%description -n texlive-latex-minitoc
Produce a table of contents for each chapter.

%description -n texlive-latex-minitoc -l pl.UTF-8
Tworzenie spisów treści dla każdego rozdziału.

%package -n texlive-latex-mltex
Summary:	Support for MLTeX
Summary(pl.UTF-8):	Wsparcie dla MLTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-mltex

%description -n texlive-latex-mltex
Support for MLTeX, the multilingual TeX extension from Michael J.
Ferguson.

%description -n texlive-latex-mltex -l pl.UTF-8
Wsparcie dla MLTeXa - rozszerzenia TeXa z obsługą wielu języków,
autorstwa Michaela J. Fergusona.

%package -n texlive-latex-multienum
Summary:	Multi-column enumerated lists
Summary(hu.UTF-8):	Többoszlopos számozott listák
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-multienum
Multi-column enumerated lists.

%description -n texlive-latex-multienum -l hu.UTF-8
Többoszlopos számozott listák.


%package -n texlive-latex-moreverb
Summary:	Extended verbatim
Summary(hu.UTF-8):	Kiterjesztett verbatim
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-moreverb
Extended verbatim.

%description -n texlive-latex-moreverb -l hu.UTF-8
Kiterjesztett verbatim.

%package -n texlive-latex-ntheorem
Summary:	Enhanced theorem environment
Summary(hu.UTF-8):	Bővített tétel környezet
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-ntheorem
Enhanced theorem environment.

%description -n texlive-latex-ntheorem -l hu.UTF-8
Bővített tétel környezet

%package -n texlive-latex-other
Summary:	Other LaTeX packages
Summary(hu.UTF-8):	Néhány további LaTeX csomag
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-platex

%description -n texlive-latex-other
Other LaTeX packages.

%description -n texlive-latex-other -l hu.UTF-8
Néhány további LaTeX csomag.

%package -n texlive-latex-other-doc
Summary:	Other LaTeX packages documentation
Summary(hu.UTF-8):	Néhány további LaTeX csomag dokumentációja
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-other-doc
Other LaTeX packages documentation.

%description -n texlive-latex-other-doc -l hu.UTF-8
Néhány további LaTeX csomag dokumentációja.

%package -n texlive-latex-pdfslide
Summary:	Presentation slides using pdftex
Summary(hu.UTF-8):	Prezentáció készítése pdftex-hel
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-pdfslide
Presentation slides using pdftex.

%description -n texlive-latex-pdfslide -l hu.UTF-8
Prezentáció készítése pdftex-hel.

%package -n texlive-latex-pgf
Summary:	The TeX Portable Graphic Format
Summary(hu.UTF-8):	TeX Portable Graphic Formátum
Summary(pl.UTF-8):	Przenośny format grafiki dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Requires:	%{shortname}-latex-xcolor
Obsoletes:	tetex-pgf

%description -n texlive-latex-pgf
A macro package for creating graphics directly in TeX and LaTeX.

%description -n texlive-latex-pgf -l hu.UTF-8
Makró csomag rajzok készítéséhez közvetlenül TeX-ben és LaTeX-ben.

%description -n texlive-latex-pgf -l pl.UTF-8
Pakiet makr do tworzenia grafiki bezpośrednio z TeXa i LaTeXa.

%package -n texlive-latex-polynom
Summary:	Macros for manipulating polynomials
Summary(hu.UTF-8):	Makrók polinomokkal való műveletekre
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-polynom
Macros for manipulating polynomials.

%description -n texlive-latex-polynom -l hu.UTF-8
Makrók polinomokkal való műveletekre.

%package -n texlive-latex-polynomial
Summary:	Typeset (univariate) polynomials
Summary(hu.UTF-8):	Egyváltozós polinomok szedése
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-polynomial
Typeset (univariate) polynomials.

%description -n texlive-latex-polynomial -l hu.UTF-8
Egyváltozós polinomok szedése.

%package -n texlive-latex-programming
Summary:	Additional utilities to programming LaTeX
Summary(hu.UTF-8):	További eszközök LaTeX programozásához
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-programming
This package contains:
- boolexpr: A boolean expression evaluator and a switch command.
- bophook: Provides an At-Begin-Page hook.
- chngcntr: Change the resetting of counters.
- cmdtrack: check used commands.
- codedoc: LaTeX code and documentation in LaTeX-format file.
- cool: COntent-Oriented LaTeX
- coollist: manipulate COntent Oriented LaTeX Lists.
- coolstr: string manipulation in LaTeX.
- csvtools: reading data from CSV files.
- currfile: Macros for file name and path of input files.
- datatool: tools to load and manipulate data.
- datenumber: convert a date into a number and vice versa.
- delimtxt: read and parse text tables.
- dialogl: macros for constructing interactive LaTeX scripts.
- dprogress: LaTeX-relevant log information for debugging.
- environ: a new interface for environments in LaTeX.
- excludeonly: Prevent files being \include-ed.
- exp-testopt: Expandable \@testopt (and related) macros.
- export: import and export values of LaTeX registers.
- filehook: Hooks for input files.
- fmtcount: display the value of a LaTeX counter in a variety of
  formats.
- forarray: using array structures in LaTeX.
- forloop: iteration in LaTeX.
- getfiledate: Find the date of last modification of a file.
- ifmtarg: If-then-else command for processing potentially empty
- inversepath: calculate inverse file paths.
- keycommand: Simple creation of commands with key-value arguments.
- labelcas: check the existence of labels, and fork accordingly.
- lcg: generate random integers.
- listings-ext: Automated input of source.
- locality: Various macros for keeping things local.
- localloc: Macros for localizing TeX register allocations.
- makecmds: the new \makecommand command always (re)defines a command.
- multido: a loop facility for Generic TeX.
- namespc: rudimentary c++-like namespaces in LaTeX.
- newcommand: Generate new LaTeX command definitions.
- patchcmd: change the definition of an existing command.
- progress: creates an overview of a document's state.
- randtext: randomise the order of characters in strings.
- regcount: display the allocation status of the TeX registers.
- robustcommand: declare robust command, with \newcommand checks.
- skeycommand: Create commands using parameters and keyval in parallel
- skeyval: Extensions to xkeyval.
- splitindex: unlimited number of indexes.
- stack: tools to define and use stacks.
- stringstrings: string manipulation for cosmetic and programming
  application
- substr: deal with substrings in strings.
- totcount: Find the last value of a counter.
- typedref: eliminate errors by enforcing the types of labels.
- yax: Yet Another Key System.
- ydoc: Macros for documentation of LaTeX classes and packages.

%description -n texlive-latex-programming -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- boolexpr: A boolean expression evaluator and a switch command.
- bophook: Provides an At-Begin-Page hook.
- chngcntr: Change the resetting of counters.
- cmdtrack: használt parancsok ellenőrzése
- codedoc: LaTeX code and documentation in LaTeX-format file.
- cool: tartalom-orientált (COntent-Oriented) LaTeX
- coollist: COntent Oriented LaTeX listák manipulációja
- coolstr: sztring manipuláció LaTeX-ben
- csvtools: adatok olvasása CSV fájlokból
- currfile: Macros for file name and path of input files.
- datatool: eszközök adatok beolvasására és manipulációjához
- datenumber: dátum számmá konvertálása és vissza
- delimtxt: szöveges táblázatok olvasása és feldolgozása
- dialogl: interaktív makrók LaTeX-ben
- dprogress: LaTeX-releváns log információ debuggoláshoz
- export: LaTeX regiszterek értékeinek importálása és exportálása
- environ: egy új felület környezetek létrehozására
- excludeonly: Prevent files being \include-ed.
- exp-testopt: Expandable \@testopt (and related) macros.
- filehook: Hooks for input files.
- fmtcount: LaTeX számlálók megjelenítése különböző formátumokban
- forarray: tömb struktúrák LaTeX-ben
- forloop: iteráció LaTeX-ben
- getfiledate: Find the date of last modification of a file.
- ifmtarg: If-then-else command for processing potentially empty
- inversepath: fájlútvonalak visszafele relatív meghatározása
- keycommand: Simple creation of commands with key-value arguments.
- labelcas: cimkék létezésének ellenőrzése
- lcg: véletlen egész számok generálása
- listings-ext: Automated input of source.
- locality: Various macros for keeping things local.
- localloc: Macros for localizing TeX register allocations.
- newcommand: Generate new LaTeX command definitions.
- makecmds: új \makecommand, amely mindig (újra)definiál parancsot
- multido: ciklusok szervezése LaTeX-ben
- namespc: c++-szerű névterek LaTeX-ben
- patchcmd: létező parancsok definíciójának megváltoztatása
- progress: egy áttekintést készít a dokumentum állapotáról
- randtext: sztring karaktereinek összekeverése
- regcount: display the allocation status of the TeX registers.
- robustcommand: declare robust command, with \newcommand checks.
- skeycommand: Create commands using parameters and keyval in parallel
- skeyval: Extensions to xkeyval.
- splitindex: unlimited number of indexes.
- stack: verem használata
- stringstrings: sztring manipuláció
- substr: részszövegek keresése
- totcount: Find the last value of a counter.
- typedref: eliminate errors by enforcing the types of labels.
- yax: Yet Another Key System.
- ydoc: Macros for documentation of LaTeX classes and packages.

%package -n texlive-latex-prosper
Summary:	LaTeX class for high quality slides
Summary(hu.UTF-8):	LaTeX osztály jó minőségű fóliák készítéséhez
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Requires:	%{shortname}-xetex

%description -n texlive-latex-prosper
LaTeX class for high quality slides.

%description -n texlive-latex-prosper -l hu.UTF-8
LaTeX osztály jó minőségű fóliák készítéséhez.

%package -n texlive-latex-pseudocode
Summary:	LaTeX enviroment for specifying algorithms in a natural way
Summary(hu.UTF-8):	LaTeX környezet algoritmusok bevitelére
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-pseudocode
LaTeX enviroment for specifying algorithms in a natural way.

%description -n texlive-latex-pseudocode -l hu.UTF-8
LaTeX környezet algoritmusok bevitelére.

%package -n texlive-latex-psnfss
Summary:	LaTeX font support for common PostScript fonts
Summary(pl.UTF-8):	Obsługa popularnych fontów postscriptowych w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-adobe
Requires:	%{shortname}-latex
Provides:	tetex-latex-psnfss
Obsoletes:	tetex-latex-mathptm
Obsoletes:	tetex-latex-mathptmx
Obsoletes:	tetex-latex-psnfss

%description -n texlive-latex-psnfss
LaTeX font definition files, macros and font metrics for common
PostScript fonts.

%description -n texlive-latex-psnfss -l pl.UTF-8
LaTeXowe pliki definicji fontów, makra i metryki fontów dla
popularnych fontów postscriptowych.

%package -n texlive-latex-pst-2dplot
Summary:	A PSTricks package for drawing 2D curves
Summary(hu.UTF-8):	PSTricks csomag kétdimenziós görbék rajzolásához
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-2dplot
A PSTricks package for drawing 2D curves.

%description -n texlive-latex-pst-2dplot -l hu.UTF-8
PSTricks csomag kétdimenziós görbék rajzolásához.

%package -n texlive-latex-pst-3dplot
Summary:	Draw 3d curves and graphs using PSTricks
Summary(hu.UTF-8):	3D-s görbék és grafikonok PSTricks-szel
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-3dplot
Draw 3d curves and graphs using PSTricks.

%description -n texlive-latex-pst-3dplot -l hu.UTF-8
3D-s görbék és grafikonok PSTricks-szel.


%package -n texlive-latex-pst-bar
Summary:	Produces bar charts using pstricks
Summary(hu.UTF-8):	Oszlopdiagramok pstricks-szel
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-bar
Produces bar charts using pstricks.

%description -n texlive-latex-pst-bar -l hu.UTF-8
Oszlopdiagramok pstricks-szel.

%package -n texlive-latex-pst-circ
Summary:	PSTricks package for drawing electric circuits
Summary(hu.UTF-8):	PSTricks csomag elektromos áramkörök rajzolásához
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-circ
PSTricks package for drawing electric circuits.

%description -n texlive-latex-pst-circ -l hu.UTF-8
PSTricks csomag elektromos áramkörök rajzolásához.

%package -n texlive-latex-pst-diffraction
Summary:	Print diffraction patterns from various apertures
Summary(hu.UTF-8):	Diffrakciós képek különböző eszközökön
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-diffraction
Print diffraction patterns from various apertures.

%description -n texlive-latex-pst-diffraction -l hu.UTF-8
Diffrakciós képek különböző eszközökön.

%package -n texlive-latex-pst-eucl
Summary:	Euclidian geometry with pstricks
Summary(hu.UTF-8):	Euklidészi geometria a pstricks használatával
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-eucl
Euclidian geometry with pstricks.

%description -n texlive-latex-pst-eucl -l hu.UTF-8
Euklidészi geometria a pstricks használatával.


%package -n texlive-latex-pst-fun
Summary:	Draw "funny" objects with PSTricks
Summary(hu.UTF-8):	"Vicces" rajzok PSTricks-szel
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-fun
Draw "funny" objects with PSTricks.

%description -n texlive-latex-pst-fun -l hu.UTF-8
"Vicces" rajzok PSTricks-szel

%package -n texlive-latex-pst-func
Summary:	PSTricks package for plotting mathematical functions
Summary(hu.UTF-8):	PSTricks csomag matematikai függvények ábrázolásához
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-func
PSTricks package for plotting mathematical functions.

%description -n texlive-latex-pst-func -l hu.UTF-8
PSTricks csomag matematikai függvények ábrázolásához.

%package -n texlive-latex-pst-fr3d
Summary:	Draw 3-dimensional framed boxes using PSTricks
Summary(hu.UTF-8):	Háromdimenziós dobozok PSTricks segítségével
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-fr3d
Draw 3-dimensional framed boxes using PSTricks.

%description -n texlive-latex-pst-fr3d -l hu.UTF-8
Háromdimenziós dobozok PSTricks segítségével.

%package -n texlive-latex-pst-fractal
Summary:	Draw fractal sets using PSTricks
Summary(hu.UTF-8):	Fraktálok rajzolása PSTricks segítségével
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-fractal
Draw fractal sets using PSTricks.

%description -n texlive-latex-pst-fractal -l hu.UTF-8
Fraktálok rajzolása PSTricks segítségével.

%package -n texlive-latex-pst-infixplot
Summary:	Using pstricks plotting capacities with infix expressions rather than RPN
Summary(hu.UTF-8):	Infix kifejezések ábrázolása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-infixplot
Using pstricks plotting capacities with infix expressions rather than
RPN.

%description -n texlive-latex-pst-infixplot -l hu.UTF-8
Infix kifejezések ábrázolása.

%package -n texlive-latex-pst-math
Summary:	Enhancement of PostScript math operators to use with pstricks
Summary(hu.UTF-8):	PostScript matematikai operátorok bővítése pstricks-szel
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-math
Enhancement of PostScript math operators to use with pstricks.

%description -n texlive-latex-pst-math -l hu.UTF-8
PostScript matematikai operátorok bővítése pstricks-szel.

%package -n texlive-latex-pst-ob3d
Summary:	Three dimensional objects using PSTricks
Summary(hu.UTF-8):	Háromdimenziós objektumok PSTricks-szel
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-ob3d
Three dimensional objects using PSTricks.

%description -n texlive-latex-pst-ob3d -l hu.UTF-8
Háromdimenziós objektumok PSTricks-szel.

%package -n texlive-latex-pst-optexp
Summary:	Drawing optical experimental setups
Summary(hu.UTF-8):	Optikai összeállítások rajzolása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-optexp
Drawing optical experimental setups.

%description -n texlive-latex-pst-optexp -l hu.UTF-8
Optikai összeállítások rajzolása.

%package -n texlive-latex-pst-optic
Summary:	Drawing optics diagrams
Summary(hu.UTF-8):	Optikai ábrák rajzolása
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-optic
Drawing optics diagrams.

%description -n texlive-latex-pst-optic -l hu.UTF-8
Optikai ábrák rajzolása.

%package -n texlive-latex-pst-text
Summary:	Text and character manipulation in PSTricks
Summary(hu.UTF-8):	Szöveg és karakter manipulációk PSTricks-szel
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-text
Text and character manipulation in PSTricks.

%description -n texlive-latex-pst-text -l hu.UTF-8
Szöveg és karakter manipulációk PSTricks-szel.

%package -n texlive-latex-pst-uncategorized
Summary:	Other uncategorized PSTricks packages
Summary(hu.UTF-8):	Néhány kategorizálatlan PSTricks csomag
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-tex-pstricks

%description -n texlive-latex-pst-uncategorized
Other uncategorized PSTricks packages.

%description -n texlive-latex-pst-uncategorized -l hu.UTF-8
Néhány kategorizálatlan PSTricks csomag.

%package -n texlive-latex-pxfonts
Summary:	PX fonts LaTeX support
Summary(pl.UTF-8):	Obsługa fontów PX w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-px
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-pxfonts

%description -n texlive-latex-pxfonts
PX fonts LaTeX support.

%description -n texlive-latex-pxfonts -l pl.UTF-8
Obsługa fontów PX w LaTeXu.

%package -n texlive-latex-SIstyle
Summary:	Package to typeset SI units, numbers and angles
Summary(hu.UTF-8):	Csomag SI egységek, számok és szögek szedésére
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex-ams

%description -n texlive-latex-SIstyle
Package to typeset SI units, numbers and angles.

%description -n texlive-latex-SIstyle -l hu.UTF-8
Csomag SI egységek, számok és szögek szedésére.

%package -n texlive-latex-SIunits
Summary:	The SIunits package can be used to standardise the use of units in your writings
Summary(hu.UTF-8):	Az SIunits csomag a mennyiségek egységes írásában nyújt segítséget
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex-ams

%description -n texlive-latex-SIunits
The SIunits package can be used to standardise the use of units in
your writings.

%description -n texlive-latex-SIunits -l hu.UTF-8
Az SIunits csomag a mennyiségek egységes írásában nyújt segítséget.

%package -n texlive-latex-siunitx
Summary:	A comprehensive (SI) units package
Summary(hu.UTF-8):	Egy minden részletre kiterjedő (SI) egységek kezelését végző csomag
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-siunitx
A comprehensive (SI) units package.

%description -n texlive-latex-siunitx -l hu.UTF-8
Egy minden részletre kiterjedő (SI) egységek kezelését végző csomag.

%package -n texlive-latex-sources
Summary:	LaTeX sources
Summary(hu.UTF-8):	LaTeX források
Group:		Applications/Publishing/TeX

%description -n texlive-latex-sources
LaTeX sources.

%description -n texlive-latex-sources -l hu.UTF-8
LaTeX források.

%package -n texlive-latex-styles
Summary:	Various LaTeX styles
Summary(hu.UTF-8):	Különböző LaTeX stílusok
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-styles
Various LaTeX styles.

%description -n texlive-latex-styles -l hu.UTF-8
Különböző LaTeX stílusok.

%package -n texlive-latex-lang
Summary:	LaTeX support for non-english languages
Summary(hu.UTF-8):	LaTeX támogatás nem-angol nyelvekhez
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-lang
LaTeX support for non-english languages.

%description -n texlive-latex-lang -l hu.UTF-8
LaTeX támogatás nem-angol nyelvekhez.

%package -n texlive-latex-Tabbing
Summary:	Tabbing with accented letters
Summary(hu.UTF-8):	Tabbing környezet ékezetes betűk használatával
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description -n texlive-latex-Tabbing
Tabbing with accented letters.

%description -n texlive-latex-Tabbing -l hu.UTF-8
Tabbing környezet ékezetes betűk használatával.

%package -n texlive-latex-tutorial
Summary:	LaTeX documentation (tutorial) for beginners
Summary(hu.UTF-8):	LaTeX dokumentáció (tutorial) kezdőknek
Group:		Documentation

%description -n texlive-latex-tutorial
LaTeX documentation (tutorial) for beginners.

%description -n texlive-latex-tutorial -l hu.UTF-8
LaTeX dokumentáció (tutorial) kezdőknek.

%package -n texlive-latex-txfonts
Summary:	TX fonts LaTeX support
Summary(pl.UTF-8):	Obsługa fontów TX w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-tx
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-txfonts

%description -n texlive-latex-txfonts
TX fonts LaTeX support.

%description -n texlive-latex-txfonts -l pl.UTF-8
Obsługa fontów TX w LaTeXu.

%package -n texlive-latex-ucs
Summary:	This package contains support for using UTF-8 as input encoding in LaTeX documents
Summary(hu.UTF-8):	Ez a csomag lehetővé teszi UTF-8 kódolást a LaTeX dokumentumokban
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-ucs
This package contains support for using UTF-8 as input encoding in
LaTeX documents.

%description -n texlive-latex-ucs -l hu.UTF-8
Ez a csomag lehetővé teszi UTF-8 kódolást a LaTeX dokumentumokban.

%package -n texlive-latex-umlaute
Summary:	An interface to inputenc for using alternate input encodings
Summary(pl.UTF-8):	Interfejs inputenc do używania alternatywnych kodowań wejściowych
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex
Obsoletes:	tetex-latex-umlaute

%description -n texlive-latex-umlaute
An interface to inputenc for using alternate input encodings.

%description -n texlive-latex-umlaute -l pl.UTF-8
Interfejs inputenc do używania alternatywnych kodowań wejściowych.

%package -n texlive-latex-wasysym
Summary:	Extra characters from the Waldis symbol fonts
Summary(pl.UTF-8):	Dodatkowe znaki z fontów Waldis symbol
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-fonts-wasy
Requires:	%{shortname}-latex
Provides:	tetex-latex-wasysym
Obsoletes:	tetex-latex-wasysym

%description -n texlive-latex-wasysym
Makes some additional characters available that come from the wasy
fonts (Waldis symbol fonts). These fonts are not automatically
included in NFSS2/LaTeX2e since they take up important space and often
aren't necessary if one makes use of the packages amsfonts or amssymb.
Symbols include: join box, diamond, leadsto, sqsubset, lhd, rhd,
apple, ocircle invneg, logof, varint, male, female, phone, clock,
lightning, pointer, sun, bell, permil, smiley, various electrical
symbols, shapes, music notes, circles, signs, astronomy, etc.

%description -n texlive-latex-wasysym -l pl.UTF-8
Pakiet udostępniający dodatkowe symbole pochodzące z fontów wasy
(Waldis symbol). Te fonty nie są automatycznie dołączane w
NFSS2/LaTeX2e, ponieważ zajmują miejsce i zazwyczaj nie są potrzebne
jeśli używa się pakietów amsfonts lub amssymb. Zestaw symboli zawiera
m.in.: symbole join box, diamond, leadsto, sqsubset, lhd, rhd, apple,
ocircle invneg, logof, varint, male, female, phone, clock, lightning,
pointer, sun, bell, permil, smiley oraz różne symbole elektryczne,
kształty, nuty, okręgi, znaki, symbole astronomiczne itp.

%package -n texlive-latex-xcolor
Summary:	Allows for access to color tints, shades, tones etc
Summary(hu.UTF-8):	Hozzáférés színekhez, tónusokhoz, átmenetekhez, stb.
Summary(pl.UTF-8):	Pozwala na dostęp do odcieni, gradientów itp.
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-latex-xcolor

%description -n texlive-latex-xcolor
`xcolor' provides easy driver-independent access to several kinds of
color tints, shades, tones, and mixes of arbitrary colors. It allows
to select a document-wide target color model and offers tools for
automatic color schemes, conversion between eight color models, and
alternating table row colors.

%description -n texlive-latex-xcolor -l hu.UTF-8
`xcolor' egy egyszerű meghajtó-független hozzáférést biztosít
színekhez, átmenetekhez, tónusokhóz, és a színek korlátlan
keverékéhez. Lehetőséged van a teljes dokumentumra érvényes szín
modell kiválasztásához és a színmodellek közötti konverzióra.

%description -n texlive-latex-xcolor -l pl.UTF-8
`xcolor' dostarcza łatwego, niezależnego od urządzenia dostępu do
wielu rodzai cieniowania, tonów i połączeń dowolnych kolorów. Pozwala
na wybór modelu koloru dla całego dokumentu i oferuje narzędzia dla
schematów kolorów, konwersji między ośmioma modelami kolorów oraz
naprzemiennych kolorów w tabelach.

# # TeX generic macros #

%package -n texlive-tex-babel
Summary:	Multilingual support for TeX
Summary(pl.UTF-8):	Obsługa wielu języków dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Provides:	tetex-tex-babel
Obsoletes:	tetex-tex-babel

%description -n texlive-tex-babel
Multilingual support for TeX.

%description -n texlive-tex-babel -l pl.UTF-8
Obsługa wielu języków dla TeXa.

%package -n texlive-tex-german
Summary:	Supports the new German orthography (neue deutsche Rechtschreibung)
Summary(pl.UTF-8):	Obsługa nowej ortografii niemieckiej (neue deutsche Rechtschreibung)
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Provides:	tetex-tex-german
Obsoletes:	tetex-tex-german

%description -n texlive-tex-german
Supports the new German orthography (neue deutsche Rechtschreibung).

%description -n texlive-tex-german -l pl.UTF-8
Obsługa nowej ortografii niemieckiej (neue deutsche Rechtschreibung).

%package -n texlive-tex-insbox
Summary:	A TeX macro for inserting pictures/boxes into paragraphs
Summary(hu.UTF-8):	TeX makró képek/dobozok beszúrására bekezdésekbe
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-insbox
A TeX macro for inserting pictures/boxes into paragraphs.

%description -n texlive-tex-insbox -l hu.UTF-8
TeX makró képek/dobozok beszúrására bekezdésekbe.

%package -n texlive-tex-mfpic
Summary:	Macros which generate Metafont or Metapost for drawing pictures
Summary(pl.UTF-8):	Makra generujące Metafont lub Metapost do rysowania obrazków
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-tex-mfpic

%description -n texlive-tex-mfpic
Macros which generate Metafont or Metapost for drawing pictures.

%description -n texlive-tex-mfpic -l pl.UTF-8
Makra generujące Metafont lub Metapost do rysowania obrazków.

%package -n texlive-tex-misc
Summary:	Miscellaneous TeX macros
Summary(pl.UTF-8):	Różne makra TeXowe
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Provides:	tetex-tex-misc
Obsoletes:	tetex-tex-eijkhout
Obsoletes:	tetex-tex-misc

%description -n texlive-tex-misc
Miscellaneous TeX macros.

%description -n texlive-tex-misc -l pl.UTF-8
Różne makra TeXowe.

%package -n texlive-tex-pictex
Summary:	Picture drawing macros for TeX and LaTeX
Summary(pl.UTF-8):	Makra do rysowania obrazków dla TeXa i LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-tex-pictex

%description -n texlive-tex-pictex
Picture drawing macros for TeX and LaTeX.

%description -n texlive-tex-pictex -l pl.UTF-8
Makra do rysowania obrazków dla TeXa i LaTeXa.

%package -n texlive-tex-psizzl
Summary:	A TeX format for physics papers
Summary(hu.UTF-8):	TeX formátum fizikai kiadványokhoz
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-psizzl
A TeX format for physics papers.

%description -n texlive-tex-psizzl -l hu.UTF-8
TeX formátum fizikai kiadványokhoz.

%package -n texlive-tex-pstricks
Summary:	PostScript macros for TeX
Summary(pl.UTF-8):	Makra postscriptowe dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-dvips
Requires:	%{shortname}-tex-misc
Provides:	tetex-tex-pstricks
Obsoletes:	tetex-tex-pstricks

%description -n texlive-tex-pstricks
An extensive collection of PostScript macros that is compatible with
most TeX macro packages, including Plain TeX, LaTeX, AMS-TeX, and
AMS-LaTeX. Included are macros for color, graphics, pie charts,
rotation, trees and overlays. It has many special features, including:
a wide variety of graphics (picture drawing) macros, with a flexible
interface and with color support. There are macros for coloring or
shading the cells of tables.

%description -n texlive-tex-pstricks -l pl.UTF-8
Duży zestaw makr postscriptowych kompatybilny z większością pakietów
makr TeXowych, w tym: Plain TeX, LaTeX, AMS-TeX i AMS-LaTeX. Załączono
makra obsługujące kolory, grafikę, wykresy kołowe, obroty, drzewa i
nakładanie. Mają wiele możliwości, w tym dużo makr graficznych (do
rysowania obrazków) z elastycznym interfejsem i obsługą koloru. Są też
makra do kolorowania lub cieniowania komórek tabel.

%package -n texlive-tex-qpxqtx
Summary:	QuasiTimes and TX fonts typesetting support
Summary(pl.UTF-8):	Wsparcie dla składu fontami QuasiTimes i TX
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Requires:	%{shortname}-fonts-qpxqtx
Obsoletes:	tetex-tex-qpx
Obsoletes:	tetex-tex-qtx

%description -n texlive-tex-qpxqtx
QuasiTimes and TX fonts typesetting support.

%description -n texlive-tex-qpxqtx -l pl.UTF-8
Wsparcie dla składu fontami QuasiTimes i TX.

%package -n texlive-tex-huhyphen
Summary:	Hungarian hyphenation
Summary(hu.UTF-8):	Magyar elválasztás
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-tex-huhyphen
Hungarian hyphenation.

%description -n texlive-tex-huhyphen -l hu.UTF-8
Magyar elválasztás.

%package -n texlive-tex-ruhyphen
Summary:	Russian hyphenation
Summary(pl.UTF-8):	Rosyjskie reguły przenoszenia wyrazów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Provides:	tetex-tex-ruhyphen
Obsoletes:	tetex-tex-ruhyphen

%description -n texlive-tex-ruhyphen
A collection of Russian hyphenation patterns supporting a number of
Cyrillic font encodings, including T2, UCY (Omega Unicode Cyrillic),
LCY, LWN (OT2), and koi8-r.

%description -n texlive-tex-ruhyphen -l pl.UTF-8
Zestaw rosyjskich wzorców przenoszenia wyrazów obsługujący wiele
kodowań fontów w cyrylicy, włącznie z T2, UCY (Omega Unicode
Cyrillic), LCY, LWN (OT2) i koi8-r.

%package -n texlive-tex-spanish
Summary:	Various TeX related files for typesetting documents written in Spanish
Summary(pl.UTF-8):	Różne pliki TeXowe służące do składu dokumentów w języku hiszpańskim
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-tex-spanish
Obsoletes:	tetex-tex-spanishb

%description -n texlive-tex-spanish
Various TeX related files for typesetting documents written in
Spanish, including hyphenation and dictionaries.

%description -n texlive-tex-spanish -l pl.UTF-8
Różne pliki TeXowe służące do składu dokumentów napisanych w języku
hiszpańskim - w tym reguły przenoszenia wyrazów i słowniki.

%package -n texlive-tex-texdraw
Summary:	Graphical macros, using embedded PostScript
Summary(pl.UTF-8):	Makra graficzne używające osadzanego PostScriptu
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-tex-texdraw

%description -n texlive-tex-texdraw
Graphical macros, using embedded PostScript.

%description -n texlive-tex-texdraw -l pl.UTF-8
Makra graficzne używające osadzanego PostScriptu.

%package -n texlive-tex-thumbpdf
Summary:	Thumbnails for PDFTeX and dvips/ps2pdf
Summary(pl.UTF-8):	Ikonki dla PDFTeXa i dvips/ps2pdf
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-tex-thumbpdf

%description -n texlive-tex-thumbpdf
Provides support, using Perl, for thumbnails in pdfTeX and
dvips/ps2pdf, using ghostscript to generate the thumbnails which get
represented in a TeX readable file that is read by the package
thumbpdf.sty to automatically include the thumbnails. Works with both
plain TeX and LaTeX.

%description -n texlive-tex-thumbpdf -l pl.UTF-8
Pakiet przy pomocy Perla dodaje ikonki w pdfTeXu i dvips/ps2pdf przy
użyciu ghostscripta. Ikonki są reprezentowane w pliku czytanym przez
TeXa, który jest wywoływany z thumbpdf.sty, aby automatycznie dołączyć
ikonki. Działa z formatami plain TeX i LaTeX.

%package -n texlive-tex-ukrhyph
Summary:	Ukranian hyphenation
Summary(pl.UTF-8):	Ukraińskie zasady przenoszenia wyrazów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Provides:	tetex-tex-ukrhyph
Obsoletes:	tetex-tex-ukrhyph

%description -n texlive-tex-ukrhyph
This package allows the use of different hyphenation patterns for the
Ukrainian language for various Cyrillic font encodings. Contains
packages implementing traditional rules, modern rules, and combined
English-Ukrainian hyphenation.

%description -n texlive-tex-ukrhyph -l pl.UTF-8
Ten pakiet pozwala na używanie różnych wzorców przenoszenia wyrazów
dla języka ukraińskiego z różnymi kodowaniami fontów z cyrylicą.
Zawiera pakiety z implementacją reguł tradycyjnych, współczesnych i
łączonych angielsko-ukraińskich.

%package -n texlive-latex-variations
Summary:	Typeset tables of variations of functions
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-latex-variations
Typeset tables of variations of functions.

%package -n texlive-latex-lang-thai
Summary:	Thai language support
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-latex-lang-thai
Thai language support.

%package -n texlive-latex-lang-vietnam
Summary:	Vietnamese language support
Summary(pl.UTF-8):	Wsparcie dla języka wietnamskiego
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-latex-urwvn
Obsoletes:	tetex-latex-vietnam
Obsoletes:	tetex-tex-vietnam

%description -n texlive-latex-lang-vietnam
Vietnamese language support.

%description -n texlive-latex-lang-vietnam -l pl.UTF-8
Wsparcie dla języka wietnamskiego.

%package -n texlive-tex-xypic
Summary:	Package for typesetting a variety of graphs and diagrams with TeX
Summary(pl.UTF-8):	Pakiet do składania w TeXu różnych wykresów i diagramów
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Requires:	%{shortname}-fonts-xypic
Obsoletes:	tetex-tex-xypic
Obsoletes:	tetex-xypic

%description -n texlive-tex-xypic
A package for typesetting a variety of graphs and diagrams with TeX.
Xy-pic works with most formats (including LaTeX, AMS-LaTeX, AMS-TeX,
and plain TeX), in particular Xy-pic is provided as a LaTeX2e
`supported package'.

%description -n texlive-tex-xypic -l pl.UTF-8
Pakiet do składania w TeXu różnych wykresów i diagramów. Xy-pic działa
z większością formatów (w tym LaTeX, AMS-LaTeX, AMS-TeX i plain TeX),
w szczególności jest dołączany jako "wspierany pakiet" LaTeX2e.

%package -n texlive-tex-xkeyval
Summary:	Extension to keyval package
Summary(pl.UTF-8):	Rozszerzenie do pakietu keyval
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{shortname}
Obsoletes:	tetex-tex-xkeyval

%description -n texlive-tex-xkeyval
Extension to keyval package.

%description -n texlive-tex-xkeyval -l pl.UTF-8
Rozszerzenie do pakietu keyval.

# # Fonts packages #

%package -n texlive-fonts-doc
Summary:	Font documentation
Group:		Documentation

%description -n texlive-fonts-doc
Font documentation.

%package -n texlive-fonts-adobe
Summary:	Adobe fonts
Summary(pl.UTF-8):	Fonty Adobe
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-adobe
Obsoletes:	tetex-fonts-adobe

%description -n texlive-fonts-adobe
Adobe fonts.

%description -n texlive-fonts-adobe -l pl.UTF-8
Fonty Adobe.

%package -n texlive-fonts-larm
Summary:	Larm (cyrillic) fonts
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-larm
Larm (cyrillic) fonts.

%package -n texlive-fonts-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl.UTF-8):	Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-ae

%description -n texlive-fonts-ae
Virtual fonts for PDF-files with T1 encoded CMR-fonts.

%description -n texlive-fonts-ae -l pl.UTF-8
Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1.

%package -n texlive-fonts-ams
Summary:	AMS fonts
Summary(pl.UTF-8):	Fonty AMS
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Requires:	%{shortname}-latex-bibtex
Provides:	texlive-fonts-type1-bluesky
Provides:	tetex-fonts-ams
Obsoletes:	tetex-fonts-ams

%description -n texlive-fonts-ams
AMS fonts.

%description -n texlive-fonts-ams -l pl.UTF-8
Fonty AMS.

%package -n texlive-fonts-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-antp

%description -n texlive-fonts-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%description -n texlive-fonts-antp -l pl.UTF-8
Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako
Type 1.

%package -n texlive-fonts-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl.UTF-8):	Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-antt

%description -n texlive-fonts-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description -n texlive-fonts-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package -n texlive-fonts-arphic
Summary:	Arphic fonts
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-arphic
Arphic fonts.

%package -n texlive-fonts-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl.UTF-8):	Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-bbm

%description -n texlive-fonts-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description -n texlive-fonts-bbm -l pl.UTF-8
Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa.

%package -n texlive-fonts-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl.UTF-8):	Tablicowy tłusty font sans serif dla LaTeXa
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-bbold

%description -n texlive-fonts-bbold
Sans serif blackboard bold for LaTeX.

%description -n texlive-fonts-bbold -l pl.UTF-8
Tablicowy tłusty font sans serif dla LaTeXa.

%package -n texlive-fonts-bitstream
Summary:	Bitstream fonts
Summary(pl.UTF-8):	Fonty Bitstream
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-bitstream

%description -n texlive-fonts-bitstream
Bitstream fonts.

%description -n texlive-fonts-bitstream -l pl.UTF-8
Fonty Bitstream.

%package -n texlive-fonts-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl.UTF-8):	Polska wersja fontów Computer Concrete
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-cc-pl

%description -n texlive-fonts-cc-pl
Polish version of Computer Concrete fonts.

%description -n texlive-fonts-cc-pl -l pl.UTF-8
Polska wersja fontów Computer Concrete.

%package -n texlive-fonts-cg
Summary:	Compugraphic fonts
Summary(pl.UTF-8):	Fonty Compugraphic
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-cg

%description -n texlive-fonts-cg
Compugraphic fonts.

%description -n texlive-fonts-cg -l pl.UTF-8
Fonty Compugraphic.

%package -n texlive-fonts-cm
Summary:	Computer Modern fonts
Summary(pl.UTF-8):	Fonty Computer Modern
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-cm
Obsoletes:	tetex-fonts-cm

%description -n texlive-fonts-cm
Computer Modern fonts.

%description -n texlive-fonts-cm -l pl.UTF-8
Fonty Computer Modern.

%package -n texlive-fonts-cmbright
Summary:	CM Bright fonts
Summary(pl.UTF-8):	Fonty CM Bright
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-cmbright

%description -n texlive-fonts-cmbright
CM Bright fonts.

%description -n texlive-fonts-cmbright -l pl.UTF-8
Fonty CM Bright.

%package -n texlive-fonts-cmsuper
Summary:	CM Super fonts
Summary(hu.UTF-8):	CM Super betűtípus
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-cmsuper
CM Super fonts.

%description -n texlive-fonts-cmsuper -l hu.UTF-8
CM Super betűtípus


%package -n texlive-fonts-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl.UTF-8):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-cmcyr
Obsoletes:	tetex-fonts-cmcyr
Obsoletes:	texlive-fonts-type1-cmcyr

%description -n texlive-fonts-cmcyr
Computer Modern fonts extended with Russian letters.

%description -n texlive-fonts-cmcyr -l pl.UTF-8
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package -n texlive-fonts-cmextra
Summary:	Extra Computer Modern fonts, from the American Mathematical Society
Summary(pl.UTF-8):	Dodatkowe fonty Computer Modern z AMS
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-cmextra
Obsoletes:	tetex-fonts-cmextra

%description -n texlive-fonts-cmextra
Extra Computer Modern fonts, from the American Mathematical Society.

%description -n texlive-fonts-cmextra -l pl.UTF-8
Dodatkowe fonty Computer Modern z AMS (American Mathematical Society).

%package -n texlive-fonts-concmath
Summary:	Concrete Math fonts
Summary(pl.UTF-8):	Fonty matematyczne Concrete Math
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-concmath

%description -n texlive-fonts-concmath
Concrete Math fonts.

%description -n texlive-fonts-concmath -l pl.UTF-8
Fonty matematyczne Concrete Math.

%package -n texlive-fonts-concrete
Summary:	Concrete Roman fonts
Summary(pl.UTF-8):	Fonty Concrete Roman
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-concrete

%description -n texlive-fonts-concrete
Concrete Roman fonts, designed by Donald E. Knuth, originally for use
with Euler math fonts.

%description -n texlive-fonts-concrete -l pl.UTF-8
Fonty Concrete Roman, opracowane przez Donalda E. Knutha, oryginalnie
przeznaczone do używania z fontami matematycznymi Euler.

%package -n texlive-fonts-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Summary(pl.UTF-8):	Fonty MetaFont Computer Modern dla języków czeskiego i słowackiego
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-cs

%description -n texlive-fonts-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description -n texlive-fonts-cs -l pl.UTF-8
Fonty MetaFont Computer Modern zmodyfikowane pod kątem języków
czeskiego i słowackiego.

%package -n texlive-fonts-ecc
Summary:	Sources for the European Concrete fonts
Summary(pl.UTF-8):	Źródła dla fontów European Concrete
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-ecc

%description -n texlive-fonts-ecc
The MetaFont sources and tfm files of the European Concrete Fonts.
This is the EC implementation of Knuth's Concrete fonts, including
also the corresponding text companion fonts.

%description -n texlive-fonts-ecc -l pl.UTF-8
Źródła MetaFonta i pliki tfm dla fontów European Concrete. Jest to
implementacja EC fontów Concrete Knutha, włącznie z odpowiadającymi
tekstowymi fontami towarzyszącymi.

%package -n texlive-fonts-eurosym
Summary:	The new European currency symbol for the Euro
Summary(pl.UTF-8):	Symbol nowej europejskiej waluty Euro
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-eurosym

%description -n texlive-fonts-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing
several shapes (normal, slanted, bold, outline).

%description -n texlive-fonts-eurosym -l pl.UTF-8
Symbol nowej europejskiej waluty Euro, zaimplementowany w Metafoncie,
z użyciem oficjalnych wymiarów wg Komisji Europejskiej, dostarczający
różnych kształtów (normalnego, pochylonego, tłustego, szkicowanego).

%package -n texlive-fonts-eulervm
Summary:	The Virtual Euler Math fonts
Summary(pl.UTF-8):	Fonty Virtual Euler Math
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-eulervm

%description -n texlive-fonts-eulervm
Euler-VM is a set of _virtual_ math fonts based on Euler and CM. This
approach has several advantages over immediately using the _real_
Euler fonts: Most noticeably, less TeX resources are consumed, the
quality of various math symbols is improved, and a usable \hslash
symbol can be provided.

%description -n texlive-fonts-eulervm -l pl.UTF-8
Euler-VM to zbiór _wirtualnych_ fontów matematycznych opartych na
fontach Euler i CM. Podejście to ma różne zalety nad bezpośrednim
używaniem _prawdziwych_ fontów Euler: najbardziej zauważalnie, używane
jest mniej zasobów TeXa, poprawiona jest jakość różnych symboli
matematycznych i może być dostępny używalny symbol \hslash.

%package -n texlive-fonts-euxm
Summary:	Fonts similar to EUSM but with two more characters
Summary(pl.UTF-8):	Fonty podobne do EUSM, ale z dwoma dodatkowymi znakami
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-euxm

%description -n texlive-fonts-euxm
Fonts like EUSM but with two more characters needed for Concrete Math
included in TeXLive distribution in fonts3.

%description -n texlive-fonts-euxm -l pl.UTF-8
Fonty podobne do EUSM, ale z dwoma dodatkowymi znakami, potrzebnymi
dla Concrete Math dołączonego w fonts3 dystrybucji TeXLive.

%package -n texlive-fonts-gothic
Summary:	Gothic and ornamental initial fonts by Yannis Haralambous
Summary(pl.UTF-8):	Początkowe fonty gotyckie i ornamentowe Yannisa Haralambousa
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-gothic

%description -n texlive-fonts-gothic
Gothic and ornamental initial fonts by Yannis Haralambous.

%description -n texlive-fonts-gothic -l pl.UTF-8
Początkowe fonty gotyckie i ornamentowe Yannisa Haralambousa.

%package -n texlive-fonts-hoekwater
Summary:	Converted mflogo font
Summary(pl.UTF-8):	Przekonwertowany font mflogo
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-hoekwater

%description -n texlive-fonts-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by
Taco Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2,
xipa.

%description -n texlive-fonts-hoekwater -l pl.UTF-8
Fonty oryginalnie stworzone w MetaFoncie, przekształcone do
PostScriptu przez Taco Hoekwatera; zawierają: logo, manfnt, rsfs,
stmaryrd, wasy, wasy2, xipa.

%package -n texlive-fonts-jknappen
Summary:	Miscellaneous packages by Joerg Knappen
Summary(pl.UTF-8):	Różne pakiety autorstwa Joerga Knappena
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Requires:	%{shortname}-latex
Provides:	tetex-fonts-jknappen
Obsoletes:	tetex-fonts-jknappen
Obsoletes:	tetex-latex-jknappen
Obsoletes:	texlive-latex-jknappen

%description -n texlive-fonts-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%description -n texlive-fonts-jknappen -l pl.UTF-8
Różne makra, głównie do używania dodatkowych fontów autorstwa Joerga
Knappena. Zawiera sgmlcmpt.

%package -n texlive-fonts-kpfonts
Summary:	A complete set of fonts for text and mathematics
Summary(hu.UTF-8):	Betűtípusok teljes készlete (matematikai) szövegekhez
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-kpfonts
A complete set of fonts for text and mathematics.

%description -n texlive-fonts-kpfonts -l hu.UTF-8
Betűtípusok teljes készlete (matematikai) szövegekhez.

%package -n texlive-fonts-latex
Summary:	Basic LaTeX fonts
Summary(pl.UTF-8):	Podstawowe fonty dla LaTeXa
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-latex
Obsoletes:	tetex-fonts-latex

%description -n texlive-fonts-latex
Basic LaTeX fonts.

%description -n texlive-fonts-latex -l pl.UTF-8
Podstawowe fonty dla LaTeXa.

%package -n texlive-fonts-lh
Summary:	Olga Lapko's LH fonts
Summary(pl.UTF-8):	Fonty LH Olgi Lapko
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-lh

%description -n texlive-fonts-lh
The lh fonts for the `T2'/X2 encodings (for cyrillic languages).

%description -n texlive-fonts-lh -l pl.UTF-8
Fonty lh dla kodowań `T2'/X2 (dla języków zapisywanych cyrylicą).

%package -n texlive-fonts-lm
Summary:	Latin Modern family fonts
Summary(pl.UTF-8):	Fonty z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-lm

%description -n texlive-fonts-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%description -n texlive-fonts-lm -l pl.UTF-8
Rodzina fontów Latin Modern, oparta na fontach Computer Modern
przekazanych do domeny publicznej przez AMS (copyright (C) 1997 AMS).
Zawiera wiele dodatkowych znaków, głównie z akcentami, ale nie tylko.
Jest jeden zbiór fontów postscriptowych oraz cztery zbiory plików TeX
Font Metric, odpowiadających: kodowaniu Cork (cork-*.tfm); kodowaniu
QX (qx-*.tfm); kodowaniu TeX'n'ANSI zwanemu także LY1
(texnansi-*.tfm); oraz Text Companion dla fontów EC zwanemu także TS1
(ts1-*.tfm). Zakłada się, że potencjalny użytkownik wie, co zrobić z
tymi wszystkimi plikami. Autorem jest Bogusław Jackowski.

%package -n texlive-fonts-marvosym
Summary:	Martin Vogel's Symbol (marvosym) font
Summary(pl.UTF-8):	Font Symbol Martina Vogela (marvosym)
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-marvosym

%description -n texlive-fonts-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%description -n texlive-fonts-marvosym -l pl.UTF-8
Font Symbol Martina Vogela (marvosym) to font zawierający: symbol
waluty Euro zdefiniowany przez Komisję Europejską; symbole waluty Euro
dla krojów Times, Helvetica i Courier; symbole dla inżynierii
strukturalnej; symbole dla przekroi poprzecznych; symbole
astronomiczne (Słońce, Księżyc, planety); 12 znaków Zodiaku; symbole
krawieckie; znak CE i inne.

%package -n texlive-fonts-mflogo
Summary:	Logo fonts
Summary(pl.UTF-8):	Fonty logo
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-mflogo

%description -n texlive-fonts-mflogo
Logo fonts.

%description -n texlive-fonts-mflogo -l pl.UTF-8
Fonty logo.

%package -n texlive-fonts-misc
Summary:	Miscellaneous fonts
Summary(pl.UTF-8):	Różne fonty
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-misc

%description -n texlive-fonts-misc
Miscellaneous fonts.

%description -n texlive-fonts-misc -l pl.UTF-8
Fonty różne.

%package -n texlive-fonts-monotype
Summary:	Monotype fonts
Summary(pl.UTF-8):	Fonty Monotype
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-monotype

%description -n texlive-fonts-monotype
Monotype fonts.

%description -n texlive-fonts-monotype -l pl.UTF-8
Fonty Monotype.

%package -n texlive-fonts-omega
Summary:	Fonts for Omega - extended unicode TeX
Summary(pl.UTF-8):	Fonty dla Omegi - TeXa ze wsparciem dla unikodu
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-omega

%description -n texlive-fonts-omega
Fonts for Omega - extended unicode TeX.

%description -n texlive-fonts-omega -l pl.UTF-8
Fonty dla Omegi - TeXa ze wsparciem dla unikodu.

%package -n texlive-fonts-other
Summary:	Other fonts
Summary(hu.UTF-8):	További betűtípusok
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-cbgreek
Obsoletes:	tetex-fonts-dstroke
Obsoletes:	tetex-fonts-pazo
Obsoletes:	tetex-fonts-type1-dstroke
Obsoletes:	tetex-fonts-type1-qfonts
Obsoletes:	tetex-fonts-type1-tt2001
Obsoletes:	tetex-qfonts

%description -n texlive-fonts-other
Other fonts.

%description -n texlive-fonts-other -l hu.UTF-8
További betűtípusok.

%package -n texlive-fonts-pl
Summary:	Polish fonts
Summary(pl.UTF-8):	Polskie fonty
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-pl

%description -n texlive-fonts-pl
Polish fonts.

%description -n texlive-fonts-pl -l pl.UTF-8
Polskie fonty.

%package -n texlive-fonts-px
Summary:	PX fonts
Summary(pl.UTF-8):	Fonty PX
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-px

%description -n texlive-fonts-px
PX fonts.

%description -n texlive-fonts-px -l pl.UTF-8
Fonty PX.

%package -n texlive-fonts-qpxqtx
Summary:	Additional fonts for QTX package
Summary(pl.UTF-8):	Dodatkowe fonty dla pakietu QTX
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
# I hope qpxqtx doesn't need qfonts
# Requires:	%{shortname}-fonts-qfonts = %{epoch}:%{version}-%{release}
Requires:	%{shortname}-fonts-tx
Obsoletes:	tetex-fonts-qpx
Obsoletes:	tetex-fonts-qtx

%description -n texlive-fonts-qpxqtx
Additional fonts for QTX package.

%description -n texlive-fonts-qpxqtx -l pl.UTF-8
Dodatkowe fonty dla pakietu QTX.

%package -n texlive-fonts-rsfs
Summary:	Fonts of uppercase script letters for scientific and mathematical typesetting
Summary(pl.UTF-8):	Fonty wielkich liter pisanych do składania dokumentów naukowych i matematycznych
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-rsfs

%description -n texlive-fonts-rsfs
Fonts of uppercase script letters for use as symbols in scientific and
mathematical typesetting, in contrast to the informal script fonts
such as that used for the `calligraphic' symbols in the TeX math
symbol font.

%description -n texlive-fonts-rsfs -l pl.UTF-8
Fonty wielkich liter pisanych do używania jako symbole przy składaniu
dokumentów naukowych i matematycznych, w odróżnieniu od nieformalnych
fontów pisanych takich jak używane do symboli "kaligraficznych" w
matematycznym foncie TeXowym symbol.

%package -n texlive-fonts-stmaryrd
Summary:	St Mary Road symbols for functional programming
Summary(pl.UTF-8):	Symbole St Mary Road do programowania funkcyjnego
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-stmaryrd
Obsoletes:	tetex-fonts-stmaryrd

%description -n texlive-fonts-stmaryrd
St Mary Road symbols for functional programming.

%description -n texlive-fonts-stmaryrd -l pl.UTF-8
Symbole St Mary Road do programowania funkcyjnego.

%package -n texlive-fonts-tx
Summary:	TX fonts
Summary(pl.UTF-8):	Fonty TX
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-tx

%description -n texlive-fonts-tx
TX fonts.

%description -n texlive-fonts-tx -l pl.UTF-8
Fonty TX.

%package -n texlive-fonts-uhc
Summary:	UHC fonts
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-uhc
UHC fonts.

%package -n texlive-fonts-urw
Summary:	URW fonts
Summary(pl.UTF-8):	Fonty URW
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-urw

%description -n texlive-fonts-urw
URW fonts.

%description -n texlive-fonts-urw -l pl.UTF-8
Fonty URW.

%package -n texlive-fonts-vnr
Summary:	VNR fonts
Summary(pl.UTF-8):	Fonty VNR
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-vnr

%description -n texlive-fonts-vnr
VNR fonts.

%description -n texlive-fonts-vnr -l pl.UTF-8
Fonty VNR.

%package -n texlive-fonts-urw35vf
Summary:	urw35vf fonts
Summary(hu.UTF-8):	urw35vf betűtípus
Summary(pl.UTF-8):	Fonty urw35vf
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-urw35vf
urw35vf fonts.

%description -n texlive-fonts-urw35vf -l hu.UTF-8
urw35vf betűtípus.

%package -n texlive-fonts-wadalab
Summary:	Wadalab fonts
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-wadalab
Wadalab fonts.

%package -n texlive-fonts-wasy
Summary:	Waldis symbol fonts
Summary(pl.UTF-8):	Fonty Waldis symbol
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-wasy
Obsoletes:	tetex-fonts-wasy

%description -n texlive-fonts-wasy
Waldis symbol fonts.

%description -n texlive-fonts-wasy -l pl.UTF-8
Fonty Waldis symbol.

%package -n texlive-fonts-xypic
Summary:	Xy-pic fonts
Summary(pl.UTF-8):	Fonty Xy-pic
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-xypic

%description -n texlive-fonts-xypic
Xy-pic fonts.

%description -n texlive-fonts-xypic -l pl.UTF-8
Fonty Xy-pic.

%package -n texlive-fonts-yandy
Summary:	European Modern fonts from Y&Y
Summary(pl.UTF-8):	Fonty European Modern od Y&Y
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-yandy

%description -n texlive-fonts-yandy
European Modern fonts from Y&Y.

%description -n texlive-fonts-yandy -l pl.UTF-8
Fonty European Modern od Y&Y.

%package -n texlive-fonts-type1-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl.UTF-8):	Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-antp

%description -n texlive-fonts-type1-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%description -n texlive-fonts-type1-antp -l pl.UTF-8
Antykwa Półtawskiego - rodzina tradycyjnych polskich czcionek jako
Type 1.

%package -n texlive-fonts-type1-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl.UTF-8):	Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-antt

%description -n texlive-fonts-type1-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description -n texlive-fonts-type1-antt -l pl.UTF-8
Antykwa Toruńska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package -n texlive-fonts-type1-arphic
Summary:	Type1 Arphic fonts
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-type1-arphic
Type1 Arphic fonts.

%package -n texlive-fonts-type1-belleek
Summary:	Free replacement for basic MathTime fonts
Summary(pl.UTF-8):	Wolnodostępny zamiennik podstawowych fontów MathTime
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-belleek

%description -n texlive-fonts-type1-belleek
Free replacement for basic MathTime fonts.

%description -n texlive-fonts-type1-belleek -l pl.UTF-8
Wolnodostępny zamiennik podstawowych fontów MathTime.

%package -n texlive-fonts-type1-bitstream
Summary:	Bitstream fonts
Summary(pl.UTF-8):	Fonty Bitstream
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-bitstrea

%description -n texlive-fonts-type1-bitstream
Bitstream fonts.

%description -n texlive-fonts-type1-bitstream -l pl.UTF-8
Fonty Bitstream.

%package -n texlive-fonts-type1-bluesky
Summary:	Computer Modern family fonts
Summary(pl.UTF-8):	Fonty z rodziny Computer Modern
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-type1-bluesky
Obsoletes:	tetex-fonts-type1-bluesky

%description -n texlive-fonts-type1-bluesky
Computer Modern family fonts.

%description -n texlive-fonts-type1-bluesky -l pl.UTF-8
Fonty z rodzony Computer Modern.

%package -n texlive-fonts-type1-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl.UTF-8):	Polska wersja fontów Computer Concrete
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-cc-pl

%description -n texlive-fonts-type1-cc-pl
Polish version of Computer Concrete fonts.

%description -n texlive-fonts-type1-cc-pl -l pl.UTF-8
Polska wersja fontów Computer Concrete.

%package -n texlive-fonts-type1-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl.UTF-8):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-cmcyr

%description -n texlive-fonts-type1-cmcyr
Computer Modern fonts extended with Russian letters.

%description -n texlive-fonts-type1-cmcyr -l pl.UTF-8
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package -n texlive-fonts-type1-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Summary(pl.UTF-8):	Fonty MetaFont Computer Modern dla języków czeskiego i słowackiego
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-cs

%description -n texlive-fonts-type1-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description -n texlive-fonts-type1-cs -l pl.UTF-8
Fonty MetaFont Computer Modern zmodyfikowane pod kątem języków
czeskiego i słowackiego.

%package -n texlive-fonts-type1-eurosym
Summary:	The new European currency symbol for the Euro
Summary(pl.UTF-8):	Symbol nowej europejskiej waluty Euro
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-eurosym

%description -n texlive-fonts-type1-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing
several shapes (normal, slanted, bold, outline).

%description -n texlive-fonts-type1-eurosym -l pl.UTF-8
Symbol nowej europejskiej waluty Euro, zaimplementowany w Metafoncie,
z użyciem oficjalnych wymiarów wg Komisji Europejskiej, dostarczający
różnych kształtów (normalnego, pochylonego, tłustego, szkicowanego).

%package -n texlive-fonts-type1-hoekwater
Summary:	Converted mflogo font
Summary(pl.UTF-8):	Przekonwertowany font mflogo
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-hoekwater

%description -n texlive-fonts-type1-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by
Taco Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2,
xipa.

%description -n texlive-fonts-type1-hoekwater -l pl.UTF-8
Fonty oryginalnie stworzone w MetaFoncie, przekształcone do
PostScriptu przez Taco Hoekwatera; zawierają: logo, manfnt, rsfs,
stmaryrd, wasy, wasy2, xipa.

%package -n texlive-fonts-type1-fpl
Summary:	SC/OsF fonts for URW Palladio L
Summary(pl.UTF-8):	Fonty SC/OsF dla URW Palladio L
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-fpl

%description -n texlive-fonts-type1-fpl
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L which
are compatible with respect to metrics with the Palatino SC/OsF fonts
from Adobe. Note that it is not the author's aim to exactly reproduce
the outlines of the original Adobe fonts. The SC and OsF in the FPL
Fonts were designed with the glyphs from URW Palladio L as starting
point. For some glyphs (eg 'o') the author got the best result by
scaling and boldening. For others (eg 'h') shifting selected portions
of the character gave more satisfying results. All this was done using
the free font editor FontForge <http://fontforge.sf.net/>. The kerning
data in these fonts comes from Walter Schmidt's improved Palatino
metrics.

%description -n texlive-fonts-type1-fpl -l pl.UTF-8
Fonty FPL dostarczają zbiór fontów SC/OsF dla URW Palladio L, które są
kompatybilne co do metryk z fontami Palatino SC/OsF firmy Adobe.
Należy jednak zaznaczyć, że celem autora nie jest dokładne odtworzenie
kształtów oryginalnych fontów Adobe. SC i OsF w fontach FPL były
projektowane w oparciu o glify z URW Palladio L. Dla niektórych glifów
(np. 'o') autor uzyskał najlepszy wynik poprzez skalowanie i
pogrubianie. Dla innych (np. 'h') przesuwanie wybranych części znaku
dało lepsze wyniki. Wszystko to zostało zrobione przy użyciu
wolnodostępnego edytora fontów FontForge <http://fontforge.sf.net/>.
Dane dla kerningu w tych fontach pochodzą z ulepszonych metryk
Palatino Waltera Schmidta.

%package -n texlive-fonts-type1-lm
Summary:	Type1 Latin Modern family fonts
Summary(pl.UTF-8):	Fonty Type1 z rodziny Latin Modern
Group:		Applications/Publishing/TeX
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-lm

%description -n texlive-fonts-type1-lm
Latin Modern family of fonts, based on the Computer Modern fonts
released into public domain by AMS (copyright (C) 1997 AMS). Contain a
lot of additional characters, mainly accented ones, but not only.
There is a one set of PostScript fonts and four sets of TeX Font
Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); and
Text Companion for EC fonts aka TS1 (ts1-*.tfm). It is presumed that a
potential user knows what to do with all these files. The author is
Boguslaw Jackowski.

%description -n texlive-fonts-type1-lm -l pl.UTF-8
Rodzina fontów Latin Modern, oparta na fontach Computer Modern
przekazanych do domeny publicznej przez AMS (copyright (C) 1997 AMS).
Zawiera wiele dodatkowych znaków, głównie z akcentami, ale nie tylko.
Jest jeden zbiór fontów postscriptowych oraz cztery zbiory plików TeX
Font Metric, odpowiadających: kodowaniu Cork (cork-*.tfm); kodowaniu
QX (qx-*.tfm); kodowaniu TeX'n'ANSI zwanemu także LY1
(texnansi-*.tfm); oraz Text Companion dla fontów EC zwanemu także TS1
(ts1-*.tfm). Zakłada się, że potencjalny użytkownik wie, co zrobić z
tymi wszystkimi plikami. Autorem jest Bogusław Jackowski.

%package -n texlive-fonts-type1-marvosym
Summary:	Martin Vogel's Symbol (marvosym) font
Summary(pl.UTF-8):	Font Symbol Martina Vogela (marvosym)
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-marvosym

%description -n texlive-fonts-type1-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%description -n texlive-fonts-type1-marvosym -l pl.UTF-8
Font Symbol Martina Vogela (marvosym) to font zawierający: symbol
waluty Euro zdefiniowany przez Komisję Europejską; symbole waluty Euro
dla krojów Times, Helvetica i Courier; symbole dla inżynierii
strukturalnej; symbole dla przekroi poprzecznych; symbole
astronomiczne (Słońce, Księżyc, planety); 12 znaków Zodiaku; symbole
krawieckie; znak CE i inne.

%package -n texlive-fonts-type1-mathpazo
Summary:	Pazo Math fonts
Summary(pl.UTF-8):	Fonty matematyczne Pazo Math
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-mathpazo

%description -n texlive-fonts-type1-mathpazo
Pazo Math fonts.

%description -n texlive-fonts-type1-mathpazo -l pl.UTF-8
Fonty matematyczne Pazo Math.

%package -n texlive-fonts-type1-omega
Summary:	Type1 fonts for Omega - extended unicode TeX
Summary(pl.UTF-8):	Fonty Type1 dla Omegi - TeXa ze wsparciem dla unikodu
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-omega

%description -n texlive-fonts-type1-omega
Type1 fonts for Omega - extended unicode TeX.

%description -n texlive-fonts-type1-omega -l pl.UTF-8
Fonty Type1 dla Omegi - TeXa ze wsparciem dla unikodu.

%package -n texlive-fonts-type1-pl
Summary:	Polish fonts
Summary(pl.UTF-8):	Polskie fonty
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Requires:	%{shortname}-fonts-ams
Obsoletes:	tetex-fonts-type1-pl

%description -n texlive-fonts-type1-pl
Polish fonts.

%description -n texlive-fonts-type1-pl -l pl.UTF-8
Polskie fonty.

%package -n texlive-fonts-type1-px
Summary:	PX fonts
Summary(pl.UTF-8):	Fonty PX
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-px

%description -n texlive-fonts-type1-px
PX fonts.

%description -n texlive-fonts-type1-px -l pl.UTF-8
Fonty PX.

%package -n texlive-fonts-type1-tx
Summary:	TX fonts
Summary(pl.UTF-8):	Fonty TX
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-tx

%description -n texlive-fonts-type1-tx
TX fonts.

%description -n texlive-fonts-type1-tx -l pl.UTF-8
Fonty TX.

%package -n texlive-fonts-type1-uhc
Summary:	Type1 UHC fonts
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-type1-uhc
Type1 UHC fonts.

%package -n texlive-fonts-type1-urw
Summary:	URW fonts
Summary(pl.UTF-8):	Fonty URW
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Provides:	tetex-fonts-type1-urw
Obsoletes:	tetex-fonts-type1-urw

%description -n texlive-fonts-type1-urw
URW fonts.

%description -n texlive-fonts-type1-urw -l pl.UTF-8
Fonty URW.

%package -n texlive-fonts-type1-vnr
Summary:	Type1 VNR fonts
Summary(pl.UTF-8):	Fonty Type1 VNR
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-vnr

%description -n texlive-fonts-type1-vnr
Type1 VNR fonts.

%description -n texlive-fonts-type1-vnr -l pl.UTF-8
Fonty Type1 VNR.

%package -n texlive-fonts-type1-wadalab
Summary:	Type1 Wadalab fonts
Group:		Fonts
Requires:	%{shortname}-dirs-fonts

%description -n texlive-fonts-type1-wadalab
Type1 Wadalab fonts.

%package -n texlive-fonts-type1-xypic
Summary:	Xy-pic fonts
Summary(pl.UTF-8):	Fonty Xy-pic
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-type1-xypic

%description -n texlive-fonts-type1-xypic
Xy-pic fonts.

%description -n texlive-fonts-type1-xypic -l pl.UTF-8
Fonty Xy-pic.

%package unsorted
Summary:	to be removed
Group:		Applications/Publishing/TeX

%description unsorted 
move files to proper subpackages and remove this dummy supackage

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_mandir}/man5 \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT/var/cache/fonts \
	$RPM_BUILD_ROOT/etc/cron.daily\
	$RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap\
	$RPM_BUILD_ROOT%{_localstatedir}/fonts/map\
	$RPM_BUILD_ROOT%{fmtdir}/pdftex

cd $RPM_BUILD_ROOT%{_datadir}
tar xf %{SOURCE0}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-%{version}-texmf/texmf-dist $RPM_BUILD_ROOT%{texmfdist}
%{__mv} $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots/* $RPM_BUILD_ROOT%{texmfdist}/doc/latex/pgfplots
rmdir $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots
# imho it is unneeded
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/fonts/{ec,fc,utopia}

# This is an empty directory
rmdir $RPM_BUILD_ROOT%{_datadir}/texlive-%{version}-texmf


CURDIR=$(pwd)

# We don't need it
#%{__rm} -rf $RPM_BUILD_ROOT%{texmf}/doc/man
%{__rm} -r $RPM_BUILD_ROOT%{texmfdoc}/source

#perl -pi \
#	-e "s|$RPM_BUILD_ROOT||g;" \
#	$RPM_BUILD_ROOT%{texmf}/web2c/texmf.cnf

# not included in package
#FIXME: but why not included ???
%{__rm} $RPM_BUILD_ROOT%{_datadir}/texinfo/html/texi2html.html
%{__rm} $RPM_BUILD_ROOT%{_infodir}/dir*
%{__rm} $RPM_BUILD_ROOT%{_infodir}/dvipng*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{README.*,hu/man1/readlink.1*}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/lcdf-typetools
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pdf-trans
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/source/generic/hyph-utf8
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/source/generic/patch
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/source/plain/plgraph
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/tex/generic/pdf-trans
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/tex/generic/xecyr
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/gzip

# packaged in asymptote
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/asymptote
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/asymptote
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/tex/latex/asymptote
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/support/asymptote*

# in texlive package
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/a2ping
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/accfonts
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/adhocfilelist
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/arara
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/authorindex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/bibexport
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/bundledoc
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/cachepic
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/checkcites
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/chktex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/context
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/convbkmk
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/ctanify
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/ctanupload
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/de-macro
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/dosepsbin
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/dtxgen
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/dviasm
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/ebong
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/epspdf
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/epstopdf
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/exceltex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/fig4latex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/findhyph
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/fontools
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/fragmaster
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/glossaries
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/installfont
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/jfontmaps
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/latex2man
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/latexdiff
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/latexfileversion
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/latexmk
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/latexpand
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/listbib
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/listings-ext
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/ltxfileinfo
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/lua2dox
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/luaotfload
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/match_parens
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/mathspic
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/mf2pt1
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/mkgrkindex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/mkjobtexmf
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/m-tx
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/multibibliography
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/musixtex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/oberdiek
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pax
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pdfcrop
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pdfjam
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pedigree-perl
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/perltex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pfarrei
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pkfix
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pkfix-helper
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pmx
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/ps2eps
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pst2pdf
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/pst-pdf
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/psutils
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/ptex2pdf
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/purifyeps
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/simpdftex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/splitindex
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/sty2dtx
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/svn-multi
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/tex4ht
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texcount
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texdef
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texdirflatten
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texdoc
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texdoctk
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/allcm.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/allneeded.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/dvi2fax.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/dvired.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/e2pall.pl
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/fmtutil.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/fmtutil-sys.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/fontinst.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/kpsetool.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/kpsewhere.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texliveonfly
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/ps2frag.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/pslatex.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/rubibtex.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/rumakeindex.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/rungs.tlu
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/texconfig-dialog.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/texconfig.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/texconfig-sys.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/texlinks.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/tlmgr.pl
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/updmap.pl
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texlive/updmap-sys.sh
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/texloganalyser
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/thumbpdf
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/typeoutfileinfo
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/ulqda
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/urlbst
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/scripts/vpe

# move format logs to BUILD, so $RPM_BUILD_ROOT is not polluted
# and we can still analyze them
# install -d format-logs
# mv -fv $RPM_BUILD_ROOT%{fmtdir}/*.log format-logs

# xindy files are in %%{texmf}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/xindy

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc

# Create format files
for format in \
	aleph \
 	csplain \
 	etex \
	jadetex \
	lambda \
	lamed \
 	latex \
 	mex \
 	mllatex \
 	mptopdf \
	omega \
 	pdfcsplain \
 	pdfetex \
 	pdfjadetex \
 	pdflatex \
 	pdftex \
 	pdfxmltex \
 	physe \
 	phyzzx \
 	tex \
 	texsis \
 	xetex \
 	xelatex \
 	xmltex; do
 	#TEXMFHOME=$RPM_BUILD_ROOT%{texmfdist} fmtutil --fmtdir $RPM_BUILD_ROOT%{fmtdir} --byfmt=${format}
done

# We don't need the log files
%{__rm} $(find $RPM_BUILD_ROOT%{fmtdir} -name "*.log")

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fixinfodir
%texhash

%postun
%fixinfodir
if [ "$1" = "1" ]; then
	%texhash
fi

%post -n texlive-scripts-extra
%texhash

%postun -n texlive-scripts-extra
%texhash

%post -n texlive-tex-arrayjob
%texhash

%postun -n texlive-tex-arrayjob
%texhash

%post -n texlive-tex-kastrup
%texhash

%postun -n texlive-tex-kastrup
%texhash

%post -n texlive-tex-insbox
%texhash

%postun -n texlive-tex-insbox
%texhash

%post -n texlive-tex-mathdots
%texhash

%postun -n texlive-tex-mathdots
%texhash

%post -n texlive-tex-midnight
%texhash

%postun -n texlive-tex-midnight
%texhash

%post -n texlive-tex-ofs
%texhash

%postun -n texlive-tex-ofs
%texhash

%post -n texlive-tex-physe
%texhash

%postun -n texlive-tex-physe
%texhash

%post -n texlive-tex-velthuis
%texhash

%postun -n texlive-tex-velthuis
%texhash

%post -n texlive-tex-xkeyval
%texhash

%postun -n texlive-tex-xkeyval
%texhash

%post -n texlive-tex-ytex
%texhash

%postun -n texlive-tex-ytex
%texhash

%post -n texlive-makeindex-data
%texhash

%postun -n texlive-makeindex-data
%texhash

%post -n texlive-metapost-data
%texhash

%postun -n texlive-metapost-data
%texhash

%post -n texlive-plain
%texhash

%postun -n texlive-plain
%texhash

%post -n texlive-mex
%texhash

%postun -n texlive-mex
%texhash

%postun -n texlive-amstex
%texhash

%post -n texlive-format-csplain
%texhash

%postun -n texlive-format-csplain
%texhash

%post -n texlive-cslatex
%texhash

%postun -n texlive-cslatex
%texhash

%post -n texlive-enctex
%texhash

%postun -n texlive-enctex
%texhash

%post -n texlive-eplain
%texhash

%postun -n texlive-eplain
%texhash

# ConTeXt format

%post -n texlive-context-data
%texhash

%postun -n texlive-context-data
%texhash

%post -n texlive-format-context-de
%texhash

%postun -n texlive-format-context-de
%texhash

%post -n texlive-format-context-en
%texhash

%postun -n texlive-format-context-en
%texhash

%post -n texlive-format-context-nl
%texhash

%postun -n texlive-format-context-nl
%texhash

%post -n texlive-latex-data
%fixinfodir
%texhash

%postun -n texlive-latex-data
%fixinfodir
%texhash

%post -n texlive-latex-lang
%texhash

%postun -n texlive-latex-lang
%texhash

%post -n texlive-latex-styles
%texhash

%postun -n texlive-latex-styles
%texhash

%post -n texlive-latex-pdftools
%texhash

%postun -n texlive-latex-pdftools
%texhash

%post -n texlive-latex-extend
%texhash

%postun -n texlive-latex-extend
%texhash

%post -n texlive-latex-presentation
%texhash

%postun -n texlive-latex-presentation
%texhash

%post -n texlive-latex-programming
%texhash

%postun -n texlive-latex-programming
%texhash

%post -n texlive-latex-metre
%texhash

%postun -n texlive-latex-metre
%texhash

%post -n texlive-latex-misc
%texhash

%postun -n texlive-latex-misc
%texhash

%post -n texlive-latex-effects
%texhash

%postun -n texlive-latex-effects
%texhash

%post -n texlive-latex-math
%texhash

%postun -n texlive-latex-math
%texhash

%post -n texlive-latex-music
%texhash

%postun -n texlive-latex-music
%texhash

%post -n texlive-latex-physics
%texhash

%postun -n texlive-latex-physics
%texhash

%post -n texlive-latex-games
%texhash

%postun -n texlive-latex-games
%texhash

%post -n texlive-latex-bidi
%texhash

%postun -n texlive-latex-bidi
%texhash

%post -n texlive-latex-biology
%texhash

%postun -n texlive-latex-biology
%texhash

%post -n texlive-latex-chem
%texhash

%postun -n texlive-latex-chem
%texhash

%post -n texlive-latex-ctex
%texhash

%postun -n texlive-latex-ctex
%texhash

%post -n texlive-latex-informatic
%texhash

%postun -n texlive-latex-informatic
%texhash

%post -n texlive-latex-12many
%texhash

%postun -n texlive-latex-12many
%texhash

%post -n texlive-latex-abstract
%texhash

%postun -n texlive-latex-abstract
%texhash

%post -n texlive-latex-accfonts
%texhash

%postun -n texlive-latex-accfonts
%texhash

%post -n texlive-latex-adrconv
%texhash

%postun -n texlive-latex-adrconv
%texhash

%post -n texlive-latex-ae
%texhash

%postun -n texlive-latex-ae
%texhash

%post -n texlive-latex-ams
%texhash

%postun -n texlive-latex-ams
%texhash

%post -n texlive-latex-antp
%texhash

%postun -n texlive-latex-antp
%texhash

%post -n texlive-latex-antt
%texhash

%postun -n texlive-latex-antt
%texhash

%post -n texlive-latex-appendix
%texhash

%postun -n texlive-latex-appendix
%texhash

%post -n texlive-latex-asyfig
%texhash

%postun -n texlive-latex-asyfig
%texhash

%post -n texlive-latex-bardiag
%texhash

%postun -n texlive-latex-bardiag
%texhash

%post -n texlive-latex-bbm
%texhash

%postun -n texlive-latex-bbm
%texhash

%post -n texlive-latex-bbold
%texhash

%postun -n texlive-latex-bbold
%texhash

%post -n texlive-latex-beamer
%texhash

%postun -n texlive-latex-beamer
%texhash

%post -n texlive-latex-bezos
%texhash

%postun -n texlive-latex-bezos
%texhash

%post -n texlive-latex-bibtex-ams
%texhash

%postun -n texlive-latex-bibtex-ams
%texhash

%post -n texlive-latex-bibtex-data
%texhash

%postun -n texlive-latex-bibtex-data
%texhash

%post -n texlive-latex-bibtex-german
%texhash

%postun -n texlive-latex-bibtex-german
%texhash

%post -n texlive-latex-bibtex-pl
%texhash

%postun -n texlive-latex-bibtex-pl
%texhash

%post -n texlive-latex-bibtex-revtex4
%texhash

%postun -n texlive-latex-bibtex-revtex4
%texhash

%post -n texlive-latex-bibtex-jurabib
%texhash

%postun -n texlive-latex-bibtex-jurabib
%texhash

%post -n texlive-latex-bibtex-styles
%texhash

%postun -n texlive-latex-bibtex-styles
%texhash

%post -n texlive-latex-booktabs
%texhash

%postun -n texlive-latex-booktabs
%texhash

%post -n texlive-latex-bosisio
%texhash

%postun -n texlive-latex-bosisio
%texhash

%post -n texlive-latex-caption
%texhash

%postun -n texlive-latex-caption
%texhash

%post -n texlive-latex-carlisle
%texhash

%postun -n texlive-latex-carlisle
%texhash

%post -n texlive-latex-ccfonts
%texhash

%postun -n texlive-latex-ccfonts
%texhash

%post -n texlive-latex-cite
%texhash

%postun -n texlive-latex-cite
%texhash

%post -n texlive-latex-cmbright
%texhash

%postun -n texlive-latex-cmbright
%texhash

%post -n texlive-latex-colortab
%texhash

%postun -n texlive-latex-colortab
%texhash

%post -n texlive-latex-comment
%texhash

%postun -n texlive-latex-comment
%texhash

%post -n texlive-latex-concmath
%texhash

%postun -n texlive-latex-concmath
%texhash

%post -n texlive-latex-currvita
%texhash

%postun -n texlive-latex-currvita
%texhash

%post -n texlive-latex-curves
%texhash

%postun -n texlive-latex-curves
%texhash

%post -n texlive-latex-custom-bib
%texhash

%postun -n texlive-latex-custom-bib
%texhash

%post -n texlive-latex-cyrillic
%texhash

%postun -n texlive-latex-cyrillic
%texhash

%post -n texlive-latex-enumitem
%texhash

%postun -n texlive-latex-enumitem
%texhash

%post -n texlive-latex-exams
%texhash

%postun -n texlive-latex-exams
%texhash

%post -n texlive-latex-float
%texhash

%postun -n texlive-latex-float
%texhash

%post -n texlive-latex-foiltex
%texhash

%postun -n texlive-latex-foiltex
%texhash

%post -n texlive-latex-formlett
%texhash

%postun -n texlive-latex-formlett
%texhash

%post -n texlive-latex-formular
%texhash

%postun -n texlive-latex-formular
%texhash

%post -n texlive-latex-gbrief
%texhash

%postun -n texlive-latex-gbrief
%texhash

%post -n texlive-latex-keystroke
%texhash

%postun -n texlive-latex-keystroke
%texhash

%post -n texlive-latex-labbook
%texhash

%postun -n texlive-latex-labbook
%texhash

%post -n texlive-latex-lcd
%texhash

%postun -n texlive-latex-lcd
%texhash

%post -n texlive-latex-leaflet
%texhash

%postun -n texlive-latex-leaflet
%texhash

%post -n texlive-latex-leftidx
%texhash

%postun -n texlive-latex-leftidx
%texhash

%post -n texlive-latex-lewis
%texhash

%postun -n texlive-latex-lewis
%texhash

%post -n texlive-latex-lm
%texhash

%post -n texlive-latex-lastpage
%texhash

%postun -n texlive-latex-lastpage
%texhash

%postun -n texlive-latex-lm
%texhash

%post -n texlive-latex-lucidabr
%texhash

%postun -n texlive-latex-lucidabr
%texhash

%post -n texlive-latex-marvosym
%texhash

%postun -n texlive-latex-marvosym
%texhash

%post -n texlive-latex-mflogo
%texhash

%postun -n texlive-latex-mflogo
%texhash

%post -n texlive-latex-mfnfss
%texhash

%postun -n texlive-latex-mfnfss
%texhash

%post -n texlive-latex-minitoc
%texhash

%postun -n texlive-latex-minitoc
%texhash

%post -n texlive-latex-mltex
%texhash

%postun -n texlive-latex-mltex
%texhash

%post -n texlive-latex-moreverb
%texhash

%postun -n texlive-latex-moreverb
%texhash

%post -n texlive-latex-multienum
%texhash

%postun -n texlive-latex-multienum
%texhash

%post -n texlive-latex-musictex
%texhash

%postun -n texlive-latex-musictex
%texhash

%post -n texlive-latex-ntheorem
%texhash

%postun -n texlive-latex-ntheorem
%texhash

%post -n texlive-latex-other
%texhash

%postun -n texlive-latex-other
%texhash

%post -n texlive-latex-other-doc
%texhash

%postun -n texlive-latex-other-doc
%texhash

%post -n texlive-latex-pdfslide
%texhash

%postun -n texlive-latex-pdfslide
%texhash

%post -n texlive-latex-pgf
%texhash

%postun -n texlive-latex-pgf
%texhash

%post -n texlive-latex-polynom
%texhash

%postun -n texlive-latex-polynom
%texhash

%post -n texlive-latex-polynomial
%texhash

%postun -n texlive-latex-polynomial
%texhash

%post -n texlive-latex-prosper
%texhash

%postun -n texlive-latex-prosper
%texhash

%post -n texlive-latex-pseudocode
%texhash

%postun -n texlive-latex-pseudocode
%texhash

%post -n texlive-latex-psnfss
%texhash

%postun -n texlive-latex-psnfss
%texhash

%post -n texlive-latex-pst-2dplot
%texhash

%postun -n texlive-latex-pst-2dplot
%texhash

%post -n texlive-latex-pst-3dplot
%texhash

%postun -n texlive-latex-pst-3dplot
%texhash

%post -n texlive-latex-pst-bar
%texhash

%postun -n texlive-latex-pst-bar
%texhash

%post -n texlive-latex-pst-circ
%texhash

%postun -n texlive-latex-pst-circ
%texhash

%post -n texlive-latex-pst-eucl
%texhash

%postun -n texlive-latex-pst-eucl
%texhash

%post -n texlive-latex-pst-diffraction
%texhash

%postun -n texlive-latex-pst-diffraction
%texhash

%post -n texlive-latex-pst-fun
%texhash

%postun -n texlive-latex-pst-fun
%texhash

%post -n texlive-latex-pst-func
%texhash

%postun -n texlive-latex-pst-func
%texhash

%post -n texlive-latex-pst-infixplot
%texhash

%postun -n texlive-latex-pst-infixplot
%texhash

%post -n texlive-latex-pst-fr3d
%texhash

%postun -n texlive-latex-pst-fr3d
%texhash

%post -n texlive-latex-pst-fractal
%texhash

%postun -n texlive-latex-pst-fractal
%texhash

%post -n texlive-latex-pxfonts
%texhash

%post -n texlive-latex-pst-math
%texhash

%postun -n texlive-latex-pst-math
%texhash

%post -n texlive-latex-pst-ob3d
%texhash

%postun -n texlive-latex-pst-ob3d
%texhash

%post -n texlive-latex-pst-optic
%texhash

%postun -n texlive-latex-pst-optic
%texhash

%post -n texlive-latex-pst-optexp
%texhash

%postun -n texlive-latex-pst-optexp
%texhash

%post -n texlive-latex-pst-text
%texhash

%postun -n texlive-latex-pst-text
%texhash

%post -n texlive-latex-pst-uncategorized
%texhash

%postun -n texlive-latex-pst-uncategorized
%texhash

%postun -n texlive-latex-pxfonts
%texhash

%post -n texlive-latex-SIstyle
%texhash

%postun -n texlive-latex-SIstyle
%texhash

%post -n texlive-latex-SIunits
%texhash

%postun -n texlive-latex-SIunits
%texhash

%post -n texlive-latex-siunitx
%texhash

%postun -n texlive-latex-siunitx
%texhash

%post -n texlive-latex-Tabbing
%texhash

%postun -n texlive-latex-Tabbing
%texhash

%post -n texlive-latex-txfonts
%texhash

%postun -n texlive-latex-txfonts
%texhash

%post -n texlive-latex-ucs
%texhash

%postun -n texlive-latex-ucs
%texhash

%post -n texlive-latex-umlaute
%texhash

%postun -n texlive-latex-umlaute
%texhash

%post -n texlive-latex-variations
%texhash

%postun -n texlive-latex-variations
%texhash

%post -n texlive-latex-wasysym
%texhash

%postun -n texlive-latex-wasysym
%texhash

%post -n texlive-latex-xcolor
%texhash

%postun -n texlive-latex-xcolor
%texhash

%post -n texlive-tex-babel
%texhash

%postun -n texlive-tex-babel
%texhash

%post -n texlive-tex-german
%texhash

%postun -n texlive-tex-german
%texhash

%post -n texlive-tex-mfpic
%texhash

%postun -n texlive-tex-mfpic
%texhash

%post -n texlive-tex-misc
%texhash

%postun -n texlive-tex-misc
%texhash

%post -n texlive-tex-pictex
%texhash

%postun -n texlive-tex-pictex
%texhash

%post -n texlive-tex-psizzl
%texhash

%postun -n texlive-tex-psizzl
%texhash

%post -n texlive-tex-pstricks
%texhash

%postun -n texlive-tex-pstricks
%texhash

%post -n texlive-tex-qpxqtx
%texhash

%postun -n texlive-tex-qpxqtx
%texhash

%post -n texlive-tex-huhyphen
%texhash

%postun -n texlive-tex-huhyphen
%texhash

%post -n texlive-tex-ruhyphen
%texhash

%postun -n texlive-tex-ruhyphen
%texhash

%post -n texlive-tex-spanish
%texhash

%postun -n texlive-tex-spanish
%texhash

%post -n texlive-tex-texdraw
%texhash

%postun -n texlive-tex-texdraw
%texhash

%post -n texlive-tex-thumbpdf
%texhash

%postun -n texlive-tex-thumbpdf
%texhash

%post -n texlive-tex-ukrhyph
%texhash

%postun -n texlive-tex-ukrhyph
%texhash

%post -n texlive-latex-lang-thai
%texhash

%postun -n texlive-latex-lang-thai
%texhash

%post -n texlive-latex-lang-vietnam
%texhash

%postun -n texlive-latex-lang-vietnam
%texhash

%post -n texlive-tex-xypic
%texhash

%postun -n texlive-tex-xypic
%texhash

%post -n texlive-fonts-adobe
%texhash

%postun -n texlive-fonts-adobe
%texhash

%post -n texlive-fonts-ams
%texhash

%postun -n texlive-fonts-ams
%texhash

%post -n texlive-fonts-larm
%texhash

%postun -n texlive-fonts-larm
%texhash

%post -n texlive-fonts-ae
%texhash

%postun -n texlive-fonts-ae
%texhash

%post -n texlive-fonts-antp
%texhash

%postun -n texlive-fonts-antp
%texhash

%post -n texlive-fonts-antt
%texhash

%postun -n texlive-fonts-antt
%texhash

%post -n texlive-fonts-bbm
%texhash

%postun -n texlive-fonts-bbm
%texhash

%post -n texlive-fonts-bbold
%texhash

%postun -n texlive-fonts-bbold
%texhash

%post -n texlive-fonts-bitstream
%texhash

%postun -n texlive-fonts-bitstream
%texhash

%post -n texlive-fonts-cc-pl
%texhash

%postun -n texlive-fonts-cc-pl
%texhash

%post -n texlive-fonts-cg
%texhash

%postun -n texlive-fonts-cg
%texhash

%post -n texlive-fonts-cm
%texhash

%postun -n texlive-fonts-cm
%texhash

%post -n texlive-fonts-cmbright
%texhash

%postun -n texlive-fonts-cmbright
%texhash

%post -n texlive-fonts-cmcyr
%texhash

%postun -n texlive-fonts-cmcyr
%texhash

%post -n texlive-fonts-cmextra
%texhash

%postun -n texlive-fonts-cmextra
%texhash

%post -n texlive-fonts-cmsuper
%texhash

%postun -n texlive-fonts-cmsuper
%texhash

%post -n texlive-fonts-concmath
%texhash

%postun -n texlive-fonts-concmath
%texhash

%post -n texlive-fonts-concrete
%texhash

%postun -n texlive-fonts-concrete
%texhash

%post -n texlive-fonts-cs
%texhash

%postun -n texlive-fonts-cs
%texhash

%post -n texlive-fonts-ecc
%texhash

%postun -n texlive-fonts-ecc
%texhash

%post -n texlive-fonts-eurosym
%texhash

%postun -n texlive-fonts-eurosym
%texhash

%post -n texlive-fonts-euxm
%texhash

%postun -n texlive-fonts-euxm
%texhash

%post -n texlive-fonts-gothic
%texhash

%postun -n texlive-fonts-gothic
%texhash

%post -n texlive-fonts-hoekwater
%texhash

%postun -n texlive-fonts-hoekwater
%texhash

%post -n texlive-fonts-jknappen
%texhash

%postun -n texlive-fonts-jknappen
%texhash

%post -n texlive-fonts-latex
%texhash

%postun -n texlive-fonts-latex
%texhash

%post -n texlive-fonts-kpfonts
%texhash

%postun -n texlive-fonts-kpfonts
%texhash

%post -n texlive-fonts-lh
%texhash

%postun -n texlive-fonts-lh
%texhash

%post -n texlive-fonts-lm
%texhash

%postun -n texlive-fonts-lm
%texhash

%post -n texlive-fonts-marvosym
%texhash

%postun -n texlive-fonts-marvosym
%texhash

%post -n texlive-fonts-mflogo
%texhash

%postun -n texlive-fonts-mflogo
%texhash

%post -n texlive-fonts-misc
%texhash

%postun -n texlive-fonts-misc
%texhash

%post -n texlive-fonts-monotype
%texhash

%postun -n texlive-fonts-monotype
%texhash

%post -n texlive-fonts-omega
%texhash

%postun -n texlive-fonts-omega
%texhash

%post -n texlive-fonts-other
%texhash

%postun -n texlive-fonts-other
%texhash

%post -n texlive-fonts-pl
%texhash

%postun -n texlive-fonts-pl
%texhash

%post -n texlive-fonts-px
%texhash

%postun -n texlive-fonts-px
%texhash

%post -n texlive-fonts-qpxqtx
%texhash

%postun -n texlive-fonts-qpxqtx
%texhash

%post -n texlive-fonts-rsfs
%texhash

%postun -n texlive-fonts-rsfs
%texhash

%post -n texlive-fonts-stmaryrd
%texhash

%postun -n texlive-fonts-stmaryrd
%texhash

%post -n texlive-fonts-tx
%texhash

%postun -n texlive-fonts-tx
%texhash

%post -n texlive-fonts-urw
%texhash

%postun -n texlive-fonts-urw
%texhash

%post -n texlive-fonts-urw35vf
%texhash

%postun -n texlive-fonts-urw35vf
%texhash

%post -n texlive-fonts-vnr
%texhash

%postun -n texlive-fonts-vnr
%texhash

%post -n texlive-fonts-wasy
%texhash

%postun -n texlive-fonts-wasy
%texhash

%post -n texlive-fonts-xypic
%texhash

%postun -n texlive-fonts-xypic
%texhash

%post -n texlive-fonts-yandy
%texhash

%postun -n texlive-fonts-yandy
%texhash

%post -n texlive-fonts-type1-antp
%texhash

%postun -n texlive-fonts-type1-antp
%texhash

%post -n texlive-fonts-type1-antt
%texhash

%postun -n texlive-fonts-type1-antt
%texhash

%post -n texlive-fonts-type1-belleek
%texhash

%postun -n texlive-fonts-type1-belleek
%texhash

%post -n texlive-fonts-type1-bitstream
%texhash

%postun -n texlive-fonts-type1-bitstream
%texhash

%post -n texlive-fonts-type1-bluesky
%texhash

%postun -n texlive-fonts-type1-bluesky
%texhash

%post -n texlive-fonts-type1-cc-pl
%texhash

%postun -n texlive-fonts-type1-cc-pl
%texhash

%post -n texlive-fonts-type1-cmcyr
%texhash

%postun -n texlive-fonts-type1-cmcyr
%texhash

%post -n texlive-fonts-type1-cs
%texhash

%postun -n texlive-fonts-type1-cs
%texhash

%post -n texlive-fonts-type1-eurosym
%texhash

%postun -n texlive-fonts-type1-eurosym
%texhash

%post -n texlive-fonts-type1-hoekwater
%texhash

%postun -n texlive-fonts-type1-hoekwater
%texhash

%post -n texlive-fonts-type1-lm
%texhash

%postun -n texlive-fonts-type1-lm
%texhash

%post -n texlive-fonts-type1-marvosym
%texhash

%postun -n texlive-fonts-type1-marvosym
%texhash

%post -n texlive-fonts-type1-mathpazo
%texhash

%postun -n texlive-fonts-type1-mathpazo
%texhash

%post -n texlive-fonts-type1-omega
%texhash

%postun -n texlive-fonts-type1-omega
%texhash

%post -n texlive-fonts-type1-pl
%texhash

%postun -n texlive-fonts-type1-pl
%texhash

%post -n texlive-fonts-type1-px
%texhash

%postun -n texlive-fonts-type1-px
%texhash

%post -n texlive-fonts-type1-tx
%texhash

%postun -n texlive-fonts-type1-tx
%texhash

%post -n texlive-fonts-type1-urw
%texhash

%postun -n texlive-fonts-type1-urw
%texhash

%post -n texlive-fonts-type1-vnr
%texhash

%postun -n texlive-fonts-type1-vnr
%texhash

%post -n texlive-fonts-type1-xypic
%texhash

%postun -n texlive-fonts-type1-xypic
%texhash

%files
%defattr(644,root,root,755)
%dir %{texmfdist}
%dir %{texmfdist}/doc
%dir %{texmfdist}/doc/fonts
%dir %{texmfdist}/doc/generic
%dir %{texmfdist}/doc/latex
%dir %{texmfdist}/doc/support
%dir %{texmfdist}/metapost
%dir %{texmfdist}/scripts
%dir %{texmfdist}/source
%dir %{texmfdist}/source/generic
%dir %{texmfdist}/source/latex
%dir %{texmfdist}/tex
%dir %{texmfdist}/tex/generic
%dir %{texmfdist}/tex/generic/misc
%dir %{texmfdist}/tex/latex


%ghost %{texmfdist}/ls-R

%attr(1777,root,root) /var/cache/fonts


# ***********
# Directories
# ***********
%attr(1777,root,root) %dir %{_localstatedir}
%attr(1777,root,root) %dir %{_localstatedir}/fonts
%attr(1777,root,root) %dir %{_localstatedir}/fonts/map
%attr(1777,root,root) %dir %{fmtdir}
%dir %{fmtdir}/pdftex

%{texmfdist}/fonts/map/fontname

#%{texmf}/fonts/enc/dvips/tetex/09fbbfac.enc
#%{texmf}/fonts/enc/dvips/tetex/0ef0afca.enc
#%{texmf}/fonts/enc/dvips/tetex/10037936.enc
#%{texmf}/fonts/enc/dvips/tetex/1b6d048e.enc
#%{texmf}/fonts/enc/dvips/tetex/71414f53.enc
#%{texmf}/fonts/enc/dvips/tetex/74afc74c.enc
#%{texmf}/fonts/enc/dvips/tetex/aae443f0.enc
#%{texmf}/fonts/enc/dvips/tetex/b6a4d7c7.enc
#%{texmf}/fonts/enc/dvips/tetex/bbad153f.enc
#%{texmf}/fonts/enc/dvips/tetex/d9b29452.enc
#%{texmf}/fonts/enc/dvips/tetex/f7b6d320.enc
#%{texmf}/fonts/map/dvips/tetex/ps2pk35.map

%{texmfdist}/metafont
%{texmfdist}/mft
%{texmfdist}/source/metafont
%{texmfdist}/tex/fontinst
%{texmfdist}/tex/generic/abbr
%{texmfdist}/tex/generic/abstyles
%{texmfdist}/tex/generic/barr
%{texmfdist}/tex/generic/borceux
%{texmfdist}/tex/generic/c-pascal
%{texmfdist}/tex/generic/dehyph-exptl
%{texmfdist}/tex/generic/dratex
%{texmfdist}/tex/generic/ean
%{texmfdist}/tex/generic/edmac
%{texmfdist}/tex/generic/encodings
%{texmfdist}/tex/generic/epsf
%{texmfdist}/tex/generic/fenixpar
%{texmfdist}/tex/generic/fltpoint
%{texmfdist}/tex/generic/iftex
%{texmfdist}/tex/generic/hyph-utf8
%{texmfdist}/tex/generic/hyphenex
%{texmfdist}/tex/generic/genmisc
%{texmfdist}/tex/generic/mathabx
%{texmfdist}/tex/generic/misc/null*
%{texmfdist}/tex/generic/misc/texnames.sty
%{texmfdist}/tex/generic/musixtex
%{texmfdist}/tex/generic/t2
%{texmfdist}/tex/generic/tabto-generic
%{texmfdist}/tex/generic/tap
%{texmfdist}/tex/generic/tex-ewd
%{texmfdist}/tex/generic/tex-ps
%{texmfdist}/tex/generic/xlop
%{texmfdist}/tex/generic/xstring
%{texmfdist}/tex/generic/zhmetrics
%{texmfdist}/tex/lualatex
%{texmfdist}/tex/luatex
%{texmfdist}/tex/texinfo
%{texmfdist}/tex/generic/hyphen
# %{texmf}/fmtutil/format.metafont.cnf
#%%{texmf}/fonts/map/dvips/updmap/*
%{texmfdist}/web2c/amiga-pl.tcx
%{texmfdist}/web2c/cp1250cs.tcx
%{texmfdist}/web2c/cp1250pl.tcx
%{texmfdist}/web2c/cp1250t1.tcx
%{texmfdist}/web2c/cp227.tcx
%{texmfdist}/web2c/cp852-cs.tcx
%{texmfdist}/web2c/cp852-pl.tcx
%{texmfdist}/web2c/cp8bit.tcx
%{texmfdist}/web2c/empty.tcx
%{texmfdist}/web2c/il1-t1.tcx
%{texmfdist}/web2c/il2-cs.tcx
%{texmfdist}/web2c/il2-pl.tcx
%{texmfdist}/web2c/il2-t1.tcx
%{texmfdist}/web2c/kam-cs.tcx
%{texmfdist}/web2c/kam-t1.tcx
%{texmfdist}/web2c/macce-pl.tcx
%{texmfdist}/web2c/macce-t1.tcx
%{texmfdist}/web2c/maz-pl.tcx
%{texmfdist}/web2c/natural.tcx
%{texmfdist}/web2c/tcvn-t5.tcx
%{texmfdist}/web2c/viscii-t5.tcx

%{fmtdir}/pdftex/pdfetex.fmt
%{fmtdir}/tex/tex.fmt

%files -n texlive-dirs-fonts
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts
%dir %{texmfdist}/fonts/afm
%dir %{texmfdist}/fonts/afm/public
%dir %{texmfdist}/fonts/afm/vntex
%dir %{texmfdist}/fonts/cmap
%dir %{texmfdist}/fonts/enc
%dir %{texmfdist}/fonts/enc/dvips
%dir %{texmfdist}/fonts/map
%dir %{texmfdist}/fonts/map/dvipdfm
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/map/fontname
%dir %{texmfdist}/fonts/map/vtex
%dir %{texmfdist}/fonts/ofm
%dir %{texmfdist}/fonts/ofm/public
%dir %{texmfdist}/fonts/ovf
%dir %{texmfdist}/fonts/ovf/public
%dir %{texmfdist}/fonts/ovp
%dir %{texmfdist}/fonts/ovp/public
%dir %{texmfdist}/fonts/opentype
%dir %{texmfdist}/fonts/opentype/public
%dir %{texmfdist}/fonts/pk
%dir %{texmfdist}/fonts/pk/ljfour
%dir %{texmfdist}/fonts/source
%dir %{texmfdist}/fonts/source/public
%dir %{texmfdist}/fonts/source/vntex
%dir %{texmfdist}/fonts/tfm
%dir %{texmfdist}/fonts/tfm/public
%dir %{texmfdist}/fonts/truetype
%dir %{texmfdist}/fonts/type1
%dir %{texmfdist}/fonts/type1/public
%dir %{texmfdist}/fonts/vf
%dir %{texmfdist}/fonts/vf/public
%dir %{texmfdist}/source/fonts


%files -n texlive-doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/fontinst
%doc %{texmfdist}/doc/fonts/fontname
%doc %{texmfdist}/doc/generic/FAQ-en
%doc %{texmfdist}/doc/generic/barr
%doc %{texmfdist}/doc/generic/borceux
%doc %{texmfdist}/doc/generic/c-pascal
%doc %{texmfdist}/doc/generic/dehyph-exptl
%doc %{texmfdist}/doc/generic/epsf
%doc %{texmfdist}/doc/generic/fltpoint
%doc %{texmfdist}/doc/generic/hyph-utf8
%doc %{texmfdist}/doc/generic/iftex
%doc %{texmfdist}/doc/latex/guide-to-latex
%doc %{texmfdist}/doc/latex/l2tabu-english
%doc %{texmfdist}/doc/latex/latex-course
%doc %{texmfdist}/doc/latex/latex-doc-ptr
%doc %{texmfdist}/doc/latex/latex-graphics-companion
%doc %{texmfdist}/doc/latex/latex-veryshortguide
%doc %{texmfdist}/doc/latex/latex-web-companion
%doc %{texmfdist}/doc/latex/lshort-english
%doc %{texmfdist}/doc/latex/tlc2

%files -n texlive-doc-knuth
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/knuth
%{texmfdist}/source/generic/knuth

%files -n texlive-doc-bg
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-bulgarian

%files -n texlive-doc-cs
%defattr(644,root,root,755)
 
%files -n texlive-doc-de
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/l2picfaq
%{texmfdist}/doc/latex/l2tabu
%{texmfdist}/doc/latex/lshort-german

%files -n texlive-doc-es
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/l2tabu-spanish
%{texmfdist}/doc/latex/lshort-spanish
 
%files -n texlive-doc-fi
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-finnish
 
%files -n texlive-doc-fr
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/epslatex-fr
%{texmfdist}/doc/latex/l2tabu-french
%{texmfdist}/doc/latex/lshort-french
 
%files -n texlive-doc-it
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-italian

%files -n texlive-doc-ja
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-japanese

%files -n texlive-doc-ko
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-korean

%files -n texlive-doc-mn
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-mongol

%files -n texlive-doc-nl
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-dutch
 
%files -n texlive-doc-pl
%defattr(644,root,root,755)
%{texmfdist}/doc/generic/tex-virtual-academy-pl
%{texmfdist}/doc/latex/lshort-polish

%files -n texlive-doc-pt
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-portuguese

%files -n texlive-doc-ru
%defattr(644,root,root,755)

%files -n texlive-doc-sk
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-slovak

%files -n texlive-doc-sl
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-slovenian

%files -n texlive-doc-th
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-thai

%files -n texlive-doc-tr
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-turkish

%files -n texlive-doc-uk
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-ukr

%files -n texlive-doc-vi
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-vietnamese

%files -n texlive-doc-zh_CN
%defattr(644,root,root,755)
%{texmfdist}/doc/generic/latex-notes-zh-cn
%{texmfdist}/doc/latex/lshort-chinese

%files -n texlive-doc-latex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/encxvlna
%doc %{texmfdist}/doc/generic/shapepar
%doc %{texmfdist}/doc/generic/textmerg
%doc %{texmfdist}/doc/latex/acronym
%doc %{texmfdist}/doc/latex/aeguill
%doc %{texmfdist}/doc/latex/anysize
%doc %{texmfdist}/doc/latex/base
%doc %{texmfdist}/doc/latex/beton
%doc %{texmfdist}/doc/latex/changepage
%doc %{texmfdist}/doc/latex/cjk
%doc %{texmfdist}/doc/latex/crop
%doc %{texmfdist}/doc/latex/draftcopy
%doc %{texmfdist}/doc/latex/eepic
%doc %{texmfdist}/doc/latex/endfloat
%doc %{texmfdist}/doc/latex/eso-pic
%doc %{texmfdist}/doc/latex/euler
%doc %{texmfdist}/doc/latex/eulervm
%doc %{texmfdist}/doc/latex/extsizes
%doc %{texmfdist}/doc/latex/fancybox
%doc %{texmfdist}/doc/latex/fancyhdr
%lang(it) %doc %{texmfdist}/doc/latex/fancyhdr-it
%doc %{texmfdist}/doc/latex/fancyvrb
%doc %{texmfdist}/doc/latex/filecontents
%doc %{texmfdist}/doc/latex/float
%doc %{texmfdist}/doc/latex/footmisc
%doc %{texmfdist}/doc/latex/footnpag
%doc %{texmfdist}/doc/latex/fp
%doc %{texmfdist}/doc/latex/geometry
%doc %{texmfdist}/doc/latex/graphics
%doc %{texmfdist}/doc/latex/hyperref
%doc %{texmfdist}/doc/latex/hyphenat
%doc %{texmfdist}/doc/latex/index
%doc %{texmfdist}/doc/latex/koma-script
%doc %{texmfdist}/doc/latex/labels
%doc %{texmfdist}/doc/latex/layouts
%doc %{texmfdist}/doc/latex/listings
%doc %{texmfdist}/doc/latex/ltabptch
%doc %{texmfdist}/doc/latex/mdwtools
%doc %{texmfdist}/doc/latex/memoir
%doc %{texmfdist}/doc/latex/mh
%doc %{texmfdist}/doc/latex/mparhack
%doc %{texmfdist}/doc/latex/ms
%doc %{texmfdist}/doc/latex/multibib
%doc %{texmfdist}/doc/latex/mwcls
%doc %{texmfdist}/doc/latex/nomencl
%doc %{texmfdist}/doc/latex/ntgclass
%doc %{texmfdist}/doc/latex/oberdiek
%doc %{texmfdist}/doc/latex/overpic
%doc %{texmfdist}/doc/latex/paralist
%doc %{texmfdist}/doc/latex/pb-diagram
%doc %{texmfdist}/doc/latex/pdfpages
%doc %{texmfdist}/doc/latex/picinpar
%doc %{texmfdist}/doc/latex/pict2e
%doc %{texmfdist}/doc/latex/placeins
%doc %{texmfdist}/doc/latex/preprint
%doc %{texmfdist}/doc/latex/preview
%doc %{texmfdist}/doc/latex/program
%doc %{texmfdist}/doc/latex/psfrag
%doc %{texmfdist}/doc/latex/rotating
%doc %{texmfdist}/doc/latex/rotfloat
%doc %{texmfdist}/doc/latex/scale
%doc %{texmfdist}/doc/latex/sectsty
%doc %{texmfdist}/doc/latex/seminar
%doc %{texmfdist}/doc/latex/showlabels
%doc %{texmfdist}/doc/latex/sidecap
%doc %{texmfdist}/doc/latex/soul
%doc %{texmfdist}/doc/latex/stdclsdv
%doc %{texmfdist}/doc/latex/subfig
%doc %{texmfdist}/doc/latex/subfigure
%doc %{texmfdist}/doc/latex/textfit
%doc %{texmfdist}/doc/latex/textpos
%doc %{texmfdist}/doc/latex/titlesec
%doc %{texmfdist}/doc/latex/tocbibind
%doc %{texmfdist}/doc/latex/tocloft
%doc %{texmfdist}/doc/latex/tools
%doc %{texmfdist}/doc/latex/totpages
%doc %{texmfdist}/doc/latex/type1cm
%doc %{texmfdist}/doc/latex/units
%doc %{texmfdist}/doc/latex/vmargin
%doc %{texmfdist}/doc/latex/was
%doc %{texmfdist}/doc/latex/wrapfig
%doc %{texmfdist}/doc/latex/xtab
%doc %{texmfdist}/doc/latex/yfonts
%doc %{texmfdist}/doc/support/latexmk

%files -n texlive-dvips
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/dvipdfmx
%doc %{texmfdist}/doc/dvipdfm
%doc %{texmfdist}/doc/dvips
%{texmfdist}/dvips
%{texmfdist}/fonts/enc/dvips/base
%{texmfdist}/tex/generic/dvips
%{texmfdist}/tex/latex/dvipdfmx-def
%{texmfdist}/dvipdfmx
%{texmfdist}/fonts/cmap/dvipdfmx
%dir %{texmfdist}/fonts/map/dvipdfmx
%{texmfdist}/fonts/map/dvipdfmx/japanese-otf
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/hiragino
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/hiragino-pron
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/ipa
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/ipaex
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/kozuka
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6n
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/morisawa
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/morisawa-pr6n
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/ms
%{texmfdist}/fonts/map/dvipdfmx/jfontmaps/noEmbed
%{texmfdist}/fonts/map/dvipdfmx/ptex
%{texmfdist}/fonts/map/dvipdfmx/updmap
%{texmfdist}/fonts/map/dvips/adforn
%{texmfdist}/fonts/map/dvips/adfsymbols
%{texmfdist}/fonts/map/dvips/aramaic-serto
%{texmfdist}/fonts/map/dvips/ascii-font
%{texmfdist}/fonts/map/dvips/aspectratio
%{texmfdist}/fonts/map/dvips/baskervald
%{texmfdist}/fonts/map/dvips/bbold-type1
%{texmfdist}/fonts/map/dvips/berenisadf
%{texmfdist}/fonts/map/dvips/bguq
%{texmfdist}/fonts/map/dvips/bookhands
%{texmfdist}/fonts/map/dvips/boondox
%{texmfdist}/fonts/map/dvips/cabin
%{texmfdist}/fonts/map/dvips/calligra-type1
%{texmfdist}/fonts/map/dvips/cantarell
%{texmfdist}/fonts/map/dvips/ccicons
%{texmfdist}/fonts/map/dvips/comfortaa
%{texmfdist}/fonts/map/dvips/countriesofeurope
%{texmfdist}/fonts/map/dvips/dejavu
%{texmfdist}/fonts/map/dvips/droid
%{texmfdist}/fonts/map/dvips/dutchcal
%{texmfdist}/fonts/map/dvips/ebgaramond
%{texmfdist}/fonts/map/dvips/electrum
%{texmfdist}/fonts/map/dvips/esstix
%{texmfdist}/fonts/map/dvips/fdsymbol
%{texmfdist}/fonts/map/dvips/fonts-tlwg
%{texmfdist}/fonts/map/dvips/frcursive
%{texmfdist}/fonts/map/dvips/gillcm
%{texmfdist}/fonts/map/dvips/hacm
%{texmfdist}/fonts/map/dvips/ipaex-type1
%{texmfdist}/fonts/map/dvips/jamtimes
%{texmfdist}/fonts/map/dvips/lato
%{texmfdist}/fonts/map/dvips/librebaskerville
%{texmfdist}/fonts/map/dvips/libris
%{texmfdist}/fonts/map/dvips/mathabx-type1
%{texmfdist}/fonts/map/dvips/mdsymbol
%{texmfdist}/fonts/map/dvips/metapost
#%{texmfdist}/fonts/map/dvips/musixtex-fonts
%{texmfdist}/fonts/map/dvips/mxedruli
%{texmfdist}/fonts/map/dvips/nanumtype1
%{texmfdist}/fonts/map/dvips/newpx
%{texmfdist}/fonts/map/dvips/newtx
%{texmfdist}/fonts/map/dvips/norasi-c90
%{texmfdist}/fonts/map/dvips/ocr-b-outline
%{texmfdist}/fonts/map/dvips/opensans
%{texmfdist}/fonts/map/dvips/paratype
%{texmfdist}/fonts/map/dvips/pigpen
%{texmfdist}/fonts/map/dvips/poltawski
%{texmfdist}/fonts/map/dvips/prodint
%{texmfdist}/fonts/map/dvips/pxtxalfa
%{texmfdist}/fonts/map/dvips/quattrocento
%{texmfdist}/fonts/map/dvips/raleway
%{texmfdist}/fonts/map/dvips/recycle
%{texmfdist}/fonts/map/dvips/romande
%{texmfdist}/fonts/map/dvips/rsfso
%{texmfdist}/fonts/map/dvips/sansmathaccent
%{texmfdist}/fonts/map/dvips/sansmathfonts
%{texmfdist}/fonts/map/dvips/sourcecodepro
%{texmfdist}/fonts/map/dvips/sourcesanspro
%{texmfdist}/fonts/map/dvips/starfont
%{texmfdist}/fonts/map/dvips/superiors
%{texmfdist}/fonts/map/dvips/tetex
%{texmfdist}/fonts/map/dvips/tfrupee
%{texmfdist}/fonts/map/dvips/updmap
%{texmfdist}/fonts/map/dvips/venturis
%{texmfdist}/fonts/map/dvips/venturis2
%{texmfdist}/fonts/map/dvips/venturisold
%{texmfdist}/fonts/map/dvips/venturissans
%{texmfdist}/fonts/map/dvips/venturissans2
%{texmfdist}/fonts/enc/dvips/adforn
%{texmfdist}/fonts/enc/dvips/adfsymbols
%{texmfdist}/fonts/enc/dvips/afm2pl
%{texmfdist}/fonts/enc/dvips/b1encoding
%{texmfdist}/fonts/enc/dvips/baskervald
%{texmfdist}/fonts/enc/dvips/berenisadf
%{texmfdist}/fonts/enc/dvips/c90
%{texmfdist}/fonts/enc/dvips/cabin
%{texmfdist}/fonts/enc/dvips/cantarell
%{texmfdist}/fonts/enc/dvips/ccicons
%{texmfdist}/fonts/enc/dvips/comfortaa
%{texmfdist}/fonts/enc/dvips/countriesofeurope
%{texmfdist}/fonts/enc/dvips/dejavu
%{texmfdist}/fonts/enc/dvips/droid
%{texmfdist}/fonts/enc/dvips/ebgaramond
%{texmfdist}/fonts/enc/dvips/electrum
%{texmfdist}/fonts/enc/dvips/fdsymbol
%{texmfdist}/fonts/enc/dvips/fontools
%{texmfdist}/fonts/enc/dvips/fonts-tlwg
%{texmfdist}/fonts/enc/dvips/lato
%{texmfdist}/fonts/enc/dvips/librebaskerville
%{texmfdist}/fonts/enc/dvips/libris
%{texmfdist}/fonts/enc/dvips/ly1
%{texmfdist}/fonts/enc/dvips/mdsymbol
%{texmfdist}/fonts/enc/dvips/metapost
%{texmfdist}/fonts/enc/dvips/newpx
%{texmfdist}/fonts/enc/dvips/newtx
%{texmfdist}/fonts/enc/dvips/opensans
%{texmfdist}/fonts/enc/dvips/paratype
%{texmfdist}/fonts/enc/dvips/poltawski
%{texmfdist}/fonts/enc/dvips/quattrocento
%{texmfdist}/fonts/enc/dvips/raleway
%{texmfdist}/fonts/enc/dvips/romande
%{texmfdist}/fonts/enc/dvips/sourcecodepro
%{texmfdist}/fonts/enc/dvips/sourcesanspro
%{texmfdist}/fonts/enc/dvips/superiors
%{texmfdist}/fonts/enc/dvips/tetex
%{texmfdist}/fonts/enc/dvips/venturisadf
%{texmfdist}/fonts/enc/dvips/xypic
%dir %{texmfdist}/fonts/map/dvipdfmx/jfontmaps
%{texmfdist}/fonts/map/dvipdfmx/cid-x.map
%{texmfdist}/fonts/map/dvipdfmx/ckx.map

%files -n texlive-omega
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/omega
%{texmfdist}/omega
%{texmfdist}/tex/generic/omegahyph
%{texmfdist}/tex/lambda
%{texmfdist}/tex/plain/omega
%{fmtdir}/aleph
%{fmtdir}/omega

%files -n texlive-jadetex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/otherformats/jadetex
%{texmfdist}/tex/jadetex
%{texmfdist}/source/jadetex
%{fmtdir}/pdftex/jadetex.fmt
%{fmtdir}/pdftex/pdfjadetex.fmt

%files -n texlive-scripts-extra
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/pgfplots
%dir %{texmfdist}/scripts/shipunov
%attr(755,root,root) %{texmfdist}/scripts/pgfplots/*
%attr(755,root,root) %{texmfdist}/scripts/shipunov/*

%files -n texlive-tex4ht-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/tex4ht
%{texmfdist}/tex4ht
%{texmfdist}/tex/generic/tex4ht

%files -n texlive-xetex-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/ifxetex
%doc %{texmfdist}/doc/latex/euenc
%doc %{texmfdist}/doc/latex/fontspec
%doc %{texmfdist}/doc/latex/unicode-math
%doc %{texmfdist}/doc/xelatex
%doc %{texmfdist}/doc/xetex
%dir %{fmtdir}/xetex
%{texmfdist}/scripts/xetex
%{texmfdist}/source/latex/euenc
%{texmfdist}/source/latex/fontspec
%{texmfdist}/source/latex/unicode-math
%{texmfdist}/source/xelatex
%{texmfdist}/tex/generic/ifxetex
%{texmfdist}/tex/generic/xetexconfig
%{texmfdist}/tex/latex/euenc
%{texmfdist}/tex/latex/fontspec
%{texmfdist}/tex/latex/latexconfig/xelatex.ini
%{texmfdist}/tex/latex/unicode-math
%{texmfdist}/tex/xelatex
%{texmfdist}/tex/xetex
%{fmtdir}/xetex/*.fmt

%files -n texlive-tex-arrayjob
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/arrayjobx
%{texmfdist}/tex/generic/arrayjobx

%files -n texlive-tex-insbox
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/insbox
%{texmfdist}/tex/generic/insbox

%files -n texlive-tex-kastrup
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/kastrup
%{texmfdist}/source/generic/kastrup
%{texmfdist}/tex/generic/kastrup

%files -n texlive-tex-mathdots
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/mathdots
%{texmfdist}/source/generic/mathdots
%{texmfdist}/tex/generic/mathdots

%files -n texlive-tex-ofs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/ofs
%{texmfdist}/tex/generic/ofs

%files -n texlive-tex-velthuis
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/velthuis
%{texmfdist}/tex/generic/velthuis

%files -n texlive-makeindex-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/support/makeindex
%{texmfdist}/makeindex
%exclude %{texmfdist}/makeindex/minitoc
%exclude %{texmfdist}/makeindex/arsclassica

%files -n texlive-metapost-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/metapost
%{texmfdist}/metapost/automata
%{texmfdist}/metapost/base
%{texmfdist}/metapost/bbcard
%{texmfdist}/metapost/blockdraw_mp
%{texmfdist}/metapost/bpolynomial
%{texmfdist}/metapost/cmarrows
%{texmfdist}/metapost/config
%{texmfdist}/metapost/drv
%{texmfdist}/metapost/dviincl
%{texmfdist}/metapost/epsincl
%{texmfdist}/metapost/expressg
%{texmfdist}/metapost/exteps
%{texmfdist}/metapost/featpost
#%{texmfdist}/metapost/frcursive
%{texmfdist}/metapost/garrigues
%{texmfdist}/metapost/hatching
%{texmfdist}/metapost/latexmp
%{texmfdist}/metapost/makecirc
%{texmfdist}/metapost/metago
%{texmfdist}/metapost/metaobj
%{texmfdist}/metapost/metaplot
%{texmfdist}/metapost/metauml
%{texmfdist}/metapost/mfpic
%{texmfdist}/metapost/misc
%{texmfdist}/metapost/mp3d
%{texmfdist}/metapost/mpattern
%{texmfdist}/metapost/nkarta
%{texmfdist}/metapost/piechartmp
%{texmfdist}/metapost/slideshow
%{texmfdist}/metapost/splines
%{texmfdist}/metapost/suanpan
%{texmfdist}/metapost/support
# in texlive-fonts-lh
%exclude %{texmfdist}/metapost/support/charlib/LH
%{texmfdist}/metapost/tabvar
%{texmfdist}/metapost/textpath
%{texmfdist}/metapost/venn
%{texmfdist}/tex/generic/metapost

%files -n xindy-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/xindy
%{texmfdist}/xindy

%files -n xindy-albanian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/albanian

%files -n xindy-belarusian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/belarusian

%files -n xindy-bulgarian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/bulgarian

%files -n xindy-croatian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/croatian

%files -n xindy-czech
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/czech

%files -n xindy-danish
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/danish

%files -n xindy-dutch
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/dutch

%files -n xindy-english
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/english

%files -n xindy-esperanto
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/esperanto

%files -n xindy-estonian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/estonian

%files -n xindy-finnish
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/finnish

%files -n xindy-french
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/french

%files -n xindy-general
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/general

%files -n xindy-georgian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/georgian

%files -n xindy-german
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/german

%files -n xindy-greek
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/greek

%files -n xindy-gypsy
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/gypsy

%files -n xindy-hausa
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/hausa

%files -n xindy-hebrew
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/hebrew

%files -n xindy-hungarian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/hungarian

%files -n xindy-icelandic
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/icelandic

%files -n xindy-italian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/italian

%files -n xindy-klingon
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/klingon

%files -n xindy-kurdish
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/kurdish

%files -n xindy-latin
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/latin

%files -n xindy-latvian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/latvian

%files -n xindy-lithuanian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/lithuanian

%files -n xindy-lower-sorbian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/lower-sorbian

%files -n xindy-macedonian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/macedonian

%files -n xindy-mongolian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/mongolian

%files -n xindy-norwegian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/norwegian

%files -n xindy-polish
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/polish

%files -n xindy-portuguese
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/portuguese

%files -n xindy-romanian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/romanian

%files -n xindy-russian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/russian

%files -n xindy-serbian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/serbian

%files -n xindy-slovak
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/slovak

%files -n xindy-slovenian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/slovenian

%files -n xindy-spanish
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/spanish

%files -n xindy-swedish
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/swedish

%files -n xindy-turkish
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/turkish

%files -n xindy-ukrainian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/ukrainian

%files -n xindy-upper-sorbian
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/upper-sorbian

%files -n xindy-vietnamese
%defattr(644,root,root,755)
%{texmfdist}/xindy/modules/lang/vietnamese/

%files -n texlive-plain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/plain
%{texmfdist}/tex/plain
%exclude %{texmfdist}/tex/plain/config/xetex.ini
# in texlive-amstex
%exclude %{texmfdist}/tex/plain/amsfonts
# in texlive-fonts-antt
%exclude %{texmfdist}/tex/plain/antt
# in texlive-eplain
%exclude %{texmfdist}/tex/plain/etex
# in texlive-omega-data
%exclude %{texmfdist}/tex/plain/omega

%files -n texlive-mex
%defattr(644,root,root,755)
%dir %{texmfdist}/tex/mex
%doc %{texmfdist}/doc/mex
%{texmfdist}/source/mex
%{texmfdist}/tex/mex/base
%{texmfdist}/tex/mex/config
%{texmfdist}/tex/mex/utf8mex

%files -n texlive-amstex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/amstex
%{texmfdist}/tex/amstex
%{texmfdist}/tex/plain/amsfonts

%files -n texlive-format-csplain
%defattr(644,root,root,755)
%{texmfdist}/tex/csplain
%{fmtdir}/pdftex/csplain.fmt

%files -n texlive-cslatex
%defattr(644,root,root,755)
%{texmfdist}/tex/cslatex

%files -n texlive-enctex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/enctex
%{texmfdist}/tex/generic/enctex

%files -n texlive-eplain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/etex
%doc %{texmfdist}/doc/eplain
%{texmfdist}/tex/plain/etex
%{texmfdist}/tex/eplain
%{texmfdist}/source/eplain

%files -n texlive-context-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/context
%{texmfdist}/source/lambda
%{texmfdist}/source/context
# in texlive-latex-pgf
%exclude %{texmfdist}/source/context/third/pgfplots
%{texmfdist}/bibtex/bst/context
%{texmfdist}/context
%{texmfdist}/fonts/enc/dvips/context
%{texmfdist}/fonts/fea/context
%{texmfdist}/fonts/map/dvips/context
%{texmfdist}/fonts/map/luatex/context
%{texmfdist}/fonts/map/pdftex/context
%{texmfdist}/metapost/context
%{texmfdist}/tex/context
%{texmfdist}/tex/generic/context
%{texmfdist}/tex/latex/context

%files -n texlive-latex-data
%defattr(644,root,root,755)
%dir %{texmfdist}/tex/latex
%dir %{texmfdist}/tex/latex/latexconfig
%{texmfdist}/tex/generic/shapepar
%{texmfdist}/tex/generic/textmerg
%{texmfdist}/source/generic/textmerg
%{texmfdist}/tex/latex/12many
%{texmfdist}/tex/latex/IEEEtran
%{texmfdist}/tex/latex/Tabbing
%{texmfdist}/tex/latex/a0poster
%{texmfdist}/tex/latex/acronym
%{texmfdist}/tex/latex/aeguill
%{texmfdist}/tex/latex/afthesis
%{texmfdist}/tex/latex/aguplus
%{texmfdist}/tex/latex/akletter
%{texmfdist}/tex/latex/algorithm2e
%{texmfdist}/tex/latex/algorithmicx
%{texmfdist}/tex/latex/allrunes
%{texmfdist}/tex/latex/altfont
%{texmfdist}/tex/latex/ametsoc
%{texmfdist}/tex/latex/amsaddr
%{texmfdist}/tex/latex/amsrefs
%{texmfdist}/tex/latex/animate
%{texmfdist}/tex/latex/antiqua
%{texmfdist}/tex/latex/anyfontsize
%{texmfdist}/tex/latex/anysize
%{texmfdist}/tex/latex/arabi
%{texmfdist}/tex/latex/arabtex
%{texmfdist}/tex/latex/archaic
%{texmfdist}/tex/latex/arev
%{texmfdist}/tex/latex/assignment
%{texmfdist}/tex/latex/augie
%{texmfdist}/tex/latex/auncial-new
%{texmfdist}/tex/latex/aurical
%{texmfdist}/tex/latex/authorindex
%{texmfdist}/tex/latex/auto-pst-pdf
%{texmfdist}/tex/latex/autoarea
%{texmfdist}/tex/latex/avantgar
%{texmfdist}/tex/latex/bangtex
%{texmfdist}/tex/latex/barcodes
%{texmfdist}/tex/latex/base
%{texmfdist}/tex/latex/bbding
%{texmfdist}/tex/latex/bbm-macros
%{texmfdist}/tex/latex/begriff
%{texmfdist}/tex/latex/bengali
%{texmfdist}/tex/latex/bera
%{texmfdist}/tex/latex/betababel
%{texmfdist}/tex/latex/beton
%{texmfdist}/tex/latex/bibarts
%{texmfdist}/tex/latex/bibleref
%{texmfdist}/tex/latex/biblist
%{texmfdist}/tex/latex/bigfoot
%{texmfdist}/tex/latex/bizcard
%{texmfdist}/tex/latex/blacklettert1
%{texmfdist}/tex/latex/blindtext
%{texmfdist}/tex/latex/boisik
%{texmfdist}/tex/latex/boldtensors
%{texmfdist}/tex/latex/bookest
%{texmfdist}/tex/latex/bookhands
%{texmfdist}/tex/latex/bookman
%{texmfdist}/tex/latex/boxhandler
%{texmfdist}/tex/latex/braille
%{texmfdist}/tex/latex/breakurl
%{texmfdist}/tex/latex/brushscr
%{texmfdist}/tex/latex/burmese
%{texmfdist}/tex/latex/bussproofs
%{texmfdist}/tex/latex/captcont
%{texmfdist}/tex/latex/casyl
%{texmfdist}/tex/latex/catechis
%{texmfdist}/tex/latex/cbcoptic
%{texmfdist}/tex/latex/cclicenses
%{texmfdist}/tex/latex/cd-cover
%{texmfdist}/tex/latex/cd
%{texmfdist}/tex/latex/cdpbundl
%{texmfdist}/tex/latex/cellspace
%{texmfdist}/tex/latex/changepage
%{texmfdist}/tex/latex/changes
%{texmfdist}/tex/latex/chapterfolder
%{texmfdist}/tex/latex/cherokee
%{texmfdist}/tex/latex/chicago
%{texmfdist}/tex/latex/cjhebrew
%{texmfdist}/tex/latex/cjk
%{texmfdist}/tex/latex/classicthesis
%{texmfdist}/tex/latex/cleveref
%{texmfdist}/tex/latex/clock
%{texmfdist}/tex/latex/clrscode
%{texmfdist}/tex/latex/cm-lgc
%{texmfdist}/tex/latex/cm-super
%{texmfdist}/tex/latex/cmap
%{texmfdist}/tex/latex/cmdstring
%{texmfdist}/tex/latex/cmsd
%{texmfdist}/tex/latex/codepage
%{texmfdist}/tex/latex/colorinfo
%{texmfdist}/tex/latex/commath
%{texmfdist}/tex/latex/compactbib
%{texmfdist}/tex/latex/complexity
%{texmfdist}/tex/latex/concprog
%{texmfdist}/tex/latex/confproc
%{texmfdist}/tex/latex/courier-scaled
%{texmfdist}/tex/latex/courier
%{texmfdist}/tex/latex/courseoutline
%{texmfdist}/tex/latex/coursepaper
%{texmfdist}/tex/latex/coverpage
%{texmfdist}/tex/latex/covington
%{texmfdist}/tex/latex/crop
%{texmfdist}/tex/latex/crossreference
%{texmfdist}/tex/latex/csbulletin
%{texmfdist}/tex/latex/csquotes
%{texmfdist}/tex/latex/ctib
%{texmfdist}/tex/latex/cv
%{texmfdist}/tex/latex/cweb-latex
%{texmfdist}/tex/latex/cyklop
%{texmfdist}/tex/latex/dateiliste
%{texmfdist}/tex/latex/datetime
%{texmfdist}/tex/latex/decimal
%{texmfdist}/tex/latex/diagnose
%{texmfdist}/tex/latex/dichokey
%{texmfdist}/tex/latex/dictsym
%{texmfdist}/tex/latex/digiconfigs
%{texmfdist}/tex/latex/dingbat
%{texmfdist}/tex/latex/directory
%{texmfdist}/tex/latex/dlfltxb
%{texmfdist}/tex/latex/docmfp
%{texmfdist}/tex/latex/doi
%{texmfdist}/tex/latex/doipubmed
%{texmfdist}/tex/latex/dotarrow
%{texmfdist}/tex/latex/dottex
%{texmfdist}/tex/latex/doublestroke
%{texmfdist}/tex/latex/dpfloat
%{texmfdist}/tex/latex/drac
%{texmfdist}/tex/latex/draftcopy
%{texmfdist}/tex/latex/dramatist
%{texmfdist}/tex/latex/duerer-latex
%{texmfdist}/tex/latex/dvdcoll
# in texlive-tex-spanish
%exclude %{texmfdist}/tex/latex/dvdcoll/dcl/spanish.dcl
%{texmfdist}/tex/latex/ean13isbn
%{texmfdist}/tex/latex/easy
%{texmfdist}/tex/latex/ebezier
%{texmfdist}/tex/latex/ebsthesis
%{texmfdist}/tex/latex/ecclesiastic
%{texmfdist}/tex/latex/ecltree
%{texmfdist}/tex/latex/eco
%{texmfdist}/tex/latex/ed
%{texmfdist}/tex/latex/edmargin
%{texmfdist}/tex/latex/ednotes
%{texmfdist}/tex/latex/eemeir
%{texmfdist}/tex/latex/eepic
%{texmfdist}/tex/latex/egameps
%{texmfdist}/tex/latex/eiad
%{texmfdist}/tex/latex/ellipsis
%{texmfdist}/tex/latex/elpres
%{texmfdist}/tex/latex/emp
%{texmfdist}/tex/latex/emulateapj
%{texmfdist}/tex/latex/encxvlna
%{texmfdist}/tex/latex/endfloat
%{texmfdist}/tex/latex/endheads
%{texmfdist}/tex/latex/engpron
%{texmfdist}/tex/latex/engrec
%{texmfdist}/tex/latex/envlab
%{texmfdist}/tex/latex/epigrafica
%{texmfdist}/tex/latex/epigraph
%{texmfdist}/tex/latex/epiolmec
%{texmfdist}/tex/latex/epsdice
%{texmfdist}/tex/latex/epspdfconversion
%{texmfdist}/tex/latex/eqname
%{texmfdist}/tex/latex/eqparbox
%{texmfdist}/tex/latex/errata
%{texmfdist}/tex/latex/eskdx
%{texmfdist}/tex/latex/eso-pic
%{texmfdist}/tex/latex/etex-pkg
%{texmfdist}/tex/latex/ethiop
%{texmfdist}/tex/latex/etoolbox
%{texmfdist}/tex/latex/eukdate
%{texmfdist}/tex/latex/euler
%{texmfdist}/tex/latex/euro
%{texmfdist}/tex/latex/europecv
%{texmfdist}/tex/latex/everypage
%{texmfdist}/tex/latex/examplep
%{texmfdist}/tex/latex/extarrows
%{texmfdist}/tex/latex/extract
%{texmfdist}/tex/latex/extsizes
%{texmfdist}/tex/latex/facsimile
%{texmfdist}/tex/latex/fancybox
%{texmfdist}/tex/latex/fancyhdr
%{texmfdist}/tex/latex/fancynum
%{texmfdist}/tex/latex/fancyref
%{texmfdist}/tex/latex/fancytooltips
%{texmfdist}/tex/latex/fancyvrb
%{texmfdist}/tex/latex/fc
%{texmfdist}/tex/latex/feyn
%{texmfdist}/tex/latex/fge
%{texmfdist}/tex/latex/figbib
%{texmfdist}/tex/latex/figsize
%{texmfdist}/tex/latex/filecontents
%{texmfdist}/tex/latex/fink
%{texmfdist}/tex/latex/fixfoot
%{texmfdist}/tex/latex/flabels
%{texmfdist}/tex/latex/flacards
%{texmfdist}/tex/latex/flagderiv
%{texmfdist}/tex/latex/flashcards
%{texmfdist}/tex/latex/float
%{texmfdist}/tex/latex/floatrow
%{texmfdist}/tex/latex/fmp
%{texmfdist}/tex/latex/fnbreak
%{texmfdist}/tex/latex/fncychap
%{texmfdist}/tex/latex/foekfont
%{texmfdist}/tex/latex/foilhtml
%{texmfdist}/tex/latex/fonetika
%{texmfdist}/tex/latex/fontinst
%{texmfdist}/tex/latex/fonttable
%{texmfdist}/tex/latex/footmisc
%{texmfdist}/tex/latex/footnpag
%{texmfdist}/tex/latex/fourier
%{texmfdist}/tex/latex/fouriernc
%{texmfdist}/tex/latex/fp
%{texmfdist}/tex/latex/frankenstein
%{texmfdist}/tex/latex/frcursive
%{texmfdist}/tex/latex/frenchle
%{texmfdist}/tex/latex/frletter
%{texmfdist}/tex/latex/frontespizio
%{texmfdist}/tex/latex/gaceta
%{texmfdist}/tex/latex/gastex
%{texmfdist}/tex/latex/gauss
%{texmfdist}/tex/latex/gb4e
%{texmfdist}/tex/latex/gcard
%{texmfdist}/tex/latex/gcite
%{texmfdist}/tex/latex/genmpage
%{texmfdist}/tex/latex/geometry
%{texmfdist}/tex/latex/gfsartemisia
%{texmfdist}/tex/latex/gfsbaskerville
%{texmfdist}/tex/latex/gfsbodoni
%{texmfdist}/tex/latex/gfscomplutum
%{texmfdist}/tex/latex/gfsdidot
%{texmfdist}/tex/latex/gfsneohellenic
%{texmfdist}/tex/latex/gfsporson
%{texmfdist}/tex/latex/gfssolomos
%{texmfdist}/tex/latex/gloss
%{texmfdist}/tex/latex/glossaries
%{texmfdist}/tex/latex/gmdoc
%{texmfdist}/tex/latex/gmeometric
%{texmfdist}/tex/latex/gmiflink
%{texmfdist}/tex/latex/gmutils
%{texmfdist}/tex/latex/gmverb
%{texmfdist}/tex/latex/graphics
%{texmfdist}/tex/latex/graphicx-psmin
%{texmfdist}/tex/latex/greek-inputenc
%{texmfdist}/tex/latex/greekdates
%{texmfdist}/tex/latex/greektex
%{texmfdist}/tex/latex/grfpaste
%{texmfdist}/tex/latex/grotesq
#%{texmfdist}/tex/latex/grverb
%{texmfdist}/tex/latex/gu
%{texmfdist}/tex/latex/hanging
%{texmfdist}/tex/latex/har2nat
%{texmfdist}/tex/latex/harmony
%{texmfdist}/tex/latex/harpoon
%{texmfdist}/tex/latex/harvard
%{texmfdist}/tex/latex/hc
%{texmfdist}/tex/latex/helvetic
%{texmfdist}/tex/latex/hep
%{texmfdist}/tex/latex/hepnames
%{texmfdist}/tex/latex/hepparticles
%{texmfdist}/tex/latex/hepthesis
%{texmfdist}/tex/latex/hepunits
%{texmfdist}/tex/latex/hexgame
%{texmfdist}/tex/latex/hfoldsty
%{texmfdist}/tex/latex/histogr
%{texmfdist}/tex/latex/hitec
%{texmfdist}/tex/latex/hpsdiss
%{texmfdist}/tex/latex/hvfloat
%{texmfdist}/tex/latex/hypdvips
%{texmfdist}/tex/latex/hyper
%{texmfdist}/tex/latex/hyperref
%{texmfdist}/tex/latex/hyperxmp
%{texmfdist}/tex/latex/hyphenat
%{texmfdist}/tex/latex/ibycus-babel
%{texmfdist}/tex/latex/icsv
%{texmfdist}/tex/latex/ieeepes
%{texmfdist}/tex/latex/ifmslide
%{texmfdist}/tex/latex/ifplatform
%{texmfdist}/tex/latex/ifsym
%{texmfdist}/tex/latex/ijmart
%{texmfdist}/tex/latex/imac
%{texmfdist}/tex/latex/image-gallery
%{texmfdist}/tex/latex/imtekda
%{texmfdist}/tex/latex/index
%{texmfdist}/tex/latex/initials
%{texmfdist}/tex/latex/inlinebib
%{texmfdist}/tex/latex/inlinedef
%{texmfdist}/tex/latex/interactiveworkbook
# %{texmfdist}/tex/latex/ipa
%{texmfdist}/tex/latex/iso
%{texmfdist}/tex/latex/iso10303
%{texmfdist}/tex/latex/isodate
%{texmfdist}/tex/latex/isodoc
%{texmfdist}/tex/latex/itnumpar
%{texmfdist}/tex/latex/iwona
%{texmfdist}/tex/latex/jknapltx
%{texmfdist}/tex/latex/jneurosci
%{texmfdist}/tex/latex/jpsj
%{texmfdist}/tex/latex/jura
%{texmfdist}/tex/latex/juraabbrev
%{texmfdist}/tex/latex/juramisc
%{texmfdist}/tex/latex/jurarsp
%{texmfdist}/tex/latex/koma-script
%{texmfdist}/tex/latex/labels
%{texmfdist}/tex/latex/latexconfig/graphics.cfg
%{texmfdist}/tex/latex/latexconfig/hyperref.cfg
%{texmfdist}/tex/latex/latexconfig/latex.ini
%{texmfdist}/tex/latex/latexconfig/lualatex.ini
%{texmfdist}/tex/latex/latexconfig/mllatex.ini
%{texmfdist}/tex/latex/latexconfig/pdflatex.ini
%{texmfdist}/tex/latex/layouts
%{texmfdist}/tex/latex/listings
%{texmfdist}/tex/latex/ltabptch
%{texmfdist}/tex/latex/ltxmisc
%{texmfdist}/tex/latex/mdwtools
%{texmfdist}/tex/latex/memoir
%{texmfdist}/tex/latex/mh
%{texmfdist}/tex/latex/misc209
%{texmfdist}/tex/latex/mmap
%{texmfdist}/tex/latex/mnsymbol
%{texmfdist}/tex/latex/moderncv
%{texmfdist}/tex/latex/modroman
%{texmfdist}/tex/latex/mongolian-babel
%{texmfdist}/tex/latex/montex
%{texmfdist}/tex/latex/mparhack
%{texmfdist}/tex/latex/ms
%{texmfdist}/tex/latex/multibib
%{texmfdist}/tex/latex/multirow
%{texmfdist}/tex/latex/mwcls
%{texmfdist}/tex/latex/ncclatex
%{texmfdist}/tex/latex/ncctools
%{texmfdist}/tex/latex/ncntrsbk
%{texmfdist}/tex/latex/nddiss
%{texmfdist}/tex/latex/newfile
%{texmfdist}/tex/latex/newlfm
%{texmfdist}/tex/latex/newspaper
%{texmfdist}/tex/latex/nomencl
%{texmfdist}/tex/latex/ntgclass
%{texmfdist}/tex/generic/oberdiek
%{texmfdist}/tex/latex/oberdiek
%{texmfdist}/tex/latex/overpic
%{texmfdist}/tex/latex/paralist
%{texmfdist}/tex/latex/pb-diagram
%{texmfdist}/tex/latex/pdftex-def
%{texmfdist}/tex/latex/pdfpages
%{texmfdist}/tex/latex/picinpar
%{texmfdist}/tex/latex/pict2e
%{texmfdist}/tex/latex/placeins
%{texmfdist}/tex/latex/preprint
%{texmfdist}/tex/latex/preview
%{texmfdist}/tex/latex/program
%{texmfdist}/tex/latex/psfrag
%{texmfdist}/tex/latex/pslatex
%{texmfdist}/tex/latex/revtex
%{texmfdist}/tex/latex/rotating
%{texmfdist}/tex/latex/rotfloat
%{texmfdist}/tex/latex/scale
%{texmfdist}/tex/latex/sectsty
%{texmfdist}/tex/latex/seminar
%{texmfdist}/tex/latex/setspace
%{texmfdist}/tex/latex/showdim
%{texmfdist}/tex/latex/showlabels
%{texmfdist}/tex/latex/sidecap
%{texmfdist}/tex/latex/soul
%{texmfdist}/tex/latex/stdclsdv
%{texmfdist}/tex/latex/stmaryrd
%{texmfdist}/tex/latex/subfig
%{texmfdist}/tex/latex/subfigure
%{texmfdist}/tex/latex/supertabular
%{texmfdist}/tex/latex/t2
%{texmfdist}/tex/latex/t-angles
%{texmfdist}/tex/latex/tableaux
%{texmfdist}/tex/latex/tablists
%{texmfdist}/tex/latex/tablor
%{texmfdist}/tex/latex/tabto-ltx
%{texmfdist}/tex/latex/tabulary
%{texmfdist}/tex/latex/tabvar
%{texmfdist}/tex/latex/talk
%{texmfdist}/tex/latex/tcldoc
%{texmfdist}/tex/latex/tdsfrmath
%{texmfdist}/tex/latex/technics
%{texmfdist}/tex/latex/ted
%{texmfdist}/tex/latex/tengwarscript
%{texmfdist}/tex/latex/tensor
%{texmfdist}/tex/latex/teubner
%{texmfdist}/tex/latex/tex-gyre
%{texmfdist}/tex/latex/texilikecover
%{texmfdist}/tex/latex/texlogos
%{texmfdist}/tex/latex/texmate
%{texmfdist}/tex/latex/texpower
%{texmfdist}/tex/latex/texshade
%{texmfdist}/tex/latex/textcase
%{texmfdist}/tex/latex/textfit
%{texmfdist}/tex/latex/textopo
%{texmfdist}/tex/latex/textpath
%{texmfdist}/tex/latex/textpos
%{texmfdist}/tex/latex/theoremref
%{texmfdist}/tex/latex/thesis-titlepage-fhac
%{texmfdist}/tex/latex/thinsp
%{texmfdist}/tex/latex/thmtools
%{texmfdist}/tex/latex/thumb
%{texmfdist}/tex/latex/thuthesis
%{texmfdist}/tex/latex/ticket
%{texmfdist}/tex/latex/tikz-inet
%{texmfdist}/tex/latex/times
%{texmfdist}/tex/latex/tipa
%{texmfdist}/tex/latex/titlefoot
%{texmfdist}/tex/latex/titlesec
%{texmfdist}/tex/latex/titling
%{texmfdist}/tex/latex/tocbibind
%{texmfdist}/tex/latex/tocloft
%{texmfdist}/tex/latex/tools
%{texmfdist}/tex/latex/totpages
%{texmfdist}/tex/latex/type1cm
%{texmfdist}/tex/latex/units
%{texmfdist}/tex/latex/unitsdef
%{texmfdist}/tex/latex/universa
%{texmfdist}/tex/latex/upmethodology
%{texmfdist}/tex/latex/upquote
%{texmfdist}/tex/latex/varindex
%{texmfdist}/tex/latex/varsfromjobname
%{texmfdist}/tex/latex/velthuis
%{texmfdist}/tex/latex/verse
%{texmfdist}/tex/latex/versions
%{texmfdist}/tex/latex/vhistory
%{texmfdist}/tex/latex/vmargin
%{texmfdist}/tex/latex/volumes
%{texmfdist}/tex/latex/vpe
%{texmfdist}/tex/latex/vwcol
%{texmfdist}/tex/latex/wallpaper
%{texmfdist}/tex/latex/warning
%{texmfdist}/tex/latex/warpcol
%{texmfdist}/tex/latex/was
%{texmfdist}/tex/latex/williams
%{texmfdist}/tex/latex/wrapfig
%{texmfdist}/tex/latex/wsuipa
%{texmfdist}/tex/latex/xargs
%{texmfdist}/tex/latex/xcolor
%{texmfdist}/tex/latex/xdoc
%{texmfdist}/tex/latex/xfor
%{texmfdist}/tex/latex/xifthen
%{texmfdist}/tex/latex/xmpincl
%{texmfdist}/tex/latex/xnewcommand
%{texmfdist}/tex/latex/xoptarg
%{texmfdist}/tex/latex/xq
%{texmfdist}/tex/latex/xskak
%{texmfdist}/tex/latex/xtab
%{texmfdist}/tex/latex/xyling
%{texmfdist}/tex/latex/xytree
%{texmfdist}/tex/latex/yafoot
%{texmfdist}/tex/latex/yfonts
%{texmfdist}/tex/latex/yhmath
%{texmfdist}/tex/latex/york-thesis
%{texmfdist}/tex/latex/youngtab
%{texmfdist}/tex/latex/yplan
%{texmfdist}/tex/latex/zapfchan
%{texmfdist}/tex/latex/zapfding
%{texmfdist}/tex/latex/zed-csp
%{texmfdist}/tex/latex/ziffer
%{texmfdist}/tex/latex/zwgetfdate

%files -n texlive-latex-12many
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/12many
%{texmfdist}/source/latex/12many

%files -n texlive-latex-abstract
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/abstract
%{texmfdist}/tex/latex/abstract
%{texmfdist}/source/latex/abstract

%files -n texlive-latex-accfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/accfonts
%{texmfdist}/tex/latex/accfonts

%files -n texlive-latex-adrconv
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/adrconv
%{texmfdist}/doc/latex/adrconv

%files -n texlive-latex-algorithms
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/algorithms
%{texmfdist}/source/latex/algorithms
%{texmfdist}/tex/latex/algorithms

%files -n texlive-latex-ae
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/ae

%files -n texlive-latex-ams
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/amsfonts
%lang(it) %doc %{texmfdist}/doc/latex/amsldoc-it
%lang(it) %doc %{texmfdist}/doc/latex/amsmath-it
%lang(it) %doc %{texmfdist}/doc/latex/amsthdoc-it
%lang(vn) %doc %{texmfdist}/doc/latex/amsldoc-vn
%doc %{texmfdist}/doc/latex/amscls
%doc %{texmfdist}/doc/latex/amslatex-primer
%doc %{texmfdist}/doc/latex/amsmath
%doc %{texmfdist}/doc/latex/onlyamsmath
%{texmfdist}/tex/latex/amscls
%{texmfdist}/tex/latex/amsmath
%{texmfdist}/tex/latex/amsfonts
%{texmfdist}/tex/latex/onlyamsmath
%{texmfdist}/source/latex/onlyamsmath
%{texmfdist}/source/latex/amsaddr
%{texmfdist}/source/latex/amscls
%{texmfdist}/source/latex/amsfonts
%{texmfdist}/source/latex/amsmath
%{texmfdist}/source/latex/amsrefs

%files -n texlive-latex-antt
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/antt
%{texmfdist}/tex/latex/antt

%files -n texlive-latex-appendix
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/appendix
%{texmfdist}/tex/latex/appendix
%{texmfdist}/source/latex/appendix

%files -n texlive-latex-asyfig
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/asyfig
%{texmfdist}/tex/latex/asyfig

%files -n texlive-latex-bardiag
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bardiag
%{texmfdist}/tex/latex/bardiag

# %files -n texlive-latex-bbm
# %defattr(644,root,root,755)
# %{texmfdist}/tex/latex/bbm

%files -n texlive-latex-bbold
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bbold
%{texmfdist}/tex/latex/bbold
%{texmfdist}/source/latex/bbold

%files -n texlive-latex-beamer
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/beamer
%doc %{texmfdist}/doc/latex/beamerposter
%doc %{texmfdist}/doc/latex/beamer-FUBerlin
%{texmfdist}/tex/latex/beamerposter
%{texmfdist}/tex/latex/beamer-FUBerlin
%{texmfdist}/tex/latex/beamer

%files -n texlive-latex-bezos
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bezos
%{texmfdist}/tex/latex/bezos

%files -n texlive-latex-bibtex-ams
%defattr(644,root,root,755)
%{texmfdist}/bibtex/bst/amscls
%{texmfdist}/bibtex/bst/amsrefs
%{texmfdist}/bibtex/bib/amsrefs

%files -n texlive-latex-bibtex-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bibtopic
%doc %{texmfdist}/doc/latex/bibunits
%doc %{texmfdist}/doc/latex/chembst
%doc %{texmfdist}/doc/latex/footbib
%doc %{texmfdist}/doc/latex/natbib
%doc %{texmfdist}/doc/latex/cell

%dir %{texmfdist}/bibtex/bib
%{texmfdist}/bibtex/bib/base

# maybe can create subpackages
%dir %{texmfdist}/bibtex/bst
%{texmfdist}/bibtex/bib/biblatex
%{texmfdist}/bibtex/bst/adrconv
%{texmfdist}/bibtex/bst/apalike*
%{texmfdist}/bibtex/bst/base
%{texmfdist}/bibtex/bst/bib-fr
%{texmfdist}/bibtex/bst/biblatex
%{texmfdist}/bibtex/bst/cell
%{texmfdist}/bibtex/bst/chembst
%{texmfdist}/bibtex/bst/chicago-annote
%{texmfdist}/bibtex/bst/disser
%{texmfdist}/bibtex/bst/elsarticle
%{texmfdist}/bibtex/bst/natbib
%{texmfdist}/bibtex/bst/persian-bib
%{texmfdist}/bibtex/csf/biblatex

%{texmfdist}/bibtex/csf/base

%{texmfdist}/source/latex/adrconv
%{texmfdist}/source/latex/bibtopic
%{texmfdist}/source/latex/bibunits
%{texmfdist}/source/latex/footbib
%{texmfdist}/tex/latex/bibtopic
%{texmfdist}/tex/latex/bibunits
%{texmfdist}/tex/latex/footbib
%{texmfdist}/tex/latex/natbib

%files -n texlive-latex-bibtex-pl
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bib/gustlib
%{texmfdist}/bibtex/bib/gustlib/plbib.bib
%{texmfdist}/bibtex/csf/polish-csf

%files -n texlive-latex-bibtex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/bibtex/germbib
%{texmfdist}/bibtex/bst/germbib
%{texmfdist}/tex/latex/germbib

%files -n texlive-latex-bibtex-revtex4
%defattr(644,root,root,755)
%dir %{texmfdist}/source/latex/revtex
%doc %{texmfdist}/doc/latex/revtex
%{texmfdist}/bibtex/bib/revtex4
%{texmfdist}/bibtex/bst/revtex4

%files -n texlive-latex-bibtex-jurabib
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/jurabib
%{texmfdist}/bibtex/bst/jurabib
%{texmfdist}/bibtex/bib/jurabib
%{texmfdist}/source/latex/jurabib
%{texmfdist}/tex/latex/jurabib

%files -n texlive-latex-bibtex-dk
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/dk-bib
%{texmfdist}/bibtex/bst/dk-bib
%{texmfdist}/bibtex/csf/dk-bib
%{texmfdist}/bibtex/bib/dk-bib
%{texmfdist}/source/latex/dk-bib
%{texmfdist}/tex/latex/dk-bib

%files -n texlive-latex-bibtex-styles
%defattr(644,root,root,755)
%dir %{texmfdist}/source/bibtex
%doc %{texmfdist}/doc/bibtex/abstyles
%doc %{texmfdist}/doc/bibtex/bibhtml
%doc %{texmfdist}/doc/bibtex/dinat
%doc %{texmfdist}/doc/bibtex/gost
%doc %{texmfdist}/doc/bibtex/ijqc
%doc %{texmfdist}/doc/bibtex/iopart-num
%doc %{texmfdist}/doc/generic/t2
%doc %{texmfdist}/doc/latex/IEEEtran
%doc %{texmfdist}/doc/latex/authorindex
%doc %{texmfdist}/doc/latex/biblatex-chem
%doc %{texmfdist}/doc/latex/biblatex-dw
%doc %{texmfdist}/doc/latex/biblatex-historian
%doc %{texmfdist}/doc/latex/biblatex-philosophy
%doc %{texmfdist}/doc/latex/biblatex-science
%doc %{texmfdist}/doc/latex/biblatex
%{texmfdist}/bibtex/bib/IEEEtran
%{texmfdist}/bibtex/bib/abstyles
%{texmfdist}/bibtex/bib/beebe
%{texmfdist}/bibtex/bib/directory
%{texmfdist}/bibtex/bib/frankenstein
%{texmfdist}/bibtex/bib/gloss
%{texmfdist}/bibtex/bib/harvard
%{texmfdist}/bibtex/bib/lsc
%{texmfdist}/bibtex/bib/msc
%{texmfdist}/bibtex/bib/nostarch
%{texmfdist}/bibtex/bib/spie
%{texmfdist}/bibtex/bst/IEEEtran
%{texmfdist}/bibtex/bst/abstyles
%{texmfdist}/bibtex/bst/achemso
%{texmfdist}/bibtex/bst/afthesis
%{texmfdist}/bibtex/bst/aguplus
%{texmfdist}/bibtex/bst/aichej
%{texmfdist}/bibtex/bst/ametsoc
%{texmfdist}/bibtex/bst/beebe
%{texmfdist}/bibtex/bst/bibhtml
%{texmfdist}/bibtex/bst/chem-journal
%{texmfdist}/bibtex/bst/chicago
%{texmfdist}/bibtex/bst/confproc
%{texmfdist}/bibtex/bst/din1505
%{texmfdist}/bibtex/bst/dinat
%{texmfdist}/bibtex/bst/directory
%{texmfdist}/bibtex/bst/dvdcoll
%{texmfdist}/bibtex/bst/fbs
%{texmfdist}/bibtex/bst/figbib
%{texmfdist}/bibtex/bst/finbib
%{texmfdist}/bibtex/bst/frankenstein
%{texmfdist}/bibtex/bst/gloss
%{texmfdist}/bibtex/bst/gost
%{texmfdist}/bibtex/bst/gustlib
%{texmfdist}/bibtex/bst/harvard
%{texmfdist}/bibtex/bst/hc
%{texmfdist}/bibtex/bst/ieeepes
%{texmfdist}/bibtex/bst/ijmart
%{texmfdist}/bibtex/bst/ijqc
%{texmfdist}/bibtex/bst/imac
%{texmfdist}/bibtex/bst/index
%{texmfdist}/bibtex/bst/inlinebib
%{texmfdist}/bibtex/bst/iopart-num
%{texmfdist}/bibtex/bst/jneurosci
%{texmfdist}/bibtex/bst/jurarsp
%{texmfdist}/bibtex/bst/kluwer
%{texmfdist}/bibtex/bst/multibib
%{texmfdist}/bibtex/bst/munich
%{texmfdist}/bibtex/bst/nature
%{texmfdist}/bibtex/bst/nddiss
%{texmfdist}/bibtex/bst/opcit
%{texmfdist}/bibtex/bst/perception
%{texmfdist}/bibtex/bst/revtex
%{texmfdist}/bibtex/bst/savetrees
%{texmfdist}/bibtex/bst/shipunov
%{texmfdist}/bibtex/bst/sort-by-letters
%{texmfdist}/bibtex/bst/spie
%{texmfdist}/bibtex/bst/stellenbosch
%{texmfdist}/bibtex/bst/swebib
%{texmfdist}/bibtex/bst/texsis
%{texmfdist}/bibtex/bst/thuthesis
%{texmfdist}/bibtex/bst/tugboat
%{texmfdist}/bibtex/bst/urlbst
%{texmfdist}/bibtex/csf/gost
%{texmfdist}/tex/latex/biblatex-chem
%{texmfdist}/tex/latex/biblatex-dw
%{texmfdist}/tex/latex/biblatex-historian
%{texmfdist}/tex/latex/biblatex-philosophy
%{texmfdist}/tex/latex/biblatex-science
%{texmfdist}/tex/latex/biblatex
%{texmfdist}/source/bibtex/gost

%files -n texlive-latex-bibtex-vancouver
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bst/vancouver
%dir %{texmfdist}/doc/bibtex/vancouver
%doc %{texmfdist}/doc/bibtex/vancouver/README
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.pdf
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.tex
%{texmfdist}/bibtex/bst/vancouver/vancouver.bst

%files -n texlive-latex-booktabs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/booktabs
%{texmfdist}/source/latex/booktabs
%{texmfdist}/tex/latex/booktabs

%files -n texlive-latex-bosisio
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bosisio
%{texmfdist}/tex/latex/bosisio
%{texmfdist}/source/latex/bosisio

%files -n texlive-latex-caption
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/caption
%{texmfdist}/tex/latex/caption
%{texmfdist}/source/latex/caption

%files -n texlive-latex-carlisle
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/carlisle
%{texmfdist}/tex/latex/carlisle
%{texmfdist}/source/latex/carlisle

%files -n texlive-latex-ccfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ccfonts
%{texmfdist}/source/latex/ccfonts
%{texmfdist}/tex/latex/ccfonts

%files -n texlive-latex-cite
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/cite

%files -n texlive-latex-cmbright
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cmbright
%{texmfdist}/tex/latex/cmbright

%files -n texlive-latex-colortab
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/colortab
%{texmfdist}/tex/generic/colortab

%files -n texlive-latex-comment
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/comment
%{texmfdist}/tex/latex/comment

%files -n texlive-latex-concmath
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/concmath

%files -n texlive-ptex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/ptex
%{texmfdist}/tex/ptex
%{texmfdist}/fonts/source/ptex
%{texmfdist}/fonts/tfm/ptex
%{texmfdist}/fonts/type1/ptex
%{texmfdist}/fonts/vf/ptex

%files -n texlive-latex-ctex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ctex-faq
%doc %{texmfdist}/doc/latex/ctex
%{texmfdist}/tex/latex/ctex

%files -n texlive-latex-currvita
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/currvita
%{texmfdist}/tex/latex/currvita
%{texmfdist}/source/latex/currvita
%doc %{texmfdist}/doc/latex/curve
%{texmfdist}/source/latex/curve
%{texmfdist}/tex/latex/curve
%doc %{texmfdist}/doc/latex/ecv
%{texmfdist}/source/latex/ecv
%{texmfdist}/tex/latex/ecv
%doc %{texmfdist}/doc/latex/simplecv
%{texmfdist}/source/latex/simplecv
%{texmfdist}/tex/latex/simplecv

%files -n texlive-latex-curves
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/curves
%{texmfdist}/source/latex/curves
%{texmfdist}/tex/latex/curves

%files -n texlive-latex-custom-bib
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/custom-bib
%doc %{texmfdist}/doc/latex/chbibref
%{texmfdist}/source/latex/custom-bib
%{texmfdist}/tex/latex/chbibref
%{texmfdist}/tex/latex/custom-bib

%files -n texlive-latex-cyrillic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cyrillic
%{texmfdist}/source/latex/cyrillic
%{texmfdist}/tex/latex/cyrillic
%{texmfdist}/tex/latex/lh

%files -n texlive-latex-enumitem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/enumitem
%{texmfdist}/tex/latex/enumitem

%files -n texlive-latex-exams
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/alterqcm
%doc %{texmfdist}/doc/latex/answers
%doc %{texmfdist}/doc/latex/exam
%doc %{texmfdist}/doc/latex/examdesign
%doc %{texmfdist}/doc/latex/exercise
%doc %{texmfdist}/doc/latex/mathexam
%doc %{texmfdist}/doc/latex/probsoln
%doc %{texmfdist}/doc/latex/qcm
%doc %{texmfdist}/doc/latex/uebungsblatt
%{texmfdist}/source/latex/answers
%{texmfdist}/source/latex/examdesign
%{texmfdist}/source/latex/exercise
%{texmfdist}/source/latex/mathexam
%{texmfdist}/source/latex/probsoln
%{texmfdist}/source/latex/qcm
%{texmfdist}/tex/latex/alterqcm
%{texmfdist}/tex/latex/answers
%{texmfdist}/tex/latex/exam
%{texmfdist}/tex/latex/examdesign
%{texmfdist}/tex/latex/exercise
%{texmfdist}/tex/latex/mathexam
%{texmfdist}/tex/latex/probsoln
%{texmfdist}/tex/latex/qcm
%{texmfdist}/tex/latex/uebungsblatt

%files -n texlive-latex-float
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ccaption
%doc %{texmfdist}/doc/latex/photo
%doc %{texmfdist}/doc/latex/topfloat
%{texmfdist}/source/latex/ccaption
%{texmfdist}/source/latex/photo
%{texmfdist}/tex/latex/ccaption
%{texmfdist}/tex/latex/photo
%{texmfdist}/tex/latex/topfloat

%files -n texlive-latex-formular
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/formular
%{texmfdist}/tex/latex/formular
%{texmfdist}/source/latex/formular

%files -n texlive-latex-gbrief
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/g-brief
%{texmfdist}/source/latex/g-brief
%{texmfdist}/tex/latex/g-brief

%files -n texlive-latex-keystroke
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/keystroke
%doc %{texmfdist}/doc/latex/keystroke

%files -n texlive-latex-labbook
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/labbook
%{texmfdist}/source/latex/labbook
%{texmfdist}/tex/latex/labbook

%files -n texlive-latex-lastpage
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lastpage
%{texmfdist}/tex/latex/lastpage
%{texmfdist}/source/latex/lastpage

%files -n texlive-latex-lcd
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lcd
%{texmfdist}/source/latex/lcd
%{texmfdist}/tex/latex/lcd

%files -n texlive-latex-leaflet
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/leaflet
%{texmfdist}/source/latex/leaflet
%{texmfdist}/tex/latex/leaflet

%files -n texlive-latex-leftidx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/leftidx
%{texmfdist}/tex/latex/leftidx
%{texmfdist}/source/latex/leftidx

%files -n texlive-latex-lewis
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lewis
%{texmfdist}/tex/latex/lewis

%files -n texlive-latex-lm
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/cfr-lm
%{texmfdist}/tex/latex/lm
%{texmfdist}/fonts/vf/public/cfr-lm
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/enc/dvips/cfr-lm
%{texmfdist}/fonts/enc/dvips/lm
%{texmfdist}/fonts/map/dvips/cfr-lm
%{texmfdist}/fonts/map/dvips/lm
%{texmfdist}/fonts/map/dvipdfm/lm
%{texmfdist}/source/fonts/cfr-lm
%{texmfdist}/fonts/tfm/public/cfr-lm
%{texmfdist}/fonts/tfm/public/oldlatin
%{texmfdist}/fonts/source/public/oldlatin

%files -n texlive-latex-lineno
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/lineno
%{texmfdist}/tex/latex/lineno

%files -n texlive-latex-metre
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/metre
%{texmfdist}/source/latex/metre
%{texmfdist}/tex/latex/metre

%files -n texlive-latex-marvosym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/marvosym
%{texmfdist}/tex/latex/marvosym

%files -n texlive-latex-microtype
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/microtype
%{texmfdist}/source/latex/microtype
%{texmfdist}/tex/latex/microtype

%files -n texlive-latex-misc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/xcomment
%doc %{texmfdist}/doc/latex/advdate
%doc %{texmfdist}/doc/latex/chronology
%doc %{texmfdist}/doc/latex/cooking
%doc %{texmfdist}/doc/latex/cuisine
%doc %{texmfdist}/doc/latex/envbig
%doc %{texmfdist}/doc/latex/fixme
%doc %{texmfdist}/doc/latex/fn2end
%doc %{texmfdist}/doc/latex/fnpara
%doc %{texmfdist}/doc/latex/fwlw
%doc %{texmfdist}/doc/fonts/knitting
%doc %{texmfdist}/doc/latex/knittingpattern
%doc %{texmfdist}/doc/latex/liturg
%doc %{texmfdist}/doc/latex/mailmerge
%doc %{texmfdist}/doc/latex/menu
%doc %{texmfdist}/doc/latex/nicetext
%doc %{texmfdist}/doc/latex/ot-tableau
%doc %{texmfdist}/doc/latex/papermas
%doc %{texmfdist}/doc/latex/plantslabels
%doc %{texmfdist}/doc/latex/recipe
%doc %{texmfdist}/doc/latex/recipecard
%doc %{texmfdist}/doc/latex/simplecd
%doc %{texmfdist}/doc/latex/termcal
%doc %{texmfdist}/doc/latex/thumby
%doc %{texmfdist}/doc/latex/tkz-tab
%doc %{texmfdist}/doc/latex/truncate
%doc %{texmfdist}/doc/latex/twoinone
%doc %{texmfdist}/doc/latex/todo
%doc %{texmfdist}/doc/latex/todonotes
%doc %{texmfdist}/doc/latex/typehtml
%doc %{texmfdist}/doc/latex/vruler
%doc %{texmfdist}/doc/latex/wordlike
%{texmfdist}/fonts/afm/public/knitting
%{texmfdist}/fonts/map/dvips/knitting
%{texmfdist}/fonts/tfm/public/knitting
%{texmfdist}/fonts/type1/public/knitting
%{texmfdist}/fonts/source/public/knitting
%{texmfdist}/source/latex/cooking
%{texmfdist}/source/latex/cuisine
%{texmfdist}/source/latex/fixme
%{texmfdist}/source/latex/mailmerge
%{texmfdist}/source/latex/menu
%{texmfdist}/source/latex/papermas
%{texmfdist}/source/latex/recipecard
%{texmfdist}/source/latex/simplecd
%{texmfdist}/source/latex/termcal
%{texmfdist}/source/latex/todo
%{texmfdist}/source/latex/todonotes
%{texmfdist}/source/latex/wordlike
%{texmfdist}/tex/generic/xcomment
%{texmfdist}/tex/latex/advdate
%{texmfdist}/tex/latex/chronology
%{texmfdist}/tex/latex/cooking
%{texmfdist}/tex/latex/cuisine
%{texmfdist}/tex/latex/envbig
%{texmfdist}/tex/latex/fixme
%{texmfdist}/tex/latex/fn2end
%{texmfdist}/tex/latex/fnpara
%{texmfdist}/tex/latex/fwlw
%{texmfdist}/tex/latex/knitting
%{texmfdist}/tex/latex/knittingpattern
%{texmfdist}/tex/latex/liturg
%{texmfdist}/tex/latex/mailmerge
%{texmfdist}/tex/latex/menu
%{texmfdist}/tex/latex/nicetext
%{texmfdist}/tex/latex/ot-tableau
%{texmfdist}/tex/latex/papermas
%{texmfdist}/tex/latex/plantslabels
%{texmfdist}/tex/latex/recipe
%{texmfdist}/tex/latex/recipecard
%{texmfdist}/tex/latex/simplecd
%{texmfdist}/tex/latex/termcal
%{texmfdist}/tex/latex/thumby
%{texmfdist}/tex/latex/tkz-tab
%{texmfdist}/tex/latex/twoinone
%{texmfdist}/tex/latex/todo
%{texmfdist}/tex/latex/todonotes
%{texmfdist}/tex/latex/truncate
%{texmfdist}/tex/latex/typehtml
%{texmfdist}/tex/latex/vruler
%{texmfdist}/tex/latex/wordlike

%files -n texlive-latex-mflogo
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mflogo
%{texmfdist}/tex/latex/mflogo

%files -n texlive-latex-mfnfss
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mfnfss
%{texmfdist}/source/latex/mfnfss
%{texmfdist}/tex/latex/mfnfss

%files -n texlive-latex-minitoc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/minitoc
%{texmfdist}/bibtex/bst/minitoc
%{texmfdist}/makeindex/minitoc
%{texmfdist}/source/latex/minitoc
%{texmfdist}/tex/latex/minitoc

%files -n texlive-latex-mltex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mltex
%{texmfdist}/tex/latex/mltex
%dir %{texmfdist}/tex/mltex
%{texmfdist}/tex/mltex/config

%files -n texlive-latex-moreverb
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/moreverb
%{texmfdist}/tex/latex/moreverb
%{texmfdist}/source/latex/moreverb

%files -n texlive-latex-multienum
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/multenum
%dir %{texmfdist}/tex/latex/multenum
%{texmfdist}/tex/latex/multenum/*

%files -n texlive-latex-ntheorem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ntheorem
%{texmfdist}/tex/latex/ntheorem
%{texmfdist}/source/latex/ntheorem

%files -n texlive-latex-other-doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/a0poster
%doc %{texmfdist}/doc/latex/afthesis
%doc %{texmfdist}/doc/latex/aguplus
%doc %{texmfdist}/doc/latex/akletter
%doc %{texmfdist}/doc/latex/algorithm2e
%doc %{texmfdist}/doc/latex/algorithmicx
%doc %{texmfdist}/doc/latex/altfont
%doc %{texmfdist}/doc/latex/ametsoc
%doc %{texmfdist}/doc/latex/amsaddr
%doc %{texmfdist}/doc/latex/amsrefs
%doc %{texmfdist}/doc/latex/animate
%doc %{texmfdist}/doc/latex/anyfontsize
%doc %{texmfdist}/doc/latex/arabi
%doc %{texmfdist}/doc/latex/arabtex
%doc %{texmfdist}/doc/latex/assignment
%doc %{texmfdist}/doc/latex/augie
%doc %{texmfdist}/doc/latex/aurical
%doc %{texmfdist}/doc/latex/autoarea
%doc %{texmfdist}/doc/latex/bangtex
%doc %{texmfdist}/doc/latex/barcodes
%doc %{texmfdist}/doc/latex/bbm-macros
%doc %{texmfdist}/doc/latex/begriff
%doc %{texmfdist}/doc/latex/betababel
%doc %{texmfdist}/doc/latex/bibarts
%doc %{texmfdist}/doc/latex/bibleref
%doc %{texmfdist}/doc/latex/biblist
%doc %{texmfdist}/doc/latex/bigfoot
%doc %{texmfdist}/doc/latex/bizcard
%doc %{texmfdist}/doc/latex/blindtext
%doc %{texmfdist}/doc/latex/boldtensors
%doc %{texmfdist}/doc/latex/bookest
%doc %{texmfdist}/doc/latex/boxhandler
%doc %{texmfdist}/doc/latex/braille
%doc %{texmfdist}/doc/latex/breakurl
%doc %{texmfdist}/doc/latex/bussproofs
%doc %{texmfdist}/doc/latex/captcont
%doc %{texmfdist}/doc/latex/casyl
%doc %{texmfdist}/doc/latex/catechis
%doc %{texmfdist}/doc/latex/cbcoptic
%doc %{texmfdist}/doc/latex/cclicenses
%doc %{texmfdist}/doc/latex/cd-cover
%doc %{texmfdist}/doc/latex/cd
%doc %{texmfdist}/doc/latex/cdpbundl
%doc %{texmfdist}/doc/latex/cellspace
%doc %{texmfdist}/doc/latex/changes
%doc %{texmfdist}/doc/latex/chapterfolder
%doc %{texmfdist}/doc/latex/cite
%doc %{texmfdist}/doc/latex/classicthesis
%doc %{texmfdist}/doc/latex/cleveref
%doc %{texmfdist}/doc/latex/clock
%doc %{texmfdist}/doc/latex/clrscode
%doc %{texmfdist}/doc/latex/cmap
%doc %{texmfdist}/doc/latex/cmdstring
%doc %{texmfdist}/doc/latex/codepage
%doc %{texmfdist}/doc/latex/colorinfo
%doc %{texmfdist}/doc/latex/commath
%doc %{texmfdist}/doc/latex/complexity
%doc %{texmfdist}/doc/latex/concprog
%doc %{texmfdist}/doc/latex/confproc
%doc %{texmfdist}/doc/latex/courseoutline
%doc %{texmfdist}/doc/latex/coursepaper
%doc %{texmfdist}/doc/latex/coverpage
%doc %{texmfdist}/doc/latex/covington
%doc %{texmfdist}/doc/latex/crossreference
%doc %{texmfdist}/doc/latex/cryst
%doc %{texmfdist}/doc/latex/csbulletin
%doc %{texmfdist}/doc/latex/csquotes
%doc %{texmfdist}/doc/latex/ctib
%doc %{texmfdist}/doc/latex/cv
%doc %{texmfdist}/doc/latex/cweb-latex
%doc %{texmfdist}/doc/latex/dateiliste
%doc %{texmfdist}/doc/latex/datetime
%doc %{texmfdist}/doc/latex/diagnose
%doc %{texmfdist}/doc/latex/dichokey
%doc %{texmfdist}/doc/latex/digiconfigs
%doc %{texmfdist}/doc/latex/din1505
%doc %{texmfdist}/doc/latex/directory
%doc %{texmfdist}/doc/latex/dlfltxb
%doc %{texmfdist}/doc/latex/docmfp
%doc %{texmfdist}/doc/latex/doi
%doc %{texmfdist}/doc/latex/doipubmed
%doc %{texmfdist}/doc/latex/dotarrow
%doc %{texmfdist}/doc/latex/dottex
%doc %{texmfdist}/doc/latex/dpfloat
%doc %{texmfdist}/doc/latex/drac
%doc %{texmfdist}/doc/latex/dramatist
%doc %{texmfdist}/doc/latex/dtxgallery
%doc %{texmfdist}/doc/latex/duerer-latex
%doc %{texmfdist}/doc/latex/dvdcoll
%doc %{texmfdist}/doc/latex/ean13isbn
%doc %{texmfdist}/doc/latex/easy
%doc %{texmfdist}/doc/latex/ebezier
%doc %{texmfdist}/doc/latex/ebong
%doc %{texmfdist}/doc/latex/ebsthesis
%doc %{texmfdist}/doc/latex/ecclesiastic
%doc %{texmfdist}/doc/latex/ecltree
%doc %{texmfdist}/doc/latex/ed
%doc %{texmfdist}/doc/latex/edmac
%doc %{texmfdist}/doc/latex/edmargin
%doc %{texmfdist}/doc/latex/ednotes
%doc %{texmfdist}/doc/latex/eemeir
%doc %{texmfdist}/doc/latex/egameps
%doc %{texmfdist}/doc/latex/ellipsis
%doc %{texmfdist}/doc/latex/elpres
%doc %{texmfdist}/doc/latex/emp
%doc %{texmfdist}/doc/latex/emulateapj
%doc %{texmfdist}/doc/latex/endheads
%doc %{texmfdist}/doc/latex/engpron
%doc %{texmfdist}/doc/latex/engrec
%doc %{texmfdist}/doc/latex/envlab
%doc %{texmfdist}/doc/latex/epigraph
%doc %{texmfdist}/doc/latex/epiolmec
%doc %{texmfdist}/doc/latex/epsdice
%doc %{texmfdist}/doc/latex/epspdfconversion
%doc %{texmfdist}/doc/latex/eqparbox
%doc %{texmfdist}/doc/latex/errata
%doc %{texmfdist}/doc/latex/eskdx
%doc %{texmfdist}/doc/latex/etex-pkg
%doc %{texmfdist}/doc/latex/ethiop-t1
%doc %{texmfdist}/doc/latex/ethiop
%doc %{texmfdist}/doc/latex/etoolbox
%doc %{texmfdist}/doc/latex/eukdate
%doc %{texmfdist}/doc/latex/euro
%doc %{texmfdist}/doc/latex/europecv
%doc %{texmfdist}/doc/latex/everypage
%doc %{texmfdist}/doc/latex/examplep
%doc %{texmfdist}/doc/latex/extarrows
%doc %{texmfdist}/doc/latex/extract
%doc %{texmfdist}/doc/latex/facsimile
%doc %{texmfdist}/doc/latex/fancynum
%doc %{texmfdist}/doc/latex/fancyref
%doc %{texmfdist}/doc/latex/fancytooltips
%doc %{texmfdist}/doc/latex/figbib
%doc %{texmfdist}/doc/latex/figsize
%doc %{texmfdist}/doc/latex/fink
%doc %{texmfdist}/doc/latex/fixfoot
%doc %{texmfdist}/doc/latex/flabels
%doc %{texmfdist}/doc/latex/flacards
%doc %{texmfdist}/doc/latex/flagderiv
%doc %{texmfdist}/doc/latex/flashcards
%doc %{texmfdist}/doc/latex/floatrow
%doc %{texmfdist}/doc/latex/fmp
%doc %{texmfdist}/doc/latex/fnbreak
%doc %{texmfdist}/doc/latex/fncychap
%doc %{texmfdist}/doc/latex/foekfont
%doc %{texmfdist}/doc/latex/fonttable
%doc %{texmfdist}/doc/latex/frankenstein
%doc %{texmfdist}/doc/latex/frenchle
%doc %{texmfdist}/doc/latex/frletter
%doc %{texmfdist}/doc/latex/frontespizio
%doc %{texmfdist}/doc/latex/fullblck
%doc %{texmfdist}/doc/latex/gaceta
%doc %{texmfdist}/doc/latex/gastex
%doc %{texmfdist}/doc/latex/gauss
%doc %{texmfdist}/doc/latex/gb4e
%doc %{texmfdist}/doc/latex/gcard
%doc %{texmfdist}/doc/latex/gcite
%doc %{texmfdist}/doc/latex/genmpage
%doc %{texmfdist}/doc/latex/gloss
%doc %{texmfdist}/doc/latex/glossaries
%doc %{texmfdist}/doc/latex/gmdoc
%doc %{texmfdist}/doc/latex/gmeometric
%doc %{texmfdist}/doc/latex/gmiflink
%doc %{texmfdist}/doc/latex/gmutils
%doc %{texmfdist}/doc/latex/gmverb
%doc %{texmfdist}/doc/latex/graphicx-psmin
%doc %{texmfdist}/doc/latex/greek-inputenc
%doc %{texmfdist}/doc/latex/greekdates
%doc %{texmfdist}/doc/latex/grfpaste
%doc %{texmfdist}/doc/latex/gu
%doc %{texmfdist}/doc/latex/hanging
%doc %{texmfdist}/doc/latex/har2nat
%doc %{texmfdist}/doc/latex/harmony
%doc %{texmfdist}/doc/latex/harpoon
%doc %{texmfdist}/doc/latex/harvard
%doc %{texmfdist}/doc/latex/hc
%doc %{texmfdist}/doc/latex/hep
%doc %{texmfdist}/doc/latex/hepnames
%doc %{texmfdist}/doc/latex/hepparticles
%doc %{texmfdist}/doc/latex/hepthesis
%doc %{texmfdist}/doc/latex/hepunits
%doc %{texmfdist}/doc/latex/hexgame
%doc %{texmfdist}/doc/latex/histogr
%doc %{texmfdist}/doc/latex/hitec
%doc %{texmfdist}/doc/latex/hpsdiss
%doc %{texmfdist}/doc/latex/hvfloat
%doc %{texmfdist}/doc/latex/hypdvips
%doc %{texmfdist}/doc/latex/hyperref-docsrc
%doc %{texmfdist}/doc/latex/hyperxmp
%doc %{texmfdist}/doc/latex/ibycus-babel
%doc %{texmfdist}/doc/latex/icsv
%doc %{texmfdist}/doc/latex/ieeepes
%doc %{texmfdist}/doc/latex/ifmslide
%doc %{texmfdist}/doc/latex/ifplatform
%doc %{texmfdist}/doc/latex/ijmart
%doc %{texmfdist}/doc/latex/imac
%doc %{texmfdist}/doc/latex/image-gallery
%doc %{texmfdist}/doc/latex/imtekda
%doc %{texmfdist}/doc/latex/inlinedef
%doc %{texmfdist}/doc/latex/interactiveworkbook
%doc %{texmfdist}/doc/latex/iso
%doc %{texmfdist}/doc/latex/iso10303
%doc %{texmfdist}/doc/latex/isodate
%doc %{texmfdist}/doc/latex/isodoc
%doc %{texmfdist}/doc/latex/itnumpar
%doc %{texmfdist}/doc/latex/jknapltx
%doc %{texmfdist}/doc/latex/jneurosci
%doc %{texmfdist}/doc/latex/jpsj
%doc %{texmfdist}/doc/latex/jura
%doc %{texmfdist}/doc/latex/juraabbrev
%doc %{texmfdist}/doc/latex/juramisc
%doc %{texmfdist}/doc/latex/jurarsp
%doc %{texmfdist}/doc/latex/karnaugh
%doc %{texmfdist}/doc/latex/kerkis
%doc %{texmfdist}/doc/latex/kerntest
%doc %{texmfdist}/doc/latex/kluwer
%doc %{texmfdist}/doc/latex/lazylist
%doc %{texmfdist}/doc/latex/lcyw
%doc %{texmfdist}/doc/latex/ledmac
%doc %{texmfdist}/doc/latex/lgreek
%doc %{texmfdist}/doc/latex/lhelp
%doc %{texmfdist}/doc/latex/linguex
%doc %{texmfdist}/doc/latex/lipsum
%doc %{texmfdist}/doc/latex/lkproof
%doc %{texmfdist}/doc/latex/ltxindex
%doc %{texmfdist}/doc/latex/mafr
%doc %{texmfdist}/doc/latex/mailing
%doc %{texmfdist}/doc/latex/makebarcode
%doc %{texmfdist}/doc/latex/makedtx
%doc %{texmfdist}/doc/latex/makeglos
%doc %{texmfdist}/doc/latex/mathdesign
%doc %{texmfdist}/doc/latex/mathpazo
%doc %{texmfdist}/doc/latex/mceinleger
%doc %{texmfdist}/doc/latex/memexsupp
%doc %{texmfdist}/doc/latex/metaplot
%doc %{texmfdist}/doc/latex/mftinc
%doc %{texmfdist}/doc/latex/minutes
%doc %{texmfdist}/doc/latex/mmap
%doc %{texmfdist}/doc/latex/mnsymbol
%doc %{texmfdist}/doc/latex/moderncv
%doc %{texmfdist}/doc/latex/modroman
%doc %{texmfdist}/doc/latex/mongolian-babel
%doc %{texmfdist}/doc/latex/montex
%doc %{texmfdist}/doc/latex/moresize
%doc %{texmfdist}/doc/latex/msg
%doc %{texmfdist}/doc/latex/mtgreek
%doc %{texmfdist}/doc/latex/multibbl
%doc %{texmfdist}/doc/latex/multirow
%doc %{texmfdist}/doc/latex/munich
%doc %{texmfdist}/doc/latex/muthesis
%doc %{texmfdist}/doc/latex/ncclatex
%doc %{texmfdist}/doc/latex/ncctools
%doc %{texmfdist}/doc/latex/nddiss
%doc %{texmfdist}/doc/latex/newfile
%doc %{texmfdist}/doc/latex/newlfm
%doc %{texmfdist}/doc/latex/newspaper
%doc %{texmfdist}/doc/latex/nomentbl
%doc %{texmfdist}/doc/latex/nonfloat
%doc %{texmfdist}/doc/latex/numname
%doc %{texmfdist}/doc/latex/ocr-latex
%doc %{texmfdist}/doc/latex/opcit
%doc %{texmfdist}/doc/latex/ordinalpt
%doc %{texmfdist}/doc/latex/otibet
%doc %{texmfdist}/doc/latex/outline
%doc %{texmfdist}/doc/latex/outliner
%doc %{texmfdist}/doc/latex/pagenote
%doc %{texmfdist}/doc/latex/papercdcase
%doc %{texmfdist}/doc/latex/paresse
%doc %{texmfdist}/doc/latex/parrun
%doc %{texmfdist}/doc/latex/pauldoc
%doc %{texmfdist}/doc/latex/pdfwin
%doc %{texmfdist}/doc/latex/pecha
%doc %{texmfdist}/doc/latex/perception
%doc %{texmfdist}/doc/latex/perltex
%doc %{texmfdist}/doc/latex/pgf-soroban
%doc %{texmfdist}/doc/latex/pgfopts
%doc %{texmfdist}/doc/latex/philex
%doc %{texmfdist}/doc/latex/plates
%doc %{texmfdist}/doc/latex/plweb
%doc %{texmfdist}/doc/latex/pmgraph
%doc %{texmfdist}/doc/latex/polski
%doc %{texmfdist}/doc/latex/postcards
%doc %{texmfdist}/doc/latex/prettyref
%doc %{texmfdist}/doc/latex/proba
%doc %{texmfdist}/doc/latex/procIAGssymp
%doc %{texmfdist}/doc/latex/protex
%doc %{texmfdist}/doc/latex/protocol
%doc %{texmfdist}/doc/latex/psfragx
%doc %{texmfdist}/doc/latex/psgo
%doc %{texmfdist}/doc/latex/pspicture
%doc %{texmfdist}/doc/latex/pst2pdf
%doc %{texmfdist}/doc/latex/qobitree
%doc %{texmfdist}/doc/latex/qstest
%doc %{texmfdist}/doc/latex/quotmark
%doc %{texmfdist}/doc/latex/r_und_s
%doc %{texmfdist}/doc/latex/randbild
%doc %{texmfdist}/doc/latex/rcs
%doc %{texmfdist}/doc/latex/rcsinfo
%doc %{texmfdist}/doc/latex/rectopma
%doc %{texmfdist}/doc/latex/refcheck
%doc %{texmfdist}/doc/latex/refstyle
%doc %{texmfdist}/doc/latex/relenc
%doc %{texmfdist}/doc/latex/repeatindex
%doc %{texmfdist}/doc/latex/rmpage
%doc %{texmfdist}/doc/latex/robustindex
%doc %{texmfdist}/doc/latex/rtkinenc
%doc %{texmfdist}/doc/latex/rtklage
%doc %{texmfdist}/doc/latex/sanskrit
%doc %{texmfdist}/doc/latex/sauerj
%doc %{texmfdist}/doc/latex/sauterfonts
%doc %{texmfdist}/doc/latex/savefnmark
%doc %{texmfdist}/doc/latex/savetrees
%doc %{texmfdist}/doc/latex/scalebar
%doc %{texmfdist}/doc/latex/semioneside
%doc %{texmfdist}/doc/latex/seqsplit
%doc %{texmfdist}/doc/latex/sf298
%doc %{texmfdist}/doc/latex/sffms
%doc %{texmfdist}/doc/latex/sfg
%doc %{texmfdist}/doc/latex/shorttoc
%doc %{texmfdist}/doc/latex/show2e
%doc %{texmfdist}/doc/latex/showexpl
%doc %{texmfdist}/doc/latex/slantsc
%doc %{texmfdist}/doc/latex/smalltableof
%doc %{texmfdist}/doc/latex/smartref
%doc %{texmfdist}/doc/latex/snapshot
%doc %{texmfdist}/doc/latex/sparklines
%doc %{texmfdist}/doc/latex/spie
%doc %{texmfdist}/doc/latex/splitbib
%doc %{texmfdist}/doc/latex/spotcolor
%doc %{texmfdist}/doc/latex/srcltx
%doc %{texmfdist}/doc/latex/statistik
%doc %{texmfdist}/doc/latex/stdpage
%doc %{texmfdist}/doc/latex/stellenbosch
%doc %{texmfdist}/doc/latex/stex
%doc %{texmfdist}/doc/latex/struktex
%doc %{texmfdist}/doc/latex/sttools
%doc %{texmfdist}/doc/latex/stubs
%doc %{texmfdist}/doc/latex/sugconf
%doc %{texmfdist}/doc/latex/supertabular
%doc %{texmfdist}/doc/latex/svgcolor
%doc %{texmfdist}/doc/latex/svn-multi
%doc %{texmfdist}/doc/latex/svn
%doc %{texmfdist}/doc/latex/svninfo
%doc %{texmfdist}/doc/latex/swebib
%doc %{texmfdist}/doc/latex/swimgraf
%doc %{texmfdist}/doc/latex/synproof
%doc %{texmfdist}/doc/latex/syntax
%doc %{texmfdist}/doc/latex/syntrace
%doc %{texmfdist}/doc/latex/synttree
%doc %{texmfdist}/doc/latex/t-angles
%doc %{texmfdist}/doc/latex/tableaux
%doc %{texmfdist}/doc/latex/tablists
%doc %{texmfdist}/doc/latex/tablor
%doc %{texmfdist}/doc/latex/tabto-ltx
%doc %{texmfdist}/doc/latex/tabulary
%doc %{texmfdist}/doc/latex/tabvar
%doc %{texmfdist}/doc/latex/talk
%doc %{texmfdist}/doc/latex/tcldoc
%doc %{texmfdist}/doc/latex/tdsfrmath
%doc %{texmfdist}/doc/latex/technics
%doc %{texmfdist}/doc/latex/ted
%doc %{texmfdist}/doc/latex/tengwarscript
%doc %{texmfdist}/doc/latex/tensor
%doc %{texmfdist}/doc/latex/teubner
%doc %{texmfdist}/doc/latex/texmate
%doc %{texmfdist}/doc/latex/texpower
%doc %{texmfdist}/doc/latex/texshade
%doc %{texmfdist}/doc/latex/textcase
%doc %{texmfdist}/doc/latex/textopo
%doc %{texmfdist}/doc/latex/theoremref
%doc %{texmfdist}/doc/latex/thesis-titlepage-fhac
%doc %{texmfdist}/doc/latex/thinsp
%doc %{texmfdist}/doc/latex/thmtools
%doc %{texmfdist}/doc/latex/thumb
%doc %{texmfdist}/doc/latex/thuthesis
%doc %{texmfdist}/doc/latex/ticket
%doc %{texmfdist}/doc/latex/tikz-inet
%doc %{texmfdist}/doc/latex/titling
%doc %{texmfdist}/doc/latex/tocvsec2
%doc %{texmfdist}/doc/latex/tokenizer
%doc %{texmfdist}/doc/latex/toolbox
%doc %{texmfdist}/doc/latex/toptesi
%doc %{texmfdist}/doc/latex/trajan
%doc %{texmfdist}/doc/latex/trivfloat
%doc %{texmfdist}/doc/latex/turnstile
%doc %{texmfdist}/doc/latex/twoup
%doc %{texmfdist}/doc/latex/typogrid
%doc %{texmfdist}/doc/latex/umlaute
%doc %{texmfdist}/doc/latex/unitsdef
%doc %{texmfdist}/doc/latex/upmethodology
%doc %{texmfdist}/doc/latex/varindex
%doc %{texmfdist}/doc/latex/varsfromjobname
%doc %{texmfdist}/doc/latex/verse
%doc %{texmfdist}/doc/latex/vhistory
%doc %{texmfdist}/doc/latex/volumes
%doc %{texmfdist}/doc/latex/vpe
%doc %{texmfdist}/doc/latex/vwcol
%doc %{texmfdist}/doc/latex/wallpaper
%doc %{texmfdist}/doc/latex/warpcol
%doc %{texmfdist}/doc/latex/xargs
%doc %{texmfdist}/doc/latex/xdoc
%doc %{texmfdist}/doc/latex/xfor
%doc %{texmfdist}/doc/latex/xifthen
%doc %{texmfdist}/doc/latex/xmpincl
%doc %{texmfdist}/doc/latex/xnewcommand
%doc %{texmfdist}/doc/latex/xoptarg
%doc %{texmfdist}/doc/latex/xskak
%doc %{texmfdist}/doc/latex/xyling
%doc %{texmfdist}/doc/latex/xytree
%doc %{texmfdist}/doc/latex/yafoot
%doc %{texmfdist}/doc/latex/yhmath
%doc %{texmfdist}/doc/latex/york-thesis
%doc %{texmfdist}/doc/latex/yplan
%doc %{texmfdist}/doc/latex/zed-csp
%doc %{texmfdist}/doc/latex/ziffer
%doc %{texmfdist}/doc/latex/zwgetfdate

%files -n texlive-latex-math-sources
%defattr(644,root,root,755)
%{texmfdist}/source/latex/bez123
%{texmfdist}/source/latex/binomexp
%{texmfdist}/source/latex/cmll
%{texmfdist}/source/latex/constants
%{texmfdist}/source/latex/coordsys
%{texmfdist}/source/latex/dotseqn
%{texmfdist}/source/latex/egplot
%{texmfdist}/source/latex/eqlist
%{texmfdist}/source/latex/esdiff
%{texmfdist}/source/latex/esvect
%{texmfdist}/source/latex/extpfeil
%{texmfdist}/source/latex/fouridx
%{texmfdist}/source/latex/functan
%{texmfdist}/source/latex/galois
%{texmfdist}/source/latex/gnuplottex
%{texmfdist}/source/latex/hhtensor
%{texmfdist}/source/latex/logpap
%{texmfdist}/source/latex/mathcomp
%{texmfdist}/source/latex/noitcrul
%{texmfdist}/source/latex/permute
%{texmfdist}/source/latex/qsymbols
%{texmfdist}/source/latex/subdepth
%{texmfdist}/source/latex/faktor
%{texmfdist}/source/latex/ionumbers
%{texmfdist}/source/latex/sseq
%{texmfdist}/source/latex/trsym
%{texmfdist}/source/latex/mattens
%{texmfdist}/source/latex/mlist
%{texmfdist}/source/latex/numprint

%files -n texlive-latex-math
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/eco
%doc %{texmfdist}/doc/generic/dcpic
%doc %{texmfdist}/doc/latex/bez123
%doc %{texmfdist}/doc/latex/bigints
%doc %{texmfdist}/doc/latex/binomexp
%doc %{texmfdist}/doc/latex/cancel
%doc %{texmfdist}/doc/latex/cases
%doc %{texmfdist}/doc/latex/constants
%doc %{texmfdist}/doc/latex/coordsys
%doc %{texmfdist}/doc/latex/diagmac2
%doc %{texmfdist}/doc/latex/dotseqn
%doc %{texmfdist}/doc/latex/dot2texi
%doc %{texmfdist}/doc/latex/egplot
%doc %{texmfdist}/doc/latex/eqlist
%doc %{texmfdist}/doc/latex/esdiff
%doc %{texmfdist}/doc/latex/esvect
%doc %{texmfdist}/doc/latex/extpfeil
%doc %{texmfdist}/doc/latex/faktor
%doc %{texmfdist}/doc/latex/fouridx
%doc %{texmfdist}/doc/latex/functan
%doc %{texmfdist}/doc/latex/galois
%doc %{texmfdist}/doc/latex/gene-logic
%doc %{texmfdist}/doc/latex/gnuplottex
%doc %{texmfdist}/doc/latex/hhtensor
%doc %{texmfdist}/doc/latex/ionumbers
%doc %{texmfdist}/doc/latex/isomath
%doc %{texmfdist}/doc/latex/isonums
%doc %{texmfdist}/doc/latex/logpap
%doc %{texmfdist}/doc/latex/makeplot
%doc %{texmfdist}/doc/latex/mathcomp
%doc %{texmfdist}/doc/latex/maybemath
%doc %{texmfdist}/doc/latex/mattens
%doc %{texmfdist}/doc/latex/mfpic4ode
%doc %{texmfdist}/doc/latex/mhequ
%doc %{texmfdist}/doc/latex/mlist
%doc %{texmfdist}/doc/latex/nath
%doc %{texmfdist}/doc/latex/noitcrul
%doc %{texmfdist}/doc/latex/numprint
%doc %{texmfdist}/doc/latex/oubraces
%doc %{texmfdist}/doc/latex/permute
%doc %{texmfdist}/doc/latex/qsymbols
%doc %{texmfdist}/doc/latex/qtree
%doc %{texmfdist}/doc/latex/sdrt
%doc %{texmfdist}/doc/latex/semantic
%doc %{texmfdist}/doc/latex/simplewick
%doc %{texmfdist}/doc/latex/sseq
%doc %{texmfdist}/doc/latex/subdepth
%doc %{texmfdist}/doc/latex/subeqn
%doc %{texmfdist}/doc/latex/subeqnarray
%doc %{texmfdist}/doc/latex/subsupscripts
%doc %{texmfdist}/doc/latex/tikz-3dplot
%doc %{texmfdist}/doc/latex/tkz-linknodes
%doc %{texmfdist}/doc/latex/trfsigns
%doc %{texmfdist}/doc/latex/trsym
%{texmfdist}/fonts/map/dvips/cmll
%{texmfdist}/fonts/map/dvips/esvect
%{texmfdist}/fonts/opentype/public/stix
%{texmfdist}/fonts/opentype/public/xits
%{texmfdist}/source/fonts/xits
%{texmfdist}/fonts/source/public/cmll
%{texmfdist}/fonts/source/public/esvect
%{texmfdist}/fonts/source/public/trsym
%{texmfdist}/fonts/tfm/public/cmll
%{texmfdist}/fonts/tfm/public/eco
%{texmfdist}/fonts/tfm/public/esvect
%{texmfdist}/fonts/tfm/public/trsym
%{texmfdist}/fonts/type1/public/cmll
%{texmfdist}/fonts/type1/public/esvect
%{texmfdist}/fonts/vf/public/eco
%{texmfdist}/source/fonts/eco
%{texmfdist}/source/latex/makeplot
%{texmfdist}/source/latex/mfpic4ode
%{texmfdist}/source/latex/semantic
%{texmfdist}/source/latex/simplewick
%{texmfdist}/source/latex/subeqn
%{texmfdist}/source/latex/subeqnarray
%{texmfdist}/source/latex/trfsigns
%{texmfdist}/tex/generic/dcpic
%{texmfdist}/tex/latex/bez123
%{texmfdist}/tex/latex/bigints
%{texmfdist}/tex/latex/binomexp
%{texmfdist}/tex/latex/cmll
%{texmfdist}/tex/latex/cancel
%{texmfdist}/tex/latex/cases
%{texmfdist}/tex/latex/constants
%{texmfdist}/tex/latex/coordsys
%{texmfdist}/tex/latex/diagmac2
%{texmfdist}/tex/latex/dot2texi
%{texmfdist}/tex/latex/dotseqn
%{texmfdist}/tex/latex/egplot
%{texmfdist}/tex/latex/eqlist
%{texmfdist}/tex/latex/esdiff
%{texmfdist}/tex/latex/esvect
%{texmfdist}/tex/latex/extpfeil
%{texmfdist}/tex/latex/faktor
%{texmfdist}/tex/latex/fouridx
%{texmfdist}/tex/latex/functan
%{texmfdist}/tex/latex/galois
%{texmfdist}/tex/latex/gene-logic
%{texmfdist}/tex/latex/gnuplottex
%{texmfdist}/tex/latex/hhtensor
%{texmfdist}/tex/latex/ionumbers
%{texmfdist}/tex/latex/isomath
%{texmfdist}/tex/latex/isonums
%{texmfdist}/tex/latex/logpap
%{texmfdist}/tex/latex/makeplot
%{texmfdist}/tex/latex/maybemath
%{texmfdist}/tex/latex/mathcomp
%{texmfdist}/tex/latex/mattens
%{texmfdist}/tex/latex/mfpic4ode
%{texmfdist}/tex/latex/mhequ
%{texmfdist}/tex/latex/mlist
%{texmfdist}/tex/latex/nath
%{texmfdist}/tex/latex/noitcrul
%{texmfdist}/tex/latex/numprint
%{texmfdist}/tex/latex/oubraces
%{texmfdist}/tex/latex/permute
%{texmfdist}/tex/latex/qsymbols
%{texmfdist}/tex/latex/qtree
%{texmfdist}/tex/latex/sdrt
%{texmfdist}/tex/latex/semantic
%{texmfdist}/tex/latex/sfmath
%{texmfdist}/tex/latex/simplewick
%{texmfdist}/tex/latex/sseq
%{texmfdist}/tex/latex/subdepth
%{texmfdist}/tex/latex/subeqn
%{texmfdist}/tex/latex/subeqnarray
%{texmfdist}/tex/latex/subsupscripts
%{texmfdist}/tex/latex/tikz-3dplot
%{texmfdist}/tex/latex/tkz-linknodes
%{texmfdist}/tex/latex/trfsigns
%{texmfdist}/tex/latex/trsym
%doc %{texmfdist}/doc/latex/tree-dvips
%{texmfdist}/tex/latex/tree-dvips

%files -n texlive-latex-physics
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/feyn
%doc %{texmfdist}/doc/latex/braket
%doc %{texmfdist}/doc/latex/circ
%doc %{texmfdist}/doc/latex/circuitikz
%doc %{texmfdist}/doc/latex/colorwav
%doc %{texmfdist}/doc/latex/dyntree
%doc %{texmfdist}/doc/latex/eltex
%doc %{texmfdist}/doc/latex/engtlc
%doc %{texmfdist}/doc/latex/feynmf
%doc %{texmfdist}/doc/latex/listofsymbols
%doc %{texmfdist}/doc/latex/miller
%doc %{texmfdist}/doc/latex/susy
%{texmfdist}/metapost/feynmf
%{texmfdist}/source/generic/pst-electricfield
%{texmfdist}/source/generic/pst-magneticfield
%{texmfdist}/source/latex/circ
%{texmfdist}/source/latex/colorwav
%{texmfdist}/source/latex/dyntree
%{texmfdist}/source/latex/feynmf
%{texmfdist}/source/latex/isotope
%{texmfdist}/source/latex/listofsymbols
%{texmfdist}/source/latex/miller
%{texmfdist}/tex/generic/pst-electricfield
%{texmfdist}/tex/generic/pst-magneticfield
%{texmfdist}/tex/latex/braket
%{texmfdist}/tex/latex/circ
%{texmfdist}/tex/latex/circuitikz
%{texmfdist}/tex/latex/colorwav
%{texmfdist}/tex/latex/dyntree
%{texmfdist}/tex/latex/eltex
%{texmfdist}/tex/latex/engtlc
%{texmfdist}/tex/latex/feynmf
%{texmfdist}/tex/latex/isotope
%{texmfdist}/tex/latex/listofsymbols
%{texmfdist}/tex/latex/miller
%{texmfdist}/tex/latex/pst-electricfield
%{texmfdist}/tex/latex/pst-magneticfield
%{texmfdist}/tex/latex/susy
%{texmfdist}/fonts/source/public/circ
%{texmfdist}/fonts/tfm/public/circ
%{texmfdist}/fonts/source/public/feyn
%{texmfdist}/fonts/tfm/public/feyn
%{texmfdist}/source/fonts/feyn

%files -n texlive-latex-chem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/achemso
%doc %{texmfdist}/doc/latex/bpchem
%doc %{texmfdist}/doc/latex/chemstyle
%doc %{texmfdist}/doc/latex/mhchem
%doc %{texmfdist}/doc/fonts/chemarrow
%doc %{texmfdist}/doc/latex/chemcompounds
%doc %{texmfdist}/doc/latex/chemcono
%{texmfdist}/fonts/afm/public/chemarrow
%{texmfdist}/fonts/map/dvips/chemarrow
%{texmfdist}/fonts/source/public/chemarrow
%{texmfdist}/fonts/tfm/public/chemarrow
%{texmfdist}/fonts/type1/public/chemarrow
%{texmfdist}/source/fonts/chemarrow
%{texmfdist}/source/latex/achemso
%{texmfdist}/source/latex/bpchem
%{texmfdist}/source/latex/chemcompounds
%{texmfdist}/source/latex/chemstyle
%{texmfdist}/tex/latex/achemso
%{texmfdist}/tex/latex/bpchem
%{texmfdist}/tex/latex/chemarrow
%{texmfdist}/tex/latex/chemcompounds
%{texmfdist}/tex/latex/chemcono
%{texmfdist}/tex/latex/chemstyle
%{texmfdist}/tex/latex/mhchem

%files -n texlive-latex-bidi
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bidi
%{texmfdist}/tex/latex/bidi

%files -n texlive-latex-biology
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/biocon
%doc %{texmfdist}/doc/latex/dnaseq
%{texmfdist}/source/latex/dnaseq
%{texmfdist}/tex/latex/biocon
%{texmfdist}/tex/latex/dnaseq

%files -n texlive-latex-pdftools
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/attachfile
%doc %{texmfdist}/doc/latex/cooltooltips
%doc %{texmfdist}/doc/latex/flashmovie
%doc %{texmfdist}/doc/latex/movie15
%doc %{texmfdist}/doc/latex/pax
%doc %{texmfdist}/doc/latex/pdf14
%doc %{texmfdist}/doc/latex/pdfcomment
%doc %{texmfdist}/doc/latex/pdfcprot
%doc %{texmfdist}/doc/latex/pdfmarginpar
%doc %{texmfdist}/doc/latex/pdfscreen
%doc %{texmfdist}/doc/latex/pdfsync
%doc %{texmfdist}/doc/latex/pdftricks
%doc %{texmfdist}/doc/latex/tdclock
%doc %{texmfdist}/doc/support/fragmaster
%{texmfdist}/source/latex/attachfile
%{texmfdist}/source/latex/cooltooltips
%{texmfdist}/source/latex/pdf14
%{texmfdist}/source/latex/pdfcprot
%{texmfdist}/tex/latex/attachfile
%{texmfdist}/tex/latex/cooltooltips
%{texmfdist}/tex/latex/flashmovie
%{texmfdist}/tex/latex/movie15
%{texmfdist}/tex/latex/pdf14
%{texmfdist}/tex/latex/pdfcomment
%{texmfdist}/tex/latex/pdfcprot
%{texmfdist}/tex/latex/pdfmarginpar
%{texmfdist}/tex/latex/pdfscreen
%{texmfdist}/tex/latex/pdfsync
%{texmfdist}/tex/latex/pdftricks
%{texmfdist}/tex/latex/tdclock

%files -n texlive-latex-informatic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/dirtree
%doc %{texmfdist}/doc/generic/vaucanson-g
%doc %{texmfdist}/doc/latex/alg
%doc %{texmfdist}/doc/latex/bytefield
%doc %{texmfdist}/doc/latex/colordoc
%doc %{texmfdist}/doc/latex/drs
%doc %{texmfdist}/doc/latex/lsc
%doc %{texmfdist}/doc/latex/method
%doc %{texmfdist}/doc/latex/minted
%doc %{texmfdist}/doc/latex/msc
%doc %{texmfdist}/doc/latex/multiobjective
%doc %{texmfdist}/doc/latex/register
%doc %{texmfdist}/doc/latex/uml
%{texmfdist}/source/generic/dirtree
%{texmfdist}/source/latex/alg
%{texmfdist}/source/latex/bytefield
%{texmfdist}/source/latex/colordoc
%{texmfdist}/source/latex/method
%{texmfdist}/source/latex/minted
%{texmfdist}/source/latex/multiobjective
%{texmfdist}/source/latex/register
%{texmfdist}/source/latex/uml
%{texmfdist}/tex/generic/dirtree
%{texmfdist}/tex/generic/vaucanson-g
%{texmfdist}/tex/latex/alg
%{texmfdist}/tex/latex/bytefield
%{texmfdist}/tex/latex/colordoc
%{texmfdist}/tex/latex/drs
%{texmfdist}/tex/latex/lsc
%{texmfdist}/tex/latex/method
%{texmfdist}/tex/latex/minted
%{texmfdist}/tex/latex/msc
%{texmfdist}/tex/latex/multiobjective
%{texmfdist}/tex/latex/register
%{texmfdist}/tex/latex/uml

%files -n texlive-latex-games
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/chess-problem-diagrams
%doc %{texmfdist}/doc/latex/chessboard
%doc %{texmfdist}/doc/latex/chessfss
%doc %{texmfdist}/doc/latex/crossword
%doc %{texmfdist}/doc/latex/crosswrd
%doc %{texmfdist}/doc/latex/othello
%doc %{texmfdist}/doc/latex/sgame
%doc %{texmfdist}/doc/latex/skak
%doc %{texmfdist}/doc/latex/sudoku
%doc %{texmfdist}/doc/latex/sudokubundle
%{texmfdist}/fonts/enc/dvips/chessfss
%{texmfdist}/fonts/source/public/chess
%{texmfdist}/fonts/source/public/go
%{texmfdist}/fonts/source/public/othello
%{texmfdist}/fonts/source/public/skak
%{texmfdist}/fonts/tfm/public/go
%{texmfdist}/fonts/tfm/public/othello
%{texmfdist}/fonts/tfm/public/skak
%{texmfdist}/source/latex/chess-problem-diagrams
%{texmfdist}/source/latex/chessboard
%{texmfdist}/source/latex/chessfss
%{texmfdist}/source/latex/crossword
%{texmfdist}/source/latex/crosswrd
%{texmfdist}/source/latex/sudoku
%{texmfdist}/source/latex/sudokubundle
%{texmfdist}/tex/latex/chess
%{texmfdist}/tex/latex/chess-problem-diagrams
%{texmfdist}/tex/latex/chessboard
%{texmfdist}/tex/latex/chessfss
%{texmfdist}/tex/latex/crossword
%{texmfdist}/tex/latex/crosswrd
%{texmfdist}/tex/latex/go
%{texmfdist}/tex/latex/othello
%{texmfdist}/tex/latex/sgame
%{texmfdist}/tex/latex/skak
%{texmfdist}/tex/latex/sudoku
%{texmfdist}/tex/latex/sudokubundle

%files -n texlive-latex-sources
%defattr(644,root,root,755)
%{texmfdist}/source/generic/fltpoint
%{texmfdist}/source/latex/acronym
%{texmfdist}/source/latex/altfont
%{texmfdist}/source/latex/barcodes
%{texmfdist}/source/latex/bbding
%{texmfdist}/source/latex/bbm-macros
%{texmfdist}/source/latex/bengali
%{texmfdist}/source/latex/beton
%{texmfdist}/source/latex/bibarts
%{texmfdist}/source/latex/bibleref
%{texmfdist}/source/latex/bigfoot
%{texmfdist}/source/latex/bizcard
%{texmfdist}/source/latex/blindtext
%{texmfdist}/source/latex/boxhandler
%{texmfdist}/source/latex/breakurl
%{texmfdist}/source/latex/captcont
%{texmfdist}/source/latex/catechis
%{texmfdist}/source/latex/cclicenses
%{texmfdist}/source/latex/cd
%{texmfdist}/source/latex/cd-cover
%{texmfdist}/source/latex/cdpbundl
%{texmfdist}/source/latex/changes
%{texmfdist}/source/latex/chapterfolder
%{texmfdist}/source/latex/cjk
%{texmfdist}/source/latex/cleveref
%{texmfdist}/source/latex/codepage
%{texmfdist}/source/latex/confproc
%{texmfdist}/source/latex/coverpage
%{texmfdist}/source/latex/crop
%{texmfdist}/source/latex/crossreference
%{texmfdist}/source/latex/ctib
%{texmfdist}/source/latex/dateiliste
%{texmfdist}/source/latex/datetime
%{texmfdist}/source/latex/decimal
%{texmfdist}/source/latex/docmfp
%{texmfdist}/source/latex/doipubmed
%{texmfdist}/source/latex/dotarrow
%{texmfdist}/source/latex/dottex
%{texmfdist}/source/latex/drac
%{texmfdist}/source/latex/draftcopy
%{texmfdist}/source/latex/dramatist
%{texmfdist}/source/latex/ebezier
%{texmfdist}/source/latex/ebsthesis
%{texmfdist}/source/latex/ecclesiastic
%{texmfdist}/source/latex/edmargin
%{texmfdist}/source/latex/eemeir
%{texmfdist}/source/latex/ellipsis
%{texmfdist}/source/latex/emp
%{texmfdist}/source/latex/endfloat
%{texmfdist}/source/latex/endheads
%{texmfdist}/source/latex/engpron
%{texmfdist}/source/latex/engrec
%{texmfdist}/source/latex/envlab
%{texmfdist}/source/latex/epigraph
%{texmfdist}/source/latex/epiolmec
%{texmfdist}/source/latex/epsdice
%{texmfdist}/source/latex/eqparbox
%{texmfdist}/source/latex/errata
%{texmfdist}/source/latex/eso-pic
%{texmfdist}/source/latex/ethiop
%{texmfdist}/source/latex/eukdate
%{texmfdist}/source/latex/euro
%{texmfdist}/source/latex/everypage
%{texmfdist}/source/latex/extract
%{texmfdist}/source/latex/facsimile
%{texmfdist}/source/latex/fancynum
%{texmfdist}/source/latex/fancyref
%{texmfdist}/source/latex/fancytooltips
%{texmfdist}/source/latex/fancyvrb
%{texmfdist}/source/latex/filecontents
%{texmfdist}/source/latex/fink
%{texmfdist}/source/latex/flabels
%{texmfdist}/source/latex/flagderiv
%{texmfdist}/source/latex/flashcards
%{texmfdist}/source/latex/float
%{texmfdist}/source/latex/floatrow
%{texmfdist}/source/latex/fmp
%{texmfdist}/source/latex/fnbreak
%{texmfdist}/source/latex/foilhtml
%{texmfdist}/source/latex/fonttable
%{texmfdist}/source/latex/footmisc
%{texmfdist}/source/latex/footnpag
%{texmfdist}/source/latex/frankenstein
%{texmfdist}/source/latex/frontespizio
%{texmfdist}/source/latex/fullblck
%{texmfdist}/source/latex/gcite
%{texmfdist}/source/latex/genmpage
%{texmfdist}/source/latex/geometry
%{texmfdist}/source/latex/glossaries
%{texmfdist}/source/latex/graphics
%{texmfdist}/source/latex/graphicx-psmin
%{texmfdist}/source/latex/greekdates
%{texmfdist}/source/latex/hanging
%{texmfdist}/source/latex/harvard
%{texmfdist}/source/latex/hc
%{texmfdist}/source/latex/histogr
%{texmfdist}/source/latex/hpsdiss
%{texmfdist}/source/latex/hyper
%{texmfdist}/source/latex/hyperref
%{texmfdist}/source/latex/hyperxmp
%{texmfdist}/source/latex/hyphenat
%{texmfdist}/source/latex/ibycus-babel
%{texmfdist}/source/latex/icsv
%{texmfdist}/source/latex/ifplatform
%{texmfdist}/source/latex/ijmart
%{texmfdist}/source/latex/imtekda
%{texmfdist}/source/latex/index
%{texmfdist}/source/latex/inlinedef
%{texmfdist}/source/latex/iso
%{texmfdist}/source/latex/iso10303
%{texmfdist}/source/latex/isodate
%{texmfdist}/source/latex/isodoc
%{texmfdist}/source/latex/itnumpar
%{texmfdist}/source/latex/jura
%{texmfdist}/source/latex/juraabbrev
%{texmfdist}/source/latex/jurarsp
%{texmfdist}/source/latex/koma-script
%{texmfdist}/source/latex/labels
%{texmfdist}/source/latex/layouts
%{texmfdist}/source/latex/listings
%{texmfdist}/source/latex/mathpazo
%{texmfdist}/source/latex/mdwtools
%{texmfdist}/source/latex/memoir
%{texmfdist}/source/latex/mh
%{texmfdist}/source/latex/mnsymbol
%{texmfdist}/source/latex/modroman
%{texmfdist}/source/latex/mongolian-babel
%{texmfdist}/source/latex/mparhack
%{texmfdist}/source/latex/ms
%{texmfdist}/source/latex/multibib
%{texmfdist}/source/latex/mwcls
%{texmfdist}/source/latex/natbib
%{texmfdist}/source/latex/ncctools
%{texmfdist}/source/latex/nddiss
%{texmfdist}/source/latex/newfile
%{texmfdist}/source/latex/newlfm
%{texmfdist}/source/latex/newspaper
%{texmfdist}/source/latex/nomencl
%{texmfdist}/source/latex/ntgclass
%{texmfdist}/source/latex/oberdiek
%{texmfdist}/source/latex/paralist
%{texmfdist}/source/latex/pdfpages
%{texmfdist}/source/latex/pict2e
%{texmfdist}/source/latex/preprint
%{texmfdist}/source/latex/preview
%{texmfdist}/source/latex/psfrag
%{texmfdist}/source/latex/pslatex
%{texmfdist}/source/latex/revtex
%{texmfdist}/source/latex/rotating
%{texmfdist}/source/latex/rotfloat
%{texmfdist}/source/latex/scale
%{texmfdist}/source/latex/sectsty
%{texmfdist}/source/latex/showlabels
%{texmfdist}/source/latex/sidecap
%{texmfdist}/source/latex/soul
%{texmfdist}/source/latex/stdclsdv
%{texmfdist}/source/latex/subfig
%{texmfdist}/source/latex/subfigure
%{texmfdist}/source/latex/supertabular
%{texmfdist}/source/latex/tablists
%{texmfdist}/source/latex/tabulary
%{texmfdist}/source/latex/tabvar
%{texmfdist}/source/latex/talk
%{texmfdist}/source/latex/tcldoc
%{texmfdist}/source/latex/tdsfrmath
%{texmfdist}/source/latex/ted
%{texmfdist}/source/latex/tengwarscript
%{texmfdist}/source/latex/tensor
%{texmfdist}/source/latex/teubner
%{texmfdist}/source/latex/texmate
%{texmfdist}/source/latex/texpower
%{texmfdist}/source/latex/texshade
%{texmfdist}/source/latex/textcase
%{texmfdist}/source/latex/textfit
%{texmfdist}/source/latex/textopo
%{texmfdist}/source/latex/textpos
%{texmfdist}/source/latex/thesis-titlepage-fhac
%{texmfdist}/source/latex/thmtools
%{texmfdist}/source/latex/thumb
%{texmfdist}/source/latex/thuthesis
%{texmfdist}/source/latex/titling
%{texmfdist}/source/latex/tocbibind
%{texmfdist}/source/latex/tocloft
%{texmfdist}/source/latex/tools
%{texmfdist}/source/latex/totpages
%{texmfdist}/source/latex/type1cm
%{texmfdist}/source/latex/units
%{texmfdist}/source/latex/unitsdef
%{texmfdist}/source/latex/varindex
%{texmfdist}/source/latex/verse
%{texmfdist}/source/latex/vmargin
%{texmfdist}/source/latex/volumes
%{texmfdist}/source/latex/vwcol
%{texmfdist}/source/latex/warpcol
%{texmfdist}/source/latex/was
%{texmfdist}/source/latex/xargs
%{texmfdist}/source/latex/xdoc
%{texmfdist}/source/latex/xfor
%{texmfdist}/source/latex/xmpincl
%{texmfdist}/source/latex/xskak
%{texmfdist}/source/latex/xtab
%{texmfdist}/source/latex/yafoot
%{texmfdist}/source/latex/yfonts
%{texmfdist}/source/latex/yhmath
%{texmfdist}/source/latex/york-thesis
%{texmfdist}/source/latex/youngtab

%files -n texlive-latex-styles
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/IEEEconf
%doc %{texmfdist}/doc/latex/aastex
%doc %{texmfdist}/doc/latex/acmconf
%doc %{texmfdist}/doc/latex/active-conf
%doc %{texmfdist}/doc/latex/aiaa
%doc %{texmfdist}/doc/latex/apa
%doc %{texmfdist}/doc/latex/arsclassica
%doc %{texmfdist}/doc/latex/asaetr
%doc %{texmfdist}/doc/latex/ascelike
%doc %{texmfdist}/doc/latex/biblatex-apa
%doc %{texmfdist}/doc/latex/biblatex-nature
%doc %{texmfdist}/doc/latex/computational-complexity
%doc %{texmfdist}/doc/latex/dtk
%doc %{texmfdist}/doc/latex/elbioimp
%doc %{texmfdist}/doc/latex/elsarticle
%doc %{texmfdist}/doc/latex/erdc
%doc %{texmfdist}/doc/latex/estcpmm
%doc %{texmfdist}/doc/latex/gatech-thesis
%doc %{texmfdist}/doc/latex/historische-zeitschrift
%doc %{texmfdist}/doc/latex/jmlr
%doc %{texmfdist}/doc/latex/lettre
%doc %{texmfdist}/doc/latex/lexikon
%doc %{texmfdist}/doc/latex/lps
%doc %{texmfdist}/doc/latex/magaz
%doc %{texmfdist}/doc/latex/manuscript
%doc %{texmfdist}/doc/latex/mentis
%doc %{texmfdist}/doc/latex/mslapa
%doc %{texmfdist}/doc/latex/nature
%doc %{texmfdist}/doc/latex/nih
%doc %{texmfdist}/doc/latex/nostarch
%doc %{texmfdist}/doc/latex/nrc
%doc %{texmfdist}/doc/latex/octavo
%doc %{texmfdist}/doc/latex/onrannual
%doc %{texmfdist}/doc/latex/paper
%doc %{texmfdist}/doc/latex/papertex
%doc %{texmfdist}/doc/latex/pbsheet
%doc %{texmfdist}/doc/latex/petiteannonce
%doc %{texmfdist}/doc/latex/philosophersimprint
%doc %{texmfdist}/doc/latex/pittetd
%doc %{texmfdist}/doc/latex/plari
%doc %{texmfdist}/doc/latex/play
%doc %{texmfdist}/doc/latex/poemscol
%doc %{texmfdist}/doc/latex/pracjourn
%doc %{texmfdist}/doc/latex/psu-thesis
%doc %{texmfdist}/doc/latex/ptptex
%doc %{texmfdist}/doc/latex/refman
%doc %{texmfdist}/doc/latex/revtex4
%doc %{texmfdist}/doc/latex/ryethesis
%doc %{texmfdist}/doc/latex/rsc
%doc %{texmfdist}/doc/latex/sageep
%doc %{texmfdist}/doc/latex/seuthesis
%doc %{texmfdist}/doc/latex/screenplay
%doc %{texmfdist}/doc/latex/shipunov
%doc %{texmfdist}/doc/latex/sides
%doc %{texmfdist}/doc/latex/soton
%doc %{texmfdist}/doc/latex/stage
%doc %{texmfdist}/doc/latex/tufte-latex
%doc %{texmfdist}/doc/latex/tugboat
%doc %{texmfdist}/doc/latex/uaclasses
%doc %{texmfdist}/doc/latex/ucthesis
%doc %{texmfdist}/doc/latex/ucdavisthesis
%doc %{texmfdist}/doc/latex/uiucthesis
%doc %{texmfdist}/doc/latex/umich-thesis
%doc %{texmfdist}/doc/latex/umthesis
%doc %{texmfdist}/doc/latex/ut-thesis
%doc %{texmfdist}/doc/latex/uwthesis
%{texmfdist}/bibtex/bib/computational-complexity
%{texmfdist}/bibtex/bst/aiaa
%{texmfdist}/bibtex/bst/apacite
%{texmfdist}/bibtex/bst/ascelike
%{texmfdist}/bibtex/bst/asaetr
%{texmfdist}/bibtex/bst/computational-complexity
%{texmfdist}/bibtex/bst/dtk
%{texmfdist}/bibtex/bst/gatech-thesis
%{texmfdist}/bibtex/bst/mslapa
%{texmfdist}/bibtex/bst/psu-thesis
%{texmfdist}/bibtex/bst/rsc
%{texmfdist}/bibtex/bst/sageep
%{texmfdist}/bibtex/bst/seuthesis
%{texmfdist}/makeindex/arsclassica
%{texmfdist}/source/latex/IEEEconf
%{texmfdist}/source/latex/aastex
%{texmfdist}/source/latex/acmconf
%{texmfdist}/source/latex/active-conf
%{texmfdist}/source/latex/aiaa
%{texmfdist}/source/latex/computational-complexity
%{texmfdist}/source/latex/erdc
%{texmfdist}/source/latex/elsarticle
%{texmfdist}/source/latex/estcpmm
%{texmfdist}/source/latex/jmlr
%{texmfdist}/source/latex/lps
%{texmfdist}/source/latex/manuscript
%{texmfdist}/source/latex/mentis
%{texmfdist}/source/latex/nostarch
%{texmfdist}/source/latex/nrc
%{texmfdist}/source/latex/octavo
%{texmfdist}/source/latex/paper
%{texmfdist}/source/latex/papertex
%{texmfdist}/source/latex/pbsheet
%{texmfdist}/source/latex/philosophersimprint
%{texmfdist}/source/latex/pittetd
%{texmfdist}/source/latex/plari
%{texmfdist}/source/latex/play
%{texmfdist}/source/latex/poemscol
%{texmfdist}/source/latex/pracjourn
%{texmfdist}/source/latex/refman
%{texmfdist}/source/latex/revtex4
%{texmfdist}/source/latex/ryethesis
%{texmfdist}/source/latex/rsc
%{texmfdist}/source/latex/sageep
%{texmfdist}/source/latex/screenplay
%{texmfdist}/source/latex/seuthesis
%{texmfdist}/source/latex/tugboat
%{texmfdist}/source/latex/uaclasses
%{texmfdist}/source/latex/ucdavisthesis
%{texmfdist}/source/latex/uiucthesis
%{texmfdist}/tex/latex/IEEEconf
%{texmfdist}/tex/latex/aastex
%{texmfdist}/tex/latex/acmconf
%{texmfdist}/tex/latex/active-conf
%{texmfdist}/tex/latex/aiaa
%{texmfdist}/tex/latex/apa
%{texmfdist}/tex/latex/apacite
%{texmfdist}/tex/latex/arsclassica
%{texmfdist}/tex/latex/asaetr
%{texmfdist}/tex/latex/ascelike
%{texmfdist}/tex/latex/biblatex-apa
%{texmfdist}/tex/latex/biblatex-nature
%{texmfdist}/tex/latex/computational-complexity
%{texmfdist}/tex/latex/dtk
%{texmfdist}/tex/latex/elbioimp
%{texmfdist}/tex/latex/elsarticle
%{texmfdist}/tex/latex/erdc
%{texmfdist}/tex/latex/estcpmm
%{texmfdist}/tex/latex/gatech-thesis
%{texmfdist}/tex/latex/historische-zeitschrift
%{texmfdist}/tex/latex/jmlr
%{texmfdist}/tex/latex/lettre
%{texmfdist}/tex/latex/lexikon
%{texmfdist}/tex/latex/lps
%{texmfdist}/tex/latex/magaz
%{texmfdist}/tex/latex/manuscript
%{texmfdist}/tex/latex/mentis
%{texmfdist}/tex/latex/mslapa
%{texmfdist}/tex/latex/muthesis
%{texmfdist}/tex/latex/nature
%{texmfdist}/tex/latex/nih
%{texmfdist}/tex/latex/nostarch
%{texmfdist}/tex/latex/nrc
%{texmfdist}/tex/latex/octavo
%{texmfdist}/tex/latex/onrannual
%{texmfdist}/tex/latex/paper
%{texmfdist}/tex/latex/papertex
%{texmfdist}/tex/latex/pbsheet
%{texmfdist}/tex/latex/petiteannonce
%{texmfdist}/tex/latex/philosophersimprint
%{texmfdist}/tex/latex/pittetd
%{texmfdist}/tex/latex/plari
%{texmfdist}/tex/latex/play
%{texmfdist}/tex/latex/poemscol
%{texmfdist}/tex/latex/pracjourn
%{texmfdist}/tex/latex/psu-thesis
%{texmfdist}/tex/latex/ptptex
%{texmfdist}/tex/latex/refman
%{texmfdist}/tex/latex/revtex4
%{texmfdist}/tex/latex/rsc
%{texmfdist}/tex/latex/ryethesis
%{texmfdist}/tex/latex/sageep
%{texmfdist}/tex/latex/screenplay
%{texmfdist}/tex/latex/seuthesis
%{texmfdist}/tex/latex/shipunov
%{texmfdist}/tex/latex/sides
%{texmfdist}/tex/latex/soton
%{texmfdist}/tex/latex/stage
%{texmfdist}/tex/latex/tufte-latex
%{texmfdist}/tex/latex/tugboat
%{texmfdist}/tex/latex/uaclasses
%{texmfdist}/tex/latex/ucdavisthesis
%{texmfdist}/tex/latex/ucthesis
%{texmfdist}/tex/latex/uiucthesis
%{texmfdist}/tex/latex/umich-thesis
%{texmfdist}/tex/latex/umthesis
%{texmfdist}/tex/latex/ut-thesis
%{texmfdist}/tex/latex/uwthesis

%files -n texlive-latex-lang
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ESIEEcv
%doc %{texmfdist}/doc/latex/chletter
%doc %{texmfdist}/doc/latex/dinbrief
%doc %{texmfdist}/doc/latex/disser
%doc %{texmfdist}/doc/latex/elmath
%doc %{texmfdist}/doc/latex/eskd
%doc %{texmfdist}/doc/latex/ginpenc
%doc %{texmfdist}/doc/latex/hrlatex
%doc %{texmfdist}/doc/latex/lithuanian
%doc %{texmfdist}/doc/latex/mla-paper
%{texmfdist}/source/latex/ESIEEcv
%{texmfdist}/source/latex/chletter
%{texmfdist}/source/latex/dinbrief
%{texmfdist}/source/latex/disser
%{texmfdist}/source/latex/elmath
%{texmfdist}/source/latex/eskd
%{texmfdist}/source/latex/ginpenc
%{texmfdist}/source/latex/hrlatex
%{texmfdist}/tex/latex/ESIEEcv
%{texmfdist}/tex/latex/chletter
%{texmfdist}/tex/latex/dinbrief
%{texmfdist}/tex/latex/disser
%{texmfdist}/tex/latex/elmath
%{texmfdist}/tex/latex/eskd
%{texmfdist}/tex/latex/ginpenc
%{texmfdist}/tex/latex/hrlatex
%{texmfdist}/tex/latex/lithuanian
%{texmfdist}/tex/latex/mla-paper
%{texmfdist}/fonts/enc/dvips/lithuanian
%{texmfdist}/fonts/map/dvips/lithuanian

%files -n texlive-latex-music
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/abc
%doc %{texmfdist}/doc/latex/gchords
%doc %{texmfdist}/doc/latex/guitar
%doc %{texmfdist}/doc/latex/songbook
%{texmfdist}/source/latex/abc
%{texmfdist}/source/latex/guitar
%{texmfdist}/source/latex/songbook
%{texmfdist}/tex/latex/abc
%{texmfdist}/tex/latex/gchords
%{texmfdist}/tex/latex/guitar
%{texmfdist}/tex/latex/songbook

%files -n texlive-latex-extend
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/librarian
%doc %{texmfdist}/doc/latex/HA-prosper
%doc %{texmfdist}/doc/latex/a4wide
%doc %{texmfdist}/doc/latex/a5comb
%doc %{texmfdist}/doc/latex/addlines
%doc %{texmfdist}/doc/latex/alnumsec
%doc %{texmfdist}/doc/latex/anonchap
%doc %{texmfdist}/doc/latex/arydshln
%doc %{texmfdist}/doc/latex/authoraftertitle
%doc %{texmfdist}/doc/latex/bibtopicprefix
%doc %{texmfdist}/doc/latex/blkarray
%doc %{texmfdist}/doc/latex/block
%doc %{texmfdist}/doc/latex/boites
%doc %{texmfdist}/doc/latex/booklet
%doc %{texmfdist}/doc/latex/bullcntr
%doc %{texmfdist}/doc/latex/ccicons
%doc %{texmfdist}/doc/latex/chappg
%doc %{texmfdist}/doc/latex/clefval
%doc %{texmfdist}/doc/latex/collref
%doc %{texmfdist}/doc/latex/colortbl
%doc %{texmfdist}/doc/latex/combine
%doc %{texmfdist}/doc/latex/combinedgraphics
%doc %{texmfdist}/doc/latex/contour
%doc %{texmfdist}/doc/latex/ctable
%doc %{texmfdist}/doc/latex/curve2e
%doc %{texmfdist}/doc/latex/dashrule
%doc %{texmfdist}/doc/latex/docmute
%doc %{texmfdist}/doc/latex/dox
%doc %{texmfdist}/doc/latex/easylist
%doc %{texmfdist}/doc/latex/emptypage
%doc %{texmfdist}/doc/latex/esk
%doc %{texmfdist}/doc/latex/etaremune
%doc %{texmfdist}/doc/latex/expdlist
%doc %{texmfdist}/doc/latex/fix2col
%doc %{texmfdist}/doc/latex/fncylab
%doc %{texmfdist}/doc/latex/ftcap
%doc %{texmfdist}/doc/latex/ftnxtra
%doc %{texmfdist}/doc/latex/import
%doc %{texmfdist}/doc/latex/layaureo
%doc %{texmfdist}/doc/latex/leading
%doc %{texmfdist}/doc/latex/listbib
%doc %{texmfdist}/doc/latex/listliketab
%doc %{texmfdist}/doc/latex/makebox
%doc %{texmfdist}/doc/latex/makecell
%doc %{texmfdist}/doc/latex/marginnote
%doc %{texmfdist}/doc/latex/mcaption
%doc %{texmfdist}/doc/latex/mcite
%doc %{texmfdist}/doc/latex/mciteplus
%doc %{texmfdist}/doc/latex/minipage-marginpar
%doc %{texmfdist}/doc/latex/miniplot
%doc %{texmfdist}/doc/latex/modref
%doc %{texmfdist}/doc/latex/multicap
%doc %{texmfdist}/doc/latex/newvbtm
%doc %{texmfdist}/doc/latex/nopageno
%doc %{texmfdist}/doc/latex/notes2bib
%doc %{texmfdist}/doc/latex/notoccite
%doc %{texmfdist}/doc/latex/pagecont
%doc %{texmfdist}/doc/latex/pagerange
%doc %{texmfdist}/doc/latex/pbox
%doc %{texmfdist}/doc/latex/pinlabel
%doc %{texmfdist}/doc/latex/polytable
%doc %{texmfdist}/doc/latex/rccol
%doc %{texmfdist}/doc/latex/romannum
%doc %{texmfdist}/doc/latex/spreadtab
%doc %{texmfdist}/doc/latex/subfloat
%doc %{texmfdist}/doc/latex/thmbox
%doc %{texmfdist}/doc/latex/titlepic
%doc %{texmfdist}/doc/latex/umoline
%doc %{texmfdist}/doc/latex/underlin
%doc %{texmfdist}/doc/latex/underscore
%doc %{texmfdist}/doc/latex/undolabl
%doc %{texmfdist}/doc/latex/widetable
%doc %{texmfdist}/doc/latex/zwpagelayout
%{texmfdist}/bibtex/bst/babelbib
%{texmfdist}/bibtex/bst/mciteplus
%{texmfdist}/source/latex/HA-prosper
%{texmfdist}/source/latex/addlines
%{texmfdist}/source/latex/alnumsec
%{texmfdist}/source/latex/arydshln
%{texmfdist}/source/latex/bibtopicprefix
%{texmfdist}/source/latex/boites
%{texmfdist}/source/latex/booklet
%{texmfdist}/source/latex/bullcntr
%{texmfdist}/source/latex/ccicons
%{texmfdist}/source/latex/chappg
%{texmfdist}/source/latex/clefval
%{texmfdist}/source/latex/collref
%{texmfdist}/source/latex/colortbl
%{texmfdist}/source/latex/combine
%{texmfdist}/source/latex/combinedgraphics
%{texmfdist}/source/latex/contour
%{texmfdist}/source/latex/ctable
%{texmfdist}/source/latex/curve2e
%{texmfdist}/source/latex/dashbox
%{texmfdist}/source/latex/dashrule
%{texmfdist}/source/latex/docmute
%{texmfdist}/source/latex/dox
%{texmfdist}/source/latex/emptypage
%{texmfdist}/source/latex/esk
%{texmfdist}/source/latex/etaremune
%{texmfdist}/source/latex/expdlist
%{texmfdist}/source/latex/fix2col
%{texmfdist}/source/latex/ftnxtra
%{texmfdist}/source/latex/layaureo
%{texmfdist}/source/latex/leading
%{texmfdist}/source/latex/listbib
%{texmfdist}/source/latex/listliketab
%{texmfdist}/source/latex/makebox
%{texmfdist}/source/latex/makecell
%{texmfdist}/source/latex/marginnote
%{texmfdist}/source/latex/mcaption
%{texmfdist}/source/latex/mcite
%{texmfdist}/source/latex/minipage-marginpar
%{texmfdist}/source/latex/modref
%{texmfdist}/source/latex/multicap
%{texmfdist}/source/latex/newvbtm
%{texmfdist}/source/latex/notes2bib
%{texmfdist}/source/latex/pagecont
%{texmfdist}/source/latex/pbox
%{texmfdist}/source/latex/polytable
%{texmfdist}/source/latex/rccol
%{texmfdist}/source/latex/romannum
%{texmfdist}/source/latex/subfloat
%{texmfdist}/source/latex/thmbox
%{texmfdist}/source/latex/umoline
%{texmfdist}/source/latex/underlin
%{texmfdist}/source/latex/undolabl
%{texmfdist}/source/latex/widetable
%{texmfdist}/tex/generic/librarian
%{texmfdist}/tex/latex/HA-prosper
%{texmfdist}/tex/latex/a4wide
%{texmfdist}/tex/latex/a5comb
%{texmfdist}/tex/latex/addlines
%{texmfdist}/tex/latex/alnumsec
%{texmfdist}/tex/latex/anonchap
%{texmfdist}/tex/latex/arydshln
%{texmfdist}/tex/latex/authoraftertitle
%{texmfdist}/tex/latex/babelbib
%{texmfdist}/tex/latex/bibtopicprefix
%{texmfdist}/tex/latex/blkarray
%{texmfdist}/tex/latex/block
%{texmfdist}/tex/latex/boites
%{texmfdist}/tex/latex/booklet
%{texmfdist}/tex/latex/bullcntr
%{texmfdist}/tex/latex/ccicons
%{texmfdist}/tex/latex/chappg
%{texmfdist}/tex/latex/clefval
%{texmfdist}/tex/latex/collref
%{texmfdist}/tex/latex/colortbl
%{texmfdist}/tex/latex/combine
%{texmfdist}/tex/latex/combinedgraphics
%{texmfdist}/tex/latex/contour
%{texmfdist}/tex/latex/ctable
%{texmfdist}/tex/latex/curve2e
%{texmfdist}/tex/latex/dashbox
%{texmfdist}/tex/latex/dashrule
%{texmfdist}/tex/latex/docmute
%{texmfdist}/tex/latex/dox
%{texmfdist}/tex/latex/easylist
%{texmfdist}/tex/latex/emptypage
%{texmfdist}/tex/latex/esk
%{texmfdist}/tex/latex/etaremune
%{texmfdist}/tex/latex/expdlist
%{texmfdist}/tex/latex/fix2col
%{texmfdist}/tex/latex/fncylab
%{texmfdist}/tex/latex/ftcap
%{texmfdist}/tex/latex/ftnxtra
%{texmfdist}/tex/latex/import
%{texmfdist}/tex/latex/layaureo
%{texmfdist}/tex/latex/leading
%{texmfdist}/tex/latex/listbib
%{texmfdist}/tex/latex/listliketab
%{texmfdist}/tex/latex/makebox
%{texmfdist}/tex/latex/makecell
%{texmfdist}/tex/latex/marginnote
%{texmfdist}/tex/latex/mcaption
%{texmfdist}/tex/latex/mcite
%{texmfdist}/tex/latex/mciteplus
%{texmfdist}/tex/latex/minipage-marginpar
%{texmfdist}/tex/latex/miniplot
%{texmfdist}/tex/latex/modref
%{texmfdist}/tex/latex/multicap
%{texmfdist}/tex/latex/newvbtm
%{texmfdist}/tex/latex/nextpage
%{texmfdist}/tex/latex/nopageno
%{texmfdist}/tex/latex/notes2bib
%{texmfdist}/tex/latex/notoccite
%{texmfdist}/tex/latex/pagecont
%{texmfdist}/tex/latex/pagerange
%{texmfdist}/tex/latex/pbox
%{texmfdist}/tex/latex/pinlabel
%{texmfdist}/tex/latex/polytable
%{texmfdist}/tex/latex/rccol
%{texmfdist}/tex/latex/romannum
%{texmfdist}/tex/latex/spreadtab
%{texmfdist}/tex/latex/subfloat
%{texmfdist}/tex/latex/thmbox
%{texmfdist}/tex/latex/titlepic
%{texmfdist}/tex/latex/umoline
%{texmfdist}/tex/latex/underlin
%{texmfdist}/tex/latex/underscore
%{texmfdist}/tex/latex/undolabl
%{texmfdist}/tex/latex/widetable
%{texmfdist}/tex/latex/zwpagelayout

%files -n texlive-latex-presentation
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/poster-mac
%doc %{texmfdist}/doc/latex/powerdot
%doc %{texmfdist}/doc/latex/powerdot-FUBerlin
%doc %{texmfdist}/doc/latex/sciposter
%doc %{texmfdist}/doc/latex/tpslifonts
%doc %{texmfdist}/doc/latex/presentations
%{texmfdist}/tex/generic/poster-mac
%{texmfdist}/tex/latex/powerdot
%{texmfdist}/tex/latex/powerdot-FUBerlin
%{texmfdist}/tex/latex/sciposter
%{texmfdist}/tex/latex/tpslifonts

%files -n texlive-latex-programming
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/yax
%doc %{texmfdist}/doc/latex/boolexpr
%doc %{texmfdist}/doc/latex/bophook
%doc %{texmfdist}/doc/latex/chngcntr
%doc %{texmfdist}/doc/latex/cmdtrack
%doc %{texmfdist}/doc/latex/codedoc
%doc %{texmfdist}/doc/latex/cool
%doc %{texmfdist}/doc/latex/coollist
%doc %{texmfdist}/doc/latex/coolstr
%doc %{texmfdist}/doc/latex/csvtools
%doc %{texmfdist}/doc/latex/currfile
%doc %{texmfdist}/doc/latex/datatool
%doc %{texmfdist}/doc/latex/datenumber
%doc %{texmfdist}/doc/latex/delimtxt
%doc %{texmfdist}/doc/latex/dialogl
%doc %{texmfdist}/doc/latex/dprogress
%doc %{texmfdist}/doc/latex/environ
%doc %{texmfdist}/doc/latex/excludeonly
%doc %{texmfdist}/doc/latex/export
%doc %{texmfdist}/doc/latex/exp-testopt
%doc %{texmfdist}/doc/latex/filehook
%doc %{texmfdist}/doc/latex/fmtcount
%doc %{texmfdist}/doc/latex/forarray
%doc %{texmfdist}/doc/latex/forloop
%doc %{texmfdist}/doc/latex/getfiledate
%doc %{texmfdist}/doc/latex/ifmtarg
%doc %{texmfdist}/doc/latex/inversepath
%doc %{texmfdist}/doc/latex/keycommand
%doc %{texmfdist}/doc/latex/labelcas
%doc %{texmfdist}/doc/latex/listings-ext
%doc %{texmfdist}/doc/latex/locality
%doc %{texmfdist}/doc/latex/localloc
%doc %{texmfdist}/doc/latex/makecmds
%doc %{texmfdist}/doc/latex/nag
%doc %{texmfdist}/doc/latex/namespc
%doc %{texmfdist}/doc/latex/newcommand
%doc %{texmfdist}/doc/latex/patchcmd
%doc %{texmfdist}/doc/latex/progress
%doc %{texmfdist}/doc/latex/randtext
%doc %{texmfdist}/doc/latex/regcount
%doc %{texmfdist}/doc/latex/robustcommand
%doc %{texmfdist}/doc/latex/skeycommand
%doc %{texmfdist}/doc/latex/skeyval
%doc %{texmfdist}/doc/latex/splitindex
%doc %{texmfdist}/doc/latex/stringstrings
%doc %{texmfdist}/doc/latex/substr
%doc %{texmfdist}/doc/latex/totcount
%doc %{texmfdist}/doc/latex/ydoc
%{texmfdist}/source/latex/bophook
%{texmfdist}/source/latex/boolexpr
%{texmfdist}/source/latex/cmdtrack
%{texmfdist}/source/latex/cool
%{texmfdist}/source/latex/coollist
%{texmfdist}/source/latex/coolstr
%{texmfdist}/source/latex/csvtools
%{texmfdist}/source/latex/currfile
%{texmfdist}/source/latex/datatool
%{texmfdist}/source/latex/datenumber
%{texmfdist}/source/latex/delimtxt
%{texmfdist}/source/latex/dialogl
%{texmfdist}/source/latex/dprogress
%{texmfdist}/source/latex/environ
%{texmfdist}/source/latex/exp-testopt
%{texmfdist}/source/latex/export
%{texmfdist}/source/latex/filehook
%{texmfdist}/source/latex/fmtcount
%{texmfdist}/source/latex/forarray
%{texmfdist}/source/latex/forloop
%{texmfdist}/source/latex/ifmtarg
%{texmfdist}/source/latex/inversepath
%{texmfdist}/source/latex/keycommand
%{texmfdist}/source/latex/labelcas
%{texmfdist}/source/latex/lcg
%{texmfdist}/source/latex/listings-ext
%{texmfdist}/source/latex/locality
%{texmfdist}/source/latex/localloc
%{texmfdist}/source/latex/makecmds
%{texmfdist}/source/latex/nag
%{texmfdist}/source/latex/namespc
%{texmfdist}/source/latex/patchcmd
%{texmfdist}/source/latex/regcount
%{texmfdist}/source/latex/robustcommand
%{texmfdist}/source/latex/splitindex
%{texmfdist}/source/latex/stack
%{texmfdist}/source/latex/stringstrings
%{texmfdist}/source/latex/totcount
#%{texmfdist}/source/latex/typedref
%{texmfdist}/source/latex/ydoc
%{texmfdist}/tex/generic/yax
%{texmfdist}/tex/latex/boolexpr
%{texmfdist}/tex/latex/bophook
%{texmfdist}/tex/latex/chngcntr
%{texmfdist}/tex/latex/cmdtrack
%{texmfdist}/tex/latex/codedoc
%{texmfdist}/tex/latex/cool
%{texmfdist}/tex/latex/coollist
%{texmfdist}/tex/latex/coolstr
%{texmfdist}/tex/latex/csvtools
%{texmfdist}/tex/latex/currfile
%{texmfdist}/tex/latex/datatool
%{texmfdist}/tex/latex/datenumber
%{texmfdist}/tex/latex/delimtxt
%{texmfdist}/tex/latex/dialogl
%{texmfdist}/tex/latex/dprogress
%{texmfdist}/tex/latex/environ
%{texmfdist}/tex/latex/excludeonly
%{texmfdist}/tex/latex/exp-testopt
%{texmfdist}/tex/latex/export
%{texmfdist}/tex/latex/filehook
%{texmfdist}/tex/latex/fmtcount
%{texmfdist}/tex/latex/forarray
%{texmfdist}/tex/latex/forloop
%{texmfdist}/tex/latex/getfiledate
%{texmfdist}/tex/latex/ifmtarg
%{texmfdist}/tex/latex/inversepath
%{texmfdist}/tex/latex/keycommand
%{texmfdist}/tex/latex/labelcas
%{texmfdist}/tex/latex/lcg
%{texmfdist}/tex/latex/listings-ext
%{texmfdist}/tex/latex/locality
%{texmfdist}/tex/latex/localloc
%{texmfdist}/tex/latex/makecmds
%{texmfdist}/tex/latex/multido
%{texmfdist}/tex/latex/nag
%{texmfdist}/tex/latex/namespc
%{texmfdist}/tex/latex/patchcmd
%{texmfdist}/tex/latex/progress
%{texmfdist}/tex/latex/randtext
%{texmfdist}/tex/latex/regcount
%{texmfdist}/tex/latex/robustcommand
%{texmfdist}/tex/latex/skeycommand
%{texmfdist}/tex/latex/skeyval
%{texmfdist}/tex/latex/splitindex
%{texmfdist}/tex/latex/stack
%{texmfdist}/tex/latex/stringstrings
%{texmfdist}/tex/latex/substr
%{texmfdist}/tex/latex/totcount
%{texmfdist}/tex/latex/ydoc

%files -n texlive-latex-effects
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/rlepsf
%doc %{texmfdist}/doc/generic/shade
%doc %{texmfdist}/doc/generic/ulem
%doc %{texmfdist}/doc/latex/arcs
%doc %{texmfdist}/doc/latex/background
%doc %{texmfdist}/doc/latex/bclogo
%doc %{texmfdist}/doc/latex/blowup
%doc %{texmfdist}/doc/latex/boxedminipage
%doc %{texmfdist}/doc/latex/capt-of
%doc %{texmfdist}/doc/latex/changebar
%doc %{texmfdist}/doc/latex/changelayout
%doc %{texmfdist}/doc/latex/censor
%doc %{texmfdist}/doc/latex/combelow
%doc %{texmfdist}/doc/latex/comma
%doc %{texmfdist}/doc/latex/dashundergaps
%doc %{texmfdist}/doc/latex/dblfloatfix
%doc %{texmfdist}/doc/latex/draftwatermark
%doc %{texmfdist}/doc/latex/endnotes
%doc %{texmfdist}/doc/latex/fancypar
%doc %{texmfdist}/doc/latex/flippdf
%doc %{texmfdist}/doc/latex/flowfram
%doc %{texmfdist}/doc/latex/framed
%doc %{texmfdist}/doc/latex/grid
%doc %{texmfdist}/doc/latex/isorot
%doc %{texmfdist}/doc/latex/lettrine
%doc %{texmfdist}/doc/latex/mdframed
%doc %{texmfdist}/doc/latex/midpage
%doc %{texmfdist}/doc/latex/minibox
%doc %{texmfdist}/doc/latex/niceframe
%doc %{texmfdist}/doc/latex/nolbreaks
%doc %{texmfdist}/doc/latex/notes
%doc %{texmfdist}/doc/latex/objectz
%doc %{texmfdist}/doc/latex/pageslts
%doc %{texmfdist}/doc/latex/parallel
%doc %{texmfdist}/doc/latex/quotchap
%doc %{texmfdist}/doc/latex/rotpages
%doc %{texmfdist}/doc/latex/roundbox
%doc %{texmfdist}/doc/latex/sectionbox
%doc %{texmfdist}/doc/latex/shadethm
%doc %{texmfdist}/doc/latex/ushort
%doc %{texmfdist}/doc/latex/xwatermark
%{texmfdist}/fonts/source/public/shade
%{texmfdist}/fonts/source/public/niceframe
%{texmfdist}/fonts/tfm/public/niceframe
%{texmfdist}/source/latex/arcs
%{texmfdist}/source/latex/background
%{texmfdist}/source/latex/blowup
%{texmfdist}/source/latex/changebar
%{texmfdist}/source/latex/draftwatermark
%{texmfdist}/source/latex/fancypar
%{texmfdist}/source/latex/flippdf
%{texmfdist}/source/latex/flowfram
%{texmfdist}/source/latex/isorot
%{texmfdist}/source/latex/grid
%{texmfdist}/source/latex/lettrine
%{texmfdist}/source/latex/minibox
%{texmfdist}/source/latex/niceframe
%{texmfdist}/source/latex/notes
%{texmfdist}/source/latex/objectz
%{texmfdist}/source/latex/parallel
%{texmfdist}/source/latex/pageslts
%{texmfdist}/source/latex/quotchap
%{texmfdist}/source/latex/ushort
%{texmfdist}/tex/generic/shade
%{texmfdist}/tex/generic/rlepsf
%{texmfdist}/tex/generic/ulem
%{texmfdist}/tex/latex/arcs
%{texmfdist}/tex/latex/background
%{texmfdist}/tex/latex/bclogo
%{texmfdist}/tex/latex/blowup
%{texmfdist}/tex/latex/boxedminipage
%{texmfdist}/tex/latex/capt-of
%{texmfdist}/tex/latex/censor
%{texmfdist}/tex/latex/changebar
%{texmfdist}/tex/latex/changelayout
%{texmfdist}/tex/latex/combelow
%{texmfdist}/tex/latex/comma
%{texmfdist}/tex/latex/dashundergaps
%{texmfdist}/tex/latex/dblfloatfix
%{texmfdist}/tex/latex/draftwatermark
%{texmfdist}/tex/latex/endnotes
%{texmfdist}/tex/latex/fancypar
%{texmfdist}/tex/latex/flippdf
%{texmfdist}/tex/latex/flowfram
%{texmfdist}/tex/latex/framed
%{texmfdist}/tex/latex/grid
%{texmfdist}/tex/latex/isorot
%{texmfdist}/tex/latex/lettrine
%{texmfdist}/tex/latex/mdframed
%{texmfdist}/tex/latex/midpage
%{texmfdist}/tex/latex/minibox
%{texmfdist}/tex/latex/niceframe
%{texmfdist}/tex/latex/nolbreaks
%{texmfdist}/tex/latex/notes
%{texmfdist}/tex/latex/objectz
%{texmfdist}/tex/latex/pageslts
%{texmfdist}/tex/latex/parallel
%{texmfdist}/tex/latex/quotchap
%{texmfdist}/tex/latex/roundbox
%{texmfdist}/tex/latex/rotpages
%{texmfdist}/tex/latex/sectionbox
%{texmfdist}/tex/latex/shadethm
%{texmfdist}/tex/latex/xwatermark
%{texmfdist}/tex/latex/ushort

# I don't sort them, because maybe can splitting and grouping them
%files -n texlive-latex-other
%defattr(644,root,root,755)
%dir %{texmfdist}/source/cslatex
%{texmfdist}/source/cslatex/base
# Definitive source of Plain TeX on CTAN.
%{texmfdist}/source/latex/base
# A small collection of minimal DTX examples.
%{texmfdist}/source/latex/dtxgallery
# Editorial Notes for LaTeX documents.
%{texmfdist}/source/latex/ed
# Typeset scholarly edition.
%{texmfdist}/source/latex/edmac
# Use AMS Euler fonts for math.
%{texmfdist}/source/latex/euler
%dir %{texmfdist}/source/plain
# Typeset Karnaugh-Veitch-maps.
%{texmfdist}/tex/latex/karnaugh
# Kerkis (Greek) font family.
%{texmfdist}/tex/latex/kerkis
# Print tables and generate control files to adjust kernings.
%{texmfdist}/source/latex/kerntest
%{texmfdist}/tex/latex/kerntest
%{texmfdist}/tex/latex/kluwer
%{texmfdist}/source/latex/kluwer
# A two-element sans-serif typeface.
%{texmfdist}/tex/latex/kurier
# Lists in TeX's "mouth".
%{texmfdist}/tex/latex/lazylist
# This package makes available Classic Cyrillic CM fonts
%{texmfdist}/source/latex/lcyw
%{texmfdist}/tex/latex/lcyw
# Typeset scholarly editions in parallel texts.
%{texmfdist}/source/latex/ledmac
%{texmfdist}/tex/latex/ledmac
# Macros for using Silvio Levy's Greek fonts.
%{texmfdist}/tex/latex/lgreek
# A non-standard Cyrillic input scheme.
%{texmfdist}/source/latex/lhcyr
%{texmfdist}/tex/latex/lhcyr
# Miscellaneous helper packages.
%{texmfdist}/source/latex/lhelp
%{texmfdist}/tex/latex/lhelp
# Use the font Libertine with LaTeX.
%{texmfdist}/tex/latex/libertine
# Typeset maps and blocks according to the Information Mapping
%{texmfdist}/source/latex/limap
%{texmfdist}/tex/latex/limap
%{texmfdist}/tex/latex/linearA
# Format linguists' examples.
%{texmfdist}/tex/latex/linguex
# Easy access to the Lorem Ipsum dummy text.
%{texmfdist}/source/latex/lipsum
%{texmfdist}/tex/latex/lipsum
# LK Proof figure macros.
%{texmfdist}/tex/latex/lkproof
# A LaTeX package to typeset indices with GNU's Texindex.
%{texmfdist}/source/latex/ltxindex
%{texmfdist}/tex/latex/ltxindex
# Set of slide fonts based on CM.
%{texmfdist}/tex/latex/lxfonts
# Support for LY1 LaTeX encoding.
%{texmfdist}/tex/latex/ly1
# Mathematics in accord with French usage.
%{texmfdist}/tex/latex/mafr
# Macros for mail merging.
%{texmfdist}/source/latex/mailing
%{texmfdist}/tex/latex/mailing
# Print various kinds 2/5 and Code 39 bar codes.
%{texmfdist}/tex/latex/makebarcode
# Perl script to help generate dtx and ins files
%{texmfdist}/source/latex/makedtx
%{texmfdist}/tex/latex/makedtx
# Include a glossary into a document.
%{texmfdist}/tex/latex/makeglos
# LaTeX support for the TeX book symbols.
%{texmfdist}/source/latex/manfnt
%{texmfdist}/tex/latex/manfnt
# Mathematical fonts to fit with particular text fonts.
%{texmfdist}/tex/latex/mathdesign
# Creating covers for music cassettes.
%{texmfdist}/tex/latex/mceinleger
# Experimental memoir support.
%{texmfdist}/tex/latex/memexsupp
# Pretty-print Metafont source.
%{texmfdist}/source/latex/mftinc
%{texmfdist}/tex/latex/mftinc
# Package for writing minutes of meetings.
%{texmfdist}/source/latex/minutes
%{texmfdist}/tex/latex/minutes
# Allows font sizes up to 35.83pt.
%{texmfdist}/source/latex/moresize
%{texmfdist}/tex/latex/moresize
# A package for LaTeX localisation.
%{texmfdist}/source/latex/msg
%{texmfdist}/tex/latex/msg
# Use italic and upright greek letters with mathtime.
%{texmfdist}/source/latex/mtgreek
%{texmfdist}/tex/latex/mtgreek
# Multiple bibliographies.
%{texmfdist}/source/latex/multibbl
%{texmfdist}/tex/latex/multibbl
# A pair of Georgian fonts.
%{texmfdist}/tex/latex/mxedruli
# Nomenclature typeset in a longtable
%{texmfdist}/source/latex/nomentbl
%{texmfdist}/tex/latex/nomentbl
# Non-floating table and figure captions.
%{texmfdist}/source/latex/nonfloat
%{texmfdist}/tex/latex/nonfloat
# Convert a number to its English expression.
%{texmfdist}/tex/latex/numname
# LaTeX support for ocr fonts.
%{texmfdist}/tex/latex/ocr-latex
# Old style numbers in OT1 encoding.
%{texmfdist}/source/latex/oldstyle
%{texmfdist}/tex/latex/oldstyle
# Footnote-style bibliographical references.
%{texmfdist}/source/latex/opcit
%{texmfdist}/tex/latex/opcit
# Counters as ordinal numbers in Portuguese.
%{texmfdist}/source/latex/ordinalpt
%{texmfdist}/tex/latex/ordinalpt
%{texmfdist}/tex/latex/otibet
%{texmfdist}/source/latex/otibet
# List environment for making outlines.
%{texmfdist}/tex/latex/outline
# Change section levels easily.
%{texmfdist}/tex/latex/outliner
# Fonts designed by Fra Luca de Pacioli in 1497.
%{texmfdist}/tex/latex/pacioli
# Notes at end of document.
%{texmfdist}/source/latex/pagenote
%{texmfdist}/tex/latex/pagenote
%{texmfdist}/tex/latex/palatino
# Origami-style folding paper CD case.
%{texmfdist}/source/latex/papercdcase
%{texmfdist}/tex/latex/papercdcase
# Defines simple macros for greek letters.
%{texmfdist}/source/latex/paresse
%{texmfdist}/tex/latex/paresse
# Typesets (two) streams of text running parallel.
%{texmfdist}/source/latex/parrun
%{texmfdist}/tex/latex/parrun
# German LaTeX package documentation.
%{texmfdist}/source/latex/pauldoc
%{texmfdist}/tex/latex/pauldoc
# Using graphics from PAW.
%{texmfdist}/source/latex/pawpict
%{texmfdist}/tex/latex/pawpict
%{texmfdist}/tex/latex/pdfwin
# Print Tibetan text in the classic pecha layout style.
%{texmfdist}/tex/latex/pecha
# Define LaTeX macros in terms of Perl code
%{texmfdist}/source/latex/perltex
%{texmfdist}/tex/latex/perltex
# Create images of the soroban using TikZ/PGF.
%{texmfdist}/tex/latex/pgf-soroban
# Disk of Phaistos font.
%{texmfdist}/tex/latex/phaistos
# Cross references for named and numbered environments.
%{texmfdist}/tex/latex/philex
# MetaFont Phonetic fonts, based on Computer Modern.
%{texmfdist}/tex/latex/phonetic
# Adds relative coordinates and improves the \plot command.
%{texmfdist}/tex/latex/pictex2
# Arrange for "plates" sections of documents.
%{texmfdist}/tex/latex/plates
%{texmfdist}/source/latex/plweb
%{texmfdist}/tex/latex/plweb
# "Poor man's" graphics.
%{texmfdist}/tex/latex/pmgraph
# Typeset Polish documents with LaTeX and Polish fonts.
%{texmfdist}/source/latex/polski
%{texmfdist}/tex/latex/polski
# Facilitates mass-mailing of postcards (junkmail).
%{texmfdist}/tex/latex/postcards
# Make label references "self-identify".
%{texmfdist}/source/latex/prettyref
%{texmfdist}/tex/latex/prettyref
# Shortcuts commands to symbols used in probability texts.
%{texmfdist}/source/latex/proba
%{texmfdist}/tex/latex/proba
%{texmfdist}/tex/latex/procIAGssymp
# Literate programming package.
%{texmfdist}/tex/latex/protex
# A class for typesetting minutes (only german).
%{texmfdist}/source/latex/protocol
%{texmfdist}/tex/latex/protocol
# A psfrag eXtension.
%{texmfdist}/source/latex/psfragx
%{texmfdist}/tex/latex/psfragx
%{texmfdist}/tex/latex/psgo
# PostScript picture support.
%{texmfdist}/source/latex/pspicture
%{texmfdist}/tex/latex/pspicture
# LaTeX macros for typesetting trees.
%{texmfdist}/tex/latex/qobitree
# Bundle for unit tests and pattern matching.
%{texmfdist}/source/latex/qstest
%{texmfdist}/tex/latex/qstest
# Consistent quote marks.
%{texmfdist}/source/latex/quotmark
%{texmfdist}/tex/latex/quotmark
%{texmfdist}/tex/latex/r_und_s
# Marginal pictures.
%{texmfdist}/source/latex/randbild
%{texmfdist}/tex/latex/randbild
# Use RCS (revision control system) tags in LaTeX documents.
%{texmfdist}/source/latex/rcs
%{texmfdist}/tex/latex/rcs
# Support for the revision control system.
%{texmfdist}/source/latex/rcsinfo
%{texmfdist}/tex/latex/rcsinfo
# Recycle top matter.
%{texmfdist}/tex/latex/rectopma
# Check references (in figures, table, equations, etc).
%{texmfdist}/tex/latex/refcheck
# Advanced formatting of cross references.
%{texmfdist}/source/latex/refstyle
%{texmfdist}/tex/latex/refstyle
# A "relaxed" font encoding.
%{texmfdist}/source/latex/relenc
%{texmfdist}/tex/latex/relenc
# Repeat items in an index after a page or column break
%{texmfdist}/tex/latex/repeatindex
# A package to help change page layout parameters in LaTeX.
%{texmfdist}/tex/latex/rmpage
# Create index with pagerefs.
%{texmfdist}/tex/latex/robustindex
# Input encoding with fallback procedures.
%{texmfdist}/source/latex/rtkinenc
%{texmfdist}/tex/latex/rtkinenc
%{texmfdist}/tex/latex/rtklage
# Sanskrit support.
%{texmfdist}/source/latex/sanskrit
%{texmfdist}/tex/latex/sanskrit
# A bundle of utilities by Jonathan Sauer.
%{texmfdist}/source/latex/sauerj
%{texmfdist}/tex/latex/sauerj
# Use sauter fonts in LaTeX.
%{texmfdist}/source/latex/sauterfonts
%{texmfdist}/tex/latex/sauterfonts
# Save name of the footnote mark for reuse.
%{texmfdist}/source/latex/savefnmark
%{texmfdist}/tex/latex/savefnmark
# Redefine symbols where names conflict.
%{texmfdist}/tex/latex/savesym
# Pack as much as possible onto each page of a LaTeX document.
%{texmfdist}/source/latex/savetrees
%{texmfdist}/tex/latex/savetrees
# Create scalebars for maps, diagrams or photos.
%{texmfdist}/source/latex/scalebar
%{texmfdist}/tex/latex/scalebar
# Semaphore alphabet font.
%{texmfdist}/tex/latex/semaphor
# Put only special contents on left-hand pages in two sided layout.
%{texmfdist}/source/latex/semioneside
%{texmfdist}/tex/latex/semioneside
# Split long sequences of characters in a neutral way.
%{texmfdist}/source/latex/seqsplit
%{texmfdist}/tex/latex/seqsplit
%{texmfdist}/source/latex/sf298
%{texmfdist}/tex/latex/sf298
# Typesetting science fiction/fantasy manuscripts.
%{texmfdist}/source/latex/sffms
%{texmfdist}/tex/latex/sffms
# Draw signal flow graphs.
%{texmfdist}/tex/latex/sfg
# Table of contents with different depths.
%{texmfdist}/source/latex/shorttoc
%{texmfdist}/tex/latex/shorttoc
# Variants of \show for LaTeX2e.
%{texmfdist}/source/latex/show2e
%{texmfdist}/tex/latex/show2e
%{texmfdist}/source/latex/showexpl
%{texmfdist}/tex/latex/showexpl
# A font to draw a skull.
%{texmfdist}/tex/latex/skull
# Access different-shaped small-caps fonts.
%{texmfdist}/source/latex/slantsc
%{texmfdist}/tex/latex/slantsc
# Create listoffigures etc. in a single chapter.
%{texmfdist}/tex/latex/smalltableof
# Extend LaTeX's \ref capability.
%{texmfdist}/tex/latex/smartref
# List the external dependencies of a LaTeX document.
%{texmfdist}/source/latex/snapshot
%{texmfdist}/tex/latex/snapshot
# Drawing sparklines: intense, simple, wordlike graphics.
%{texmfdist}/tex/latex/sparklines
# Support for formatting SPIE Proceedings manuscripts.
%{texmfdist}/tex/latex/spie
# Split and reorder your bibliography.
%{texmfdist}/source/latex/splitbib
%{texmfdist}/tex/latex/splitbib
# Jump between DVI and TeX files.
%{texmfdist}/source/latex/srcltx
%{texmfdist}/tex/latex/srcltx
# Statistics style.
%{texmfdist}/tex/latex/statex2
# Store statistics of a document.
%{texmfdist}/source/latex/statistik
%{texmfdist}/tex/latex/statistik
# Typeset Icelandic staves and runic letters.
%{texmfdist}/source/latex/staves
%{texmfdist}/tex/latex/staves
# Standard pages with n lines of at most m characters each.
%{texmfdist}/source/latex/stdpage
%{texmfdist}/tex/latex/stdpage
# Stellenbosch thesis bundle.
%{texmfdist}/source/latex/stellenbosch
%{texmfdist}/tex/latex/stellenbosch
# An Infrastructure for Semantic Preloading of LaTeX Documents.
%{texmfdist}/source/latex/stex
%{texmfdist}/tex/latex/stex
# Draw Nassi-Schneidermann charts
%{texmfdist}/source/latex/struktex
%{texmfdist}/tex/latex/struktex
# Various macros.
%{texmfdist}/tex/latex/sttools
# Create tear-off stubs at the bottom of a page.
%{texmfdist}/tex/latex/stubs
# SAS(R) user group conference proceedings document class.
%{texmfdist}/tex/latex/sugconf
# Define SVG named colours.
%{texmfdist}/tex/latex/svgcolor
# Subversion keywords in multi-file LaTeX documents
%{texmfdist}/source/latex/svn-multi
%{texmfdist}/tex/latex/svn-multi
# Typeset Subversion keywords.
%{texmfdist}/source/latex/svn
%{texmfdist}/tex/latex/svn
# Typeset Subversion Keywords.
%{texmfdist}/source/latex/svninfo
%{texmfdist}/tex/latex/svninfo
%{texmfdist}/tex/latex/symbol
# Easy drawing of syntactic proofs.
%{texmfdist}/tex/latex/synproof
%{texmfdist}/tex/latex/syntax
# Labels for tracing in a syntax tree.
%{texmfdist}/source/latex/syntrace
%{texmfdist}/tex/latex/syntrace
# Typeset syntactic trees.
%{texmfdist}/source/latex/synttree
%{texmfdist}/tex/latex/synttree
# Section numbering and table of contents control.
%{texmfdist}/source/latex/tocvsec2
%{texmfdist}/tex/latex/tocvsec2
# A tokenizer.
%{texmfdist}/tex/latex/tokenizer
# Macros for writing indices, glossaries.
%{texmfdist}/source/latex/toolbox
%{texmfdist}/tex/latex/toolbox
# Bundle of files for typsetting theses.
%{texmfdist}/source/latex/toptesi
%{texmfdist}/tex/latex/toptesi
# Fonts from the Trajan column in Rome.
%{texmfdist}/source/latex/trajan
%{texmfdist}/tex/latex/trajan
# Quick float definitions in LaTeX.
%{texmfdist}/source/latex/trivfloat
%{texmfdist}/tex/latex/trivfloat
# Typeset the (logic) turnstile notation.
%{texmfdist}/source/latex/turnstile
%{texmfdist}/tex/latex/turnstile
%{texmfdist}/source/latex/twoup
%{texmfdist}/tex/latex/twoup
# Print a typographic grid.
%{texmfdist}/source/latex/typogrid
%{texmfdist}/tex/latex/typogrid
%{texmfdist}/source/latex/pax
%{texmfdist}/tex/latex/pax
%{texmfdist}/source/latex/pdfx
%{texmfdist}/tex/latex/pdfx
%{texmfdist}/tex/latex/pigpen
%{texmfdist}/tex/latex/printlen
%{texmfdist}/tex/latex/properties
%{texmfdist}/tex/latex/psbao
%{texmfdist}/source/latex/pstool
%{texmfdist}/tex/latex/pstool
%{texmfdist}/tex/latex/pstricks
%{texmfdist}/source/latex/rcs-multi
%{texmfdist}/tex/latex/rcs-multi
%{texmfdist}/tex/latex/recycle
%{texmfdist}/source/latex/rjlparshap
%{texmfdist}/tex/latex/rjlparshap
%{texmfdist}/tex/latex/schemabloc
%{texmfdist}/tex/latex/selectp
%{texmfdist}/source/latex/shuffle
%{texmfdist}/tex/latex/shuffle
%{texmfdist}/source/latex/silence
%{texmfdist}/tex/latex/silence
%{texmfdist}/tex/latex/spotcolor
%{texmfdist}/source/latex/spverbatim
%{texmfdist}/tex/latex/spverbatim
%{texmfdist}/source/latex/steinmetz
%{texmfdist}/tex/latex/steinmetz
%{texmfdist}/source/latex/svn-prov
%{texmfdist}/tex/latex/svn-prov
%{texmfdist}/tex/latex/syllogism
%{texmfdist}/tex/latex/tabls
%{texmfdist}/tex/latex/tabularcalc
%{texmfdist}/source/latex/tabularew
%{texmfdist}/tex/latex/tabularew
%{texmfdist}/source/latex/termlist
%{texmfdist}/tex/latex/termlist
%{texmfdist}/source/latex/texments
%{texmfdist}/tex/latex/texments
%{texmfdist}/tex/latex/threeparttablex
%{texmfdist}/tex/latex/tikz-timing
%{texmfdist}/tex/latex/tkz-doc
%{texmfdist}/tex/latex/trimspaces
%{texmfdist}/tex/latex/ulqda
%{texmfdist}/tex/latex/varwidth
%{texmfdist}/tex/latex/venturis
%{texmfdist}/tex/latex/venturis2
%{texmfdist}/tex/latex/venturisadf
%{texmfdist}/tex/latex/venturisold
%{texmfdist}/tex/latex/venturissans
%{texmfdist}/tex/latex/venturissans2
%{texmfdist}/tex/latex/verbatimbox
%{texmfdist}/tex/latex/verbatimcopy
%{texmfdist}/tex/latex/version
%{texmfdist}/tex/latex/vertbars
%{texmfdist}/tex/latex/yagusylo
%{texmfdist}/tex/latex/zhmetrics

%files -n texlive-latex-pdfslide
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/pdfslide
%{texmfdist}/tex/latex/pdfslide

%files -n texlive-latex-pgf
%defattr(644,root,root,755)
%dir %{texmfdist}/source/context
%dir %{texmfdist}/source/context/third
%doc %{texmfdist}/doc/generic/pgf
%doc %{texmfdist}/doc/latex/pgfplots
%{texmfdist}/source/context/third/pgfplots
%{texmfdist}/source/latex/pgfopts
%{texmfdist}/source/latex/pgfplots
%{texmfdist}/tex/generic/pgf
%{texmfdist}/tex/generic/pgfplots
%{texmfdist}/tex/latex/pgf
%{texmfdist}/tex/latex/pgfopts
%{texmfdist}/tex/latex/pgfplots

%files -n texlive-latex-prosper
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ppr-prv
%doc %{texmfdist}/doc/latex/prosper
%{texmfdist}/source/latex/ppr-prv
%{texmfdist}/source/latex/prosper
%{texmfdist}/tex/latex/ppr-prv
%{texmfdist}/tex/latex/prosper

%files -n texlive-latex-polynom
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/polynom
%{texmfdist}/source/latex/polynom
%{texmfdist}/tex/latex/polynom

%files -n texlive-latex-polynomial
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/polynomial
%{texmfdist}/source/latex/polynomial
%{texmfdist}/tex/latex/polynomial

%files -n texlive-latex-pseudocode
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/pseudocode
%{texmfdist}/tex/latex/pseudocode

%files -n texlive-latex-pst-2dplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-2dplot
%{texmfdist}/tex/latex/pst-2dplot

%files -n texlive-latex-pst-3dplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-3d
%doc %{texmfdist}/doc/generic/pst-3dplot
%{texmfdist}/source/generic/pst-3d
%{texmfdist}/source/generic/pst-3dplot
%{texmfdist}/tex/generic/pst-3d
%{texmfdist}/tex/generic/pst-3dplot
%{texmfdist}/tex/latex/pst-3d
%{texmfdist}/tex/latex/pst-3dplot

%files -n texlive-latex-pst-bar
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/pst-bar
%{texmfdist}/tex/latex/pst-bar

%files -n texlive-latex-pst-circ
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-circ
%{texmfdist}/tex/generic/pst-circ
%{texmfdist}/tex/latex/pst-circ

%files -n texlive-latex-pst-diffraction
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-diffraction
%{texmfdist}/tex/generic/pst-diffraction
%{texmfdist}/tex/latex/pst-diffraction

%files -n texlive-latex-pst-eucl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-eucl
%lang(bg) %doc %{texmfdist}/doc/latex/pst-eucl-translation-bg
%{texmfdist}/tex/generic/pst-eucl
%{texmfdist}/tex/latex/pst-eucl

%files -n texlive-latex-pst-fun
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fun
%{texmfdist}/tex/generic/pst-fun
%{texmfdist}/tex/latex/pst-fun

%files -n texlive-latex-pst-func
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-func
%{texmfdist}/tex/generic/pst-func
%{texmfdist}/tex/latex/pst-func

%files -n texlive-latex-pst-infixplot
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-infixplot
%{texmfdist}/tex/generic/pst-infixplot
%{texmfdist}/tex/latex/pst-infixplot

%files -n texlive-latex-pst-fr3d
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fr3d
%{texmfdist}/source/generic/pst-fr3d
%{texmfdist}/tex/generic/pst-fr3d
%{texmfdist}/tex/latex/pst-fr3d

%files -n texlive-latex-pst-fractal
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-fractal
%{texmfdist}/tex/generic/pst-fractal
%{texmfdist}/tex/latex/pst-fractal

%files -n texlive-latex-pst-math
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-math
%{texmfdist}/tex/generic/pst-math
%{texmfdist}/tex/latex/pst-math

%files -n texlive-latex-pst-ob3d
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-ob3d
%{texmfdist}/source/generic/pst-ob3d
%{texmfdist}/tex/generic/pst-ob3d
%{texmfdist}/tex/latex/pst-ob3d

%files -n texlive-latex-pst-optexp
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/pst-optexp

%files -n texlive-latex-pst-optic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-optic
%{texmfdist}/tex/generic/pst-optic
%{texmfdist}/tex/latex/pst-optic

%files -n texlive-latex-pst-text
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-text
%{texmfdist}/tex/generic/pst-text
%{texmfdist}/tex/latex/pst-text

%files -n texlive-latex-pst-uncategorized
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pst-asr
%doc %{texmfdist}/doc/generic/pst-bar
%doc %{texmfdist}/doc/generic/pst-barcode
%doc %{texmfdist}/doc/generic/pst-blur
%doc %{texmfdist}/doc/generic/pst-coil
%doc %{texmfdist}/doc/generic/pst-cox
%doc %{texmfdist}/doc/generic/pst-dbicons
%doc %{texmfdist}/doc/generic/pst-eps
%doc %{texmfdist}/doc/generic/pst-fill
%doc %{texmfdist}/doc/generic/pst-geo
%doc %{texmfdist}/doc/generic/pst-ghsb
%doc %{texmfdist}/doc/generic/pst-gr3d
%doc %{texmfdist}/doc/generic/pst-grad
%doc %{texmfdist}/doc/generic/pst-jtree
%doc %{texmfdist}/doc/generic/pst-labo
%doc %{texmfdist}/doc/generic/pst-lens
%doc %{texmfdist}/doc/generic/pst-light3d
%doc %{texmfdist}/doc/generic/pst-osci
%doc %{texmfdist}/doc/generic/pst-pad
%doc %{texmfdist}/doc/generic/pst-pdgr
%doc %{texmfdist}/doc/generic/pst-poly
%doc %{texmfdist}/doc/generic/pst-qtree
%doc %{texmfdist}/doc/generic/pst-slpe
%doc %{texmfdist}/doc/generic/pst-solides3d
%doc %{texmfdist}/doc/generic/pst-soroban
%doc %{texmfdist}/doc/generic/pst-spectra
%doc %{texmfdist}/doc/generic/pst-stru
%doc %{texmfdist}/doc/generic/pst-uml
%doc %{texmfdist}/doc/generic/pst-vue3d
%doc %{texmfdist}/doc/latex/auto-pst-pdf
%doc %{texmfdist}/doc/latex/pst-pdf
%doc %{texmfdist}/doc/latex/pst-calendar
%{texmfdist}/source/generic/pst-barcode
%{texmfdist}/source/generic/pst-blur
%{texmfdist}/source/generic/pst-circ
%{texmfdist}/source/generic/pst-coil
%{texmfdist}/source/generic/pst-dbicons
%{texmfdist}/source/generic/pst-diffraction
%{texmfdist}/source/generic/pst-eps
%{texmfdist}/source/generic/pst-fill
%{texmfdist}/source/generic/pst-fun
%{texmfdist}/source/generic/pst-func
%{texmfdist}/source/generic/pst-lens
%{texmfdist}/source/generic/pst-light3d
%{texmfdist}/source/generic/pst-optic
%{texmfdist}/source/generic/pst-pad
%{texmfdist}/source/generic/pst-pdgr
%{texmfdist}/source/generic/pst-slpe
%{texmfdist}/source/generic/pst-soroban
%{texmfdist}/source/generic/pst-text
%{texmfdist}/source/generic/pst-uml
%{texmfdist}/source/generic/pst-vue3d
%{texmfdist}/source/latex/auto-pst-pdf
%{texmfdist}/source/latex/pst-gr3d
%{texmfdist}/source/latex/pst-pdf
%{texmfdist}/tex/generic/pst-abspos
%{texmfdist}/tex/generic/pst-asr
%{texmfdist}/tex/generic/pst-barcode
%{texmfdist}/tex/generic/pst-bezier
%{texmfdist}/tex/generic/pst-blur
%{texmfdist}/tex/generic/pst-bspline
%{texmfdist}/tex/generic/pst-coil
%{texmfdist}/tex/generic/pst-cox
%{texmfdist}/tex/generic/pst-eps
%{texmfdist}/tex/generic/pst-fill
%{texmfdist}/tex/generic/pst-gantt
%{texmfdist}/tex/generic/pst-geo
%{texmfdist}/tex/generic/pst-ghsb
%{texmfdist}/tex/generic/pst-gr3d
%{texmfdist}/tex/generic/pst-grad
%{texmfdist}/tex/generic/pst-jtree
%{texmfdist}/tex/generic/pst-labo
%{texmfdist}/tex/generic/pst-lens
%{texmfdist}/tex/generic/pst-light3d
%{texmfdist}/tex/generic/pst-osci
%{texmfdist}/tex/generic/pst-pad
%{texmfdist}/tex/generic/pst-pdgr
%{texmfdist}/tex/generic/pst-poly
%{texmfdist}/tex/generic/pst-qtree
%{texmfdist}/tex/generic/pst-slpe
%{texmfdist}/tex/generic/pst-solides3d
%{texmfdist}/tex/generic/pst-spectra
%{texmfdist}/tex/generic/pst-stru
%{texmfdist}/tex/generic/pst-tree
%{texmfdist}/tex/generic/pst-vue3d
%{texmfdist}/tex/latex/pst-abspos
%{texmfdist}/tex/latex/pst-asr
%{texmfdist}/tex/latex/pst-barcode
%{texmfdist}/tex/latex/pst-bezier
%{texmfdist}/tex/latex/pst-blur
%{texmfdist}/tex/latex/pst-bspline
%{texmfdist}/tex/latex/pst-calendar
%{texmfdist}/tex/latex/pst-coil
%{texmfdist}/tex/latex/pst-cox
%{texmfdist}/tex/latex/pst-dbicons
%{texmfdist}/tex/latex/pst-eps
%{texmfdist}/tex/latex/pst-fill
%{texmfdist}/tex/latex/pst-gantt
%{texmfdist}/tex/latex/pst-geo
%{texmfdist}/tex/latex/pst-ghsb
%{texmfdist}/tex/latex/pst-gr3d
%{texmfdist}/tex/latex/pst-grad
%{texmfdist}/tex/latex/pst-jtree
%{texmfdist}/tex/latex/pst-labo
%{texmfdist}/tex/latex/pst-lens
%{texmfdist}/tex/latex/pst-light3d
%{texmfdist}/tex/latex/pst-osci
%{texmfdist}/tex/latex/pst-pad
%{texmfdist}/tex/latex/pst-pdf
%{texmfdist}/tex/latex/pst-pdgr
%{texmfdist}/tex/latex/pst-poly
%{texmfdist}/tex/latex/pst-qtree
%{texmfdist}/tex/latex/pst-sigsys
%{texmfdist}/tex/latex/pst-slpe
%{texmfdist}/tex/latex/pst-solides3d
%{texmfdist}/tex/latex/pst-soroban
%{texmfdist}/tex/latex/pst-spectra
%{texmfdist}/tex/latex/pst-stru
%{texmfdist}/tex/latex/pst-tree
%{texmfdist}/tex/latex/pst-uml
%{texmfdist}/tex/latex/pst-vowel
%{texmfdist}/tex/latex/pst-vue3d

%files -n texlive-latex-psnfss
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/psnfss
%{texmfdist}/fonts/map/dvips/psnfss
%{texmfdist}/source/latex/psnfss
%{texmfdist}/source/latex/latex-tds
%{texmfdist}/tex/latex/psnfss

%files -n texlive-latex-pxfonts
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/pxfonts
%{texmfdist}/fonts/type1/public/pxfonts
%{texmfdist}/fonts/afm/public/pxfonts
%{texmfdist}/fonts/vf/public/pxfonts
%{texmfdist}/fonts/map/dvips/pxfonts

%files -n texlive-latex-SIstyle
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/SIstyle
%{texmfdist}/source/latex/SIstyle
%{texmfdist}/tex/latex/SIstyle

%files -n texlive-latex-SIunits
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/SIunits
%{texmfdist}/tex/latex/SIunits
%{texmfdist}/source/latex/SIunits

%files -n texlive-latex-siunitx
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/siunitx
%{texmfdist}/tex/latex/siunitx
%{texmfdist}/source/latex/siunitx

%files -n texlive-latex-Tabbing
%defattr(644,root,root,755)
%{texmfdist}/source/latex/Tabbing
%{texmfdist}/doc/latex/Tabbing

%files -n texlive-latex-tutorial
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/around-the-bend
%doc %{texmfdist}/doc/generic/components-of-TeX
%doc %{texmfdist}/doc/latex/comprehensive
%doc %{texmfdist}/doc/latex/cursolatex
%doc %{texmfdist}/doc/latex/dtxtut
%doc %{texmfdist}/doc/latex/first-latex-doc
%doc %{texmfdist}/doc/latex/intro-scientific
%doc %{texmfdist}/doc/latex/latex2e-help-texinfo
%doc %{texmfdist}/doc/latex/latex-referenz
%doc %{texmfdist}/doc/latex/latex-tabellen
%doc %{texmfdist}/doc/latex/lshort-persian
%doc %{texmfdist}/doc/latex/lshort-russian
%doc %{texmfdist}/doc/latex/mathmode
%doc %{texmfdist}/doc/latex/tex-font-errors-cheatsheet
%doc %{texmfdist}/doc/latex/titlepages
%doc %{texmfdist}/doc/latex/tkz-doc
%doc %{texmfdist}/doc/latex/visualfaq
%doc %{texmfdist}/doc/latex/webguide
%lang(es) %doc %{texmfdist}/doc/generic/es-tex-faq
%doc %{texmfdist}/doc/latex/latexcheat
%lang(es) %doc %{texmfdist}/doc/latex/latexcheat-esmx
%lang(pt) %doc %{texmfdist}/doc/latex/latexcheat-ptbr
%lang(fr) %doc %{texmfdist}/doc/latex/apprends-latex
%lang(pt) %doc %{texmfdist}/doc/latex/beamer-tut-pt

%files -n texlive-latex-txfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/txfonts
%{texmfdist}/fonts/afm/public/txfonts
%{texmfdist}/fonts/afm/public/txfontsb
%{texmfdist}/fonts/enc/dvips/txfonts
%{texmfdist}/fonts/enc/dvips/txfontsb
%{texmfdist}/fonts/map/dvips/txfonts
%{texmfdist}/fonts/map/dvips/txfontsb
%{texmfdist}/fonts/tfm/public/txfontsb
%{texmfdist}/fonts/type1/public/txfonts
%{texmfdist}/fonts/type1/public/txfontsb
%{texmfdist}/fonts/vf/public/txfonts
%{texmfdist}/fonts/vf/public/txfontsb
%{texmfdist}/source/fonts/txfontsb
%{texmfdist}/tex/latex/txfonts
%{texmfdist}/tex/latex/txfontsb

%files -n texlive-latex-ucs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ucs
%{texmfdist}/tex/latex/ucs

%files -n texlive-latex-umlaute
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/umlaute
%{texmfdist}/source/latex/umlaute

%files -n texlive-latex-variations
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/variations
%{texmfdist}/tex/generic/variations

%files -n texlive-latex-wasysym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/wasysym
%{texmfdist}/tex/latex/wasysym
%{texmfdist}/source/latex/wasysym

%files -n texlive-latex-xcolor
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/xcolor
%{texmfdist}/source/latex/xcolor

%files -n texlive-tex-babel
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/babel

%files -n texlive-tex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/german
%{texmfdist}/tex/generic/german
%{texmfdist}/source/generic/german

%files -n texlive-tex-mfpic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/mfpic
%{texmfdist}/tex/generic/mfpic
%{texmfdist}/source/generic/mfpic

%files -n texlive-tex-midnight
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/midnight
%{texmfdist}/tex/generic/midnight

%files -n texlive-tex-misc
%defattr(644,root,root,755)
%{texmfdist}/source/generic/multido
%{texmfdist}/source/generic/tap
%doc %{texmfdist}/doc/generic/multido
%doc %{texmfdist}/doc/generic/tap

%{texmfdist}/tex/generic/eijkhout
%{texmfdist}/tex/generic/multido
%{texmfdist}/tex/generic/misc
%exclude %{texmfdist}/tex/generic/misc/null*
%exclude %{texmfdist}/tex/generic/misc/texnames.sty


%files -n texlive-tex-pictex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pictex
%{texmfdist}/tex/generic/pictex

%files -n texlive-tex-psizzl
%defattr(644,root,root,755)
%{texmfdist}/source/psizzl
%{texmfdist}/tex/psizzl

%files -n texlive-tex-pstricks
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pstricks
%doc %{texmfdist}/doc/generic/pstricks-add
%doc %{texmfdist}/doc/generic/pst-abspos
%doc %{texmfdist}/doc/generic/pst-am
%doc %{texmfdist}/doc/generic/pst-bezier
%doc %{texmfdist}/doc/generic/pst-bspline
%doc %{texmfdist}/doc/generic/pst-electricfield
%doc %{texmfdist}/doc/generic/pst-gantt
%doc %{texmfdist}/doc/generic/pst-knot
%doc %{texmfdist}/doc/generic/pst-magneticfield
%doc %{texmfdist}/doc/generic/pst-mirror
%doc %{texmfdist}/doc/generic/pst-node
%doc %{texmfdist}/doc/generic/pst-platon
%doc %{texmfdist}/doc/generic/pst-plot
%doc %{texmfdist}/doc/generic/pst-sigsys
%doc %{texmfdist}/doc/generic/pst-support
%doc %{texmfdist}/doc/generic/pst-thick
%doc %{texmfdist}/doc/generic/pst-tree
%{texmfdist}/tex/generic/pstricks
%{texmfdist}/tex/latex/pstricks-add
%{texmfdist}/source/generic/pstricks-add
%{texmfdist}/tex/generic/pstricks-add

%files -n texlive-tex-qpxqtx
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/qpxqtx
%{texmfdist}/fonts/vf/public/qpxqtx
%{texmfdist}/tex/generic/qpxqtx

%files -n texlive-tex-ruhyphen
%defattr(644,root,root,755)
%{texmfdist}/tex/generic/ruhyphen
%{texmfdist}/source/generic/ruhyphen

%files -n texlive-tex-huhyphen
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/huhyphen

%files -n texlive-tex-spanish
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/spanish-mx
%dir %{texmfdist}/tex/latex/babelbib
%{texmfdist}/tex/latex/spanish-mx
%{texmfdist}/tex/latex/dvdcoll/dcl/spanish.dcl

%files -n texlive-tex-texdraw
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/support/texdraw
%{texmfdist}/tex/generic/texdraw

%files -n texlive-tex-thumbpdf
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/thumbpdf
%attr(755,root,root) %{_bindir}/thumbpdf
%{texmfdist}/tex/generic/thumbpdf

%files -n texlive-tex-ukrhyph
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/ukrhyph
%{texmfdist}/tex/generic/ukrhyph

%files -n texlive-latex-lang-thai
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/garuda-c90
%{texmfdist}/fonts/tfm/public/garuda-c90

%files -n texlive-latex-lang-vietnam
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/vntex
%{texmfdist}/fonts/afm/vntex/chartervn
%{texmfdist}/fonts/afm/vntex/grotesqvn
%{texmfdist}/fonts/afm/vntex/urwvn
%{texmfdist}/fonts/afm/vntex/vntopia
%{texmfdist}/fonts/enc/dvips/vntex/
%{texmfdist}/fonts/enc/pdftex/vntex
%{texmfdist}/fonts/map/dvips/vntex
%{texmfdist}/fonts/tfm/vntex
%{texmfdist}/fonts/type1/vntex
%{texmfdist}/fonts/vf/vntex
%{texmfdist}/source/generic/vntex
%{texmfdist}/tex/latex/vntex

%files -n texlive-tex-xypic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/xypic
%{texmfdist}/tex/generic/xypic

%files -n texlive-tex-xkeyval
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/xkeyval
%{texmfdist}/source/latex/xkeyval
%{texmfdist}/tex/generic/xkeyval
%{texmfdist}/tex/latex/xkeyval

%files -n texlive-fonts-adobe
%defattr(644,root,root,755)
%{texmfdist}/fonts/cmap/adobemapping
%{texmfdist}/fonts/type1/adobe
%{texmfdist}/fonts/afm/adobe
%{texmfdist}/fonts/tfm/adobe
%{texmfdist}/fonts/vf/adobe

%files -n texlive-fonts-ae
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/ae
%{texmfdist}/fonts/tfm/public/ae
%{texmfdist}/fonts/vf/public/ae
%{texmfdist}/source/fonts/ae

%files -n texlive-fonts-ams
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/amsfonts
%{texmfdist}/fonts/afm/public/amsfonts
%{texmfdist}/fonts/tfm/public/amsfonts
%{texmfdist}/fonts/map/dvips/amsfonts
%{texmfdist}/fonts/type1/public/amsfonts

%files -n texlive-fonts-antt
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antt
%{texmfdist}/fonts/afm/public/antt
%{texmfdist}/fonts/opentype/public/antt
%{texmfdist}/fonts/enc/dvips/antt
%{texmfdist}/fonts/tfm/public/antt
%{texmfdist}/fonts/map/dvips/antt
%{texmfdist}/tex/plain/antt

%files -n texlive-fonts-arphic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/arphic
%{texmfdist}/fonts/afm/arphic
%{texmfdist}/fonts/tfm/arphic
%{texmfdist}/fonts/vf/arphic

%files -n texlive-fonts-bbm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/bbm
%{texmfdist}/fonts/source/public/bbm
%{texmfdist}/fonts/tfm/public/bbm

%files -n texlive-fonts-bbold
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/bbold
%{texmfdist}/fonts/tfm/public/bbold

%files -n texlive-fonts-bitstream
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/bitstrea
%{texmfdist}/fonts/tfm/bitstrea
%{texmfdist}/fonts/vf/bitstrea

%files -n texlive-fonts-cc-pl
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cc-pl
%{texmfdist}/fonts/tfm/public/cc-pl
%{texmfdist}/fonts/map/dvips/cc-pl

%files -n texlive-fonts-cg
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/cg
%{texmfdist}/fonts/vf/cg

%files -n texlive-fonts-cm
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/pk/ljfour/public
%doc %{texmfdist}/doc/fonts/cm
%{texmfdist}/fonts/map/dvips/cm
%{texmfdist}/fonts/pk/ljfour/public/cm
%{texmfdist}/fonts/source/public/cm
%{texmfdist}/fonts/tfm/public/cm
%{texmfdist}/fonts/afm/public/cm-unicode
%{texmfdist}/fonts/enc/dvips/cm-unicode
%{texmfdist}/fonts/map/dvips/cm-unicode
%{texmfdist}/fonts/opentype/public/cm-unicode
%{texmfdist}/fonts/type1/public/cm-unicode

%files -n texlive-fonts-cmbright
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cmbright
%{texmfdist}/fonts/tfm/public/cmbright
%{texmfdist}/source/latex/cmbright

%files -n texlive-fonts-cmcyr
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cmcyr
%{texmfdist}/fonts/source/public/cmcyr
%{texmfdist}/fonts/type1/public/cmcyr
%{texmfdist}/fonts/tfm/public/cmcyr
%{texmfdist}/fonts/vf/public/cmcyr
%{texmfdist}/fonts/map/dvips/cmcyr

%files -n texlive-fonts-cmextra
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cmextra
%{texmfdist}/fonts/tfm/public/cmextra

%files -n texlive-fonts-cmsuper
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cm-super
%{texmfdist}/fonts/afm/public/cm-super
%{texmfdist}/fonts/enc/dvips/cm-super
%{texmfdist}/fonts/map/dvips/cm-super
%{texmfdist}/fonts/map/vtex/cm-super
%{texmfdist}/fonts/type1/public/cm-super

%files -n texlive-fonts-concmath
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/concmath
%{texmfdist}/fonts/source/public/concmath-fonts
%{texmfdist}/fonts/tfm/public/concmath-fonts
%{texmfdist}/source/latex/concmath

%files -n texlive-fonts-concrete
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/concrete
%{texmfdist}/fonts/source/public/concrete
%{texmfdist}/fonts/tfm/public/concrete

%files -n texlive-fonts-cs
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cs
%{texmfdist}/fonts/enc/dvips/cs
%{texmfdist}/fonts/tfm/public/cs
%{texmfdist}/fonts/map/dvips/cs

%files -n texlive-fonts-ecc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/ecc
%{texmfdist}/fonts/source/public/ecc
%{texmfdist}/fonts/tfm/public/ecc

%files -n texlive-fonts-eurosym
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/eurosym
%{texmfdist}/fonts/source/public/eurosym
%{texmfdist}/fonts/tfm/public/eurosym
%{texmfdist}/fonts/map/dvips/eurosym
%{texmfdist}/tex/latex/eurosym

%files -n texlive-fonts-eulervm
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/public/eulervm
%{texmfdist}/fonts/vf/public/eulervm
%{texmfdist}/source/latex/eulervm
%{texmfdist}/tex/latex/eulervm

%files -n texlive-fonts-euxm
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/euxm
%{texmfdist}/fonts/tfm/public/euxm

%files -n texlive-fonts-gothic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/gothic
%{texmfdist}/fonts/source/public/gothic
%{texmfdist}/fonts/type1/public/gothic
%{texmfdist}/fonts/afm/public/gothic
%{texmfdist}/fonts/tfm/public/gothic
%{texmfdist}/fonts/vf/public/gothic
%{texmfdist}/fonts/map/dvips/gothic

%files -n texlive-fonts-hoekwater
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/hoekwater
%{texmfdist}/fonts/tfm/hoekwater

%files -n texlive-fonts-jknappen
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/jknappen
%{texmfdist}/fonts/tfm/jknappen

%files -n texlive-fonts-kpfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/kpfonts
%{texmfdist}/fonts/map/dvips/kpfonts
%{texmfdist}/fonts/afm/public/kpfonts
%{texmfdist}/fonts/enc/dvips/kpfonts
%{texmfdist}/fonts/enc/pdftex/kpfonts
%{texmfdist}/fonts/source/public/kpfonts
%{texmfdist}/fonts/tfm/public/kpfonts
%{texmfdist}/fonts/type1/public/kpfonts
%{texmfdist}/fonts/vf/public/kpfonts
%{texmfdist}/tex/latex/kpfonts

%files -n texlive-fonts-latex
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts/source/public/latex-fonts
%dir %{texmfdist}/fonts/tfm/public/latex-fonts
%doc %{texmfdist}/doc/latex/esint
%{texmfdist}/fonts/source/public/esint
%{texmfdist}/fonts/source/public/latex-fonts/*
%{texmfdist}/fonts/tfm/public/esint
%{texmfdist}/fonts/tfm/public/latex-fonts/*
%{texmfdist}/source/latex/esint
%{texmfdist}/tex/latex/esint

%files -n texlive-fonts-lh
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lh
%{texmfdist}/fonts/source/lh
%{texmfdist}/metapost/support/charlib/LH
%{texmfdist}/source/fonts/lh
%{texmfdist}/source/latex/lh


%files -n texlive-fonts-marvosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/marvosym
%{texmfdist}/fonts/afm/public/marvosym
%{texmfdist}/fonts/tfm/public/marvosym
%{texmfdist}/fonts/map/dvips/marvosym

%files -n texlive-fonts-mflogo
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/mflogo
%{texmfdist}/fonts/tfm/public/mflogo
%{texmfdist}/fonts/map/dvips/mflogo
%{texmfdist}/source/latex/mflogo

%files -n texlive-fonts-misc
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/misc
%{texmfdist}/fonts/tfm/public/misc
%{texmfdist}/fonts/misc

%files -n texlive-fonts-monotype
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/monotype
%{texmfdist}/fonts/vf/monotype

%files -n texlive-fonts-other
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/glyphlist
%{texmfdist}/fonts/source/public/knuthotherfonts

%{texmfdist}/fonts/cid

%{texmfdist}/fonts/tfm/public/pslatex
%{texmfdist}/fonts/map/dvips/pslatex
%{texmfdist}/fonts/vf/public/pslatex

%doc %{texmfdist}/doc/fonts/allrunes
%{texmfdist}/fonts/map/dvips/allrunes
%{texmfdist}/fonts/source/public/allrunes
%{texmfdist}/fonts/type1/public/allrunes
%{texmfdist}/source/fonts/allrunes

%doc %{texmfdist}/doc/fonts/antiqua
%{texmfdist}/fonts/map/dvips/antiqua

%{texmfdist}/fonts/afm/arabi
%{texmfdist}/fonts/tfm/arabi
%{texmfdist}/fonts/type1/arabi
%{texmfdist}/fonts/enc/dvips/arabi
%{texmfdist}/fonts/map/dvips/arabi

%{texmfdist}/fonts/map/dvips/arabtex
%{texmfdist}/fonts/source/public/arabtex
%{texmfdist}/fonts/tfm/public/arabtex
%{texmfdist}/fonts/type1/public/arabtex

%doc %{texmfdist}/doc/fonts/archaic
%{texmfdist}/fonts/afm/public/archaic
%{texmfdist}/fonts/map/dvips/archaic
%{texmfdist}/fonts/source/public/archaic
%{texmfdist}/fonts/tfm/public/archaic
%{texmfdist}/fonts/type1/public/archaic
%{texmfdist}/source/fonts/archaic

%doc %{texmfdist}/doc/fonts/arev
%{texmfdist}/fonts/afm/public/arev
%{texmfdist}/fonts/enc/dvips/arev
%{texmfdist}/fonts/map/dvips/arev
%{texmfdist}/fonts/tfm/public/arev
%{texmfdist}/fonts/type1/public/arev
%{texmfdist}/fonts/vf/public/arev
%{texmfdist}/source/fonts/arev

%{texmfdist}/fonts/afm/arkandis
%{texmfdist}/fonts/vf/arkandis
%{texmfdist}/fonts/tfm/arkandis
%{texmfdist}/fonts/type1/arkandis

%{texmfdist}/fonts/map/dvips/arphic

%doc %{texmfdist}/doc/fonts/Asana-Math
%{texmfdist}/fonts/opentype/public/Asana-Math

%doc %{texmfdist}/doc/fonts/astro
%{texmfdist}/fonts/source/public/astro
%{texmfdist}/fonts/tfm/public/astro

%{texmfdist}/fonts/afm/public/augie
%{texmfdist}/fonts/map/dvips/augie
%{texmfdist}/fonts/tfm/public/augie
%{texmfdist}/fonts/type1/public/augie
%{texmfdist}/fonts/vf/public/augie

%doc %{texmfdist}/doc/fonts/auncial-new
%{texmfdist}/fonts/afm/public/auncial-new
%{texmfdist}/fonts/map/dvips/auncial-new
%{texmfdist}/fonts/tfm/public/auncial-new
%{texmfdist}/fonts/type1/public/auncial-new
%{texmfdist}/source/fonts/auncial-new

%{texmfdist}/fonts/afm/public/aurical
%{texmfdist}/fonts/map/dvips/aurical
%{texmfdist}/fonts/source/public/aurical
%{texmfdist}/fonts/tfm/public/aurical
%{texmfdist}/fonts/type1/public/aurical

%{texmfdist}/fonts/map/dvips/avantgar

%{texmfdist}/fonts/source/public/bangtex
%{texmfdist}/fonts/tfm/public/bangtex

%{texmfdist}/fonts/source/public/barcodes
%{texmfdist}/fonts/tfm/public/barcodes

%{texmfdist}/fonts/source/public/bbding
%{texmfdist}/fonts/tfm/public/bbding

%{texmfdist}/fonts/truetype/public

%{texmfdist}/fonts/source/public/bengali
%{texmfdist}/fonts/tfm/public/bengali

%doc %{texmfdist}/doc/fonts/bera
%{texmfdist}/fonts/afm/public/bera
%{texmfdist}/fonts/map/dvips/bera
%{texmfdist}/fonts/tfm/public/bera
%{texmfdist}/fonts/type1/public/bera
%{texmfdist}/fonts/vf/public/bera

%{texmfdist}/fonts/tfm/public/bgreek
%{texmfdist}/fonts/vf/public/bgreek

%doc %{texmfdist}/doc/fonts/blacklettert1
%{texmfdist}/fonts/tfm/public/blacklettert1
%{texmfdist}/fonts/vf/public/blacklettert1
%{texmfdist}/source/fonts/blacklettert1

%doc %{texmfdist}/doc/fonts/boisik
%{texmfdist}/fonts/source/public/boisik
%{texmfdist}/fonts/tfm/public/boisik

%doc %{texmfdist}/doc/fonts/bookhands
%{texmfdist}/fonts/source/public/bookhands

%{texmfdist}/fonts/map/dvips/bookman

%{texmfdist}/fonts/afm/public/brushscr
%{texmfdist}/fonts/map/dvips/brushscr
%{texmfdist}/fonts/tfm/public/brushscr
%{texmfdist}/fonts/type1/public/brushscr
%{texmfdist}/fonts/vf/public/brushscr

%doc %{texmfdist}/doc/fonts/burmese
%{texmfdist}/fonts/map/dvips/burmese
%{texmfdist}/fonts/tfm/public/burmese
%{texmfdist}/fonts/type1/public/burmese

%doc %{texmfdist}/doc/fonts/cns
%{texmfdist}/fonts/tfm/cns

%doc %{texmfdist}/doc/latex/calligra
%{texmfdist}/fonts/source/public/calligra
%{texmfdist}/fonts/tfm/public/calligra

%doc %{texmfdist}/doc/fonts/carolmin-ps
%{texmfdist}/fonts/afm/public/carolmin-ps
%{texmfdist}/fonts/map/dvips/carolmin-ps
%{texmfdist}/fonts/type1/public/carolmin-ps

%{texmfdist}/fonts/source/public/casyl
%{texmfdist}/fonts/tfm/public/casyl

%{texmfdist}/fonts/source/public/cbcoptic
%{texmfdist}/fonts/tfm/public/cbcoptic
%{texmfdist}/fonts/type1/public/cbcoptic

%doc %{texmfdist}/doc/fonts/cbfonts
%{texmfdist}/fonts/enc/dvips/cbfonts
%{texmfdist}/fonts/map/dvips/cbfonts
%{texmfdist}/fonts/source/public/cbfonts
%{texmfdist}/fonts/tfm/public/cbfonts
%{texmfdist}/fonts/type1/public/cbfonts

%doc %{texmfdist}/doc/fonts/charter

%{texmfdist}/fonts/source/public/cherokee
%{texmfdist}/fonts/tfm/public/cherokee

%doc %{texmfdist}/doc/fonts/cjhebrew
%{texmfdist}/fonts/afm/public/cjhebrew
%{texmfdist}/fonts/enc/dvips/cjhebrew
%{texmfdist}/fonts/map/dvips/cjhebrew
%{texmfdist}/fonts/tfm/public/cjhebrew
%{texmfdist}/fonts/type1/public/cjhebrew
%{texmfdist}/fonts/vf/public/cjhebrew

%{texmfdist}/fonts/source/public/clock
%{texmfdist}/fonts/tfm/public/clock

%{texmfdist}/fonts/afm/public/cm-lgc
%{texmfdist}/fonts/enc/dvips/cm-lgc
%{texmfdist}/fonts/map/dvips/cm-lgc
%{texmfdist}/fonts/ofm/public/cm-lgc
%{texmfdist}/fonts/ovf/public/cm-lgc
%{texmfdist}/fonts/tfm/public/cm-lgc
%{texmfdist}/fonts/type1/public/cm-lgc
%{texmfdist}/fonts/vf/public/cm-lgc

%{texmfdist}/fonts/source/public/cmpica
%{texmfdist}/fonts/tfm/public/cmpica

%{texmfdist}/fonts/afm/ibm
%{texmfdist}/fonts/map/dvips/courier

%{texmfdist}/fonts/afm/public/cryst
%{texmfdist}/fonts/source/public/cryst
%{texmfdist}/fonts/tfm/public/cryst
%{texmfdist}/fonts/type1/public/cryst

%{texmfdist}/fonts/source/public/ctib
%{texmfdist}/fonts/tfm/public/ctib

%doc %{texmfdist}/doc/fonts/cyklop
%{texmfdist}/fonts/afm/public/cyklop
%{texmfdist}/fonts/enc/dvips/cyklop
%{texmfdist}/fonts/map/dvips/cyklop
%{texmfdist}/fonts/opentype/public/cyklop
%{texmfdist}/fonts/tfm/public/cyklop
%{texmfdist}/fonts/type1/public/cyklop

%{texmfdist}/fonts/source/public/dancers
%{texmfdist}/fonts/tfm/public/dancers

%doc %{texmfdist}/doc/fonts/dice
%{texmfdist}/fonts/source/public/dice
%{texmfdist}/fonts/tfm/public/dice

%doc %{texmfdist}/doc/fonts/dictsym
%{texmfdist}/fonts/afm/public/dictsym
%{texmfdist}/fonts/map/dvips/dictsym
%{texmfdist}/fonts/tfm/public/dictsym
%{texmfdist}/fonts/type1/public/dictsym

%{texmfdist}/fonts/tfm/public/dingbat
%{texmfdist}/fonts/source/public/dingbat

%doc %{texmfdist}/doc/fonts/doublestroke
%{texmfdist}/fonts/map/dvips/doublestroke
%{texmfdist}/fonts/source/public/doublestroke
%{texmfdist}/fonts/tfm/public/doublestroke
%{texmfdist}/fonts/type1/public/doublestroke

%{texmfdist}/fonts/map/dvips/dozenal
%{texmfdist}/fonts/source/public/dozenal
%{texmfdist}/fonts/tfm/public/dozenal
%{texmfdist}/fonts/type1/public/dozenal
%{texmfdist}/fonts/vf/public/dozenal

%doc %{texmfdist}/doc/fonts/duerer
%{texmfdist}/fonts/source/public/duerer
%{texmfdist}/fonts/tfm/public/duerer

%doc %{texmfdist}/doc/fonts/eiad
%{texmfdist}/fonts/source/public/eiad-ltx
%{texmfdist}/fonts/source/public/eiad
%{texmfdist}/fonts/tfm/public/eiad

%doc %{texmfdist}/doc/fonts/elvish
%{texmfdist}/fonts/source/public/elvish
%{texmfdist}/fonts/tfm/public/elvish

%doc %{texmfdist}/doc/fonts/epigrafica
%{texmfdist}/fonts/afm/public/epigrafica
%{texmfdist}/fonts/enc/dvips/epigrafica
%{texmfdist}/fonts/map/dvips/epigrafica
%{texmfdist}/fonts/tfm/public/epigrafica
%{texmfdist}/fonts/type1/public/epigrafica
%{texmfdist}/fonts/vf/public/epigrafica

%{texmfdist}/fonts/map/dvips/epiolmec
%{texmfdist}/fonts/tfm/public/epiolmec
%{texmfdist}/fonts/type1/public/epiolmec

%doc %{texmfdist}/doc/fonts/esint-type1
%{texmfdist}/fonts/map/dvips/esint-type1
%{texmfdist}/fonts/type1/public/esint-type1

%{texmfdist}/fonts/ofm/public/ethiop
%{texmfdist}/fonts/ovf/public/ethiop
%{texmfdist}/fonts/ovp/public/ethiop
%{texmfdist}/fonts/source/public/ethiop
%{texmfdist}/fonts/tfm/public/ethiop

%{texmfdist}/fonts/map/dvips/ethiop-t1
%{texmfdist}/fonts/type1/public/ethiop-t1

%doc %{texmfdist}/doc/fonts/euro-ce
%{texmfdist}/fonts/source/public/euro-ce
%{texmfdist}/fonts/tfm/public/euro-ce

%doc %{texmfdist}/doc/fonts/fge
%{texmfdist}/fonts/source/public/fge
%{texmfdist}/fonts/map/dvips/fge
%{texmfdist}/fonts/tfm/public/fge
%{texmfdist}/fonts/type1/public/fge
%{texmfdist}/source/fonts/fge

%{texmfdist}/fonts/map/dvips/figbas
%{texmfdist}/fonts/afm/public/figbas
%{texmfdist}/fonts/type1/public/figbas
%{texmfdist}/fonts/tfm/public/figbas

%{texmfdist}/fonts/map/dvips/foekfont
%{texmfdist}/fonts/tfm/public/foekfont
%{texmfdist}/fonts/type1/public/foekfont

%doc %{texmfdist}/doc/fonts/fonetika
%{texmfdist}/fonts/afm/public/fonetika
%{texmfdist}/fonts/map/dvips/fonetika
%{texmfdist}/fonts/tfm/public/fonetika
%{texmfdist}/fonts/type1/public/fonetika

%doc %{texmfdist}/doc/fonts/fourier
%{texmfdist}/fonts/afm/public/fourier
%{texmfdist}/fonts/map/dvips/fourier
%{texmfdist}/fonts/tfm/public/fourier
%{texmfdist}/fonts/type1/public/fourier
%{texmfdist}/fonts/vf/public/fourier
%{texmfdist}/source/fonts/fourier

%doc %{texmfdist}/doc/fonts/fouriernc
%{texmfdist}/fonts/afm/public/fouriernc
%{texmfdist}/fonts/tfm/public/fouriernc
%{texmfdist}/fonts/vf/public/fouriernc

%doc %{texmfdist}/doc/fonts/frcursive
%{texmfdist}/fonts/tfm/public/frcursive

%doc %{texmfdist}/doc/fonts/genealogy
%{texmfdist}/fonts/source/public/genealogy
%{texmfdist}/fonts/tfm/public/genealogy

%{texmfdist}/source/fonts/gentium
%{texmfdist}/fonts/afm/public/gentium
%{texmfdist}/fonts/enc/dvips/gentium
%{texmfdist}/fonts/map/pdftex/gentium
%{texmfdist}/fonts/tfm/public/gentium

%doc %{texmfdist}/doc/fonts/gfsartemisia
%{texmfdist}/fonts/afm/public/gfsartemisia
%{texmfdist}/fonts/enc/dvips/gfsartemisia
%{texmfdist}/fonts/map/dvips/gfsartemisia
%{texmfdist}/fonts/opentype/public/gfsartemisia
%{texmfdist}/fonts/tfm/public/gfsartemisia
%{texmfdist}/fonts/type1/public/gfsartemisia
%{texmfdist}/fonts/vf/public/gfsartemisia

%doc %{texmfdist}/doc/fonts/gfsbaskerville
%{texmfdist}/fonts/afm/public/gfsbaskerville
%{texmfdist}/fonts/enc/dvips/gfsbaskerville
%{texmfdist}/fonts/map/dvips/gfsbaskerville
%{texmfdist}/fonts/opentype/public/gfsbaskerville
%{texmfdist}/fonts/tfm/public/gfsbaskerville
%{texmfdist}/fonts/type1/public/gfsbaskerville
%{texmfdist}/fonts/vf/public/gfsbaskerville

%doc %{texmfdist}/doc/fonts/gfsbodoni
%{texmfdist}/fonts/afm/public/gfsbodoni
%{texmfdist}/fonts/enc/dvips/gfsbodoni
%{texmfdist}/fonts/map/dvips/gfsbodoni
%{texmfdist}/fonts/opentype/public/gfsbodoni
%{texmfdist}/fonts/tfm/public/gfsbodoni
%{texmfdist}/fonts/type1/public/gfsbodoni
%{texmfdist}/fonts/vf/public/gfsbodoni

%doc %{texmfdist}/doc/fonts/gfscomplutum
%{texmfdist}/fonts/afm/public/gfscomplutum
%{texmfdist}/fonts/enc/dvips/gfscomplutum
%{texmfdist}/fonts/map/dvips/gfscomplutum
%{texmfdist}/fonts/opentype/public/gfscomplutum
%{texmfdist}/fonts/tfm/public/gfscomplutum
%{texmfdist}/fonts/type1/public/gfscomplutum
%{texmfdist}/fonts/vf/public/gfscomplutum

%doc %{texmfdist}/doc/fonts/gfsdidot
%{texmfdist}/fonts/afm/public/gfsdidot
%{texmfdist}/fonts/enc/dvips/gfsdidot
%{texmfdist}/fonts/map/dvips/gfsdidot
%{texmfdist}/fonts/opentype/public/gfsdidot
%{texmfdist}/fonts/tfm/public/gfsdidot
%{texmfdist}/fonts/type1/public/gfsdidot
%{texmfdist}/fonts/vf/public/gfsdidot

%doc %{texmfdist}/doc/fonts/gfsneohellenic
%{texmfdist}/fonts/afm/public/gfsneohellenic
%{texmfdist}/fonts/enc/dvips/gfsneohellenic
%{texmfdist}/fonts/map/dvips/gfsneohellenic
%{texmfdist}/fonts/opentype/public/gfsneohellenic
%{texmfdist}/fonts/tfm/public/gfsneohellenic
%{texmfdist}/fonts/type1/public/gfsneohellenic
%{texmfdist}/fonts/vf/public/gfsneohellenic

%doc %{texmfdist}/doc/fonts/gfsporson
%{texmfdist}/fonts/afm/public/gfsporson
%{texmfdist}/fonts/enc/dvips/gfsporson
%{texmfdist}/fonts/map/dvips/gfsporson
%{texmfdist}/fonts/opentype/public/gfsporson
%{texmfdist}/fonts/tfm/public/gfsporson
%{texmfdist}/fonts/type1/public/gfsporson
%{texmfdist}/fonts/vf/public/gfsporson

%doc %{texmfdist}/doc/fonts/gfssolomos
%{texmfdist}/fonts/afm/public/gfssolomos
%{texmfdist}/fonts/enc/dvips/gfssolomos
%{texmfdist}/fonts/map/dvips/gfssolomos
%{texmfdist}/fonts/opentype/public/gfssolomos
%{texmfdist}/fonts/tfm/public/gfssolomos
%{texmfdist}/fonts/type1/public/gfssolomos
%{texmfdist}/fonts/vf/public/gfssolomos

%doc %{texmfdist}/doc/fonts/greenpoint
%{texmfdist}/fonts/source/public/greenpoint
%{texmfdist}/fonts/tfm/public/greenpoint

%doc %{texmfdist}/doc/fonts/grotesq
%{texmfdist}/fonts/map/dvips/grotesq

%{texmfdist}/fonts/source/public/hands
%{texmfdist}/fonts/tfm/public/hands

%{texmfdist}/fonts/afm/jmn
%{texmfdist}/fonts/tfm/jmn
%{texmfdist}/fonts/type1/jmn

%{texmfdist}/fonts/map/dvips/helvetic

%doc %{texmfdist}/doc/fonts/hfbright
%{texmfdist}/fonts/afm/public/hfbright
%{texmfdist}/fonts/enc/dvips/hfbright
%{texmfdist}/fonts/map/dvips/hfbright
%{texmfdist}/fonts/type1/public/hfbright

%doc %{texmfdist}/doc/fonts/hfoldsty
%{texmfdist}/fonts/tfm/public/hfoldsty
%{texmfdist}/fonts/vf/public/hfoldsty
%{texmfdist}/source/fonts/hfoldsty

%doc %{texmfdist}/doc/fonts/ibygrk
%{texmfdist}/tex/generic/ibygrk
%{texmfdist}/fonts/afm/public/ibygrk
%{texmfdist}/fonts/enc/dvips/ibygrk
%{texmfdist}/fonts/map/dvips/ibygrk
%{texmfdist}/fonts/source/public/ibygrk
%{texmfdist}/fonts/tfm/public/ibygrk
%{texmfdist}/fonts/type1/public/ibygrk

%doc %{texmfdist}/doc/fonts/ifsym
%{texmfdist}/fonts/source/public/ifsym
%{texmfdist}/fonts/tfm/public/ifsym

%{texmfdist}/fonts/opentype/public/inconsolata
%{texmfdist}/fonts/map/dvips/inconsolata
%{texmfdist}/fonts/tfm/public/inconsolata
%{texmfdist}/fonts/type1/public/inconsolata
%{texmfdist}/fonts/enc/dvips/inconsolata

%doc %{texmfdist}/doc/fonts/initials
%{texmfdist}/fonts/afm/public/initials
%{texmfdist}/fonts/map/dvips/initials
%{texmfdist}/fonts/tfm/public/initials
%{texmfdist}/fonts/type1/public/initials

%doc %{texmfdist}/doc/fonts/iwona
%{texmfdist}/fonts/enc/dvips/iwona
%{texmfdist}/fonts/map/dvips/iwona

%{texmfdist}/fonts/enc/dvips/jmn
%{texmfdist}/fonts/map/dvips/jmn

%{texmfdist}/fonts/afm/public/kerkis
%{texmfdist}/fonts/enc/dvips/kerkis
%{texmfdist}/fonts/map/dvips/kerkis
%{texmfdist}/fonts/tfm/public/kerkis
%{texmfdist}/fonts/type1/public/kerkis
%{texmfdist}/fonts/vf/public/kerkis

%doc %{texmfdist}/doc/fonts/kixfont
%{texmfdist}/fonts/source/public/kixfont
%{texmfdist}/fonts/tfm/public/kixfont

%doc %{texmfdist}/doc/fonts/kurier
%{texmfdist}/fonts/enc/dvips/kurier
%{texmfdist}/fonts/map/dvips/kurier
%doc %{texmfdist}/doc/fonts/levy
%{texmfdist}/fonts/source/public/levy

%doc %{texmfdist}/doc/fonts/lfb
%{texmfdist}/fonts/source/public/lfb
%{texmfdist}/fonts/tfm/public/lfb

%doc %{texmfdist}/doc/fonts/libertine
%{texmfdist}/fonts/enc/dvips/libertine
%{texmfdist}/fonts/map/dvips/libertine
%{texmfdist}/fonts/tfm/public/libertine
%{texmfdist}/fonts/type1/public/libertine
%{texmfdist}/fonts/vf/public/libertine
%{texmfdist}/fonts/opentype/public/libertine

%doc %{texmfdist}/doc/fonts/linearA
%{texmfdist}/fonts/afm/public/linearA
%{texmfdist}/fonts/map/dvips/linearA
%{texmfdist}/fonts/tfm/public/linearA
%{texmfdist}/fonts/type1/public/linearA
%{texmfdist}/source/fonts/linearA

%{texmfdist}/fonts/tfm/public/lithuanian

%doc %{texmfdist}/doc/fonts/lxfonts
%{texmfdist}/fonts/map/dvips/lxfonts
%{texmfdist}/fonts/source/public/lxfonts
%{texmfdist}/fonts/tfm/public/lxfonts
%{texmfdist}/fonts/type1/public/lxfonts

%doc %{texmfdist}/doc/fonts/ly1
%{texmfdist}/fonts/map/dvips/ly1

%{texmfdist}/fonts/map/dvips/manfnt

%{texmfdist}/fonts/map/dvips/mathdesign

%{texmfdist}/fonts/tfm/public/mathpazo
%{texmfdist}/fonts/vf/public/mathpazo

%{texmfdist}/fonts/source/public/mathabx
%{texmfdist}/fonts/tfm/public/mathabx

%{texmfdist}/fonts/afm/mathdesign
%{texmfdist}/fonts/tfm/mathdesign
%{texmfdist}/fonts/type1/mathdesign
%{texmfdist}/fonts/vf/mathdesign

%{texmfdist}/fonts/enc/dvips/mnsymbol
%{texmfdist}/fonts/map/dvips/mnsymbol
%dir %{texmfdist}/fonts/map/vtex
%{texmfdist}/fonts/map/vtex/mnsymbol
%{texmfdist}/fonts/opentype/public/mnsymbol
%{texmfdist}/fonts/source/public/mnsymbol
%{texmfdist}/fonts/tfm/public/mnsymbol
%{texmfdist}/fonts/type1/public/mnsymbol

%{texmfdist}/fonts/map/dvips/montex
%{texmfdist}/fonts/source/public/montex
%{texmfdist}/fonts/tfm/public/montex
%{texmfdist}/fonts/type1/public/montex

%doc %{texmfdist}/doc/generic/musixtex
%doc %{texmfdist}/doc/fonts/musixtex-fonts
%{texmfdist}/fonts/map/dvips/musixtex-fonts
%{texmfdist}/fonts/source/public/musixtex-fonts
%{texmfdist}/fonts/tfm/public/musixtex-fonts
%{texmfdist}/fonts/type1/public/musixtex-fonts

%{texmfdist}/fonts/source/public/mxedruli
%{texmfdist}/fonts/tfm/public/mxedruli

%{texmfdist}/fonts/map/dvips/ncntrsbk

%doc %{texmfdist}/doc/fonts/nkarta
%{texmfdist}/fonts/source/public/nkarta
%{texmfdist}/fonts/tfm/public/nkarta

%{texmfdist}/fonts/tfm/public/norasi-c90

%{texmfdist}/fonts/afm/public/ocherokee
%{texmfdist}/fonts/map/dvips/ocherokee
%{texmfdist}/fonts/ofm/public/ocherokee
%{texmfdist}/fonts/ovf/public/ocherokee
%{texmfdist}/fonts/ovp/public/ocherokee
%{texmfdist}/fonts/tfm/public/ocherokee
%{texmfdist}/fonts/type1/public/ocherokee

%{texmfdist}/fonts/source/public/ogham
%{texmfdist}/fonts/tfm/public/ogham

%doc %{texmfdist}/doc/fonts/oinuit
%{texmfdist}/fonts/map/dvips/oinuit
%{texmfdist}/fonts/ofm/public/oinuit
%{texmfdist}/fonts/ovf/public/oinuit
%{texmfdist}/fonts/tfm/public/oinuit
%{texmfdist}/fonts/type1/public/oinuit

%{texmfdist}/fonts/source/public/orkhun
%{texmfdist}/fonts/tfm/public/orkhun

%{texmfdist}/fonts/ofm/public/otibet
%{texmfdist}/fonts/ovf/public/otibet
%{texmfdist}/fonts/ovp/public/otibet
%{texmfdist}/fonts/source/public/otibet
%{texmfdist}/fonts/tfm/public/otibet

%doc %{texmfdist}/doc/fonts/pacioli
%{texmfdist}/fonts/source/public/pacioli
%{texmfdist}/fonts/tfm/public/pacioli

%{texmfdist}/fonts/map/dvips/palatino

%doc %{texmfdist}/doc/fonts/phaistos
%{texmfdist}/fonts/afm/public/phaistos
%{texmfdist}/fonts/map/dvips/phaistos
%{texmfdist}/fonts/opentype/public/phaistos
%{texmfdist}/fonts/tfm/public/phaistos
%{texmfdist}/fonts/type1/public/phaistos
%{texmfdist}/source/fonts/phaistos

%{texmfdist}/fonts/opentype/public/philokalia

%doc %{texmfdist}/doc/fonts/phonetic
%{texmfdist}/fonts/source/public/phonetic
%{texmfdist}/fonts/tfm/public/phonetic

%{texmfdist}/fonts/source/public/pigpen
%{texmfdist}/fonts/tfm/public/pigpen
%{texmfdist}/fonts/type1/public/pigpen


%{texmfdist}/fonts/source/public/punk
%{texmfdist}/fonts/tfm/public/punk

%{texmfdist}/fonts/source/public/recycle
%{texmfdist}/fonts/tfm/public/recycle
%{texmfdist}/fonts/type1/public/recycle

%{texmfdist}/fonts/tfm/public/relenc
%{texmfdist}/fonts/vf/public/relenc

%{texmfdist}/fonts/map/dvips/sanskrit
%{texmfdist}/fonts/source/public/sanskrit
%{texmfdist}/fonts/tfm/public/sanskrit
%{texmfdist}/fonts/type1/public/sanskrit

%{texmfdist}/fonts/source/public/sauter

%doc %{texmfdist}/doc/fonts/semaphor
%{texmfdist}/fonts/afm/public/semaphor
%{texmfdist}/fonts/enc/dvips/semaphor
%{texmfdist}/fonts/map/dvips/semaphor
%{texmfdist}/fonts/opentype/public/semaphor
%{texmfdist}/fonts/source/public/semaphor
%{texmfdist}/fonts/tfm/public/semaphor
%{texmfdist}/fonts/type1/public/semaphor

%{texmfdist}/fonts/source/public/shuffle
%{texmfdist}/fonts/tfm/public/shuffle

%doc %{texmfdist}/doc/fonts/skaknew
%{texmfdist}/fonts/afm/public/skaknew
%{texmfdist}/fonts/map/dvips/skaknew
%{texmfdist}/fonts/tfm/public/skaknew
%{texmfdist}/fonts/type1/public/skaknew
%{texmfdist}/fonts/opentype/public/skaknew

%{texmfdist}/fonts/source/public/skull

%doc %{texmfdist}/doc/fonts/staves
%{texmfdist}/fonts/map/dvips/staves
%{texmfdist}/fonts/tfm/public/staves
%{texmfdist}/fonts/type1/public/staves

%{texmfdist}/fonts/map/dvips/stmaryrd
%{texmfdist}/fonts/source/public/stmaryrd

%{texmfdist}/fonts/map/dvips/symbol

%{texmfdist}/fonts/afm/public/tabvar
%{texmfdist}/fonts/map/dvips/tabvar
%{texmfdist}/fonts/tfm/public/tabvar
%{texmfdist}/fonts/type1/public/tabvar


%{texmfdist}/fonts/source/public/tapir
%{texmfdist}/fonts/type1/public/tapir

%{texmfdist}/fonts/enc/dvips/tengwarscript
%{texmfdist}/fonts/map/dvips/tengwarscript
%{texmfdist}/fonts/tfm/public/tengwarscript
%{texmfdist}/fonts/vf/public/tengwarscript

%doc %{texmfdist}/doc/fonts/tex-gyre
%{texmfdist}/fonts/afm/public/tex-gyre
%{texmfdist}/fonts/enc/dvips/tex-gyre
%{texmfdist}/fonts/map/dvips/tex-gyre
%{texmfdist}/fonts/opentype/public/tex-gyre
%{texmfdist}/fonts/tfm/public/tex-gyre
%{texmfdist}/fonts/type1/public/tex-gyre

%{texmfdist}/fonts/map/dvips/times

%doc %{texmfdist}/doc/fonts/tipa
%{texmfdist}/fonts/map/dvips/tipa
%{texmfdist}/fonts/source/public/tipa
%{texmfdist}/fonts/tfm/public/tipa
%{texmfdist}/fonts/type1/public/tipa

%{texmfdist}/fonts/afm/public/trajan
%{texmfdist}/fonts/map/dvips/trajan
%{texmfdist}/fonts/tfm/public/trajan
%{texmfdist}/fonts/type1/public/trajan


%{texmfdist}/fonts/map/dvips/uhc

%{texmfdist}/fonts/opentype/public/umtypewriter

%doc %{texmfdist}/doc/fonts/universa
%{texmfdist}/fonts/source/public/universa
%{texmfdist}/fonts/tfm/public/universa
%{texmfdist}/source/fonts/universa

%{texmfdist}/fonts/afm/public/velthuis
%{texmfdist}/fonts/map/dvips/velthuis
%{texmfdist}/fonts/source/public/velthuis
%{texmfdist}/fonts/tfm/public/velthuis
%{texmfdist}/fonts/type1/public/velthuis


%{texmfdist}/fonts/map/dvips/wadalab

%doc %{texmfdist}/doc/fonts/wasy
%{texmfdist}/fonts/afm/public/wasy
%{texmfdist}/fonts/map/dvips/wasy
%{texmfdist}/fonts/type1/public/wasy

%{texmfdist}/fonts/source/public/wnri
%{texmfdist}/fonts/tfm/public/wnri

%{texmfdist}/fonts/source/public/wsuipa
%{texmfdist}/fonts/tfm/public/wsuipa

%{texmfdist}/fonts/source/public/xbmc
%{texmfdist}/fonts/tfm/public/xbmc

%doc %{texmfdist}/doc/fonts/xq
%{texmfdist}/fonts/source/public/xq
%{texmfdist}/fonts/tfm/public/xq

%{texmfdist}/fonts/source/public/yannisgr

%{texmfdist}/fonts/map/dvips/yhmath
%{texmfdist}/fonts/source/public/yhmath
%{texmfdist}/fonts/tfm/public/yhmath
%{texmfdist}/fonts/type1/public/yhmath
%{texmfdist}/fonts/vf/public/yhmath

%{texmfdist}/fonts/map/dvips/zapfchan
%{texmfdist}/fonts/tfm/urw35vf

%{texmfdist}/fonts/map/dvips/zapfding

%doc %{texmfdist}/doc/fonts/zhmetrics
%{texmfdist}/fonts/tfm/zhmetrics
%{texmfdist}/source/fonts/zhmetrics

%files -n texlive-fonts-omega
# duplicate?
%defattr(644,root,root,755)
%{texmfdist}/fonts/ofm/public/omega
%{texmfdist}/fonts/afm/public/omega
%{texmfdist}/fonts/ovp/public/omega
%{texmfdist}/fonts/tfm/public/omega
%{texmfdist}/fonts/ovf/public/omega
%{texmfdist}/fonts/map/dvips/omega

%files -n texlive-fonts-pl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pl
%{texmfdist}/fonts/source/public/pl
%{texmfdist}/fonts/type1/public/pl
%{texmfdist}/fonts/afm/public/pl
%{texmfdist}/fonts/enc/dvips/pl
%{texmfdist}/fonts/tfm/public/pl
%{texmfdist}/fonts/map/dvips/pl

%files -n texlive-fonts-rsfs
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/rsfs
%doc %{texmfdist}/doc/latex/calrsfs
%{texmfdist}/tex/latex/calrsfs
%{texmfdist}/fonts/source/public/rsfs
%{texmfdist}/fonts/tfm/public/rsfs
%{texmfdist}/fonts/afm/public/rsfs
%{texmfdist}/fonts/type1/public/rsfs
%{texmfdist}/fonts/map/dvips/rsfs


%files -n texlive-fonts-stmaryrd
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/stmaryrd
%{texmfdist}/source/fonts/stmaryrd
%{texmfdist}/fonts/tfm/public/stmaryrd

%files -n texlive-fonts-uhc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/uhc
%{texmfdist}/fonts/afm/uhc
%{texmfdist}/fonts/tfm/uhc
%{texmfdist}/fonts/vf/uhc

%files -n texlive-fonts-urw
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/urw
%{texmfdist}/fonts/tfm/urw
%{texmfdist}/fonts/vf/urw

%files -n texlive-fonts-vnr
# merge with texlive-latex-lang-vietnam?
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/vntex/vnr

%files -n texlive-fonts-urw35vf
%defattr(644,root,root,755)
%{texmfdist}/fonts/vf/urw35vf

%files -n texlive-fonts-wadalab
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/wadalab
%{texmfdist}/fonts/afm/wadalab
%{texmfdist}/fonts/tfm/wadalab
%{texmfdist}/fonts/vf/wadalab

%files -n texlive-fonts-wasy
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/wasy
%{texmfdist}/fonts/tfm/public/wasy

%files -n texlive-fonts-xypic
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/public/xypic
%{texmfdist}/fonts/map/dvips/xypic
%{texmfdist}/fonts/source/public/xypic
%{texmfdist}/fonts/tfm/public/xypic

%files -n texlive-fonts-type1-antt
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/antt

%files -n texlive-fonts-type1-arphic
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/arphic

%files -n texlive-fonts-type1-belleek
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/belleek
%{texmfdist}/source/latex/belleek
%{texmfdist}/fonts/type1/public/belleek
%{texmfdist}/fonts/map/dvips/belleek

%files -n texlive-fonts-type1-bitstream
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/bitstrea

%files -n texlive-fonts-type1-cc-pl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/cc-pl
%{texmfdist}/fonts/type1/public/cc-pl

%files -n texlive-fonts-type1-cs
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/cs

%files -n texlive-fonts-type1-eurosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/eurosym

%files -n texlive-fonts-type1-hoekwater
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/hoekwater

%files -n texlive-fonts-type1-fpl
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/fpl
%{texmfdist}/fonts/afm/public/fpl
%{texmfdist}/fonts/type1/public/fpl
%{texmfdist}/source/fonts/fpl

%files -n texlive-fonts-type1-mathpazo
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/public/mathpazo
%{texmfdist}/fonts/type1/public/mathpazo

%files -n texlive-fonts-type1-omega
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/omega

%files -n texlive-fonts-type1-uhc
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/uhc

%files -n texlive-fonts-type1-urw
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/urw

%files -n texlive-fonts-type1-wadalab
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/wadalab

%files -n texlive-fonts-type1-xypic
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/xypic

%files unsorted
%defattr(644,root,root,755)
%dir %{texmfdist}/doc/pdftex/thanh
%dir %{texmfdist}/scripts/texlive/lua
%dir %{texmfdist}/tex/texsis/config

%{texmfdist}/README
%{texmfdist}/bibtex/bib/abntex2
%{texmfdist}/bibtex/bib/oberdiek
%{texmfdist}/bibtex/bst/abntex2
%{texmfdist}/bibtex/bst/adfathesis
%{texmfdist}/bibtex/bst/aomart
%{texmfdist}/bibtex/bst/bgteubner
%{texmfdist}/bibtex/bst/bibexport
%{texmfdist}/bibtex/bst/cascadilla
%{texmfdist}/bibtex/bst/chet
%{texmfdist}/bibtex/bst/chscite
%{texmfdist}/bibtex/bst/cmpj
%{texmfdist}/bibtex/bst/dlfltxb
%{texmfdist}/bibtex/bst/francais-bst
%{texmfdist}/bibtex/bst/ksfh_nat
%{texmfdist}/bibtex/bst/listbib
%{texmfdist}/bibtex/bst/multibibliography/chronological.bst
%{texmfdist}/bibtex/bst/pnas2009/pnas2009.bst
%{texmfdist}/bibtex/bst/przechlewski-book/papalike.bst
%{texmfdist}/bibtex/bst/resphilosophica/resphilosophica.bst
%{texmfdist}/bibtex/bst/sapthesis/sapthesis.bst
%{texmfdist}/bibtex/bst/uestcthesis/uestcthesis.bst
%{texmfdist}/bibtex/bst/unamthesis/UNAMThesis.bst
%{texmfdist}/bibtex/bst/vak/vak.bst
%{texmfdist}/bibtex/csf/disser/cp1251lc.csf
%{texmfdist}/bibtex/csf/persian-bib/cp1256fa.csf
%{texmfdist}/chktex/chktexrc
%{texmfdist}/doc/aleph/base
%{texmfdist}/doc/bg5conv
%{texmfdist}/doc/bibtex/apacite
%{texmfdist}/doc/bibtex/babelbib
%{texmfdist}/doc/bibtex/base
%{texmfdist}/doc/bibtex/bib-fr
%{texmfdist}/doc/bibtex/biber
%{texmfdist}/doc/bibtex/bibexport
%{texmfdist}/doc/bibtex/chicago-annote
%{texmfdist}/doc/bibtex/francais-bst
%{texmfdist}/doc/bibtex/inlinebib
%{texmfdist}/doc/bibtex/sort-by-letters
%{texmfdist}/doc/bibtex/tamethebeast
%{texmfdist}/doc/bibtex/urlbst
%{texmfdist}/doc/bibtex/vak
%{texmfdist}/doc/bibtex8
%{texmfdist}/doc/bibtexu
%{texmfdist}/doc/cef5conv
%{texmfdist}/doc/cefconv/
%{texmfdist}/doc/cefsconv
%{texmfdist}/doc/chktex
%{texmfdist}/doc/cstex
%{texmfdist}/doc/dvipng
%{texmfdist}/doc/extconv
%{texmfdist}/doc/fonts/Type1fonts
%{texmfdist}/doc/fonts/adforn
%{texmfdist}/doc/fonts/adfsymbols
%{texmfdist}/doc/fonts/aecc
%{texmfdist}/doc/fonts/amiri
%{texmfdist}/doc/fonts/ascii-font
%{texmfdist}/doc/fonts/bartel-chess-fonts
%{texmfdist}/doc/fonts/baskervald
%{texmfdist}/doc/fonts/bbold-type1
%{texmfdist}/doc/fonts/bengali
%{texmfdist}/doc/fonts/berenisadf
%{texmfdist}/doc/fonts/bguq
%{texmfdist}/doc/fonts/boondox
%{texmfdist}/doc/fonts/brushscr
%{texmfdist}/doc/fonts/cabin
%{texmfdist}/doc/fonts/calligra-type1
%{texmfdist}/doc/fonts/cantarell
%{texmfdist}/doc/fonts/ccicons
%{texmfdist}/doc/fonts/cfr-lm
%{texmfdist}/doc/fonts/cherokee
%{texmfdist}/doc/fonts/chess
%{texmfdist}/doc/fonts/cm-lgc
%{texmfdist}/doc/fonts/cm-unicode
%{texmfdist}/doc/fonts/cmbright
%{texmfdist}/doc/fonts/cmll
%{texmfdist}/doc/fonts/comfortaa
%{texmfdist}/doc/fonts/concmath-fonts
%{texmfdist}/doc/fonts/countriesofeurope
%{texmfdist}/doc/fonts/courier-scaled
%{texmfdist}/doc/fonts/dejavu
%{texmfdist}/doc/fonts/dingbat
%{texmfdist}/doc/fonts/dozenal
%{texmfdist}/doc/fonts/droid
%{texmfdist}/doc/fonts/dutchcal
%{texmfdist}/doc/fonts/ebgaramond
%{texmfdist}/doc/fonts/electrum
%{texmfdist}/doc/fonts/enc/c90
%{texmfdist}/doc/fonts/esstix
%{texmfdist}/doc/fonts/fdsymbol
%{texmfdist}/doc/fonts/figbas
%{texmfdist}/doc/fonts/fonts-tlwg
%{texmfdist}/doc/fonts/gentium
%{texmfdist}/doc/fonts/gnu-freefont
%{texmfdist}/doc/fonts/go
%{texmfdist}/doc/fonts/greektex
%{texmfdist}/doc/fonts/hacm
%{texmfdist}/doc/fonts/inconsolata
%{texmfdist}/doc/fonts/ipaex
%{texmfdist}/doc/fonts/ipaex-type1
%{texmfdist}/doc/fonts/jablantile
%{texmfdist}/doc/fonts/japanese-otf
%{texmfdist}/doc/fonts/japanese-otf-uptex
%{texmfdist}/doc/fonts/jfontmaps
%{texmfdist}/doc/fonts/junicode
%{texmfdist}/doc/fonts/latex-fonts
%{texmfdist}/doc/fonts/lato
%{texmfdist}/doc/fonts/librebaskerville
%{texmfdist}/doc/fonts/libris
%{texmfdist}/doc/fonts/lm
%{texmfdist}/doc/fonts/lm-math
%{texmfdist}/doc/fonts/mathabx
%{texmfdist}/doc/fonts/mathabx-type1
%{texmfdist}/doc/fonts/mathdesign
%{texmfdist}/doc/fonts/mdsymbol
%{texmfdist}/doc/fonts/memdesign
%{texmfdist}/doc/fonts/metafont-beginners
%{texmfdist}/doc/fonts/mxedruli
%{texmfdist}/doc/fonts/nanumtype1
%{texmfdist}/doc/fonts/newpx
%{texmfdist}/doc/fonts/ocr-b-outline
%{texmfdist}/doc/fonts/ogham
%{texmfdist}/doc/fonts/oldlatin
%{texmfdist}/doc/fonts/oldstandard
%{texmfdist}/doc/fonts/opensans
%{texmfdist}/doc/fonts/orkhun
%{texmfdist}/doc/fonts/paratype
%{texmfdist}/doc/fonts/persian-modern
%{texmfdist}/doc/fonts/poltawski
%{texmfdist}/doc/fonts/prodint
%{texmfdist}/doc/fonts/punk
%{texmfdist}/doc/fonts/punknova
%{texmfdist}/doc/fonts/pxfonts
%{texmfdist}/doc/fonts/pxtxalfa
%{texmfdist}/doc/fonts/quattrocento
%{texmfdist}/doc/fonts/recycle
%{texmfdist}/doc/fonts/romande
%{texmfdist}/doc/fonts/rsfso
%{texmfdist}/doc/fonts/sansmathaccent
%{texmfdist}/doc/fonts/sansmathfonts
%{texmfdist}/doc/fonts/schulschriften
%{texmfdist}/doc/fonts/starfont
%{texmfdist}/doc/fonts/stix
%{texmfdist}/doc/fonts/superiors
%{texmfdist}/doc/fonts/tapir
%{texmfdist}/doc/fonts/tex-gyre-math
%{texmfdist}/doc/fonts/tfrupee
%{texmfdist}/doc/fonts/txfontsb
%{texmfdist}/doc/fonts/urwchancal
%{texmfdist}/doc/fonts/venturisadf
%{texmfdist}/doc/fonts/wnri
%{texmfdist}/doc/fonts/wsuipa
%{texmfdist}/doc/fonts/xits
%{texmfdist}/doc/fonts/yannisgr
%{texmfdist}/doc/generic/2up
%{texmfdist}/doc/generic/abbr
%{texmfdist}/doc/generic/babel-albanian
%{texmfdist}/doc/generic/babel-bahasa
%{texmfdist}/doc/generic/babel-basque
%{texmfdist}/doc/generic/babel-breton
%{texmfdist}/doc/generic/babel-bulgarian
%{texmfdist}/doc/generic/babel-catalan
%{texmfdist}/doc/generic/babel-croatian
%{texmfdist}/doc/generic/babel-czech
%{texmfdist}/doc/generic/babel-danish
%{texmfdist}/doc/generic/babel-dutch
%{texmfdist}/doc/generic/babel-english
%{texmfdist}/doc/generic/babel-esperanto
%{texmfdist}/doc/generic/babel-estonian
%{texmfdist}/doc/generic/babel-finnish
%{texmfdist}/doc/generic/babel-french
%{texmfdist}/doc/generic/babel-friulan
%{texmfdist}/doc/generic/babel-galician
%{texmfdist}/doc/generic/babel-german
%{texmfdist}/doc/generic/babel-greek
%{texmfdist}/doc/generic/babel-hebrew
%{texmfdist}/doc/generic/babel-icelandic
%{texmfdist}/doc/generic/babel-interlingua
%{texmfdist}/doc/generic/babel-irish
%{texmfdist}/doc/generic/babel-italian
%{texmfdist}/doc/generic/babel-kurmanji
%{texmfdist}/doc/generic/babel-latin
%{texmfdist}/doc/generic/babel-norsk
%{texmfdist}/doc/generic/babel-piedmontese
%{texmfdist}/doc/generic/babel-polish
%{texmfdist}/doc/generic/babel-portuges
%{texmfdist}/doc/generic/babel-romanian
%{texmfdist}/doc/generic/babel-romansh
%{texmfdist}/doc/generic/babel-russian
%{texmfdist}/doc/generic/babel-samin
%{texmfdist}/doc/generic/babel-scottish
%{texmfdist}/doc/generic/babel-serbian
%{texmfdist}/doc/generic/babel-serbianc
%{texmfdist}/doc/generic/babel-slovak
%{texmfdist}/doc/generic/babel-slovenian
%{texmfdist}/doc/generic/babel-sorbian
%{texmfdist}/doc/generic/babel-spanish
%{texmfdist}/doc/generic/babel-swedish
%{texmfdist}/doc/generic/babel-thai
%{texmfdist}/doc/generic/babel-turkish
%{texmfdist}/doc/generic/babel-ukraineb
%{texmfdist}/doc/generic/babel-welsh
%{texmfdist}/doc/generic/bitelist
%{texmfdist}/doc/generic/catcodes
%{texmfdist}/doc/generic/chemfig
%{texmfdist}/doc/generic/chronosys
%{texmfdist}/doc/generic/commado
%{texmfdist}/doc/generic/doc-pictex
%{texmfdist}/doc/generic/dowith
%{texmfdist}/doc/generic/dratex
%{texmfdist}/doc/generic/ean
%{texmfdist}/doc/generic/elhyphen
%{texmfdist}/doc/generic/fenixpar
%{texmfdist}/doc/generic/fntproof
%{texmfdist}/doc/generic/formlett
%{texmfdist}/doc/generic/frame
%{texmfdist}/doc/generic/gates
%{texmfdist}/doc/generic/huhyphen
%{texmfdist}/doc/generic/langcode
%{texmfdist}/doc/generic/lecturer
%{texmfdist}/doc/generic/m-tx
%{texmfdist}/doc/generic/minifp
%{texmfdist}/doc/generic/mkjobtexmf
%{texmfdist}/doc/generic/navigator
%{texmfdist}/doc/generic/path
%{texmfdist}/doc/generic/petri-nets
%{texmfdist}/doc/generic/plainpkg
%{texmfdist}/doc/generic/pmx
%{texmfdist}/doc/generic/pst-fit
%{texmfdist}/doc/generic/pst-graphicx
%{texmfdist}/doc/generic/pst-ode
%{texmfdist}/doc/generic/pst-pulley
%{texmfdist}/doc/generic/pst-rubans
%{texmfdist}/doc/generic/pst-solarsystem
%{texmfdist}/doc/generic/pst-tools
%{texmfdist}/doc/generic/pst-tvz
%{texmfdist}/doc/generic/schemata
%{texmfdist}/doc/generic/systeme
%{texmfdist}/doc/generic/tds
%{texmfdist}/doc/generic/tex-ewd
%{texmfdist}/doc/generic/tex-ps/cmyk-hax
%{texmfdist}/doc/generic/tex-ps/poligraf
%{texmfdist}/doc/generic/tex-refs
%{texmfdist}/doc/generic/texapi
%{texmfdist}/doc/generic/upca
%{texmfdist}/doc/generic/voss-de
%{texmfdist}/doc/generic/xint
%{texmfdist}/doc/generic/xlop
%{texmfdist}/doc/generic/xstring
%{texmfdist}/doc/generic/xypic-tut-pt
%{texmfdist}/doc/hbf2gf
%{texmfdist}/doc/kpathsea
%{texmfdist}/doc/latex/GS1
%{texmfdist}/doc/latex/MemoirChapStyles
%{texmfdist}/doc/latex/abntex2
%{texmfdist}/doc/latex/abraces
%{texmfdist}/doc/latex/acro
%{texmfdist}/doc/latex/acroterm
%{texmfdist}/doc/latex/actuarialangle
%{texmfdist}/doc/latex/adfathesis
%{texmfdist}/doc/latex/adjmulticol
%{texmfdist}/doc/latex/adjustbox
%{texmfdist}/doc/latex/akktex
%{texmfdist}/doc/latex/anufinalexam
%{texmfdist}/doc/latex/aomart
%{texmfdist}/doc/latex/apa6
%{texmfdist}/doc/latex/apa6e
%{texmfdist}/doc/latex/appendixnumberbeamer
%{texmfdist}/doc/latex/apptools
%{texmfdist}/doc/latex/aramaic-serto
%{texmfdist}/doc/latex/articleingud
%{texmfdist}/doc/latex/aspectratio
%{texmfdist}/doc/latex/autonum
%{texmfdist}/doc/latex/autopdf
%{texmfdist}/doc/latex/b1encoding
%{texmfdist}/doc/latex/babel
%{texmfdist}/doc/latex/backnaur
%{texmfdist}/doc/latex/bashful
%{texmfdist}/doc/latex/basque-book
%{texmfdist}/doc/latex/basque-date
%{texmfdist}/doc/latex/bbding
%{texmfdist}/doc/latex/bchart
%{texmfdist}/doc/latex/beamer2thesis
%{texmfdist}/doc/latex/beameraudience
%{texmfdist}/doc/latex/beamersubframe
%{texmfdist}/doc/latex/beamertheme-upenn-bc
%{texmfdist}/doc/latex/beamerthemenirma
%{texmfdist}/doc/latex/bgreek
%{texmfdist}/doc/latex/bgteubner
%{texmfdist}/doc/latex/bhcexam
%{texmfdist}/doc/latex/biblatex-bwl
%{texmfdist}/doc/latex/biblatex-caspervector
%{texmfdist}/doc/latex/biblatex-chicago
%{texmfdist}/doc/latex/biblatex-fiwi
%{texmfdist}/doc/latex/biblatex-gost
%{texmfdist}/doc/latex/biblatex-ieee
%{texmfdist}/doc/latex/biblatex-juradiss
%{texmfdist}/doc/latex/biblatex-luh-ipw
%{texmfdist}/doc/latex/biblatex-mla
%{texmfdist}/doc/latex/biblatex-musuos
%{texmfdist}/doc/latex/biblatex-nejm
%{texmfdist}/doc/latex/biblatex-phys
%{texmfdist}/doc/latex/biblatex-publist
%{texmfdist}/doc/latex/biblatex-swiss-legal
%{texmfdist}/doc/latex/biblatex-trad
%{texmfdist}/doc/latex/bibleref-french
%{texmfdist}/doc/latex/bibleref-german
%{texmfdist}/doc/latex/bibleref-lds
%{texmfdist}/doc/latex/bibleref-mouth
%{texmfdist}/doc/latex/bibleref-parse
%{texmfdist}/doc/latex/bloques
%{texmfdist}/doc/latex/bodegraph
%{texmfdist}/doc/latex/bohr
%{texmfdist}/doc/latex/bold-extra
%{texmfdist}/doc/latex/bondgraph
%{texmfdist}/doc/latex/booktabs-de
%{texmfdist}/doc/latex/booktabs-fr
%{texmfdist}/doc/latex/bracketkey
%{texmfdist}/doc/latex/braids
%{texmfdist}/doc/latex/breakcites
%{texmfdist}/doc/latex/bropd
%{texmfdist}/doc/latex/bxbase
%{texmfdist}/doc/latex/bxdpx-beamer
%{texmfdist}/doc/latex/bxeepic
%{texmfdist}/doc/latex/bxjscls
%{texmfdist}/doc/latex/cachepic
%{texmfdist}/doc/latex/calcage
%{texmfdist}/doc/latex/calctab
%{texmfdist}/doc/latex/calculator
%{texmfdist}/doc/latex/cals
%{texmfdist}/doc/latex/calxxxx-yyyy
%{texmfdist}/doc/latex/canoniclayout
%{texmfdist}/doc/latex/captdef
%{texmfdist}/doc/latex/cascadilla
%{texmfdist}/doc/latex/catchfilebetweentags
%{texmfdist}/doc/latex/catoptions
%{texmfdist}/doc/latex/chemexec
%{texmfdist}/doc/latex/chemmacros
%{texmfdist}/doc/latex/chemnum
%{texmfdist}/doc/latex/chet
%{texmfdist}/doc/latex/chextras
%{texmfdist}/doc/latex/chkfloat
%{texmfdist}/doc/latex/chscite
%{texmfdist}/doc/latex/cjk-ko
%{texmfdist}/doc/latex/cjkpunct
%{texmfdist}/doc/latex/classics
%{texmfdist}/doc/latex/clipboard
%{texmfdist}/doc/latex/cmpica
%{texmfdist}/doc/latex/cmpj
%{texmfdist}/doc/latex/cmsd
%{texmfdist}/doc/latex/cmtiup
%{texmfdist}/doc/latex/codicefiscaleitaliano
%{texmfdist}/doc/latex/collcell
%{texmfdist}/doc/latex/collectbox
%{texmfdist}/doc/latex/colourchange
%{texmfdist}/doc/latex/concepts
%{texmfdist}/doc/latex/conteq
%{texmfdist}/doc/latex/contracard
%{texmfdist}/doc/latex/cookingsymbols
%{texmfdist}/doc/latex/coolthms
%{texmfdist}/doc/latex/copyrightbox
%{texmfdist}/doc/latex/coseoul
%{texmfdist}/doc/latex/counttexruns
%{texmfdist}/doc/latex/cprotect
%{texmfdist}/doc/latex/crbox
%{texmfdist}/doc/latex/csquotes-de
%{texmfdist}/doc/latex/csvsimple
%{texmfdist}/doc/latex/ctanify
%{texmfdist}/doc/latex/cutwin
%{texmfdist}/doc/latex/dashbox
%{texmfdist}/doc/latex/decimal
%{texmfdist}/doc/latex/decorule
%{texmfdist}/doc/latex/delim
%{texmfdist}/doc/latex/dhua
%{texmfdist}/doc/latex/diagbox
%{texmfdist}/doc/latex/dirtytalk
%{texmfdist}/doc/latex/documentation
%{texmfdist}/doc/latex/download
%{texmfdist}/doc/latex/drawstack
%{texmfdist}/doc/latex/droit-fr
%{texmfdist}/doc/latex/duotenzor
%{texmfdist}/doc/latex/dvgloss
%{texmfdist}/doc/latex/dynblocks
%{texmfdist}/doc/latex/easy-todo
%{texmfdist}/doc/latex/easyfig
%{texmfdist}/doc/latex/ebook
%{texmfdist}/doc/latex/edfnotes
%{texmfdist}/doc/latex/eiad-ltx
%{texmfdist}/doc/latex/einfuehrung
%{texmfdist}/doc/latex/ejpecp
%{texmfdist}/doc/latex/eledform
%{texmfdist}/doc/latex/eledmac
%{texmfdist}/doc/latex/elteikthesis
%{texmfdist}/doc/latex/emarks
%{texmfdist}/doc/latex/embrac
%{texmfdist}/doc/latex/endiagram
%{texmfdist}/doc/latex/enotez
%{texmfdist}/doc/latex/enumitem-zref
%{texmfdist}/doc/latex/eqell
%{texmfdist}/doc/latex/eqnarray
%{texmfdist}/doc/latex/esami
%{texmfdist}/doc/latex/etextools
%{texmfdist}/doc/latex/etoc
%{texmfdist}/doc/latex/etoolbox-de
%{texmfdist}/doc/latex/everyhook
%{texmfdist}/doc/latex/exceltex
%{texmfdist}/doc/latex/exsheets
%{texmfdist}/doc/latex/exsol
%{texmfdist}/doc/latex/factura
%{texmfdist}/doc/latex/fancytabs
%{texmfdist}/doc/latex/fast-diagram
%{texmfdist}/doc/latex/fbithesis
%{texmfdist}/doc/latex/fcltxdoc
%{texmfdist}/doc/latex/fdsymbol
%{texmfdist}/doc/latex/feynmp-auto
%{texmfdist}/doc/latex/fifinddo-info
%{texmfdist}/doc/latex/filedate
%{texmfdist}/doc/latex/fileinfo
%{texmfdist}/doc/latex/filemod
%{texmfdist}/doc/latex/finstrut
%{texmfdist}/doc/latex/fixltxhyph
%{texmfdist}/doc/latex/fixmetodonotes
%{texmfdist}/doc/latex/fjodor
%{texmfdist}/doc/latex/flipbook
%{texmfdist}/doc/latex/floatflt
%{texmfdist}/doc/latex/flowchart
%{texmfdist}/doc/latex/fnpct
%{texmfdist}/doc/latex/fnumprint
%{texmfdist}/doc/latex/foilhtml
%{texmfdist}/doc/latex/fontawesome
%{texmfdist}/doc/latex/fontaxes
%{texmfdist}/doc/latex/footnotebackref
%{texmfdist}/doc/latex/footnoterange
%{texmfdist}/doc/latex/foreign
%{texmfdist}/doc/latex/forest
%{texmfdist}/doc/latex/fragments
%{texmfdist}/doc/latex/frege
%{texmfdist}/doc/latex/fullwidth
%{texmfdist}/doc/latex/fundus-calligra
%{texmfdist}/doc/latex/fundus-sueterlin
%{texmfdist}/doc/latex/gamebook
%{texmfdist}/doc/latex/geometry-de
%{texmfdist}/doc/latex/germkorr
%{texmfdist}/doc/latex/geschichtsfrkl
%{texmfdist}/doc/latex/ghab
%{texmfdist}/doc/latex/gillcm
%{texmfdist}/doc/latex/gincltex
%{texmfdist}/doc/latex/gitinfo
%{texmfdist}/doc/latex/gmdoc-enhance
%{texmfdist}/doc/latex/gmp
%{texmfdist}/doc/latex/gmverse
%{texmfdist}/doc/latex/gradientframe
%{texmfdist}/doc/latex/grafcet
%{texmfdist}/doc/latex/greek-fontenc
%{texmfdist}/doc/latex/gridset
%{texmfdist}/doc/latex/gtrcrd
%{texmfdist}/doc/latex/guitlogo
%{texmfdist}/doc/latex/hardwrap
%{texmfdist}/doc/latex/harnon-cv
%{texmfdist}/doc/latex/hausarbeit-jura
%{texmfdist}/doc/latex/he-she
%{texmfdist}/doc/latex/here
%{texmfdist}/doc/latex/hf-tikz
%{texmfdist}/doc/latex/hletter
%{texmfdist}/doc/latex/hobby
%{texmfdist}/doc/latex/hobete
%{texmfdist}/doc/latex/horoscop
%{texmfdist}/doc/latex/hrefhide
%{texmfdist}/doc/latex/hvindex
%{texmfdist}/doc/latex/hypernat
%{texmfdist}/doc/latex/idxlayout
%{texmfdist}/doc/latex/ifetex
%{texmfdist}/doc/latex/ifnextok
%{texmfdist}/doc/latex/ifoddpage
%{texmfdist}/doc/latex/ifthenx
%{texmfdist}/doc/latex/iitem
%{texmfdist}/doc/latex/imakeidx
%{texmfdist}/doc/latex/impnattypo
%{texmfdist}/doc/latex/incgraph
%{texmfdist}/doc/latex/inputtrc
%{texmfdist}/doc/latex/interfaces
%{texmfdist}/doc/latex/interval
%{texmfdist}/doc/latex/invoice
%{texmfdist}/doc/latex/isotope
%{texmfdist}/doc/latex/issuulinks
%{texmfdist}/doc/latex/iwhdp
%{texmfdist}/doc/latex/jamtimes
%{texmfdist}/doc/latex/jlabels
%{texmfdist}/doc/latex/jvlisting
%{texmfdist}/doc/latex/kantlipsum
%{texmfdist}/doc/latex/kdgdocs
%{texmfdist}/doc/latex/keyreader
%{texmfdist}/doc/latex/keyval2e
%{texmfdist}/doc/latex/kix
%{texmfdist}/doc/latex/koma-moderncvclassic
%{texmfdist}/doc/latex/koma-script-examples
%{texmfdist}/doc/latex/koma-script-sfs
%{texmfdist}/doc/latex/ktv-texdata
%{texmfdist}/doc/latex/l2tabu-italian
%{texmfdist}/doc/latex/l3experimental
%{texmfdist}/doc/latex/l3kernel
%{texmfdist}/doc/latex/l3packages
%{texmfdist}/doc/latex/lapdf
%{texmfdist}/doc/latex/latex-bib-ex
%{texmfdist}/doc/latex/latex-brochure
%{texmfdist}/doc/latex/latex-tds
%{texmfdist}/doc/latex/latex2e-help-texinfo-spanish
%{texmfdist}/doc/latex/latex4wp
%{texmfdist}/doc/latex/latex4wp-it
%{texmfdist}/doc/latex/latexfileinfo-pkgs
%{texmfdist}/doc/latex/lcg
%{texmfdist}/doc/latex/leipzig
%{texmfdist}/doc/latex/lgrx
%{texmfdist}/doc/latex/libgreek
%{texmfdist}/doc/latex/linegoal
%{texmfdist}/doc/latex/lisp-on-tex
%{texmfdist}/doc/latex/listing
%{texmfdist}/doc/latex/lmake
%{texmfdist}/doc/latex/logbox
%{texmfdist}/doc/latex/logical-markup-utils
%{texmfdist}/doc/latex/logicpuzzle
%{texmfdist}/doc/latex/logreq
%{texmfdist}/doc/latex/longnamefilelist
%{texmfdist}/doc/latex/loops
%{texmfdist}/doc/latex/lpic
%{texmfdist}/doc/latex/lshort-czech
%{texmfdist}/doc/latex/lstaddons
%{texmfdist}/doc/latex/ltablex
%{texmfdist}/doc/latex/ltxdockit
%{texmfdist}/doc/latex/ltxkeys
%{texmfdist}/doc/latex/ltxnew
%{texmfdist}/doc/latex/ltxtools
%{texmfdist}/doc/latex/lualatex-doc-de
%{texmfdist}/doc/latex/macros2e
%{texmfdist}/doc/latex/makeshape
%{texmfdist}/doc/latex/mandi
%{texmfdist}/doc/latex/margbib
%{texmfdist}/doc/latex/marginfix
%{texmfdist}/doc/latex/matc3
%{texmfdist}/doc/latex/matc3mem
%{texmfdist}/doc/latex/math-e
%{texmfdist}/doc/latex/mathalfa
%{texmfdist}/doc/latex/mathastext
%{texmfdist}/doc/latex/mathspic
%{texmfdist}/doc/latex/mbenotes
%{texmfdist}/doc/latex/mdputu
%{texmfdist}/doc/latex/mdsymbol
%{texmfdist}/doc/latex/media9
%{texmfdist}/doc/latex/meetingmins
%{texmfdist}/doc/latex/memory
%{texmfdist}/doc/latex/menukeys
%{texmfdist}/doc/latex/metalogo
%{texmfdist}/doc/latex/microtype-de
%{texmfdist}/doc/latex/mil3
%{texmfdist}/doc/latex/mnotes
%{texmfdist}/doc/latex/moderntimeline
%{texmfdist}/doc/latex/modiagram
%{texmfdist}/doc/latex/monofill
%{texmfdist}/doc/latex/moreenum
%{texmfdist}/doc/latex/morefloats
%{texmfdist}/doc/latex/morehype
%{texmfdist}/doc/latex/morewrites
%{texmfdist}/doc/latex/mpgraphics
%{texmfdist}/doc/latex/msu-thesis
%{texmfdist}/doc/latex/multibibliography
%{texmfdist}/doc/latex/multienv
%{texmfdist}/doc/latex/multiexpand
%{texmfdist}/doc/latex/musixguit
%{texmfdist}/doc/latex/musuos
%{texmfdist}/doc/latex/mversion
%{texmfdist}/doc/latex/mwe
%{texmfdist}/doc/latex/mychemistry
%{texmfdist}/doc/latex/mycv
%{texmfdist}/doc/latex/mylatexformat
%{texmfdist}/doc/latex/nameauth
%{texmfdist}/doc/latex/needspace
%{texmfdist}/doc/latex/newenviron
%{texmfdist}/doc/latex/newunicodechar
%{texmfdist}/doc/latex/newverbs
%{texmfdist}/doc/latex/nfssext-cfr
%{texmfdist}/doc/latex/nicefilelist
%{texmfdist}/doc/latex/nlctdoc
%{texmfdist}/doc/latex/noconflict
%{texmfdist}/doc/latex/nonumonpart
%{texmfdist}/doc/latex/nowidow
%{texmfdist}/doc/latex/ntheorem-vn
%{texmfdist}/doc/latex/nuc
%{texmfdist}/doc/latex/numberedblock
%{texmfdist}/doc/latex/numericplots
%{texmfdist}/doc/latex/ocg-p
%{texmfdist}/doc/latex/ocgx
%{texmfdist}/doc/latex/oldstyle
%{texmfdist}/doc/latex/opteng
%{texmfdist}/doc/latex/optional
%{texmfdist}/doc/latex/oscola
%{texmfdist}/doc/latex/othelloboard
%{texmfdist}/doc/latex/outlines
%{texmfdist}/doc/latex/pagecolor
%{texmfdist}/doc/latex/paracol
%{texmfdist}/doc/latex/parnotes
%{texmfdist}/doc/latex/parselines
%{texmfdist}/doc/latex/parskip
%{texmfdist}/doc/latex/pawpict
%{texmfdist}/doc/latex/pdfx
%{texmfdist}/doc/latex/pfarrei
%{texmfdist}/doc/latex/pgf
%{texmfdist}/doc/latex/pgf-blur
%{texmfdist}/doc/latex/pgf-umlsd
%{texmfdist}/doc/latex/pgfgantt
%{texmfdist}/doc/latex/pgfkeyx
%{texmfdist}/doc/latex/physics
%{texmfdist}/doc/latex/physymb
%{texmfdist}/doc/latex/piano
%{texmfdist}/doc/latex/pictexsum
%{texmfdist}/doc/latex/piff
%{texmfdist}/doc/latex/pigpen
%{texmfdist}/doc/latex/pkuthss
%{texmfdist}/doc/latex/poetrytex
%{texmfdist}/doc/latex/polyglossia
%{texmfdist}/doc/latex/prerex
%{texmfdist}/doc/latex/presentations-en
%{texmfdist}/doc/latex/printlen
%{texmfdist}/doc/latex/productbox
%{texmfdist}/doc/latex/progressbar
%{texmfdist}/doc/latex/properties
%{texmfdist}/doc/latex/proposal
%{texmfdist}/doc/latex/przechlewski-book
%{texmfdist}/doc/latex/psbao
%{texmfdist}/doc/latex/psfrag-italian
%{texmfdist}/doc/latex/pst-exa
%{texmfdist}/doc/latex/pst-layout
%{texmfdist}/doc/latex/pst-optexp
%{texmfdist}/doc/latex/pst-vectorian
%{texmfdist}/doc/latex/pst-vowel
%{texmfdist}/doc/latex/pstool
%{texmfdist}/doc/latex/pstricks-examples
%{texmfdist}/doc/latex/pstricks-examples-en
%{texmfdist}/doc/latex/pstricks_calcnotes
%{texmfdist}/doc/latex/ptex2pdf
%{texmfdist}/doc/latex/punk-latex
%{texmfdist}/doc/latex/pxcjkcat
%{texmfdist}/doc/latex/pxgreeks
%{texmfdist}/doc/latex/pxpgfmark
%{texmfdist}/doc/latex/python
%{texmfdist}/doc/latex/quoting
%{texmfdist}/doc/latex/raleway
%{texmfdist}/doc/latex/ran_toks/doc
%{texmfdist}/doc/latex/ran_toks/examples
%{texmfdist}/doc/latex/randomwalk
%{texmfdist}/doc/latex/rcs-multi
%{texmfdist}/doc/latex/readarray
%{texmfdist}/doc/latex/realboxes
%{texmfdist}/doc/latex/realscripts
%{texmfdist}/doc/latex/rec-thy
%{texmfdist}/doc/latex/regexpatch
%{texmfdist}/doc/latex/regstats
%{texmfdist}/doc/latex/relsize
%{texmfdist}/doc/latex/reotex
%{texmfdist}/doc/latex/resphilosophica
%{texmfdist}/doc/latex/rjlparshap
%{texmfdist}/doc/latex/romanbar
%{texmfdist}/doc/latex/romanneg
%{texmfdist}/doc/latex/rrgtrees
%{texmfdist}/doc/latex/rterface
%{texmfdist}/doc/latex/russ
%{texmfdist}/doc/latex/rviewport
%{texmfdist}/doc/latex/rvwrite
%{texmfdist}/doc/latex/sa-tikz
%{texmfdist}/doc/latex/sansmath
%{texmfdist}/doc/latex/sapthesis
%{texmfdist}/doc/latex/sasnrdisplay
%{texmfdist}/doc/latex/scalerel
%{texmfdist}/doc/latex/schemabloc
%{texmfdist}/doc/latex/schwalbe-chess
%{texmfdist}/doc/latex/scrjrnl
%{texmfdist}/doc/latex/secdot
%{texmfdist}/doc/latex/section
%{texmfdist}/doc/latex/selectp
%{texmfdist}/doc/latex/sepfootnotes
%{texmfdist}/doc/latex/sepnum
%{texmfdist}/doc/latex/serbian-apostrophe
%{texmfdist}/doc/latex/serbian-date-lat
%{texmfdist}/doc/latex/serbian-def-cyr
%{texmfdist}/doc/latex/serbian-lig
%{texmfdist}/doc/latex/setdeck
%{texmfdist}/doc/latex/setspace
%{texmfdist}/doc/latex/shadow
%{texmfdist}/doc/latex/shadowtext
%{texmfdist}/doc/latex/showcharinbox
%{texmfdist}/doc/latex/showdim
%{texmfdist}/doc/latex/showtags
%{texmfdist}/doc/latex/shuffle
%{texmfdist}/doc/latex/sidenotes
%{texmfdist}/doc/latex/silence
%{texmfdist}/doc/latex/simplified-latex
%{texmfdist}/doc/latex/sitem
%{texmfdist}/doc/latex/skb
%{texmfdist}/doc/latex/skdoc
%{texmfdist}/doc/latex/skmath
%{texmfdist}/doc/latex/skrapport
%{texmfdist}/doc/latex/smartdiagram
%{texmfdist}/doc/latex/snotez
%{texmfdist}/doc/latex/songs
%{texmfdist}/doc/latex/sourcecodepro
%{texmfdist}/doc/latex/sourcesanspro
%{texmfdist}/doc/latex/spanglish
%{texmfdist}/doc/latex/spath3
%{texmfdist}/doc/latex/sphack
%{texmfdist}/doc/latex/spot
%{texmfdist}/doc/latex/spverbatim
%{texmfdist}/doc/latex/srbook-mem
%{texmfdist}/doc/latex/standalone
%{texmfdist}/doc/latex/statex
%{texmfdist}/doc/latex/statex2
%{texmfdist}/doc/latex/steinmetz
%{texmfdist}/doc/latex/storebox
%{texmfdist}/doc/latex/storecmd
%{texmfdist}/doc/latex/subfigmat
%{texmfdist}/doc/latex/subfiles
%{texmfdist}/doc/latex/substances
%{texmfdist}/doc/latex/substitutefont
%{texmfdist}/doc/latex/suftesi
%{texmfdist}/doc/latex/svg
%{texmfdist}/doc/latex/svg-inkscape
%{texmfdist}/doc/latex/svn-prov
%{texmfdist}/doc/latex/syllogism
%{texmfdist}/doc/latex/tabfigures
%{texmfdist}/doc/latex/tablefootnote
%{texmfdist}/doc/latex/tableof
%{texmfdist}/doc/latex/tabls
%{texmfdist}/doc/latex/tabriz-thesis
%{texmfdist}/doc/latex/tabu
%{texmfdist}/doc/latex/tabularborder
%{texmfdist}/doc/latex/tabularcalc
%{texmfdist}/doc/latex/tabularew
%{texmfdist}/doc/latex/tabulars-e
%{texmfdist}/doc/latex/tagging
%{texmfdist}/doc/latex/tamefloats
%{texmfdist}/doc/latex/tcolorbox
%{texmfdist}/doc/latex/templates-fenn
%{texmfdist}/doc/latex/templates-sommer
%{texmfdist}/doc/latex/termlist
%{texmfdist}/doc/latex/tex-label
%{texmfdist}/doc/latex/tex-overview
%{texmfdist}/doc/latex/texments
%{texmfdist}/doc/latex/textglos
%{texmfdist}/doc/latex/textgreek
%{texmfdist}/doc/latex/threadcol
%{texmfdist}/doc/latex/threeparttable
%{texmfdist}/doc/latex/threeparttablex
%{texmfdist}/doc/latex/thumbs
%{texmfdist}/doc/latex/tikz-bayesnet
%{texmfdist}/doc/latex/tikz-cd
%{texmfdist}/doc/latex/tikz-dependency
%{texmfdist}/doc/latex/tikz-qtree
%{texmfdist}/doc/latex/tikz-timing
%{texmfdist}/doc/latex/tikzinclude
%{texmfdist}/doc/latex/tikzmark
%{texmfdist}/doc/latex/tikzorbital
%{texmfdist}/doc/latex/tikzpagenodes
%{texmfdist}/doc/latex/tikzpfeile
%{texmfdist}/doc/latex/tikzposter
%{texmfdist}/doc/latex/tikzscale
%{texmfdist}/doc/latex/tikzsymbols
%{texmfdist}/doc/latex/tipa-de
%{texmfdist}/doc/latex/titlecaps
%{texmfdist}/doc/latex/titleref
%{texmfdist}/doc/latex/tkz-base
%{texmfdist}/doc/latex/tkz-berge
%{texmfdist}/doc/latex/tkz-euclide
%{texmfdist}/doc/latex/tkz-fct
%{texmfdist}/doc/latex/tkz-graph
%{texmfdist}/doc/latex/tkz-kiviat
%{texmfdist}/doc/latex/tkz-orm
%{texmfdist}/doc/latex/tqft
%{texmfdist}/doc/latex/tram
%{texmfdist}/doc/latex/translation-array-fr
%{texmfdist}/doc/latex/translation-arsclassica-de
%{texmfdist}/doc/latex/translation-biblatex-de
%{texmfdist}/doc/latex/translation-chemsym-de
%{texmfdist}/doc/latex/translation-dcolumn-fr
%{texmfdist}/doc/latex/translation-ecv-de
%{texmfdist}/doc/latex/translation-enumitem-de
%{texmfdist}/doc/latex/translation-europecv-de
%{texmfdist}/doc/latex/translation-filecontents-de
%{texmfdist}/doc/latex/translation-moreverb-de
%{texmfdist}/doc/latex/translation-natbib-fr
%{texmfdist}/doc/latex/translation-tabbing-fr
%{texmfdist}/doc/latex/trimspaces
%{texmfdist}/doc/latex/tucv
%{texmfdist}/doc/latex/tui
%{texmfdist}/doc/latex/turkmen
%{texmfdist}/doc/latex/turnthepage
%{texmfdist}/doc/latex/txgreeks
%{texmfdist}/doc/latex/typeface
%{texmfdist}/doc/latex/uadocs
%{texmfdist}/doc/latex/uafthesis
%{texmfdist}/doc/latex/uestcthesis
%{texmfdist}/doc/latex/uiucredborder
%{texmfdist}/doc/latex/ulqda
%{texmfdist}/doc/latex/ulthese
%{texmfdist}/doc/latex/unamthesis
%{texmfdist}/doc/latex/underoverlap
%{texmfdist}/doc/latex/uni-wtal-ger
%{texmfdist}/doc/latex/uni-wtal-lin
%{texmfdist}/doc/latex/unswcover
%{texmfdist}/doc/latex/uothesis
%{texmfdist}/doc/latex/uowthesis
%{texmfdist}/doc/latex/upquote
%{texmfdist}/doc/latex/uri
%{texmfdist}/doc/latex/url
%{texmfdist}/doc/latex/usebib
%{texmfdist}/doc/latex/uspatent
%{texmfdist}/doc/latex/uwmslide
%{texmfdist}/doc/latex/varwidth
%{texmfdist}/doc/latex/vdmlisting
%{texmfdist}/doc/latex/venndiagram
%{texmfdist}/doc/latex/verbasef
%{texmfdist}/doc/latex/verbatimbox
%{texmfdist}/doc/latex/verbatimcopy
%{texmfdist}/doc/latex/verbdef
%{texmfdist}/doc/latex/verbments
%{texmfdist}/doc/latex/version
%{texmfdist}/doc/latex/versions
%{texmfdist}/doc/latex/vertbars
%{texmfdist}/doc/latex/vocaltract
%{texmfdist}/doc/latex/warning
%{texmfdist}/doc/latex/williams
%{texmfdist}/doc/latex/wnri-latex
%{texmfdist}/doc/latex/xcite
%{texmfdist}/doc/latex/xcookybooky
%{texmfdist}/doc/latex/xhfill
%{texmfdist}/doc/latex/xltxtra
%{texmfdist}/doc/latex/xpatch
%{texmfdist}/doc/latex/xpeek
%{texmfdist}/doc/latex/xpicture
%{texmfdist}/doc/latex/xpinyin
%{texmfdist}/doc/latex/xpunctuate
%{texmfdist}/doc/latex/yagusylo
%{texmfdist}/doc/latex/youngtab
%{texmfdist}/doc/latex/ytableau
%{texmfdist}/doc/latex/zhnumber
%{texmfdist}/doc/latex/zxjafbfont
%{texmfdist}/doc/latex/zxjafont
%{texmfdist}/doc/latex/zxjatype
%{texmfdist}/doc/lualatex/lua-check-hyphen/doc
%{texmfdist}/doc/lualatex/luabibentry
%{texmfdist}/doc/lualatex/luabidi
%{texmfdist}/doc/lualatex/luacode
%{texmfdist}/doc/lualatex/luaindex
%{texmfdist}/doc/lualatex/luainputenc
%{texmfdist}/doc/lualatex/lualatex-doc
%{texmfdist}/doc/lualatex/lualatex-math
%{texmfdist}/doc/lualatex/luasseq
%{texmfdist}/doc/lualatex/luatextra
%{texmfdist}/doc/lualatex/odsfile
%{texmfdist}/doc/lualatex/pgfmolbio
%{texmfdist}/doc/lualatex/selnolig
%{texmfdist}/doc/lualatex/showhyphens
%{texmfdist}/doc/luatex/base
%{texmfdist}/doc/luatex/chickenize
%{texmfdist}/doc/luatex/hyph-utf8
%{texmfdist}/doc/luatex/interpreter
%{texmfdist}/doc/luatex/lua-visual-debug
%{texmfdist}/doc/luatex/luaintro
%{texmfdist}/doc/luatex/lualibs
%{texmfdist}/doc/luatex/luamplib
%{texmfdist}/doc/luatex/luaotfload
%{texmfdist}/doc/luatex/luatexbase
%{texmfdist}/doc/luatex/luatexja
%{texmfdist}/doc/luatex/luatexko
%{texmfdist}/doc/luatex/luaxml
%{texmfdist}/doc/luatex/spelling
%{texmfdist}/doc/otherformats/psizzl/base
%{texmfdist}/doc/otherformats/startex/base
%{texmfdist}/doc/otherformats/texsis/base
%{texmfdist}/doc/otherformats/xmltex/base
%dir %{texmfdist}/doc/pdftex
%{texmfdist}/doc/pdftex/manual
%{texmfdist}/doc/pdftex/pdftex-pdfkeys
%{texmfdist}/doc/pdftex/thanh/ext
%{texmfdist}/doc/platex/japanese
%{texmfdist}/doc/platex/jsclasses
%{texmfdist}/doc/platex/pxbase
%{texmfdist}/doc/platex/pxchfon
%{texmfdist}/doc/platex/pxjahyper
%{texmfdist}/doc/platex/pxrubrica
%{texmfdist}/doc/sjisconv
%{texmfdist}/doc/support/adhocfilelist
%{texmfdist}/doc/support/arara
%{texmfdist}/doc/support/ascii-chart
%{texmfdist}/doc/support/bundledoc
%{texmfdist}/doc/support/checkcites
%{texmfdist}/doc/support/convbkmk
%{texmfdist}/doc/support/ctanupload
%{texmfdist}/doc/support/de-macro
%{texmfdist}/doc/support/dosepsbin
%{texmfdist}/doc/support/dtxgen
%{texmfdist}/doc/support/epspdf
%{texmfdist}/doc/support/epstopdf
%{texmfdist}/doc/support/fig4latex
%{texmfdist}/doc/support/findhyph
%{texmfdist}/doc/support/fontools
%{texmfdist}/doc/support/gustprog
%{texmfdist}/doc/support/installfont
%{texmfdist}/doc/support/latex2man
%{texmfdist}/doc/support/latexdiff
%{texmfdist}/doc/support/latexfileversion
%{texmfdist}/doc/support/latexpand
%{texmfdist}/doc/support/ltxfileinfo
%{texmfdist}/doc/support/lua-alt-getopt
%{texmfdist}/doc/support/lua2dox
%{texmfdist}/doc/support/match_parens
%{texmfdist}/doc/support/mf2pt1
%{texmfdist}/doc/support/mkgrkindex
%{texmfdist}/doc/support/patgen2-tutorial
%{texmfdist}/doc/support/pdfcrop
%{texmfdist}/doc/support/pdfjam
%{texmfdist}/doc/support/pedigree-perl
%{texmfdist}/doc/support/pkfix
%{texmfdist}/doc/support/pkfix-helper
%{texmfdist}/doc/support/purifyeps
%{texmfdist}/doc/support/sty2dtx
%{texmfdist}/doc/support/svn-multi
%{texmfdist}/doc/support/texcount
%{texmfdist}/doc/support/texdef
%{texmfdist}/doc/support/texdiff
%{texmfdist}/doc/support/texliveonfly
%{texmfdist}/doc/support/texloganalyser
%{texmfdist}/doc/support/typeoutfileinfo
%{texmfdist}/doc/tetex
%{texmfdist}/doc/texdoc
%dir %{texmfdist}/doc/texlive
%{texmfdist}/doc/texlive/texlive-common
%{texmfdist}/doc/texlive/texlive-cz
%{texmfdist}/doc/texlive/texlive-de
%{texmfdist}/doc/texlive/texlive-en
%{texmfdist}/doc/texlive/texlive-fr
%{texmfdist}/doc/texlive/texlive-it
%{texmfdist}/doc/texlive/texlive-pl
%{texmfdist}/doc/texlive/texlive-ru
%{texmfdist}/doc/texlive/texlive-sr
%{texmfdist}/doc/texlive/texlive-zh-cn
%{texmfdist}/doc/texworks
%{texmfdist}/doc/tpic2pdftex
%{texmfdist}/doc/ttf2pk
%{texmfdist}/doc/uplatex/base
%{texmfdist}/doc/uptex/base
%{texmfdist}/doc/vlna
%{texmfdist}/doc/web2c
%{texmfdist}/fonts/afm/esstix
%{texmfdist}/fonts/afm/gust/poltawski
%{texmfdist}/fonts/afm/metapost
%{texmfdist}/fonts/afm/nowacki/iwona
%{texmfdist}/fonts/afm/nowacki/kurier
%{texmfdist}/fonts/afm/paratype/ptmono
%{texmfdist}/fonts/afm/paratype/ptsans
%{texmfdist}/fonts/afm/paratype/ptserif
%{texmfdist}/fonts/afm/public/aramaic-serto
%{texmfdist}/fonts/afm/public/bbold-type1
%{texmfdist}/fonts/afm/public/bookhands
%{texmfdist}/fonts/afm/public/calligra-type1
%{texmfdist}/fonts/afm/public/cantarell
%{texmfdist}/fonts/afm/public/comfortaa
%{texmfdist}/fonts/afm/public/countriesofeurope
%{texmfdist}/fonts/afm/public/dejavu
%{texmfdist}/fonts/afm/public/dozenal
%{texmfdist}/fonts/afm/public/droid
%{texmfdist}/fonts/afm/public/dutchcal
%{texmfdist}/fonts/afm/public/fonts-tlwg
%{texmfdist}/fonts/afm/public/lato
%{texmfdist}/fonts/afm/public/mxedruli
%{texmfdist}/fonts/afm/public/nanumtype1
%{texmfdist}/fonts/afm/public/opensans
%{texmfdist}/fonts/afm/public/prodint
%{texmfdist}/fonts/afm/public/starfont
%{texmfdist}/fonts/afm/public/stmaryrd
%{texmfdist}/fonts/afm/public/tfrupee
%{texmfdist}/fonts/cmap/jfontmaps
%{texmfdist}/fonts/cmap/uptex
%{texmfdist}/fonts/enc/t2
%{texmfdist}/fonts/enc/ttf2pk/base
%{texmfdist}/fonts/lig/afm2pl
%{texmfdist}/fonts/map/pdftex/updmap
%{texmfdist}/fonts/map/vtex/antiqua
%{texmfdist}/fonts/ofm/public/japanese-otf
%{texmfdist}/fonts/opentype/adobe/sourcecodepro
%{texmfdist}/fonts/opentype/adobe/sourcesanspro
%{texmfdist}/fonts/opentype/gust/poltawski
%{texmfdist}/fonts/opentype/impallari/cabin
%{texmfdist}/fonts/opentype/impallari/librebaskerville
%{texmfdist}/fonts/opentype/impallari/quattrocento
%{texmfdist}/fonts/opentype/nowacki/iwona
%{texmfdist}/fonts/opentype/nowacki/kurier
%{texmfdist}/fonts/opentype/public/ccicons
%{texmfdist}/fonts/opentype/public/ebgaramond
%{texmfdist}/fonts/opentype/public/fdsymbol
%{texmfdist}/fonts/opentype/public/fontawesome
%{texmfdist}/fonts/opentype/public/gnu-freefont
%{texmfdist}/fonts/opentype/public/lm
%{texmfdist}/fonts/opentype/public/lm-math
%{texmfdist}/fonts/opentype/public/mdsymbol
%{texmfdist}/fonts/opentype/public/ocr-b-outline
%{texmfdist}/fonts/opentype/public/oldstandard
%{texmfdist}/fonts/opentype/public/persian-modern
%{texmfdist}/fonts/opentype/public/punknova
%{texmfdist}/fonts/opentype/public/tex-gyre-math
%{texmfdist}/fonts/opentype/theleagueofmoveabletype/raleway
%{texmfdist}/fonts/ovp/public/japanese-otf-uptex
%{texmfdist}/fonts/pfm/hoekwater/context
%{texmfdist}/fonts/sfd/dnp
%{texmfdist}/fonts/sfd/pxchfon
%{texmfdist}/fonts/sfd/ttf2pk
%{texmfdist}/fonts/source/public/aramaic-serto
%{texmfdist}/fonts/source/public/aspectratio
%{texmfdist}/fonts/source/public/bartel-chess-fonts
%{texmfdist}/fonts/source/public/bguq
%{texmfdist}/fonts/source/public/cmtiup
%{texmfdist}/fonts/source/public/cookingsymbols
%{texmfdist}/fonts/source/public/fdsymbol
%{texmfdist}/fonts/source/public/frcursive
%{texmfdist}/fonts/source/public/ghab
%{texmfdist}/fonts/source/public/jablantile
%{texmfdist}/fonts/source/public/mdsymbol
%{texmfdist}/fonts/source/public/ocr-b
%{texmfdist}/fonts/source/public/sansmathfonts
%{texmfdist}/fonts/source/public/schulschriften
%{texmfdist}/fonts/source/public/tram
%{texmfdist}/fonts/tfm/cs/cs-a35
%{texmfdist}/fonts/tfm/cs/cs-charter
%{texmfdist}/fonts/tfm/gust/poltawski
%{texmfdist}/fonts/tfm/impallari/cabin
%{texmfdist}/fonts/tfm/impallari/librebaskerville
%{texmfdist}/fonts/tfm/impallari/quattrocento
%{texmfdist}/fonts/tfm/metapost
%{texmfdist}/fonts/tfm/nowacki/iwona
%{texmfdist}/fonts/tfm/nowacki/kurier
%{texmfdist}/fonts/tfm/paratype/ptmono
%{texmfdist}/fonts/tfm/paratype/ptsans
%{texmfdist}/fonts/tfm/paratype/ptserif
%{texmfdist}/fonts/tfm/public/aecc
%{texmfdist}/fonts/tfm/public/aramaic-serto
%{texmfdist}/fonts/tfm/public/ascii-font
%{texmfdist}/fonts/tfm/public/aspectratio
%{texmfdist}/fonts/tfm/public/bartel-chess-fonts
%{texmfdist}/fonts/tfm/public/bguq
%{texmfdist}/fonts/tfm/public/bookhands
%{texmfdist}/fonts/tfm/public/boondox
%{texmfdist}/fonts/tfm/public/cantarell
%{texmfdist}/fonts/tfm/public/ccicons
%{texmfdist}/fonts/tfm/public/chess
%{texmfdist}/fonts/tfm/public/cmtiup
%{texmfdist}/fonts/tfm/public/comfortaa
%{texmfdist}/fonts/tfm/public/cookingsymbols
%{texmfdist}/fonts/tfm/public/countriesofeurope
%{texmfdist}/fonts/tfm/public/dejavu
%{texmfdist}/fonts/tfm/public/droid
%{texmfdist}/fonts/tfm/public/dutchcal
%{texmfdist}/fonts/tfm/public/ebgaramond
%{texmfdist}/fonts/tfm/public/esstix
%{texmfdist}/fonts/tfm/public/fdsymbol
%{texmfdist}/fonts/tfm/public/fonts-tlwg
%{texmfdist}/fonts/tfm/public/gillcm
%{texmfdist}/fonts/tfm/public/hacm
%{texmfdist}/fonts/tfm/public/ipaex-type1
%{texmfdist}/fonts/tfm/public/jamtimes
%{texmfdist}/fonts/tfm/public/japanese-otf
%{texmfdist}/fonts/tfm/public/japanese-otf-uptex
%{texmfdist}/fonts/tfm/public/lato
%{texmfdist}/fonts/tfm/public/levy
%{texmfdist}/fonts/tfm/public/lm
%{texmfdist}/fonts/tfm/public/mdputu
%{texmfdist}/fonts/tfm/public/mdsymbol
%{texmfdist}/fonts/tfm/public/nanumtype1
%{texmfdist}/fonts/tfm/public/newpx
%{texmfdist}/fonts/tfm/public/newtx
%{texmfdist}/fonts/tfm/public/ocr-b
%{texmfdist}/fonts/tfm/public/opensans
%{texmfdist}/fonts/tfm/public/prodint
%{texmfdist}/fonts/tfm/public/pxchfon
%{texmfdist}/fonts/tfm/public/pxfonts
%{texmfdist}/fonts/tfm/public/pxtxalfa
%{texmfdist}/fonts/tfm/public/qpxqtx
%{texmfdist}/fonts/tfm/public/rsfso
%{texmfdist}/fonts/tfm/public/sansmathaccent
%{texmfdist}/fonts/tfm/public/sansmathfonts
%{texmfdist}/fonts/tfm/public/schulschriften
%{texmfdist}/fonts/tfm/public/starfont
%{texmfdist}/fonts/tfm/public/superiors
%{texmfdist}/fonts/tfm/public/tfrupee
%{texmfdist}/fonts/tfm/public/txfonts
%{texmfdist}/fonts/tfm/public/yannisgr
%{texmfdist}/fonts/tfm/theleagueofmoveabletype/raleway
%{texmfdist}/fonts/tfm/uptex/jis
%{texmfdist}/fonts/tfm/uptex/min
%{texmfdist}/fonts/truetype/paratype/ptmono
%{texmfdist}/fonts/truetype/paratype/ptsans
%{texmfdist}/fonts/truetype/paratype/ptserif
%{texmfdist}/fonts/type1/gust/poltawski
%{texmfdist}/fonts/type1/impallari/cabin
%{texmfdist}/fonts/type1/impallari/librebaskerville
%{texmfdist}/fonts/type1/impallari/quattrocento
%{texmfdist}/fonts/type1/metapost
%{texmfdist}/fonts/type1/nowacki/iwona
%{texmfdist}/fonts/type1/nowacki/kurier
%{texmfdist}/fonts/type1/paratype/ptmono
%{texmfdist}/fonts/type1/paratype/ptsans
%{texmfdist}/fonts/type1/paratype/ptserif
%{texmfdist}/fonts/type1/public/aramaic-serto
%{texmfdist}/fonts/type1/public/ascii-font
%{texmfdist}/fonts/type1/public/aspectratio
%{texmfdist}/fonts/type1/public/bbold-type1
%{texmfdist}/fonts/type1/public/bguq
%{texmfdist}/fonts/type1/public/bookhands
%{texmfdist}/fonts/type1/public/boondox
%{texmfdist}/fonts/type1/public/calligra-type1
%{texmfdist}/fonts/type1/public/cantarell
%{texmfdist}/fonts/type1/public/ccicons
%{texmfdist}/fonts/type1/public/comfortaa
%{texmfdist}/fonts/type1/public/countriesofeurope
%{texmfdist}/fonts/type1/public/dejavu
%{texmfdist}/fonts/type1/public/droid
%{texmfdist}/fonts/type1/public/dutchcal
%{texmfdist}/fonts/type1/public/ebgaramond
%{texmfdist}/fonts/type1/public/esstix
%{texmfdist}/fonts/type1/public/fdsymbol
%{texmfdist}/fonts/type1/public/fonts-tlwg
%{texmfdist}/fonts/type1/public/frcursive
%{texmfdist}/fonts/type1/public/hacm
%{texmfdist}/fonts/type1/public/ipaex-type1
%{texmfdist}/fonts/type1/public/lato
%{texmfdist}/fonts/type1/public/lm
%{texmfdist}/fonts/type1/public/mathabx-type1
%{texmfdist}/fonts/type1/public/mdsymbol
%{texmfdist}/fonts/type1/public/mxedruli
%{texmfdist}/fonts/type1/public/nanumtype1
%{texmfdist}/fonts/type1/public/newpx
%{texmfdist}/fonts/type1/public/newtx
%{texmfdist}/fonts/type1/public/ocr-b-outline
%{texmfdist}/fonts/type1/public/opensans
%{texmfdist}/fonts/type1/public/prodint
%{texmfdist}/fonts/type1/public/sansmathfonts
%{texmfdist}/fonts/type1/public/starfont
%{texmfdist}/fonts/type1/public/stmaryrd
%{texmfdist}/fonts/type1/public/superiors
%{texmfdist}/fonts/type1/public/tfrupee
%{texmfdist}/fonts/type1/theleagueofmoveabletype/raleway
%{texmfdist}/fonts/vf/cs/cs-a35
%{texmfdist}/fonts/vf/cs/cs-charter
%{texmfdist}/fonts/vf/impallari/cabin
%{texmfdist}/fonts/vf/impallari/librebaskerville
%{texmfdist}/fonts/vf/impallari/quattrocento
%{texmfdist}/fonts/vf/paratype/ptmono
%{texmfdist}/fonts/vf/paratype/ptsans
%{texmfdist}/fonts/vf/paratype/ptserif
%{texmfdist}/fonts/vf/public/aecc
%{texmfdist}/fonts/vf/public/boondox
%{texmfdist}/fonts/vf/public/cantarell
%{texmfdist}/fonts/vf/public/cmtiup
%{texmfdist}/fonts/vf/public/comfortaa
%{texmfdist}/fonts/vf/public/dejavu
%{texmfdist}/fonts/vf/public/droid
%{texmfdist}/fonts/vf/public/dutchcal
%{texmfdist}/fonts/vf/public/ebgaramond
%{texmfdist}/fonts/vf/public/esstix
%{texmfdist}/fonts/vf/public/fonts-tlwg
%{texmfdist}/fonts/vf/public/gillcm
%{texmfdist}/fonts/vf/public/hacm
%{texmfdist}/fonts/vf/public/jamtimes
%{texmfdist}/fonts/vf/public/japanese-otf
%{texmfdist}/fonts/vf/public/japanese-otf-uptex
%{texmfdist}/fonts/vf/public/lato
%{texmfdist}/fonts/vf/public/mdputu
%{texmfdist}/fonts/vf/public/nanumtype1
%{texmfdist}/fonts/vf/public/newpx
%{texmfdist}/fonts/vf/public/newtx
%{texmfdist}/fonts/vf/public/opensans
%{texmfdist}/fonts/vf/public/pxchfon
%{texmfdist}/fonts/vf/public/pxtxalfa
%{texmfdist}/fonts/vf/public/rsfso
%{texmfdist}/fonts/vf/public/sansmathaccent
%{texmfdist}/fonts/vf/public/sansmathfonts
%{texmfdist}/fonts/vf/theleagueofmoveabletype/raleway
%{texmfdist}/fonts/vf/uptex/jis
%{texmfdist}/fonts/vf/uptex/min
%{texmfdist}/hbf2gf
%{texmfdist}/metapost/bclogo
%{texmfdist}/metapost/mf2pt1
%{texmfdist}/metapost/mpcolornames
%{texmfdist}/metapost/threeddice
%{texmfdist}/pbibtex/bib
%{texmfdist}/pbibtex/bst
%{texmfdist}/scripts/bitmap2eps
%{texmfdist}/scripts/changes
%{texmfdist}/scripts/flowfram
%{texmfdist}/scripts/fmtcount
%{texmfdist}/scripts/jmlr
%{texmfdist}/scripts/logicpuzzle
%{texmfdist}/scripts/lua-alt-getopt
%{texmfdist}/scripts/luaindex
%{texmfdist}/scripts/luasseq
%{texmfdist}/scripts/mycv
%{texmfdist}/scripts/spelling
%{texmfdist}/scripts/texdiff
%dir %{texmfdist}/scripts/texlive
%{texmfdist}/scripts/texlive/lua/texlive
%{texmfdist}/scripts/texlive/var
%{texmfdist}/scripts/tlgs/gswin32
%{texmfdist}/source/bibtex/apacite
%{texmfdist}/source/bibtex/biber
%{texmfdist}/source/bibtex/bibexport
%{texmfdist}/source/bibtex/urlbst
%{texmfdist}/source/cslatex/cspsfonts
%{texmfdist}/source/eplain
%{texmfdist}/source/fontinst/base
%{texmfdist}/source/fonts/ascii-font
%{texmfdist}/source/fonts/baskervald
%{texmfdist}/source/fonts/berenisadf
%{texmfdist}/source/fonts/bguq
%{texmfdist}/source/fonts/bookhands
%{texmfdist}/source/fonts/burmese
%{texmfdist}/source/fonts/cantarell
%{texmfdist}/source/fonts/ccicons
%{texmfdist}/source/fonts/comfortaa
%{texmfdist}/source/fonts/dozenal
%{texmfdist}/source/fonts/droid
%{texmfdist}/source/fonts/electrum
%{texmfdist}/source/fonts/enc/c90
%{texmfdist}/source/fonts/fonts-tlwg
%{texmfdist}/source/fonts/garuda-c90
%{texmfdist}/source/fonts/gnu-freefont
%{texmfdist}/source/fonts/go
%{texmfdist}/source/fonts/inconsolata
%{texmfdist}/source/fonts/japanese-otf
%{texmfdist}/source/fonts/japanese-otf-uptex
%{texmfdist}/source/fonts/lato
%{texmfdist}/source/fonts/libris
%{texmfdist}/source/fonts/marvosym
%{texmfdist}/source/fonts/norasi-c90
%{texmfdist}/source/fonts/ocr-b-outline
%{texmfdist}/source/fonts/oldstandard
%{texmfdist}/source/fonts/opensans
%{texmfdist}/source/fonts/pacioli
%{texmfdist}/source/fonts/persian-modern
%{texmfdist}/source/fonts/romande
%{texmfdist}/source/fonts/skull
%{texmfdist}/source/fonts/tfrupee
%{texmfdist}/source/fonts/uptex
%{texmfdist}/source/fonts/venturisadf
%{texmfdist}/source/generic/babel-albanian
%{texmfdist}/source/generic/babel-bahasa
%{texmfdist}/source/generic/babel-basque
%{texmfdist}/source/generic/babel-breton
%{texmfdist}/source/generic/babel-bulgarian
%{texmfdist}/source/generic/babel-catalan
%{texmfdist}/source/generic/babel-croatian
%{texmfdist}/source/generic/babel-czech
%{texmfdist}/source/generic/babel-danish
%{texmfdist}/source/generic/babel-dutch
%{texmfdist}/source/generic/babel-english
%{texmfdist}/source/generic/babel-esperanto
%{texmfdist}/source/generic/babel-estonian
%{texmfdist}/source/generic/babel-finnish
%{texmfdist}/source/generic/babel-french
%{texmfdist}/source/generic/babel-friulan
%{texmfdist}/source/generic/babel-galician
%{texmfdist}/source/generic/babel-german
%{texmfdist}/source/generic/babel-greek
%{texmfdist}/source/generic/babel-hebrew
%{texmfdist}/source/generic/babel-icelandic
%{texmfdist}/source/generic/babel-interlingua
%{texmfdist}/source/generic/babel-irish
%{texmfdist}/source/generic/babel-italian
%{texmfdist}/source/generic/babel-kurmanji
%{texmfdist}/source/generic/babel-latin
%{texmfdist}/source/generic/babel-norsk
%{texmfdist}/source/generic/babel-piedmontese
%{texmfdist}/source/generic/babel-polish
%{texmfdist}/source/generic/babel-portuges
%{texmfdist}/source/generic/babel-romanian
%{texmfdist}/source/generic/babel-romansh
%{texmfdist}/source/generic/babel-russian
%{texmfdist}/source/generic/babel-samin
%{texmfdist}/source/generic/babel-scottish
%{texmfdist}/source/generic/babel-serbian
%{texmfdist}/source/generic/babel-serbianc
%{texmfdist}/source/generic/babel-slovak
%{texmfdist}/source/generic/babel-slovenian
%{texmfdist}/source/generic/babel-sorbian
%{texmfdist}/source/generic/babel-spanish
%{texmfdist}/source/generic/babel-swedish
%{texmfdist}/source/generic/babel-thai
%{texmfdist}/source/generic/babel-turkish
%{texmfdist}/source/generic/babel-ukraineb
%{texmfdist}/source/generic/babel-vietnamese
%{texmfdist}/source/generic/babel-welsh
%{texmfdist}/source/generic/bitelist
%{texmfdist}/source/generic/catcodes
%{texmfdist}/source/generic/commado
%{texmfdist}/source/generic/dowith
%{texmfdist}/source/generic/hyphenex
%{texmfdist}/source/generic/ifxetex
%{texmfdist}/source/generic/langcode
%{texmfdist}/source/generic/minifp
%{texmfdist}/source/generic/mkjobtexmf
%{texmfdist}/source/generic/musixtex/musixcrd
%{texmfdist}/source/generic/plainpkg
%{texmfdist}/source/generic/pst-abspos
%{texmfdist}/source/generic/pst-am
%{texmfdist}/source/generic/pst-bar
%{texmfdist}/source/generic/pst-bezier
%{texmfdist}/source/generic/pst-fit
%{texmfdist}/source/generic/pst-gantt
%{texmfdist}/source/generic/pst-math
%{texmfdist}/source/generic/pst-mirror
%{texmfdist}/source/generic/pst-node
%{texmfdist}/source/generic/pst-platon
%{texmfdist}/source/generic/pst-plot
%{texmfdist}/source/generic/pst-poly
%{texmfdist}/source/generic/pst-pulley
%{texmfdist}/source/generic/pst-rubans
%{texmfdist}/source/generic/pst-solarsystem
%{texmfdist}/source/generic/pst-thick
%{texmfdist}/source/generic/pst-tools
%{texmfdist}/source/generic/pst-tree
%{texmfdist}/source/generic/pst-tvz
%{texmfdist}/source/generic/schemata
%{texmfdist}/source/generic/xint
%{texmfdist}/source/generic/xlop
%{texmfdist}/source/jfontmaps/jis04cmap_exp
%{texmfdist}/source/jfontmaps/script
%{texmfdist}/source/jfontmaps/tools
%{texmfdist}/source/latex/GS1
%{texmfdist}/source/latex/acroterm
%{texmfdist}/source/latex/adfathesis
%{texmfdist}/source/latex/adjmulticol
%{texmfdist}/source/latex/adjustbox
%{texmfdist}/source/latex/aomart
%{texmfdist}/source/latex/apa6
%{texmfdist}/source/latex/apa6e
%{texmfdist}/source/latex/apptools
%{texmfdist}/source/latex/articleingud
%{texmfdist}/source/latex/asyfig
%{texmfdist}/source/latex/autonum
%{texmfdist}/source/latex/autopdf
%{texmfdist}/source/latex/b1encoding
%{texmfdist}/source/latex/babel
%{texmfdist}/source/latex/backnaur
%{texmfdist}/source/latex/basque-book
%{texmfdist}/source/latex/basque-date
%{texmfdist}/source/latex/beamersubframe
%{texmfdist}/source/latex/bgteubner
%{texmfdist}/source/latex/bhcexam
%{texmfdist}/source/latex/biblatex-philosophy
%{texmfdist}/source/latex/bibleref-french
%{texmfdist}/source/latex/bibleref-lds
%{texmfdist}/source/latex/bibleref-mouth
%{texmfdist}/source/latex/bidi
%{texmfdist}/source/latex/braids
%{texmfdist}/source/latex/bropd
%{texmfdist}/source/latex/bxjscls
%{texmfdist}/source/latex/calcage
%{texmfdist}/source/latex/calculator
%{texmfdist}/source/latex/cals
%{texmfdist}/source/latex/canoniclayout
%{texmfdist}/source/latex/capt-of
%{texmfdist}/source/latex/catchfilebetweentags
%{texmfdist}/source/latex/changepage
%{texmfdist}/source/latex/chembst
%{texmfdist}/source/latex/chextras
%{texmfdist}/source/latex/chscite
%{texmfdist}/source/latex/cjkpunct
%{texmfdist}/source/latex/codicefiscaleitaliano
%{texmfdist}/source/latex/collcell
%{texmfdist}/source/latex/collectbox
%{texmfdist}/source/latex/conteq
%{texmfdist}/source/latex/contracard
%{texmfdist}/source/latex/cookingsymbols
%{texmfdist}/source/latex/coolthms
%{texmfdist}/source/latex/counttexruns
%{texmfdist}/source/latex/cprotect
%{texmfdist}/source/latex/cutwin
%{texmfdist}/source/latex/decorule
%{texmfdist}/source/latex/delim
%{texmfdist}/source/latex/dhua
%{texmfdist}/source/latex/diagbox
%{texmfdist}/source/latex/dingbat
%{texmfdist}/source/latex/dirtytalk
%{texmfdist}/source/latex/documentation
%{texmfdist}/source/latex/download
%{texmfdist}/source/latex/dvgloss
%{texmfdist}/source/latex/easyfig
%{texmfdist}/source/latex/edfnotes
%{texmfdist}/source/latex/eiad-ltx
%{texmfdist}/source/latex/ejpecp
%{texmfdist}/source/latex/elbioimp
%{texmfdist}/source/latex/eledform
%{texmfdist}/source/latex/eledmac
%{texmfdist}/source/latex/elteikthesis
%{texmfdist}/source/latex/emarks
%{texmfdist}/source/latex/enumitem-zref
%{texmfdist}/source/latex/eqnarray
%{texmfdist}/source/latex/etextools
%{texmfdist}/source/latex/etoc
%{texmfdist}/source/latex/everyhook
%{texmfdist}/source/latex/exsol
%{texmfdist}/source/latex/fancytabs
%{texmfdist}/source/latex/fbithesis
%{texmfdist}/source/latex/fcltxdoc
%{texmfdist}/source/latex/fdsymbol
%{texmfdist}/source/latex/feynmp-auto
%{texmfdist}/source/latex/fifinddo-info
%{texmfdist}/source/latex/filedate
%{texmfdist}/source/latex/fileinfo
%{texmfdist}/source/latex/finstrut
%{texmfdist}/source/latex/fixltxhyph
%{texmfdist}/source/latex/fixmetodonotes
%{texmfdist}/source/latex/floatflt
%{texmfdist}/source/latex/flowchart
%{texmfdist}/source/latex/fnumprint
%{texmfdist}/source/latex/fontaxes
%{texmfdist}/source/latex/footnoterange
%{texmfdist}/source/latex/foreign
%{texmfdist}/source/latex/forest
%{texmfdist}/source/latex/fundus-calligra
%{texmfdist}/source/latex/fundus-sueterlin
%{texmfdist}/source/latex/gamebook
%{texmfdist}/source/latex/geschichtsfrkl
%{texmfdist}/source/latex/gincltex
%{texmfdist}/source/latex/gmdoc-enhance
%{texmfdist}/source/latex/gmp
%{texmfdist}/source/latex/gradientframe
%{texmfdist}/source/latex/gridset
%{texmfdist}/source/latex/guitlogo
%{texmfdist}/source/latex/hardwrap
%{texmfdist}/source/latex/hausarbeit-jura
%{texmfdist}/source/latex/hf-tikz
%{texmfdist}/source/latex/hobby
%{texmfdist}/source/latex/horoscop
%{texmfdist}/source/latex/hrefhide
%{texmfdist}/source/latex/idxlayout
%{texmfdist}/source/latex/ifetex
%{texmfdist}/source/latex/ifnextok
%{texmfdist}/source/latex/ifoddpage
%{texmfdist}/source/latex/iitem
%{texmfdist}/source/latex/imakeidx
%{texmfdist}/source/latex/impnattypo
%{texmfdist}/source/latex/inputtrc
%{texmfdist}/source/latex/interfaces
%{texmfdist}/source/latex/issuulinks
%{texmfdist}/source/latex/jvlisting
%{texmfdist}/source/latex/kantlipsum
%{texmfdist}/source/latex/kdgdocs
%{texmfdist}/source/latex/ktv-texdata
%{texmfdist}/source/latex/l3experimental/l3dt
%{texmfdist}/source/latex/l3experimental/l3sort
%{texmfdist}/source/latex/l3experimental/l3str
%{texmfdist}/source/latex/l3experimental/xcoffins
%{texmfdist}/source/latex/l3experimental/xgalley
%{texmfdist}/source/latex/l3kernel
%{texmfdist}/source/latex/l3packages/l3keys2e
%{texmfdist}/source/latex/l3packages/xfrac
%{texmfdist}/source/latex/l3packages/xparse
%{texmfdist}/source/latex/l3packages/xtemplate
%{texmfdist}/source/latex/latexfileinfo-pkgs
%{texmfdist}/source/latex/leipzig
%{texmfdist}/source/latex/libgreek
%{texmfdist}/source/latex/linegoal
%{texmfdist}/source/latex/lineno
%{texmfdist}/source/latex/liturg
%{texmfdist}/source/latex/lm
%{texmfdist}/source/latex/lmake
%{texmfdist}/source/latex/logbox
%{texmfdist}/source/latex/longnamefilelist
%{texmfdist}/source/latex/lstaddons
%{texmfdist}/source/latex/ltxnew
%{texmfdist}/source/latex/makeshape
%{texmfdist}/source/latex/mandi
%{texmfdist}/source/latex/margbib
%{texmfdist}/source/latex/marginfix
%{texmfdist}/source/latex/matc3
%{texmfdist}/source/latex/matc3mem
%{texmfdist}/source/latex/mathastext
%{texmfdist}/source/latex/mdframed
%{texmfdist}/source/latex/mdsymbol
%{texmfdist}/source/latex/meetingmins
%{texmfdist}/source/latex/memory
%{texmfdist}/source/latex/menukeys
%{texmfdist}/source/latex/metalogo
%{texmfdist}/source/latex/mnotes
%{texmfdist}/source/latex/moderntimeline
%{texmfdist}/source/latex/monofill
%{texmfdist}/source/latex/morefloats
%{texmfdist}/source/latex/morehype
%{texmfdist}/source/latex/morewrites
%{texmfdist}/source/latex/mpgraphics
%{texmfdist}/source/latex/multibibliography
%{texmfdist}/source/latex/multienv
%{texmfdist}/source/latex/multiexpand
%{texmfdist}/source/latex/musuos
%{texmfdist}/source/latex/mversion
%{texmfdist}/source/latex/mwe
%{texmfdist}/source/latex/mycv
%{texmfdist}/source/latex/mylatexformat
%{texmfdist}/source/latex/nameauth
%{texmfdist}/source/latex/needspace
%{texmfdist}/source/latex/newunicodechar
%{texmfdist}/source/latex/newverbs
%{texmfdist}/source/latex/nicefilelist
%{texmfdist}/source/latex/nicetext
%{texmfdist}/source/latex/nkarta
%{texmfdist}/source/latex/nonumonpart
%{texmfdist}/source/latex/nowidow
%{texmfdist}/source/latex/ocgx
%{texmfdist}/source/latex/pagecolor
%{texmfdist}/source/latex/paracol
%{texmfdist}/source/latex/parselines
%{texmfdist}/source/latex/pfarrei
%{texmfdist}/source/latex/pgf-blur
%{texmfdist}/source/latex/pgf/incoming/GrzegorzMurzynowski
%{texmfdist}/source/latex/pgf/incoming/KarlheinzOchs
%{texmfdist}/source/latex/pgf/testsuite/external
%{texmfdist}/source/latex/pgf/testsuite/mathtest
%{texmfdist}/source/latex/pgfgantt
%{texmfdist}/source/latex/physymb
%{texmfdist}/source/latex/poetrytex
%{texmfdist}/source/latex/polyglossia
%{texmfdist}/source/latex/productbox
%{texmfdist}/source/latex/proposal/base
%{texmfdist}/source/latex/proposal/dfg
%{texmfdist}/source/latex/proposal/eu
%{texmfdist}/source/latex/pst-optexp
%{texmfdist}/source/latex/pxgreeks
%{texmfdist}/source/latex/quoting
%{texmfdist}/source/latex/ran_toks
%{texmfdist}/source/latex/randomwalk
%{texmfdist}/source/latex/realboxes
%{texmfdist}/source/latex/realscripts
%{texmfdist}/source/latex/regexpatch
%{texmfdist}/source/latex/regstats
%{texmfdist}/source/latex/resphilosophica
%{texmfdist}/source/latex/romanbar
%{texmfdist}/source/latex/rrgtrees
%{texmfdist}/source/latex/rviewport
%{texmfdist}/source/latex/schwalbe-chess
%{texmfdist}/source/latex/scrjrnl
%{texmfdist}/source/latex/showcharinbox
%{texmfdist}/source/latex/sidenotes
%{texmfdist}/source/latex/sitem
%{texmfdist}/source/latex/skb
%{texmfdist}/source/latex/skdoc
%{texmfdist}/source/latex/skmath
%{texmfdist}/source/latex/smartdiagram
%{texmfdist}/source/latex/songs
%{texmfdist}/source/latex/spath3
%{texmfdist}/source/latex/spot
%{texmfdist}/source/latex/standalone
%{texmfdist}/source/latex/storebox
%{texmfdist}/source/latex/sttools
%{texmfdist}/source/latex/subfiles
%{texmfdist}/source/latex/suftesi
%{texmfdist}/source/latex/svg
%{texmfdist}/source/latex/tabfigures
%{texmfdist}/source/latex/tablefootnote
%{texmfdist}/source/latex/tableof
%{texmfdist}/source/latex/tabu
%{texmfdist}/source/latex/tabularborder
%{texmfdist}/source/latex/tex-label
%{texmfdist}/source/latex/textglos
%{texmfdist}/source/latex/textgreek
%{texmfdist}/source/latex/threadcol
%{texmfdist}/source/latex/thumbs
%{texmfdist}/source/latex/tikz-timing
%{texmfdist}/source/latex/tikzinclude
%{texmfdist}/source/latex/tikzmark
%{texmfdist}/source/latex/tikzpagenodes
%{texmfdist}/source/latex/tikzpfeile
%{texmfdist}/source/latex/tikzposter
%{texmfdist}/source/latex/tikzscale
%{texmfdist}/source/latex/tikzsymbols
%{texmfdist}/source/latex/tpslifonts
%{texmfdist}/source/latex/tqft
%{texmfdist}/source/latex/trimspaces
%{texmfdist}/source/latex/tucv
%{texmfdist}/source/latex/tufte-latex
%{texmfdist}/source/latex/turkmen
%{texmfdist}/source/latex/txgreeks
%{texmfdist}/source/latex/typeface
%{texmfdist}/source/latex/typehtml
%{texmfdist}/source/latex/uadocs
%{texmfdist}/source/latex/uiucredborder
%{texmfdist}/source/latex/ulqda
%{texmfdist}/source/latex/ulthese
%{texmfdist}/source/latex/uothesis
%{texmfdist}/source/latex/upquote
%{texmfdist}/source/latex/uri
%{texmfdist}/source/latex/usebib
%{texmfdist}/source/latex/venndiagram
%{texmfdist}/source/latex/vertbars
%{texmfdist}/source/latex/wnri-latex
%{texmfdist}/source/latex/xcite
%{texmfdist}/source/latex/xcookybooky
%{texmfdist}/source/latex/xltxtra
%{texmfdist}/source/latex/xpatch
%{texmfdist}/source/latex/xpeek
%{texmfdist}/source/latex/xpicture
%{texmfdist}/source/latex/xpinyin
%{texmfdist}/source/latex/xpunctuate
%{texmfdist}/source/latex/yagusylo
%{texmfdist}/source/latex/ytableau
%{texmfdist}/source/latex/zhnumber
%{texmfdist}/source/lualatex/luabibentry
%{texmfdist}/source/lualatex/luacode
%{texmfdist}/source/lualatex/luaindex
%{texmfdist}/source/lualatex/luainputenc
%{texmfdist}/source/lualatex/lualatex-doc
%{texmfdist}/source/lualatex/lualatex-math
%{texmfdist}/source/lualatex/luasseq
%{texmfdist}/source/lualatex/luatextra
%{texmfdist}/source/lualatex/pgfmolbio
%{texmfdist}/source/luatex/chickenize
%{texmfdist}/source/luatex/hyph-utf8
%{texmfdist}/source/luatex/lualibs
%{texmfdist}/source/luatex/luamplib
%{texmfdist}/source/luatex/luaotfload
%{texmfdist}/source/luatex/luatexbase
%{texmfdist}/source/luatex/luatexja
%{texmfdist}/source/metapost/expressg
%{texmfdist}/source/metapost/mpcolornames
%{texmfdist}/source/metapost/splines
%{texmfdist}/source/plain/graphics-pln
%{texmfdist}/source/platex/base
%{texmfdist}/source/platex/japanese
%{texmfdist}/source/platex/jsclasses
%{texmfdist}/source/platex/pxchfon
%{texmfdist}/source/platex/pxrubrica
%{texmfdist}/source/startex/base
%{texmfdist}/source/support/adhocfilelist
%{texmfdist}/source/support/arara
%{texmfdist}/source/support/dosepsbin
%{texmfdist}/source/support/latexmk
%{texmfdist}/source/support/texdef
%{texmfdist}/source/uplatex/base
%{texmfdist}/tex/generic/2up
%{texmfdist}/tex/generic/babel-albanian
%{texmfdist}/tex/generic/babel-bahasa
%{texmfdist}/tex/generic/babel-basque
%{texmfdist}/tex/generic/babel-breton
%{texmfdist}/tex/generic/babel-bulgarian
%{texmfdist}/tex/generic/babel-catalan
%{texmfdist}/tex/generic/babel-croatian
%{texmfdist}/tex/generic/babel-czech
%{texmfdist}/tex/generic/babel-danish
%{texmfdist}/tex/generic/babel-dutch
%{texmfdist}/tex/generic/babel-english
%{texmfdist}/tex/generic/babel-esperanto
%{texmfdist}/tex/generic/babel-estonian
%{texmfdist}/tex/generic/babel-finnish
%{texmfdist}/tex/generic/babel-french
%{texmfdist}/tex/generic/babel-friulan
%{texmfdist}/tex/generic/babel-galician
%{texmfdist}/tex/generic/babel-german
%{texmfdist}/tex/generic/babel-greek
%{texmfdist}/tex/generic/babel-hebrew
%{texmfdist}/tex/generic/babel-icelandic
%{texmfdist}/tex/generic/babel-interlingua
%{texmfdist}/tex/generic/babel-irish
%{texmfdist}/tex/generic/babel-italian
%{texmfdist}/tex/generic/babel-kurmanji
%{texmfdist}/tex/generic/babel-latin
%{texmfdist}/tex/generic/babel-norsk
%{texmfdist}/tex/generic/babel-piedmontese
%{texmfdist}/tex/generic/babel-polish
%{texmfdist}/tex/generic/babel-portuges
%{texmfdist}/tex/generic/babel-romanian
%{texmfdist}/tex/generic/babel-romansh
%{texmfdist}/tex/generic/babel-russian
%{texmfdist}/tex/generic/babel-samin
%{texmfdist}/tex/generic/babel-scottish
%{texmfdist}/tex/generic/babel-serbian
%{texmfdist}/tex/generic/babel-serbianc
%{texmfdist}/tex/generic/babel-slovak
%{texmfdist}/tex/generic/babel-slovenian
%{texmfdist}/tex/generic/babel-sorbian
%{texmfdist}/tex/generic/babel-spanish
%{texmfdist}/tex/generic/babel-swedish
%{texmfdist}/tex/generic/babel-thai
%{texmfdist}/tex/generic/babel-turkish
%{texmfdist}/tex/generic/babel-ukraineb
%{texmfdist}/tex/generic/babel-vietnamese
%{texmfdist}/tex/generic/babel-welsh
%{texmfdist}/tex/generic/bibtex
%{texmfdist}/tex/generic/bitelist
%{texmfdist}/tex/generic/catcodes
%{texmfdist}/tex/generic/chemfig
%{texmfdist}/tex/generic/chronosys
%{texmfdist}/tex/generic/commado
%{texmfdist}/tex/generic/config
%{texmfdist}/tex/generic/dowith
%{texmfdist}/tex/generic/enigma
%{texmfdist}/tex/generic/epigram
%{texmfdist}/tex/generic/filemod
%{texmfdist}/tex/generic/fntproof
%{texmfdist}/tex/generic/formlett
%{texmfdist}/tex/generic/frame
%{texmfdist}/tex/generic/gates
%{texmfdist}/tex/generic/langcode
%{texmfdist}/tex/generic/lecturer
%{texmfdist}/tex/generic/levy
%{texmfdist}/tex/generic/m-tx
%{texmfdist}/tex/generic/minifp
%{texmfdist}/tex/generic/navigator
%{texmfdist}/tex/generic/path
%{texmfdist}/tex/generic/pdftex
%{texmfdist}/tex/generic/petri-nets
%{texmfdist}/tex/generic/plainpkg
%{texmfdist}/tex/generic/pmx
%{texmfdist}/tex/generic/pst-fit
%{texmfdist}/tex/generic/pst-graphicx
%{texmfdist}/tex/generic/pst-knot
%{texmfdist}/tex/generic/pst-mirror
%{texmfdist}/tex/generic/pst-node
%{texmfdist}/tex/generic/pst-ode
%{texmfdist}/tex/generic/pst-plot
%{texmfdist}/tex/generic/pst-pulley
%{texmfdist}/tex/generic/pst-rubans
%{texmfdist}/tex/generic/pst-sigsys
%{texmfdist}/tex/generic/pst-solarsystem
%{texmfdist}/tex/generic/pst-thick
%{texmfdist}/tex/generic/pst-tools
%{texmfdist}/tex/generic/pst-tvz
%{texmfdist}/tex/generic/schemata
%{texmfdist}/tex/generic/splitindex
%{texmfdist}/tex/generic/systeme
%{texmfdist}/tex/generic/texapi
%{texmfdist}/tex/generic/upca
%{texmfdist}/tex/generic/xint
%{texmfdist}/tex/generic/ydoc
%{texmfdist}/tex/latex/GS1
%{texmfdist}/tex/latex/abntex2
%{texmfdist}/tex/latex/abraces
%{texmfdist}/tex/latex/acro
%{texmfdist}/tex/latex/acroterm
%{texmfdist}/tex/latex/actuarialangle
%{texmfdist}/tex/latex/adfathesis
%{texmfdist}/tex/latex/adforn
%{texmfdist}/tex/latex/adfsymbols
%{texmfdist}/tex/latex/adjmulticol
%{texmfdist}/tex/latex/adjustbox
%{texmfdist}/tex/latex/aecc
%{texmfdist}/tex/latex/akktex
%{texmfdist}/tex/latex/aomart
%{texmfdist}/tex/latex/apa6
%{texmfdist}/tex/latex/apa6e
%{texmfdist}/tex/latex/appendixnumberbeamer
%{texmfdist}/tex/latex/apptools
%{texmfdist}/tex/latex/aramaic-serto
%{texmfdist}/tex/latex/articleingud
%{texmfdist}/tex/latex/ascii-font
%{texmfdist}/tex/latex/aspectratio
%{texmfdist}/tex/latex/autonum
%{texmfdist}/tex/latex/autopdf
%{texmfdist}/tex/latex/b1encoding
%{texmfdist}/tex/latex/babel-hungarian
%{texmfdist}/tex/latex/backnaur
%{texmfdist}/tex/latex/bashful
%{texmfdist}/tex/latex/baskervald
%{texmfdist}/tex/latex/basque-book
%{texmfdist}/tex/latex/basque-date
%{texmfdist}/tex/latex/bchart
%{texmfdist}/tex/latex/beamer2thesis
%{texmfdist}/tex/latex/beameraudience
%{texmfdist}/tex/latex/beamersubframe
%{texmfdist}/tex/latex/beamertheme-upenn-bc
%{texmfdist}/tex/latex/beamerthemejltree
%{texmfdist}/tex/latex/beamerthemenirma
%{texmfdist}/tex/latex/berenisadf
%{texmfdist}/tex/latex/bgreek
%{texmfdist}/tex/latex/bgteubner
%{texmfdist}/tex/latex/bguq
%{texmfdist}/tex/latex/bhcexam
%{texmfdist}/tex/latex/biblatex-bwl
%{texmfdist}/tex/latex/biblatex-caspervector
%{texmfdist}/tex/latex/biblatex-chicago
%{texmfdist}/tex/latex/biblatex-fiwi
%{texmfdist}/tex/latex/biblatex-gost
%{texmfdist}/tex/latex/biblatex-ieee
%{texmfdist}/tex/latex/biblatex-juradiss
%{texmfdist}/tex/latex/biblatex-luh-ipw/bbx
%{texmfdist}/tex/latex/biblatex-luh-ipw/cbx
%{texmfdist}/tex/latex/biblatex-luh-ipw/lbx
%{texmfdist}/tex/latex/biblatex-mla
%{texmfdist}/tex/latex/biblatex-musuos
%{texmfdist}/tex/latex/biblatex-nejm
%{texmfdist}/tex/latex/biblatex-phys
%{texmfdist}/tex/latex/biblatex-publist
%{texmfdist}/tex/latex/biblatex-swiss-legal
%{texmfdist}/tex/latex/biblatex-trad/bbx
%{texmfdist}/tex/latex/biblatex-trad/cbx
%{texmfdist}/tex/latex/bibleref-french
%{texmfdist}/tex/latex/bibleref-german
%{texmfdist}/tex/latex/bibleref-lds
%{texmfdist}/tex/latex/bibleref-mouth
%{texmfdist}/tex/latex/bibleref-parse
%{texmfdist}/tex/latex/bloques
%{texmfdist}/tex/latex/bodegraph
%{texmfdist}/tex/latex/bohr
%{texmfdist}/tex/latex/bold-extra
%{texmfdist}/tex/latex/bondgraph
%{texmfdist}/tex/latex/boondox
%{texmfdist}/tex/latex/bracketkey
%{texmfdist}/tex/latex/braids
%{texmfdist}/tex/latex/breakcites
%{texmfdist}/tex/latex/bropd
%{texmfdist}/tex/latex/bundledoc
%{texmfdist}/tex/latex/bxbase
%{texmfdist}/tex/latex/bxdpx-beamer
%{texmfdist}/tex/latex/bxeepic
%{texmfdist}/tex/latex/bxjscls
%{texmfdist}/tex/latex/cabin
%{texmfdist}/tex/latex/cachepic
%{texmfdist}/tex/latex/calcage
%{texmfdist}/tex/latex/calctab
%{texmfdist}/tex/latex/calculator
%{texmfdist}/tex/latex/cals
%{texmfdist}/tex/latex/calxxxx-yyyy
%{texmfdist}/tex/latex/canoniclayout
%{texmfdist}/tex/latex/cantarell
%{texmfdist}/tex/latex/captdef
%{texmfdist}/tex/latex/cascadilla
%{texmfdist}/tex/latex/catchfilebetweentags
%{texmfdist}/tex/latex/catoptions
%{texmfdist}/tex/latex/cell
%{texmfdist}/tex/latex/chemexec
%{texmfdist}/tex/latex/chemmacros
%{texmfdist}/tex/latex/chemnum
%{texmfdist}/tex/latex/chet
%{texmfdist}/tex/latex/chextras
%{texmfdist}/tex/latex/chkfloat
%{texmfdist}/tex/latex/chscite
%{texmfdist}/tex/latex/cjk-ko
%{texmfdist}/tex/latex/cjkpunct
%{texmfdist}/tex/latex/classics
%{texmfdist}/tex/latex/clipboard
%{texmfdist}/tex/latex/cmpj
%{texmfdist}/tex/latex/cmtiup
%{texmfdist}/tex/latex/codicefiscaleitaliano
%{texmfdist}/tex/latex/collcell
%{texmfdist}/tex/latex/collectbox
%{texmfdist}/tex/latex/colourchange
%{texmfdist}/tex/latex/comfortaa
%{texmfdist}/tex/latex/concepts
%{texmfdist}/tex/latex/conteq
%{texmfdist}/tex/latex/contracard
%{texmfdist}/tex/latex/cookingsymbols
%{texmfdist}/tex/latex/coolthms
%{texmfdist}/tex/latex/copyrightbox
%{texmfdist}/tex/latex/coseoul
%{texmfdist}/tex/latex/countriesofeurope
%{texmfdist}/tex/latex/counttexruns
%{texmfdist}/tex/latex/cprotect
%{texmfdist}/tex/latex/crbox
%{texmfdist}/tex/latex/csvsimple
%{texmfdist}/tex/latex/cutwin
%{texmfdist}/tex/latex/decorule
%{texmfdist}/tex/latex/dejavu
%{texmfdist}/tex/latex/delim
%{texmfdist}/tex/latex/dhua
%{texmfdist}/tex/latex/diagbox
%{texmfdist}/tex/latex/dirtytalk
%{texmfdist}/tex/latex/documentation
%{texmfdist}/tex/latex/download
%{texmfdist}/tex/latex/dozenal
%{texmfdist}/tex/latex/drawstack
%{texmfdist}/tex/latex/droid
%{texmfdist}/tex/latex/droit-fr
%{texmfdist}/tex/latex/duotenzor
%{texmfdist}/tex/latex/dutchcal
%{texmfdist}/tex/latex/dvgloss
%{texmfdist}/tex/latex/dynblocks
%{texmfdist}/tex/latex/easy-todo
%{texmfdist}/tex/latex/easyfig
%{texmfdist}/tex/latex/ebgaramond
%{texmfdist}/tex/latex/ebook
%{texmfdist}/tex/latex/edfnotes
%{texmfdist}/tex/latex/eiad-ltx
%{texmfdist}/tex/latex/ejpecp
%{texmfdist}/tex/latex/electrum
%{texmfdist}/tex/latex/eledform
%{texmfdist}/tex/latex/eledmac
%{texmfdist}/tex/latex/elteikthesis
%{texmfdist}/tex/latex/emarks
%{texmfdist}/tex/latex/embrac
%{texmfdist}/tex/latex/endiagram
%{texmfdist}/tex/latex/enigma
%{texmfdist}/tex/latex/enotez
%{texmfdist}/tex/latex/enumitem-zref
%{texmfdist}/tex/latex/eqell
%{texmfdist}/tex/latex/eqnarray
%{texmfdist}/tex/latex/esami
%{texmfdist}/tex/latex/esstix
%{texmfdist}/tex/latex/etextools
%{texmfdist}/tex/latex/etoc
%{texmfdist}/tex/latex/everyhook
%{texmfdist}/tex/latex/exceltex
%{texmfdist}/tex/latex/exsheets
%{texmfdist}/tex/latex/exsol
%{texmfdist}/tex/latex/factura
%{texmfdist}/tex/latex/fancytabs
%{texmfdist}/tex/latex/fast-diagram
%{texmfdist}/tex/latex/fbithesis
%{texmfdist}/tex/latex/fcltxdoc
%{texmfdist}/tex/latex/fdsymbol
%{texmfdist}/tex/latex/feynmp-auto
%{texmfdist}/tex/latex/filedate
%{texmfdist}/tex/latex/fileinfo
%{texmfdist}/tex/latex/filemod
%{texmfdist}/tex/latex/finstrut
%{texmfdist}/tex/latex/fixltxhyph
%{texmfdist}/tex/latex/fixmetodonotes
%{texmfdist}/tex/latex/fjodor
%{texmfdist}/tex/latex/flipbook
%{texmfdist}/tex/latex/floatflt
%{texmfdist}/tex/latex/flowchart
%{texmfdist}/tex/latex/fnpct
%{texmfdist}/tex/latex/fnumprint
%{texmfdist}/tex/latex/fontawesome
%{texmfdist}/tex/latex/fontaxes
%{texmfdist}/tex/latex/fonts-tlwg
%{texmfdist}/tex/latex/footnotebackref
%{texmfdist}/tex/latex/footnoterange
%{texmfdist}/tex/latex/foreign
%{texmfdist}/tex/latex/forest
%{texmfdist}/tex/latex/fragments
%{texmfdist}/tex/latex/frege
%{texmfdist}/tex/latex/fullblck
%{texmfdist}/tex/latex/fullwidth
%{texmfdist}/tex/latex/fundus-calligra
%{texmfdist}/tex/latex/fundus-cyr
%{texmfdist}/tex/latex/fundus-sueterlin
%{texmfdist}/tex/latex/gamebook
%{texmfdist}/tex/latex/germkorr
%{texmfdist}/tex/latex/geschichtsfrkl
%{texmfdist}/tex/latex/ghab
%{texmfdist}/tex/latex/gillcm
%{texmfdist}/tex/latex/gincltex
%{texmfdist}/tex/latex/gitinfo
%{texmfdist}/tex/latex/gmdoc-enhance
%{texmfdist}/tex/latex/gmp
%{texmfdist}/tex/latex/gmverse
%{texmfdist}/tex/latex/gradientframe
%{texmfdist}/tex/latex/grafcet
%{texmfdist}/tex/latex/greek-fontenc
%{texmfdist}/tex/latex/gridset
%{texmfdist}/tex/latex/gtrcrd
%{texmfdist}/tex/latex/guitlogo
%{texmfdist}/tex/latex/hacm
%{texmfdist}/tex/latex/hardwrap
%{texmfdist}/tex/latex/harnon-cv
%{texmfdist}/tex/latex/hausarbeit-jura
%{texmfdist}/tex/latex/he-she
%{texmfdist}/tex/latex/here
%{texmfdist}/tex/latex/hf-tikz
%{texmfdist}/tex/latex/hletter
%{texmfdist}/tex/latex/hobby
%{texmfdist}/tex/latex/hobete
%{texmfdist}/tex/latex/horoscop
%{texmfdist}/tex/latex/hrefhide
%{texmfdist}/tex/latex/hvindex
%{texmfdist}/tex/latex/hypernat
%{texmfdist}/tex/latex/idxlayout
%{texmfdist}/tex/latex/ifetex
%{texmfdist}/tex/latex/ifnextok
%{texmfdist}/tex/latex/ifoddpage
%{texmfdist}/tex/latex/ifthenx
%{texmfdist}/tex/latex/iitem
%{texmfdist}/tex/latex/imakeidx
%{texmfdist}/tex/latex/impnattypo
%{texmfdist}/tex/latex/incgraph
%{texmfdist}/tex/latex/inconsolata
%{texmfdist}/tex/latex/inputtrc
%{texmfdist}/tex/latex/interfaces
%{texmfdist}/tex/latex/interval
%{texmfdist}/tex/latex/invoice
%{texmfdist}/tex/latex/ipaex-type1
%{texmfdist}/tex/latex/issuulinks
%{texmfdist}/tex/latex/iwhdp
%{texmfdist}/tex/latex/jamtimes
%{texmfdist}/tex/latex/jlabels
%{texmfdist}/tex/latex/junicode
%{texmfdist}/tex/latex/jvlisting
%{texmfdist}/tex/latex/kantlipsum
%{texmfdist}/tex/latex/kdgdocs
%{texmfdist}/tex/latex/keyreader
%{texmfdist}/tex/latex/keyval2e
%{texmfdist}/tex/latex/kix
%{texmfdist}/tex/latex/koma-moderncvclassic
%{texmfdist}/tex/latex/koma-script-sfs
%{texmfdist}/tex/latex/ktv-texdata
%{texmfdist}/tex/latex/l3experimental/l3dt
%{texmfdist}/tex/latex/l3experimental/l3sort
%{texmfdist}/tex/latex/l3experimental/l3str
%{texmfdist}/tex/latex/l3experimental/xcoffins
%{texmfdist}/tex/latex/l3experimental/xgalley
%{texmfdist}/tex/latex/l3kernel
%{texmfdist}/tex/latex/l3packages/l3keys2e
%{texmfdist}/tex/latex/l3packages/xfrac
%{texmfdist}/tex/latex/l3packages/xparse
%{texmfdist}/tex/latex/l3packages/xtemplate
%{texmfdist}/tex/latex/lapdf
%{texmfdist}/tex/latex/latex2man
%{texmfdist}/tex/latex/latexfileinfo-pkgs
%{texmfdist}/tex/latex/lato
%{texmfdist}/tex/latex/leipzig
%{texmfdist}/tex/latex/lgrx
%{texmfdist}/tex/latex/libgreek
%{texmfdist}/tex/latex/librebaskerville
%{texmfdist}/tex/latex/libris
%{texmfdist}/tex/latex/linegoal
%{texmfdist}/tex/latex/lisp-on-tex
%{texmfdist}/tex/latex/listing
%{texmfdist}/tex/latex/lmake
%{texmfdist}/tex/latex/logbox
%{texmfdist}/tex/latex/logical-markup-utils
%{texmfdist}/tex/latex/logicpuzzle
%{texmfdist}/tex/latex/logreq
%{texmfdist}/tex/latex/longnamefilelist
%{texmfdist}/tex/latex/loops
%{texmfdist}/tex/latex/lpic
%{texmfdist}/tex/latex/lstaddons
%{texmfdist}/tex/latex/ltablex
%{texmfdist}/tex/latex/ltxdockit
%{texmfdist}/tex/latex/ltxkeys
%{texmfdist}/tex/latex/ltxnew
%{texmfdist}/tex/latex/ltxtools
%{texmfdist}/tex/latex/makeshape
%{texmfdist}/tex/latex/mandi
%{texmfdist}/tex/latex/margbib
%{texmfdist}/tex/latex/marginfix
%{texmfdist}/tex/latex/matc3
%{texmfdist}/tex/latex/matc3mem
%{texmfdist}/tex/latex/mathalfa
%{texmfdist}/tex/latex/mathastext
%{texmfdist}/tex/latex/mathspic
%{texmfdist}/tex/latex/mbenotes
%{texmfdist}/tex/latex/mdputu
%{texmfdist}/tex/latex/mdsymbol
%{texmfdist}/tex/latex/media9
%{texmfdist}/tex/latex/meetingmins
%{texmfdist}/tex/latex/memory
%{texmfdist}/tex/latex/menukeys
%{texmfdist}/tex/latex/metalogo
%{texmfdist}/tex/latex/mnotes
%{texmfdist}/tex/latex/moderntimeline
%{texmfdist}/tex/latex/modiagram
%{texmfdist}/tex/latex/monofill
%{texmfdist}/tex/latex/moreenum
%{texmfdist}/tex/latex/morefloats
%{texmfdist}/tex/latex/morehype
%{texmfdist}/tex/latex/morewrites
%{texmfdist}/tex/latex/mpgraphics
%{texmfdist}/tex/latex/msu-thesis
%{texmfdist}/tex/latex/multibibliography
%{texmfdist}/tex/latex/multienv
%{texmfdist}/tex/latex/multiexpand
%{texmfdist}/tex/latex/musixguit
%{texmfdist}/tex/latex/musixtex
%{texmfdist}/tex/latex/musuos
%{texmfdist}/tex/latex/mversion
%{texmfdist}/tex/latex/mwe
%{texmfdist}/tex/latex/mychemistry
%{texmfdist}/tex/latex/mycv
%{texmfdist}/tex/latex/mylatexformat
%{texmfdist}/tex/latex/nameauth
%{texmfdist}/tex/latex/nanumtype1
%{texmfdist}/tex/latex/needspace
%{texmfdist}/tex/latex/nestquot
%{texmfdist}/tex/latex/newenviron
%{texmfdist}/tex/latex/newpx
%{texmfdist}/tex/latex/newtx
%{texmfdist}/tex/latex/newunicodechar
%{texmfdist}/tex/latex/newverbs
%{texmfdist}/tex/latex/nfssext-cfr
%{texmfdist}/tex/latex/nicefilelist
%{texmfdist}/tex/latex/nlctdoc
%{texmfdist}/tex/latex/noconflict
%{texmfdist}/tex/latex/nonumonpart
%{texmfdist}/tex/latex/nowidow
%{texmfdist}/tex/latex/nuc
%{texmfdist}/tex/latex/numberedblock
%{texmfdist}/tex/latex/numericplots
%{texmfdist}/tex/latex/ocg-p
%{texmfdist}/tex/latex/ocgx
%{texmfdist}/tex/latex/opensans
%{texmfdist}/tex/latex/opteng
%{texmfdist}/tex/latex/optional
%{texmfdist}/tex/latex/oscola
%{texmfdist}/tex/latex/othelloboard
%{texmfdist}/tex/latex/outlines
%{texmfdist}/tex/latex/pagecolor
%{texmfdist}/tex/latex/paracol
%{texmfdist}/tex/latex/paratype
%{texmfdist}/tex/latex/parnotes
%{texmfdist}/tex/latex/parselines
%{texmfdist}/tex/latex/parskip
%{texmfdist}/tex/latex/pfarrei
%{texmfdist}/tex/latex/pgf-blur
%{texmfdist}/tex/latex/pgf-umlsd
%{texmfdist}/tex/latex/pgfgantt
%{texmfdist}/tex/latex/pgfkeyx
%{texmfdist}/tex/latex/physics
%{texmfdist}/tex/latex/physymb
%{texmfdist}/tex/latex/piano
%{texmfdist}/tex/latex/piff
%{texmfdist}/tex/latex/pkuthss
%{texmfdist}/tex/latex/poetrytex
%{texmfdist}/tex/latex/poltawski
%{texmfdist}/tex/latex/polyglossia
%{texmfdist}/tex/latex/prerex
%{texmfdist}/tex/latex/prodint
%{texmfdist}/tex/latex/productbox
%{texmfdist}/tex/latex/progressbar
%{texmfdist}/tex/latex/proposal/base
%{texmfdist}/tex/latex/proposal/dfg
%{texmfdist}/tex/latex/proposal/eu
%{texmfdist}/tex/latex/przechlewski-book
%{texmfdist}/tex/latex/pst-am
%{texmfdist}/tex/latex/pst-exa
%{texmfdist}/tex/latex/pst-fit
%{texmfdist}/tex/latex/pst-knot
%{texmfdist}/tex/latex/pst-layout
%{texmfdist}/tex/latex/pst-mirror
%{texmfdist}/tex/latex/pst-node
%{texmfdist}/tex/latex/pst-ode
%{texmfdist}/tex/latex/pst-platon
%{texmfdist}/tex/latex/pst-plot
%{texmfdist}/tex/latex/pst-pulley
%{texmfdist}/tex/latex/pst-rubans
%{texmfdist}/tex/latex/pst-solarsystem
%{texmfdist}/tex/latex/pst-thick
%{texmfdist}/tex/latex/pst-tools
%{texmfdist}/tex/latex/pst-tvz
%{texmfdist}/tex/latex/pst-vectorian
%{texmfdist}/tex/latex/public/rsfso
%{texmfdist}/tex/latex/public/superiors
%{texmfdist}/tex/latex/punk-latex
%{texmfdist}/tex/latex/pxcjkcat
%{texmfdist}/tex/latex/pxgreeks
%{texmfdist}/tex/latex/pxpgfmark
%{texmfdist}/tex/latex/pxtxalfa
%{texmfdist}/tex/latex/python
%{texmfdist}/tex/latex/quattrocento
%{texmfdist}/tex/latex/quoting
%{texmfdist}/tex/latex/raleway
%{texmfdist}/tex/latex/ran_toks
%{texmfdist}/tex/latex/randomwalk
%{texmfdist}/tex/latex/readarray
%{texmfdist}/tex/latex/realboxes
%{texmfdist}/tex/latex/realscripts
%{texmfdist}/tex/latex/rec-thy
%{texmfdist}/tex/latex/regexpatch
%{texmfdist}/tex/latex/regstats
%{texmfdist}/tex/latex/relsize
%{texmfdist}/tex/latex/reotex
%{texmfdist}/tex/latex/resphilosophica
%{texmfdist}/tex/latex/romanbar
%{texmfdist}/tex/latex/romande
%{texmfdist}/tex/latex/romanneg
%{texmfdist}/tex/latex/rrgtrees
%{texmfdist}/tex/latex/rterface
%{texmfdist}/tex/latex/russ
%{texmfdist}/tex/latex/rviewport
%{texmfdist}/tex/latex/rvwrite
%{texmfdist}/tex/latex/sa-tikz
%{texmfdist}/tex/latex/sansmath
%{texmfdist}/tex/latex/sansmathaccent
%{texmfdist}/tex/latex/sansmathfonts
%{texmfdist}/tex/latex/sapthesis
%{texmfdist}/tex/latex/sasnrdisplay
%{texmfdist}/tex/latex/scalerel
%{texmfdist}/tex/latex/schulschriften
%{texmfdist}/tex/latex/schwalbe-chess
%{texmfdist}/tex/latex/scrjrnl
%{texmfdist}/tex/latex/secdot
%{texmfdist}/tex/latex/section
%{texmfdist}/tex/latex/sepfootnotes
%{texmfdist}/tex/latex/sepnum
%{texmfdist}/tex/latex/serbian-apostrophe
%{texmfdist}/tex/latex/serbian-date-lat
%{texmfdist}/tex/latex/serbian-def-cyr
%{texmfdist}/tex/latex/serbian-lig
%{texmfdist}/tex/latex/setdeck
%{texmfdist}/tex/latex/shadow
%{texmfdist}/tex/latex/shadowtext
%{texmfdist}/tex/latex/showcharinbox
%{texmfdist}/tex/latex/showtags
%{texmfdist}/tex/latex/sidenotes
%{texmfdist}/tex/latex/sitem
%{texmfdist}/tex/latex/skb
%{texmfdist}/tex/latex/skdoc
%{texmfdist}/tex/latex/skmath
%{texmfdist}/tex/latex/skrapport
%{texmfdist}/tex/latex/smartdiagram
%{texmfdist}/tex/latex/snotez
%{texmfdist}/tex/latex/songs
%{texmfdist}/tex/latex/sourcecodepro
%{texmfdist}/tex/latex/sourcesanspro
%{texmfdist}/tex/latex/spanglish
%{texmfdist}/tex/latex/spath3
%{texmfdist}/tex/latex/sphack
%{texmfdist}/tex/latex/spot
%{texmfdist}/tex/latex/srbook-mem
%{texmfdist}/tex/latex/standalone
%{texmfdist}/tex/latex/starfont
%{texmfdist}/tex/latex/statex
%{texmfdist}/tex/latex/storebox
%{texmfdist}/tex/latex/storecmd
%{texmfdist}/tex/latex/subfigmat
%{texmfdist}/tex/latex/subfiles
%{texmfdist}/tex/latex/substances
%{texmfdist}/tex/latex/substitutefont
%{texmfdist}/tex/latex/suftesi
%{texmfdist}/tex/latex/svg
%{texmfdist}/tex/latex/swimgraf
%{texmfdist}/tex/latex/tabfigures
%{texmfdist}/tex/latex/tablefootnote
%{texmfdist}/tex/latex/tableof
%{texmfdist}/tex/latex/tabriz-thesis
%{texmfdist}/tex/latex/tabu
%{texmfdist}/tex/latex/tabularborder
%{texmfdist}/tex/latex/tagging
%{texmfdist}/tex/latex/tamefloats
%{texmfdist}/tex/latex/tcolorbox
%{texmfdist}/tex/latex/tex-label
%{texmfdist}/tex/latex/texilikechaps
%{texmfdist}/tex/latex/textglos
%{texmfdist}/tex/latex/textgreek
%{texmfdist}/tex/latex/tfrupee
%{texmfdist}/tex/latex/threadcol
%{texmfdist}/tex/latex/threeparttable
%{texmfdist}/tex/latex/thumbs
%{texmfdist}/tex/latex/tikz-cd
%{texmfdist}/tex/latex/tikz-dependency
%{texmfdist}/tex/latex/tikz-qtree
%{texmfdist}/tex/latex/tikzinclude
%{texmfdist}/tex/latex/tikzmark
%{texmfdist}/tex/latex/tikzorbital
%{texmfdist}/tex/latex/tikzpagenodes
%{texmfdist}/tex/latex/tikzpfeile
%{texmfdist}/tex/latex/tikzposter
%{texmfdist}/tex/latex/tikzscale
%{texmfdist}/tex/latex/tikzsymbols
%{texmfdist}/tex/latex/titlecaps
%{texmfdist}/tex/latex/titleref
%{texmfdist}/tex/latex/tkz-base
%{texmfdist}/tex/latex/tkz-berge
%{texmfdist}/tex/latex/tkz-euclide
%{texmfdist}/tex/latex/tkz-fct
%{texmfdist}/tex/latex/tkz-graph
%{texmfdist}/tex/latex/tkz-kiviat
%{texmfdist}/tex/latex/tkz-orm
%{texmfdist}/tex/latex/tqft
%{texmfdist}/tex/latex/tram
%{texmfdist}/tex/latex/tsemlines
%{texmfdist}/tex/latex/tucv
%{texmfdist}/tex/latex/tui
%{texmfdist}/tex/latex/turkmen
%{texmfdist}/tex/latex/turnthepage
%{texmfdist}/tex/latex/txgreeks
%{texmfdist}/tex/latex/typeface
%{texmfdist}/tex/latex/uadocs
%{texmfdist}/tex/latex/uafthesis
%{texmfdist}/tex/latex/uestcthesis
%{texmfdist}/tex/latex/uiucredborder
%{texmfdist}/tex/latex/ulthese
%{texmfdist}/tex/latex/unamthesis
%{texmfdist}/tex/latex/underoverlap
%{texmfdist}/tex/latex/uni-wtal-ger
%{texmfdist}/tex/latex/uni-wtal-lin
%{texmfdist}/tex/latex/unswcover
%{texmfdist}/tex/latex/uothesis
%{texmfdist}/tex/latex/uowthesis
%{texmfdist}/tex/latex/uri
%{texmfdist}/tex/latex/url
%{texmfdist}/tex/latex/urwchancal
%{texmfdist}/tex/latex/usebib
%{texmfdist}/tex/latex/uspatent
%{texmfdist}/tex/latex/uwmslide
%{texmfdist}/tex/latex/vdmlisting
%{texmfdist}/tex/latex/venndiagram
%{texmfdist}/tex/latex/verbasef
%{texmfdist}/tex/latex/verbdef
%{texmfdist}/tex/latex/verbments
%{texmfdist}/tex/latex/vocaltract
%{texmfdist}/tex/latex/wnri-latex
%{texmfdist}/tex/latex/xcite
%{texmfdist}/tex/latex/xcookybooky
%{texmfdist}/tex/latex/xhfill
%{texmfdist}/tex/latex/xltxtra
%{texmfdist}/tex/latex/xpatch
%{texmfdist}/tex/latex/xpeek
%{texmfdist}/tex/latex/xpicture
%{texmfdist}/tex/latex/xpinyin
%{texmfdist}/tex/latex/xpunctuate
%{texmfdist}/tex/latex/ytableau
%{texmfdist}/tex/latex/zhnumber
%{texmfdist}/tex/latex/zxjafbfont
%{texmfdist}/tex/latex/zxjafont
%{texmfdist}/tex/latex/zxjatype
%{texmfdist}/tex/platex/base
%{texmfdist}/tex/platex/config
%{texmfdist}/tex/platex/japanese
%{texmfdist}/tex/platex/japanese-otf
%{texmfdist}/tex/platex/japanese-otf-uptex
%{texmfdist}/tex/platex/jsclasses
%{texmfdist}/tex/platex/pxbase
%{texmfdist}/tex/platex/pxchfon
%{texmfdist}/tex/platex/pxjahyper
%{texmfdist}/tex/platex/pxrubrica
%{texmfdist}/tex/startex/base
%{texmfdist}/tex/support/adhocfilelist
%dir %{texmfdist}/tex/texsis
%{texmfdist}/tex/texsis/base
%{texmfdist}/tex/texsis/config/texsis.ini
%{texmfdist}/tex/uplatex/base
%{texmfdist}/tex/uplatex/config/uplatex.ini
%{texmfdist}/tex/uptex/base
%{texmfdist}/tex/uptex/config/euptex.ini
%{texmfdist}/tex/uptex/config/uptex.ini
%{texmfdist}/tex/xmltex/base
%{texmfdist}/tex/xmltex/config/pdfxmltex.ini
%{texmfdist}/tex/xmltex/config/xmltex.ini
%{texmfdist}/tex/xmltex/passivetex
%{texmfdist}/texconfig
%{texmfdist}/texdoc
%{texmfdist}/texdoctk
%{texmfdist}/ttf2pk
%{texmfdist}/web2c/fmtutil-hdr.cnf
%{texmfdist}/web2c/fmtutil.cnf
%{texmfdist}/web2c/mktex.cnf
%{texmfdist}/web2c/mktex.opt
%{texmfdist}/web2c/mktexdir
%{texmfdist}/web2c/mktexdir.opt
%{texmfdist}/web2c/mktexnam
%{texmfdist}/web2c/mktexnam.opt
%{texmfdist}/web2c/mktexupd
%{texmfdist}/web2c/texmf.cnf
%{texmfdist}/web2c/texmfcnf.lua
%{texmfdist}/web2c/updmap-hdr.cfg
%{texmfdist}/web2c/updmap.cfg

%{texmfdist}/xdvi/XDvi
%{texmfdist}/xdvi/pixmap/toolbar.xpm
%{texmfdist}/xdvi/pixmap/toolbar2.xpm
%{texmfdist}/doc/bibtex/vancouver/FAQ
%{texmfdist}/doc/bibtex/vancouver/vancouver.bib
%{texmfdist}/doc/fonts/newtx/README
%{texmfdist}/doc/fonts/newtx/implementation.pdf
%{texmfdist}/doc/fonts/newtx/implementation.tex
%{texmfdist}/doc/fonts/newtx/newtxdoc.pdf
%{texmfdist}/doc/fonts/newtx/newtxdoc.tex
%{texmfdist}/doc/fonts/newtx/sample-lib-crop.pdf
%{texmfdist}/doc/fonts/newtx/sample-libmtp-crop.pdf
%{texmfdist}/doc/fonts/newtx/sample-mtp-crop.pdf
%{texmfdist}/doc/fonts/newtx/sample-ntx-crop.pdf
%{texmfdist}/doc/fonts/newtx/sample-ptmx-crop.pdf
%{texmfdist}/doc/fonts/newtx/sample-tx-crop.pdf
%{texmfdist}/doc/fonts/ocr-b/README
%{texmfdist}/doc/latex/hyper/README
%{texmfdist}/doc/latex/hyper/TODO
%{texmfdist}/doc/latex/hyper/contrib/README
%{texmfdist}/doc/latex/hyper/contrib/harvard-to.hyp
%{texmfdist}/doc/latex/hyper/defpattern.sty
%{texmfdist}/doc/latex/hyper/hyper.pdf
%{texmfdist}/doc/latex/hyper/scontrib/README
%{texmfdist}/doc/latex/hyper/scontrib/harvard.hyp
%{texmfdist}/doc/man/Makefile
%{texmfdist}/doc/pdftex/Announcement-1.40.2
%{texmfdist}/doc/pdftex/NEWS
%{texmfdist}/doc/pdftex/README
%{texmfdist}/doc/texlive/index.html
%{texmfdist}/metapost/mpout.log
%{texmfdist}/scripts/texlive/NEWS
%attr(755,root,root) %{texmfdist}/scripts/texlive/test-tlpdb.tlu
%attr(755,root,root) %{texmfdist}/scripts/texlive/texconf.tlu
%attr(755,root,root) %{texmfdist}/scripts/texlive/tlmgrgui.pl
%attr(755,root,root) %{texmfdist}/scripts/texlive/uninstall-win32.pl
%{texmfdist}/tex/latex/latexconfig/color.cfg
%{texmfdist}/tex/latex/latexconfig/dvilualatex.ini
%{texmfdist}/tex/latex/latexconfig/epstopdf-sys.cfg
%{texmfdist}/tex/latex/latexconfig/lualatex-patch-kernel.tex
%{texmfdist}/tex/latex/latexconfig/lualatex-reset-codes.tex
%{texmfdist}/tex/latex/latexconfig/lualatexiniconfig.tex
%{texmfdist}/tex/latex/latexconfig/lualatexquotejobname.lua
%{texmfdist}/tex/latex/latexconfig/lualatexquotejobname.tex
%{texmfdist}/tex/plain/config/xetex.ini

%{texmfdist}/doc/xindy
%{texmfdist}/xindy
%{texmfdist}/scripts/xindy

# move to standard locations
%{texmfdist}/doc/info
%{texmfdist}/doc/man/man1
%{texmfdist}/doc/man/man5
