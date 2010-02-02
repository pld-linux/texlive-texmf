# TODO:
# - latex subpackage (maybe rename latex-base and texlive-latex requires latex-base)
# - maybe tex4ht-data splitting
# - consider format-files where to create (texlive or texlive-texmf)

%include	/usr/lib/rpm/macros.perl
# Conditional build:
%bcond_with	bootstrap	# bootstrap build

%define shortname texlive

#
%define		year 2009
%define		monthday 1107
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
Release:	1
Epoch:		1
License:	distributable
Group:		Applications/Publishing/TeX
Source0:	ftp://tug.org/texlive/historic/%{year}/texlive-%{version}-texmf.tar.xz
# Source0-md5:	5c6b33235ab3330626f58ca665d53a3c
Source1:	http://mirror.ctan.org/language/hungarian/babel/magyar.ldf
# Source1-md5:	3a5792398d46e6a6e70ef5006c4a2e55
Source10:	http://tug.ctan.org/get/macros/latex/contrib/floatflt.zip
# Source10-md5:	5d9fe14d289aa81ebb6b4761169dd5f2
Source11:	http://carme.pld-linux.org/~uzsolt/sources/texlive-fonts-larm.tar.bz2
# Source11-md5:	df2fcc66f0c2e90785ca6c9b27dacd34
Source12:	http://www.ctan.org/get/macros/latex/contrib/foiltex.zip
# Source12-md5:	0a6b4e64fb883a68d9b288bf3421db25
Source50:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/Splashscreen.pm
# Source50-md5:	5cc49f49010f27fdb02dd7053797ba19
Source51:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLConfig.pm
# Source51-md5:	947ee29c38c2c2cfd9a25c597a89598a
Source52:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLMedia.pm
# Source52-md5:	9f1e76f3528125691edd4fbcdd69c5cb
Source53:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPDB.pm
# Source53-md5:	47cae437999e98a7bd24f27db7b0fa34
Source54:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPOBJ.pm
# Source54-md5:	c573c407ae3d98f710d65d593a7d1745
Source55:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPSRC.pm
# Source55-md5:	834ae0ac5c59fd00ab6000ba6367a987
Source56:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPaper.pm
# Source56-md5:	326314fc034a5d9ef9d4a60033f7186f
Source57:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLPostActions.pm
# Source57-md5:	17c1968725ccf4aaafb7162b7b3609fc
Source58:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLTREE.pm
# Source58-md5:	039cc8878f380cab3b0beffe75870c6c
Source59:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLUtils.pm
# Source59-md5:	2d9a84f406da62d676b495c4f10c1adc
Source60:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TLWinGoo.pm
# Source60-md5:	825121187994692ecda0f48a5b17421a
Source61:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/TeXCatalogue.pm
# Source61-md5:	6289d93a12aa246fc2019b0109d2167f
Source62:	http://sunsite2.icm.edu.pl/pub/tex/systems/texlive/tlnet/2008/tlpkg/TeXLive/waitVariableX.pm
# Source62-md5:	f0fa0f2fc7aacb1e9b40eb65891a24c8
URL:		http://www.tug.org/texlive/
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
%if %{without bootstrap}
BuildRequires:	%{shortname}-context
BuildRequires:	%{shortname}-csplain
BuildRequires:	%{shortname}-fonts-cmsuper
BuildRequires:	%{shortname}-format-eplain
BuildRequires:	%{shortname}-format-mex
BuildRequires:	%{shortname}-format-pdflatex
BuildRequires:	%{shortname}-latex
BuildRequires:	%{shortname}-latex-cyrillic
BuildRequires:	%{shortname}-metapost
BuildRequires:	%{shortname}-mex
BuildRequires:	%{shortname}-omega
BuildRequires:	%{shortname}-other-utils
BuildRequires:	%{shortname}-pdftex
BuildRequires:	%{shortname}-phyzzx
BuildRequires:	%{shortname}-plain
BuildRequires:	%{shortname}-tex-babel
BuildRequires:	%{shortname}-tex-physe
BuildRequires:	%{shortname}-xetex
BuildRequires:	%{shortname}-xmltex
BuildRequires:	/usr/bin/latex
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

%package -n texlive-dvips-data
Summary:	Texmf files needed for texlive-dvips
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-dvips-data
Texmf files needed for texlive-dvips.

%package -n texlive-omega-data
Summary:	Texmf files needed for texlive-omega
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash

%description -n texlive-omega-data
Texmf files needed for texlive-omega.

%package -n texlive-scripts
Summary:	Various scripts
Summary(hu.UTF-8):	Néhány szkript
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}

%description -n texlive-scripts
Various scripts.

%description -n texlive-scripts -l hu.UTF-8
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
- addlines: a user-friendly wrapper around \enlargethispage.
- alnumsec: alphanumeric section numbering.
- arydshln: horizontal and vertical dashed lines in arrays and
  tabulars
- babelbib: multilingual bibliographies.
- bibtopicprefix: prefix references to bibliographies produced by
  bibtopic.
- boites: boxes that may break across pages
- booklet: aids for printing simple booklets.
- bullcntr: display list item counter as regular pattern of bullets.
- chappg: page numbering by chapter.
- cjw: a bundle of packages and classes.
- clefval: key/value support with a hash.
- colortbl: add colour to LaTeX tables.
- combine: bundle individual documents into a single document.
- contour: print a coloured contour around text.
- ctable: easily typeset centered tables.
- curve2e: extensions for package pict2e.
- dashbox: draw dashed boxes.
- dashline: draw dashed rules.
- etaremune: reverse-counting enumerate environment.
- expdlist: expanded description environments.
- HA-prosper: patches and improvements for prosper.
- leading: define leading with a length.
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
- multicap: format captions inside multicols
- newvbtm: define your own verbatim-like environment.
- notes2bib: integrating notes into the bibliography.
- ntabbing: simple tabbing extension for automatic line numbering.
- numline: LaTeX macros for numbering lines.
- pbox: a variable-width \parbox command.
- pinlabel: a TeX labelling package.
- polytable: tabular-like environments with named columns.
- rccol: decimal-centered optionally rounded numbers in tabular.
- romannum: generate roman numerals instead of arabic digits.
- schedule: weekly schedules.
- subfloat: sub-numbering for figures and tables.
- umoline: underline text allowing line breaking.
- umrand: package for fancy box frames.
- underlin: underlined running heads.
- ushort: shorter (and longer) underlines and underbars.

%description -n texlive-latex-extend -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- addlines: felhasználóbarát wrapper \enlargethispage-hez
- alnumsec: alfanumerikus section számozás
- arydshln: vízszintes és függőleges pontozott vonalak array és
  tabular környezetkben
- babelbib: többnyelvű bibliográfiák
- bibtopicprefix: prefix hivatkozás bibtopic által készített
  bibliográfiára
- boites: dobozok, amelyek törhetők oldalak között
- booklet: booklet formátumban történő nyomtatás
- bullcntr: lista elemek számlálójának megjelenítése mint...
- chappg: oldalszámozás chapter alapján
- cjw: csomagok és osztályok tömkelege
- clefval: kulcs/érték párok hash-sel
- colortbl: színek LaTeX táblázatokban
- combine: külön dokumentumok eggyé fűzése
- contour: színes kontúr nyomtatása szöveg körül
- ctable: középre igazított táblázatok szedése
- curve2e: pict2e csomaghoz kiegészítések
- dashbox: pontozott dobozok
- dashline: pontozott vonalak
- etaremune: visszafele sorszámazó enumerate környezet
- expdlist: kibővített description környezetek
- HA-prosper: foltok és bővítések a prosper-hez
- leading: sorközök definiálása hosszal
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
- multicap: formázott cimkék multicols környezetben
- newvbtm: saját verbatim-szerű környezetek
- notes2bib: megjegyzések elhelyezése bibliográfiába
- ntabbing: tabbing környezet automatikus sorszámozással
- numline: LaTeX makrók sorok számozására
- pbox: változtatható szélességű \parbox
- pinlabel: a TeX labelling package.
- polytable: tabular-like environments with named columns.
- rccol: decimal-centered optionally rounded numbers in tabular.
- romannum: generate roman numerals instead of arabic digits.
- schedule: heti időbeosztás (órarend)
- subfloat: sub-numbering for figures and tables.
- umoline: aláhúzott szövegben sortörés engedélyezése
- umrand: package for fancy box frames.
- underlin: aláhúzott élőfej
- ushort: shorter (and longer) underlines and underbars.

%package -n texlive-latex-effects
Summary:	Additional effects to fonts, texts
Summary(hu.UTF-8):	További effektek betűkhöz, szövegekhez,...
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-effects
This package contains:
- arcs: draw arcs over and under text
- blowup: upscale or downscale all pages of a document.
- changebar: generate changebars in LaTeX documents.
- draftwatermark: put a grey textual watermark on document pages.
- flippdf: horizontal flipping of pages with pdfLaTeX.
- flowfram: create text frames for posters, brochures or magazines.
- isorot: rotation of document elements.
- lettrine: typeset dropped capitals.
- niceframe: support for fancy frames.
- notes: mark sections of a document.
- objectz: macros for typesetting Object Z.
- parallel: typeset parallel texts.
- quotchap: decorative chapter headings.
- rotpages: typeset sets of pages upside-down and backwards.
- sectionbox: create fancy boxed ((sub)sub)sections.
- shadethm: theorem environments that are shaded

%description -n texlive-latex-effects -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- arcs: ívek rajzolása szöveg fölé és alá
- blowup: a dokumentum összes oldalának nagyítása vagy kicsinyítése
- changebar: oldalsávok készítése LaTeX dokumentumokban
- draftwatermark: szürke szöveges vízjel a dokumentum oldalaira
- flippdf: oldalak vízszintes tükrözése pdfLaTeX-hel
- flowfram: szövegkeretek poszterekhez, brossúrákhoz vagy magazinokhoz
- isorot: dokumentum-elemek forgatása
- lettrine: ejtett kapitálisok szedése
- niceframe: különféle keretek
- notes: dokumentum részeinek kiemelése, megjelölése
- objectz: Object Z objektumok szedése
- parallel: párhuzamos szövegek szedése
- quotchap: decorative chapter headings.
- rotpages: typeset sets of pages upside-down and backwards.
- sectionbox: create fancy boxed ((sub)sub)sections.
- shadethm: theorem environments that are shaded

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
- bez123: Support for Bezier curves.
- binomexp: Calculate Pascal's triangle
- cmll: symbols for linear logic.
- constants: automatic numbering of constants.
- coordsys: draw cartesian coordinate systems.
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
- gnuplottex: embed Gnuplot commands in LaTeX documents.
- hhtensor: print vectors, matrices, and tensors.
- logpap: generate logarithmic graph paper with LaTeX.
- makeplot: easy plots from Matlab in LaTeX.
- maybemath: make math bold or italic according to context.
- mfpic4ode: macros to draw direction fields and solutions of ODEs.
- mhequ: multicolumn equations, tags, labels, sub-numbering.
- mhs: historical mathematics.
- mlist: logical markup for lists.
- nath: natural mathematics notation.
- noitcrul: improved underlines in mathematics.
- numprint: print numbers with separators and exponent if necessary.
- permute: support for symmetric groups.
- petri-nets: A set TeX/LaTeX packages for drawing Petri nets.
- qsymbols: maths symbol abbreviations.
- qtree: draw tree structures.
- sdrt: macros for Segmented Discourse Representation Theory.
- semantic: help for writing programming language semantics.
- simplewick: simple Wick contractions.
- sseq: spectral sequence diagrams.
- subdepth: unify maths subscript height.
- subeqn: package for subequation numbering.
- subeqnarray: equation array with sub numbering.
- tree-dvips: trees and other linguists' macros.
- trfsigns: typeset transform signs.
- trsym: symbols for transformations.
- ulsy: extra mathematical characters.

%description -n texlive-latex-math -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- bez123: Bezier-görbék
- binomexp: Pascal-háromszög számítása
- cmll: szimbólumok lineáris logikához
- constants: változók automatikus sorszámozása
- coordsys: Descartes-féle koordinátarendszerek rajzolása
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
- gnuplottex: Gnuplot parancsok beágyazása LaTeX dokumentumokba
- hhtensor: vetkorok, mátrixok és tenzorok nyomtatása
- logpap: logaritmikus grafikonok
- makeplot: könnyű ábrázolások Matlab-ból LaTeX-be
- maybemath: matematikai félkövér ill. dőlt szöveg környezettől
  függően
- mfpic4ode: differenciálegyenletek megoldásainak ábrázolása
- mhequ: többoszlopos egyenletek, cimkék, al-sorszámozás
- mhs: történelmi matematika
- mlist: listák logikus jelölése
- nath: természetes matematikai jelölés
- noitcrul: kibővített aláhúzások matematikában
- numprint: számok írása elválasztókkal és kitevőkkel, ha szükséges
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
- cooking: typeset recipes.
- cuisine: typeset recipes.
- fixme: insert "fixme" notes into draft documents.
- recipecard: typeset recipes in note-card-sized boxes.
- todo: make a to-do list for a document.

%description -n texlive-latex-misc -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- cooking: receptek szedése
- cuisine: receptek szedése
- fixme: "fixme" megjegyzések elhelyezése
- recipecard: receptek szedése jegyzet-méretű dobozokba
- todo: dokumentumok teendőinek listája

%package -n texlive-latex-music
Summary:	Musical packages
Summary(hu.UTF-8):	Zenei csomagok
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}-latex

%description -n texlive-latex-music
This package contains:
- abc: support ABC music notation in LaTeX.
- guitar: guitar chords and song texts.
- songbook: package for typesetting song lyrics and chord books.

%description -n texlive-latex-music -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- abc: ABC hangjegyzések LaTeX-ben
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
- circ: macros for typesetting circuit diagrams.
- colorwav: colours by wavelength of visible light.
- dyntree: construct Dynkin tree diagrams.
- feynmf: macros and fonts for creating Feynman (and other) diagrams.
- formula: typesetting physical units.
- isotope: a package for type setting isotopes
- listofsymbols: create and manipulate lists of symbols
- miller: typeset miller indices.
- susy: macros for SuperSymmetry-related work.

%description -n texlive-latex-physics -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- circ: áramkörök szedése
- colorwav: a látható fény színei hullámhossz szerint
- dyntree: Dynkin fadiagramok készítése
- feynmf: makrók és fontok Feynman (és más) diagramok készítésére
- formula: fizikai egységek szedése
- isotope: izotópok szedése
- listofsymbols: szimbólumok listájának létrehozása és kezelése
- miller: miller indexek szedése
- susy: Szuper-Szimmetria elmélettel kapcsolatos munkákhoz makrók

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
- lsc: typesetting Live Sequence Charts.
- method: typeset method and variable declarations.
- msc: draw MSC diagrams.
- nag: detecting and warning about obsolete LaTeX commands
# - progkeys: typeset programs, recognising keywords.
- register: typeset programmable elements in digital hardware
  (registers).
- uml: UML diagrams in LaTeX.

%description -n texlive-latex-informatic -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- alg: LaTeX környezetek algoritmusok szedésére
- bytefield: hálózati protokoll specifikációk szemléltetése
- lsc: Live Sequence Charts
- method: eljárások és változók deklarációjának szedése
- msc: MSC diagramok
- nag: elavult LaTeX parancsok detektálása és figyelmeztetés
# - progkeys: programok szedése, kulcsszavakkal
- register: programozható elemek (regiszterek) szedése
- uml: UML diagramok LaTeX-ben

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
- movie15: multimedia inclusion package.
- pdfcprot: activating and setting of character protruding using
  pdflatex.
- pdfsync: provide links between source and PDF.
- pdftricks: support for pstricks in pdfTeX. . pdfscreen: support
  screen-based document design.

%description -n texlive-latex-pdftools -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- attachfile: fájlok csatolása PDF dokumentumokba
- cooltooltips: felugró ablakok és súgók társítása PDF linkekhez
- movie15: multimédia beillesztése
- pdfcprot: activating and setting of character protruding using
  pdflatex.
- pdftricks: pstricks támogatás pdfTeX-ben
- pdfsync: provide links between source and PDF.
- pdfscreen: képernyő alapú dokumentumok

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
- cmdtrack: check used commands.
- cool: COntent-Oriented LaTeX
- coollist: manipulate COntent Oriented LaTeX Lists.
- coolstr: string manipulation in LaTeX.
- csvtools: reading data from CSV files.
- datatool: tools to load and manipulate data.
- datenumber: convert a date into a number and vice versa.
- delimtxt: read and parse text tables.
- dialogl: macros for constructing interactive LaTeX scripts.
- dprogress: LaTeX-relevant log information for debugging.
- environ: a new interface for environments in LaTeX.
- export: import and export values of LaTeX registers.
- fmtcount: display the value of a LaTeX counter in a variety of
  formats.
- forarray: using array structures in LaTeX.
- forloop: iteration in LaTeX.
- inversepath: calculate inverse file paths.
- labelcas: check the existence of labels, and fork accordingly.
- lcg: generate random integers.
- makecmds: the new \makecommand command always (re)defines a command.
- multido: a loop facility for Generic TeX.
- namespc: rudimentary c++-like namespaces in LaTeX.
- patchcmd: change the definition of an existing command.
- progress: creates an overview of a document's state.
- randtext: randomise the order of characters in strings.
- regcount: display the allocation status of the TeX registers.
- robustcommand: declare robust command, with \newcommand checks.
- splitindex: unlimited number of indexes.
- stack: tools to define and use stacks.
- stringstrings: string manipulation for cosmetic and programming
  application
- substr: deal with substrings in strings.
- typedref: eliminate errors by enforcing the types of labels.

%description -n texlive-latex-programming -l hu.UTF-8
Ez a csomag a következőket tartalmazza:
- cmdtrack: használt parancsok ellenőrzése
- cool: tartalom-orientált (COntent-Oriented) LaTeX
- coollist: COntent Oriented LaTeX listák manipulációja
- coolstr: sztring manipuláció LaTeX-ben
- csvtools: adatok olvasása CSV fájlokból
- datatool: eszközök adatok beolvasására és manipulációjához
- datenumber: dátum számmá konvertálása és vissza
- delimtxt: szöveges táblázatok olvasása és feldolgozása
- dialogl: interaktív makrók LaTeX-ben
- dprogress: LaTeX-releváns log információ debuggoláshoz
- export: LaTeX regiszterek értékeinek importálása és exportálása
- environ: egy új felület környezetek létrehozására
- fmtcount: LaTeX számlálók megjelenítése különböző formátumokban
- forarray: tömb struktúrák LaTeX-ben
- forloop: iteráció LaTeX-ben
- inversepath: fájlútvonalak visszafele relatív meghatározása
- labelcas: cimkék létezésének ellenőrzése
- lcg: véletlen egész számok generálása
- makecmds: új \makecommand, amely mindig (újra)definiál parancsot
- multido: ciklusok szervezése LaTeX-ben
- namespc: c++-szerű névterek LaTeX-ben
- patchcmd: létező parancsok definíciójának megváltoztatása
- progress: egy áttekintést készít a dokumentum állapotáról
- randtext: sztring karaktereinek összekeverése
- regcount: display the allocation status of the TeX registers.
- robustcommand: declare robust command, with \newcommand checks.
- splitindex: unlimited number of indexes.
- stack: verem használata
- stringstrings: sztring manipuláció
- substr: részszövegek keresése
- typedref: eliminate errors by enforcing the types of labels.

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

%package -n texlive-latex-vietnam
Summary:	Vietnamese language support
Summary(pl.UTF-8):	Wsparcie dla języka wietnamskiego
Group:		Applications/Publishing/TeX
Requires(post,postun):	%{_bindir}/texhash
Requires:	%{shortname}
Obsoletes:	tetex-latex-urwvn
Obsoletes:	tetex-latex-vietnam
Obsoletes:	tetex-tex-vietnam

%description -n texlive-latex-vietnam
Vietnamese language support.

%description -n texlive-latex-vietnam -l pl.UTF-8
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
Obsoletes:	tetex-fonts-bitstrea

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

%package -n texlive-fonts-urwvn
Summary:	URWVN fonts
Summary(pl.UTF-8):	Fonty URWVN
Group:		Fonts
Requires:	%{shortname}-dirs-fonts
Obsoletes:	tetex-fonts-urwvn

%description -n texlive-fonts-urwvn
URWVN fonts.

%description -n texlive-fonts-urwvn -l pl.UTF-8
Fonty URWVN.

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

xz -dc %{SOURCE0} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-%{version}-texmf/texmf $RPM_BUILD_ROOT%{texmf}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-%{version}-texmf/texmf-dist $RPM_BUILD_ROOT%{texmfdist}
# %{__mv} $RPM_BUILD_ROOT%{_datadir}/texlive-%{version}-texmf/texmf-doc $RPM_BUILD_ROOT%{texmfdoc}
%{__mv} $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots/* $RPM_BUILD_ROOT%{texmfdist}/doc/latex/pgfplots
rmdir $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pgfplots
# imho it is unneeded
%{__rm} -r $RPM_BUILD_ROOT%{texmfdist}/doc/fonts/{ec,fc,utopia}
%{__rm} -r $RPM_BUILD_ROOT%{texmf}/doc/cefconv

# This is an empty directory
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/texlive-%{version}-texmf
# Useless binary
# %{__rm} $RPM_BUILD_ROOT%{_datadir}/texmf-dist/doc/latex/splitindex/splitindex{.exe,-Linux-i386,-OpenBSD-i386}

# commented out because of following (non-fatal) error:
# Can't open texmf/web2c/texmf.cnf: No such file or directory.
#perl -pi \
#	-e "s|\.\./\.\./texmf|$RPM_BUILD_ROOT%{texmf}|g;" \
#	-e "s|/var/cache/fonts|$RPM_BUILD_ROOT/var/cache/fonts|g;" \
#	texmf/web2c/texmf.cnf

install -d $RPM_BUILD_ROOT%{texmf}/fonts/opentype/public
%{__rm} $RPM_BUILD_ROOT%{texmf}/scripts/texlive/uninstall-win32.pl

CURDIR=$(pwd)

# install magyar.ldf
install %{SOURCE1} $RPM_BUILD_ROOT%{texmfdist}/tex/generic/babel

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE50} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE51} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE52} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE53} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE54} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE55} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE56} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE57} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE58} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE59} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE60} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE61} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive
install %{SOURCE62} $RPM_BUILD_ROOT%{perl_vendorlib}/TeXLive

cd $RPM_BUILD_ROOT%{texmfdist}/tex/latex

%if %{without bootstrap}
# floatflt
unzip %{SOURCE10}
cd floatflt
latex floatflt.ins
%{__rm} *.log
install -d $RPM_BUILD_ROOT%{texmfdist}/doc/latex/floatflt
%{__mv} *.txt *.tex *.pdf README $RPM_BUILD_ROOT%{texmfdist}/doc/latex/floatflt
cd ..

# foiltex
unzip %{SOURCE12}
cd foiltex
latex foiltex.ins
%{__rm} *.log
install -d $RPM_BUILD_ROOT%{texmfdist}/doc/latex/foiltex
%{__mv} *.tex *.pdf README $RPM_BUILD_ROOT%{texmfdist}/doc/latex/foiltex
cd ..

# wrong dvi in formlett, should be regenerate
cd $RPM_BUILD_ROOT%{texmfdist}/doc/latex/formlett
cp $RPM_BUILD_ROOT%{texmfdist}/tex/latex/formlett/formlett.sty .
tex user_manual.tex
yes | tex prog_manual.tex
tex example1.tex
tex example2.tex
rm formlett.sty
%endif

# larm fonts
cd $RPM_BUILD_ROOT%{texmfdist}
tar xvf %{SOURCE11}
cd fonts/tfm/la
for i in larm?00.tfm; do ln -s $i $(echo $i | sed "s@larm\(.\).*@larm0\100.tfm@") ; done

cd $CURDIR

# some tex-files need xstring.tex and doc/latex isn't in kpathsea search path
# cp $RPM_BUILD_ROOT%{texmfdist}/doc/latex/xstring/xstring.tex $RPM_BUILD_ROOT%{texmfdist}/tex/latex/xstring

#install %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}
#touch $RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap/maps.lst

# We don't need it
%{__rm} -rf $RPM_BUILD_ROOT%{texmf}/doc/man
%{__rm} -rf $RPM_BUILD_ROOT%{texmfdoc}/source

perl -pi \
	-e "s|$RPM_BUILD_ROOT||g;" \
	$RPM_BUILD_ROOT%{texmf}/web2c/texmf.cnf

# not included in package
rm -f $RPM_BUILD_ROOT%{_datadir}/texinfo/html/texi2html.html
rm -f $RPM_BUILD_ROOT%{_infodir}/dir*
rm -f $RPM_BUILD_ROOT%{_infodir}/dvipng*
rm -f $RPM_BUILD_ROOT%{_mandir}/{README.*,hu/man1/readlink.1*}
rm -f $RPM_BUILD_ROOT%{texmf}/doc/Makefile
rm -f $RPM_BUILD_ROOT%{texmf}/doc/fonts/oldgerman/COPYING
rm -f $RPM_BUILD_ROOT%{texmf}/doc/help/Catalogue-upd.sh
rm -f $RPM_BUILD_ROOT%{texmf}/doc/help/faq/uktug-faq-upd.sh
rm -f $RPM_BUILD_ROOT%{texmf}/doc/helpfile
rm -f $RPM_BUILD_ROOT%{texmf}/doc/helpindex.html
rm -f $RPM_BUILD_ROOT%{texmf}/doc/index.html
rm -f $RPM_BUILD_ROOT%{texmf}/doc/index.php
rm -f $RPM_BUILD_ROOT%{texmf}/doc/mkhtml*
rm -f $RPM_BUILD_ROOT%{texmf}/doc/programs/texinfo.*
rm -f $RPM_BUILD_ROOT%{texmf}/fonts/pk/ljfour/lh/lh-lcy/*.600pk
rm -f $RPM_BUILD_ROOT%{texmf}/generic/config/pdftex-dvi.tex
rm -f $RPM_BUILD_ROOT%{texmf}/release-tetex-{src,texmf}.txt
rm -f $RPM_BUILD_ROOT%{texmf}/scripts/uniqleaf/uniqleaf.pl
rm -f $RPM_BUILD_ROOT%{texmf}/tex/generic/pdftex/glyphtounicode.tex
rm -rf $RPM_BUILD_ROOT%{_datadir}/lcdf-typetools
rm -rf $RPM_BUILD_ROOT%{texmfdist}/doc/generic/pdf-trans
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/generic/hyph-utf8
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/generic/patch
rm -rf $RPM_BUILD_ROOT%{texmfdist}/source/plain/plgraph
rm -rf $RPM_BUILD_ROOT%{texmfdist}/tex/generic/pdf-trans
rm -rf $RPM_BUILD_ROOT%{texmfdist}/tex/generic/xecyr
rm -rf $RPM_BUILD_ROOT%{texmf}/cef5conv
rm -rf $RPM_BUILD_ROOT%{texmf}/cefsconv
rm -rf $RPM_BUILD_ROOT%{texmf}/chktex
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/cef5conv
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/cefsconv
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/chktex
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/gzip

# packaged in asymptote
rm -rf $RPM_BUILD_ROOT%{texmf}/asymptote
rm -rf $RPM_BUILD_ROOT%{texmf}/doc/asymptote

# move format logs to BUILD, so $RPM_BUILD_ROOT is not polluted
# and we can still analyze them
# install -d format-logs
# mv -fv $RPM_BUILD_ROOT%{fmtdir}/*.log format-logs

# xindy files are in %%{texmf}
rm -rf $RPM_BUILD_ROOT%{_datadir}/xindy
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

# Create format files
#  for format in \
#  	aleph \
#  	csplain \
#  	etex \
#  	lambda \
#  	lamed \
#  	latex \
#  	mex \
#  	mllatex \
#  	mptopdf \
#  	omega \
#  	pdfcsplain \
#  	pdfetex \
#  	pdflatex \
#  	pdftex \
#  	pdfxmltex \
#  	physe \
#  	phyzzx \
#  	tex \
#  	texsis \
#  	xetex \
#  	xelatex \
#  	xmltex; do
#  	fmtutil --fmtdir $RPM_BUILD_ROOT%{fmtdir} --byfmt=${format}
#  done
#  # We don't need the log files
#  rm -f $(find $RPM_BUILD_ROOT%{fmtdir} -name "*.log")

cd $RPM_BUILD_ROOT%{_bindir}
ln -sf ../share/texmf/scripts/a2ping/a2ping.pl a2ping
ln -sf ../share/texmf/scripts/tetex/e2pall.pl e2pall
ln -sf ../share/texmf-dist/scripts/thumbpdf/thumbpdf.pl thumbpdf

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

%post -n texlive-dvips-data
%texhash

%postun -n texlive-dvips-data
%texhash

%post -n texlive-omega-data
%texhash

%postun -n texlive-omega-data
%texhash

%post -n texlive-scripts
%texhash

%postun -n texlive-scripts
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

%post -n texlive-latex-biology
%texhash

%postun -n texlive-latex-biology
%texhash

%post -n texlive-latex-chem
%texhash

%postun -n texlive-latex-chem
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

%post -n texlive-latex-bibtex-pl
%texhash

%postun -n texlive-latex-bibtex-pl
%texhash

%post -n texlive-latex-bibtex-german
%texhash

%postun -n texlive-latex-bibtex-german
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

%post -n texlive-latex-vietnam
%texhash

%postun -n texlive-latex-vietnam
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
%dir %{texmf}
# texlive-doc-*
%dir %{texmf}/doc
%dir %{texmf}/doc/texlive

%dir %{texmf}/scripts
%dir %{texmf}/tex
%dir %{texmf}/tex/generic
%dir %{texmf}/tex/generic/config
%dir %{texmf}/web2c
%dir %{texmfdist}
%dir %{texmfdist}/doc
%dir %{texmfdist}/doc/fonts
%dir %{texmfdist}/doc/generic
%dir %{texmfdist}/doc/latex
%dir %{texmfdist}/metapost
%dir %{texmfdist}/scripts
%dir %{texmfdist}/source
%dir %{texmfdist}/source/generic
%dir %{texmfdist}/source/latex
%dir %{texmfdist}/tex
%dir %{texmfdist}/tex/generic
%dir %{texmfdist}/tex/generic/misc
%dir %{texmfdist}/tex/latex
# %doc %{texmfdist}/doc/fontname

# ***********
# executables
# ***********
%attr(755,root,root) %{texmf}/web2c/mktexnam
%attr(755,root,root) %{texmf}/web2c/mktexdir
%attr(755,root,root) %{texmf}/web2c/mktexupd

%ghost %{texmf}/ls-R
%ghost %{texmfdist}/ls-R

%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.dat
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.def
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.us
%config(noreplace) %verify(not md5 mtime size) %{texmf}/tex/generic/config/language.us.def

%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/fmtutil.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktex.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexdir.opt
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/mktexnam.opt
# conflicts with texlive
#%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/texmf.cnf
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/updmap.cfg
%config(noreplace) %verify(not md5 mtime size) %{texmf}/web2c/updmap-hdr.cfg

%attr(1777,root,root) /var/cache/fonts


# ***********
# Directories
# ***********
%attr(1777,root,root) %dir %{_localstatedir}
%attr(1777,root,root) %dir %{_localstatedir}/fonts
%attr(1777,root,root) %dir %{_localstatedir}/fonts/map
%attr(1777,root,root) %dir %{fmtdir}
%dir %{fmtdir}/pdftex

%{texmf}/doc/info

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
%{texmfdist}/tex/generic/dirtree
%{texmfdist}/tex/generic/dratex
%{texmfdist}/tex/generic/ean
%{texmfdist}/tex/generic/edmac
%{texmfdist}/tex/generic/encodings
%{texmfdist}/tex/generic/epsf
%{texmfdist}/tex/generic/fenixpar
%{texmfdist}/tex/generic/fltpoint
%{texmfdist}/tex/generic/hyph-utf8
%{texmfdist}/tex/generic/hyphenex
%{texmfdist}/tex/generic/genmisc
%{texmfdist}/tex/generic/mathabx
%{texmfdist}/tex/generic/misc/null*
%{texmfdist}/tex/generic/misc/texnames.sty
%{texmfdist}/tex/generic/musixtex
%{texmfdist}/tex/generic/shade
%{texmfdist}/tex/generic/t2
%{texmfdist}/tex/generic/tabto-generic
%{texmfdist}/tex/generic/tap
%{texmfdist}/tex/generic/tex-ewd
%{texmfdist}/tex/generic/tex-ps
%{texmfdist}/tex/generic/vaucanson-g
%{texmfdist}/tex/generic/xlop
%{texmfdist}/tex/generic/xstring
%{texmfdist}/tex/generic/zhmetrics
%{texmfdist}/tex/lualatex
%{texmfdist}/tex/luatex
%{texmfdist}/tex/texinfo
%{texmf}/tex/fontinst
%{texmf}/tex/generic/hyphen
# %{texmf}/fmtutil/format.metafont.cnf
#%%{texmf}/fonts/map/dvips/updmap/*
%{texmf}/web2c/*.tcx

#fmt %{fmtdir}/pdftex/pdfetex.fmt
#fmt %{fmtdir}/tex/tex.fmt

%files -n texlive-dirs-fonts
%defattr(644,root,root,755)
%dir %{texmfdist}/fonts
%dir %{texmfdist}/fonts/afm
%dir %{texmfdist}/fonts/afm/public
%dir %{texmfdist}/fonts/afm/vntex
%dir %{texmfdist}/fonts/enc
%dir %{texmfdist}/fonts/enc/dvips
%dir %{texmfdist}/fonts/enc/dvips/vntex
%dir %{texmfdist}/fonts/map
%dir %{texmfdist}/fonts/map/dvipdfm
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/map/dvips/vntex
%dir %{texmfdist}/fonts/map/fontname
# %dir %{texmfdist}/fonts/map/public
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
%dir %{texmfdist}/fonts/tfm/vntex
%dir %{texmfdist}/fonts/truetype
%dir %{texmfdist}/fonts/type1
%dir %{texmfdist}/fonts/type1/public
%dir %{texmfdist}/fonts/type1/vntex
%dir %{texmfdist}/fonts/vf
%dir %{texmfdist}/fonts/vf/public
%dir %{texmfdist}/fonts/vf/vntex
%dir %{texmfdist}/source/fonts
%dir %{texmf}/fonts
%dir %{texmf}/fonts/enc
%dir %{texmf}/fonts/map
%dir %{texmf}/fonts/opentype
%dir %{texmf}/fonts/opentype/public

%define	texlivedoc	%{texmf}/doc/texlive/texlive-

%files -n texlive-doc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/dehyph-exptl
# %dir %{texmfdoc}
# %dir %{texmfdoc}/doc
# %{texmfdoc}/README
# %{texmfdoc}/ls-R
%{texmfdist}/doc/generic/FAQ-en
%{texmfdist}/doc/latex/guide-to-latex
%{texmfdist}/doc/latex/l2tabu-english
%{texmfdist}/doc/latex/latex-course
%{texmfdist}/doc/latex/latex-doc-ptr
%{texmfdist}/doc/latex/latex-graphics-companion
%{texmfdist}/doc/latex/latex-veryshortguide
%{texmfdist}/doc/latex/latex-web-companion
%{texmfdist}/doc/latex/lshort-english
%{texmfdist}/doc/latex/pdf-forms-tutorial-en
%{texmfdist}/doc/latex/tlc2
%{texlivedoc}en
%{texmf}/doc/tetex
%{texmf}/doc/texlive/texlive-common
# %{texmfdist}/doc/fontinst

%files -n texlive-doc-bg
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-bulgarian

%files -n texlive-doc-cs
%defattr(644,root,root,755)
%{texlivedoc}cz
 
%files -n texlive-doc-de
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/kopka
%{texmfdist}/doc/latex/l2picfaq
%{texmfdist}/doc/latex/l2tabu
%{texmfdist}/doc/latex/latex-tipps-und-tricks
%{texmfdist}/doc/latex/lshort-german
%{texmfdist}/doc/latex/pdf-forms-tutorial-de
%{texlivedoc}de
# 
# %files -n texlive-doc-el
# %defattr(644,root,root,755)
# %{texmfdoc}/doc/greek
# %{texmf}/doc/generic/elhyphen
# 
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
%{texlivedoc}fr
 
%files -n texlive-doc-it
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/l2tabu-it
%{texmfdist}/doc/latex/lshort-italian
%{texlivedoc}it

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
%{texlivedoc}pl

%files -n texlive-doc-pt
%defattr(644,root,root,755)
%{texmfdist}/doc/latex/lshort-portuguese

%files -n texlive-doc-ru
%defattr(644,root,root,755)
%{texlivedoc}ru

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
%{texlivedoc}zh-cn

%files -n texlive-doc-latex
%defattr(644,root,root,755)
# %doc %{texmfdist}/doc/fonts/calrsfs
%doc %{texmfdist}/doc/generic/encxvlna
%doc %{texmfdist}/doc/generic/shapepar
%doc %{texmfdist}/doc/generic/textmerg
%doc %{texmfdist}/doc/latex/acronym
%doc %{texmfdist}/doc/latex/aeguill
%doc %{texmfdist}/doc/latex/anysize
%doc %{texmfdist}/doc/latex/base
%doc %{texmfdist}/doc/latex/beton
%doc %{texmfdist}/doc/latex/concmath
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
%doc %{texmfdist}/doc/latex/fancyvrb
%doc %{texmfdist}/doc/latex/filecontents
%doc %{texmfdist}/doc/latex/float
%if %{without bootstrap}
%doc %{texmfdist}/doc/latex/floatflt
%endif
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
%doc %{texmfdist}/doc/latex/slashbox
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

%files -n texlive-dvips-data
%defattr(644,root,root,755)
%doc %{texmf}/doc/dvipdfm
%{texmfdist}/dvips
%{texmfdist}/fonts/enc/dvips/base
%{texmfdist}/tex/generic/dvips
%{texmf}/dvipdfm
%{texmf}/dvipdfmx
%{texmf}/dvips
%{texmf}/fonts/enc/dvips
%{texmf}/fonts/map/dvipdfm
%{texmf}/fonts/map/dvipdfmx
%{texmf}/fonts/map/dvips

%files -n texlive-omega-data
%defattr(644,root,root,755)
%{texmfdist}/omega
%{texmfdist}/tex/generic/omegahyph
%{texmfdist}/tex/lambda
%{texmfdist}/tex/plain/omega

%files -n texlive-scripts
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/bengali
%dir %{texmfdist}/scripts/glossaries
%dir %{texmfdist}/scripts/oberdiek
%dir %{texmfdist}/scripts/perltex
%dir %{texmfdist}/scripts/pgfplots
%dir %{texmfdist}/scripts/pst2pdf
%dir %{texmfdist}/scripts/shipunov
%dir %{texmfdist}/scripts/texcount
%dir %{texmfdist}/scripts/vpe
%dir %{texmf}/scripts/a2ping
# %dir %{texmf}/scripts/pkfix
%dir %{texmf}/scripts/simpdftex
%dir %{texmf}/scripts/tetex
%attr(755,root,root) %{texmfdist}/scripts/bengali/*
%attr(755,root,root) %{texmfdist}/scripts/glossaries/*
%attr(755,root,root) %{texmfdist}/scripts/oberdiek/*
%attr(755,root,root) %{texmfdist}/scripts/perltex/perltex*
%attr(755,root,root) %{texmfdist}/scripts/pgfplots/*
%attr(755,root,root) %{texmfdist}/scripts/pst2pdf/pst2pdf*
%attr(755,root,root) %{texmfdist}/scripts/shipunov/*
%attr(755,root,root) %{texmfdist}/scripts/texcount/*
%attr(755,root,root) %{texmfdist}/scripts/vpe/vpe.pl
%attr(755,root,root) %{texmf}/scripts/a2ping/a2ping*
# %attr(755,root,root) %{texmf}/scripts/pkfix/pkfix*
%attr(755,root,root) %{texmf}/scripts/simpdftex/simpdftex*
%attr(755,root,root) %{texmf}/scripts/tetex/*
%attr(755,root,root) %{_bindir}/a2ping
%attr(755,root,root) %{_bindir}/e2pall
# %{_mandir}/man1/e2pall.1*
%dir %{texmf}/texdoc
%doc %{texmf}/doc/texdoc
%config(noreplace) %verify(not md5 mtime size) %{texmf}/texdoc/texdoc.cnf

%files -n texlive-tex4ht-data
%defattr(644,root,root,755)
%{texmfdist}/tex4ht
%{texmfdist}/tex/generic/tex4ht

%files -n texlive-xetex-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/xelatex
%doc %{texmfdist}/doc/xetex
#fmt %dir %{fmtdir}/xetex
%{texmfdist}/tex/generic/ifxetex
%{texmfdist}/tex/generic/xetexconfig
%{texmfdist}/tex/latex/latexconfig/xelatex.ini
%{texmfdist}/tex/xetex
%{texmfdist}/tex/xelatex
%{texmfdist}/scripts/xetex
%{texmfdist}/source/xelatex
#fmt %{fmtdir}/xetex/*.fmt

%files -n texlive-tex-arrayjob
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/arrayjob
%{texmfdist}/tex/generic/arrayjob

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

%files -n texlive-tex-physe
%defattr(644,root,root,755)
%{texmfdist}/tex/physe
# %{texmf}/fmtutil/format.physe.cnf
#fmt %{fmtdir}/pdftex/physe.fmt

%files -n texlive-tex-velthuis
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/velthuis
%{texmfdist}/tex/generic/velthuis

%files -n texlive-tex-ytex
%defattr(644,root,root,755)
%{texmfdist}/tex/ytex

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
%{texmfdist}/metapost/frcursive
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
%{texmfdist}/metapost/tabvar
%{texmfdist}/metapost/textpath
%{texmfdist}/metapost/venn
%{texmfdist}/tex/generic/metapost

%files -n xindy-data
%defattr(644,root,root,755)
%doc %{texmf}/doc/xindy
%{texmf}/xindy

%files -n xindy-albanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/albanian

%files -n xindy-belarusian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/belarusian

%files -n xindy-bulgarian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/bulgarian

%files -n xindy-croatian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/croatian

%files -n xindy-czech
%defattr(644,root,root,755)
%{texmf}/xindy/lang/czech

%files -n xindy-danish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/danish

%files -n xindy-dutch
%defattr(644,root,root,755)
%{texmf}/xindy/lang/dutch

%files -n xindy-english
%defattr(644,root,root,755)
%{texmf}/xindy/lang/english

%files -n xindy-esperanto
%defattr(644,root,root,755)
%{texmf}/xindy/lang/esperanto

%files -n xindy-estonian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/estonian

%files -n xindy-finnish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/finnish

%files -n xindy-french
%defattr(644,root,root,755)
%{texmf}/xindy/lang/french

%files -n xindy-general
%defattr(644,root,root,755)
%{texmf}/xindy/lang/general

%files -n xindy-georgian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/georgian

%files -n xindy-german
%defattr(644,root,root,755)
%{texmf}/xindy/lang/german

%files -n xindy-greek
%defattr(644,root,root,755)
%{texmf}/xindy/lang/greek

%files -n xindy-gypsy
%defattr(644,root,root,755)
%{texmf}/xindy/lang/gypsy

%files -n xindy-hausa
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hausa

%files -n xindy-hebrew
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hebrew

%files -n xindy-hungarian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/hungarian

%files -n xindy-icelandic
%defattr(644,root,root,755)
%{texmf}/xindy/lang/icelandic

%files -n xindy-italian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/italian

%files -n xindy-klingon
%defattr(644,root,root,755)
%{texmf}/xindy/lang/klingon

%files -n xindy-kurdish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/kurdish

%files -n xindy-latin
%defattr(644,root,root,755)
%{texmf}/xindy/lang/latin

%files -n xindy-latvian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/latvian

%files -n xindy-lithuanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/lithuanian

%files -n xindy-lower-sorbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/lower-sorbian

%files -n xindy-macedonian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/macedonian

%files -n xindy-mongolian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/mongolian

%files -n xindy-norwegian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/norwegian

%files -n xindy-polish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/polish

%files -n xindy-portuguese
%defattr(644,root,root,755)
%{texmf}/xindy/lang/portuguese

%files -n xindy-romanian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/romanian

%files -n xindy-russian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/russian

%files -n xindy-serbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/serbian

%files -n xindy-slovak
%defattr(644,root,root,755)
%{texmf}/xindy/lang/slovak

%files -n xindy-slovenian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/slovenian

%files -n xindy-spanish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/spanish

%files -n xindy-swedish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/swedish

%files -n xindy-turkish
%defattr(644,root,root,755)
%{texmf}/xindy/lang/turkish

%files -n xindy-ukrainian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/ukrainian

%files -n xindy-upper-sorbian
%defattr(644,root,root,755)
%{texmf}/xindy/lang/upper-sorbian

%files -n xindy-vietnamese
%defattr(644,root,root,755)
%{texmf}/xindy/lang/vietnamese/

%files -n texlive-plain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/plain
%{texmfdist}/tex/plain
%exclude %{texmfdist}/tex/plain/config/xetex.ini
# %{texmf}/fmtutil/format.tex.cnf

%files -n texlive-mex
%defattr(644,root,root,755)
%dir %{texmfdist}/tex/mex
%dir %{texmfdist}/tex/mex/config
%doc %{texmfdist}/doc/mex
%{texmfdist}/source/mex
%{texmfdist}/tex/mex/base
# %{texmf}/fmtutil/format.mex.cnf
# %{texmf}/fmtutil/format.utf8mex.cnf

%files -n texlive-amstex
%defattr(644,root,root,755)
%{texmfdist}/tex/amstex/config
%{texmfdist}/tex/plain/amsfonts

%files -n texlive-format-csplain
%defattr(644,root,root,755)
#fmt %{fmtdir}/pdftex/csplain.fmt

%files -n texlive-cslatex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/cslatex
%{texmfdist}/tex/cslatex
%{texmfdist}/tex/latex/cslatex

%files -n texlive-eplain
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/etex
%doc %{texmfdist}/doc/eplain
%{texmfdist}/tex/plain/etex
%{texmfdist}/tex/eplain
%dir %{texmfdist}/source/eplain
# %{texmfdist}/source/eplain/eplain-source-3.2.zip

%files -n texlive-context-data
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/context
%{texmfdist}/source/lambda
%{texmfdist}/bibtex/bst/context
%{texmfdist}/context
%{texmfdist}/fonts/enc/dvips/context
%{texmfdist}/fonts/fea/context
%{texmfdist}/fonts/map/dvips/context
%{texmfdist}/fonts/map/luatex/context
%{texmfdist}/fonts/map/pdftex/context
%{texmfdist}/metapost/context
%{texmfdist}/scripts/context
%{texmfdist}/tex/context
%{texmfdist}/tex/generic/context
%{texmf}/web2c/context.cnf

%files -n texlive-format-context-de
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-de.ini

%files -n texlive-format-context-en
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-en.ini
# what is the difference betwen uk and en in this particular situation?
%{texmfdist}/tex/context/config/cont-uk.ini

%files -n texlive-format-context-nl
%defattr(644,root,root,755)
%{texmfdist}/tex/context/config/cont-nl.ini

%files -n texlive-latex-data
%defattr(644,root,root,755)
%dir %{texmfdist}/scripts/pst-pdf
%dir %{texmfdist}/tex/latex
%dir %{texmfdist}/tex/latex/latexconfig
%dir %{texmf}/tex/latex
# %{texmf}/fmtutil/format.latex.cnf
%if %{without bootstrap}
%{texmfdist}/tex/latex/floatflt
%endif
%{texmfdist}/scripts/pst-pdf/ps4pdf
%{texmfdist}/tex/generic/pstricks
%{texmfdist}/tex/generic/shapepar
%{texmfdist}/tex/generic/textmerg
%{texmfdist}/source/generic/textmerg
%{texmfdist}/tex/latex/12many
%{texmfdist}/tex/latex/AkkTeX
# %{texmfdist}/tex/latex/GuIT
%{texmfdist}/tex/latex/IEEEtran
%{texmfdist}/tex/latex/Tabbing
%{texmfdist}/tex/latex/a0poster
%{texmfdist}/tex/latex/acmtrans
%{texmfdist}/tex/latex/acronym
%{texmfdist}/tex/latex/adrlist
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
%{texmfdist}/tex/latex/apa
%{texmfdist}/tex/latex/apl
%{texmfdist}/tex/latex/ar
%{texmfdist}/tex/latex/arabi
%{texmfdist}/tex/latex/arabtex
%{texmfdist}/tex/latex/archaic
%{texmfdist}/tex/latex/arev
%{texmfdist}/tex/latex/armenian
%{texmfdist}/tex/latex/ascelike
%{texmfdist}/tex/latex/ascii
%{texmfdist}/tex/latex/assignment
%{texmfdist}/tex/latex/augie
%{texmfdist}/tex/latex/auncial-new
%{texmfdist}/tex/latex/aurical
%{texmfdist}/tex/latex/authoraftertitle
%{texmfdist}/tex/latex/authorindex
%{texmfdist}/tex/latex/auto-pst-pdf
%{texmfdist}/tex/latex/autoarea
%{texmfdist}/tex/latex/autotab
%{texmfdist}/tex/latex/avantgar
%{texmfdist}/tex/latex/bangtex
%{texmfdist}/tex/latex/barcodes
%{texmfdist}/tex/latex/base
%{texmfdist}/tex/latex/bayer
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
%{texmfdist}/tex/latex/bophook
%{texmfdist}/tex/latex/boxhandler
%{texmfdist}/tex/latex/braille
%{texmfdist}/tex/latex/breakurl
%{texmfdist}/tex/latex/brushscr
%{texmfdist}/tex/latex/burmese
%{texmfdist}/tex/latex/bussproofs
%{texmfdist}/tex/latex/calrsfs
%{texmfdist}/tex/latex/calxxxx
%{texmfdist}/tex/latex/captcont
%{texmfdist}/tex/latex/casyl
%{texmfdist}/tex/latex/catechis
%{texmfdist}/tex/latex/cbcoptic
%{texmfdist}/tex/latex/cbfonts
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
%{texmfdist}/tex/latex/citeref
%{texmfdist}/tex/latex/cjhebrew
%{texmfdist}/tex/latex/cjk
%{texmfdist}/tex/latex/classicthesis
%{texmfdist}/tex/latex/cleveref
%{texmfdist}/tex/latex/clock
%{texmfdist}/tex/latex/clrscode
%{texmfdist}/tex/latex/cm-lgc
%{texmfdist}/tex/latex/cm-super
%{texmfdist}/tex/latex/cmap
%{texmfdist}/tex/latex/cmcyralt
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
%{texmfdist}/tex/latex/cursor
%{texmfdist}/tex/latex/cv
%{texmfdist}/tex/latex/cweb-latex
%{texmfdist}/tex/latex/cyklop
%{texmfdist}/tex/latex/dateiliste
%{texmfdist}/tex/latex/datetime
%{texmfdist}/tex/latex/dcpic
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
%{texmfdist}/tex/latex/dvipdfmx-def
%{texmfdist}/tex/latex/eCards
%{texmfdist}/tex/latex/ean13isbn
%{texmfdist}/tex/latex/easy
%{texmfdist}/tex/latex/ebezier
%{texmfdist}/tex/latex/ebsthesis
%{texmfdist}/tex/latex/ecclesiastic
%{texmfdist}/tex/latex/ecltree
%{texmfdist}/tex/latex/eco
%{texmfdist}/tex/latex/economic
%{texmfdist}/tex/latex/ed
%{texmfdist}/tex/latex/edmargin
%{texmfdist}/tex/latex/ednotes
%{texmfdist}/tex/latex/eemeir
%{texmfdist}/tex/latex/eepic
%{texmfdist}/tex/latex/egameps
%{texmfdist}/tex/latex/eiad
%{texmfdist}/tex/latex/ellipsis
%{texmfdist}/tex/latex/elpres
%{texmfdist}/tex/latex/elsevier
%{texmfdist}/tex/latex/em
%{texmfdist}/tex/latex/emp
%{texmfdist}/tex/latex/emulateapj
%{texmfdist}/tex/latex/encxvlna
%{texmfdist}/tex/latex/endfloat
%{texmfdist}/tex/latex/endheads
%{texmfdist}/tex/latex/engpron
%{texmfdist}/tex/latex/engrec
%{texmfdist}/tex/latex/envbig
%{texmfdist}/tex/latex/envlab
%{texmfdist}/tex/latex/epigrafica
%{texmfdist}/tex/latex/epigraph
%{texmfdist}/tex/latex/epiolmec
%{texmfdist}/tex/latex/epsdice
%{texmfdist}/tex/latex/epspdfconversion
%{texmfdist}/tex/latex/eqname
%{texmfdist}/tex/latex/eqparbox
%{texmfdist}/tex/latex/errata
%{texmfdist}/tex/latex/esint
%{texmfdist}/tex/latex/eskdx
%{texmfdist}/tex/latex/eso-pic
%{texmfdist}/tex/latex/etex-pkg
%{texmfdist}/tex/latex/ethiop
%{texmfdist}/tex/latex/etoolbox
%{texmfdist}/tex/latex/eukdate
%{texmfdist}/tex/latex/euler
%{texmfdist}/tex/latex/eulervm
%{texmfdist}/tex/latex/euproposal
%{texmfdist}/tex/latex/euro
%{texmfdist}/tex/latex/eurofont
%{texmfdist}/tex/latex/europecv
%{texmfdist}/tex/latex/eurosans
%{texmfdist}/tex/latex/eurosym
%{texmfdist}/tex/latex/everypage
%{texmfdist}/tex/latex/examplep
%{texmfdist}/tex/latex/exceltex
%{texmfdist}/tex/latex/exercise
%{texmfdist}/tex/latex/expl3
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
%{texmfdist}/tex/latex/fribrief
%{texmfdist}/tex/latex/frletter
%{texmfdist}/tex/latex/frontespizio
%{texmfdist}/tex/latex/fullpict
%{texmfdist}/tex/latex/fundus
%{texmfdist}/tex/latex/gaceta
%{texmfdist}/tex/latex/gastex
%{texmfdist}/tex/latex/gatech-thesis
%{texmfdist}/tex/latex/gauss
%{texmfdist}/tex/latex/gb4e
%{texmfdist}/tex/latex/gcard
%{texmfdist}/tex/latex/gcite
%{texmfdist}/tex/latex/genmpage
%{texmfdist}/tex/latex/geometry
%{texmfdist}/tex/latex/germbib
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
%{texmfdist}/tex/latex/grverb
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
%{texmfdist}/tex/latex/isonums
%{texmfdist}/tex/latex/itnumpar
%{texmfdist}/tex/latex/itrans
%{texmfdist}/tex/latex/iwona
%{texmfdist}/tex/latex/jhep
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
# %{texmfdist}/tex/latex/latexconfig/pdflualatex.ini
%{texmfdist}/tex/latex/layouts
%{texmfdist}/tex/latex/listings
%{texmfdist}/tex/latex/ltabptch
%{texmfdist}/tex/latex/localloc
%{texmfdist}/tex/latex/ltxmisc
%{texmfdist}/tex/latex/mathcomp
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
%{texmfdist}/tex/latex/natbib
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
%{texmfdist}/tex/latex/slashbox
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
%{texmfdist}/tex/latex/taupin
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
%{texmfdist}/tex/latex/timesht
%{texmfdist}/tex/latex/tipa
%{texmfdist}/tex/latex/titlefoot
%{texmfdist}/tex/latex/titlesec
%{texmfdist}/tex/latex/titling
%{texmfdist}/tex/latex/tocbibind
%{texmfdist}/tex/latex/tocloft
%{texmfdist}/tex/latex/tools
%{texmfdist}/tex/latex/totpages
%{texmfdist}/tex/latex/type1cm
%{texmfdist}/tex/latex/undertilde
%{texmfdist}/tex/latex/units
%{texmfdist}/tex/latex/unitsdef
%{texmfdist}/tex/latex/universa
%{texmfdist}/tex/latex/unroman
%{texmfdist}/tex/latex/upmethodology
%{texmfdist}/tex/latex/upquote
%{texmfdist}/tex/latex/varindex
%{texmfdist}/tex/latex/varsfromjobname
%{texmfdist}/tex/latex/vector
%{texmfdist}/tex/latex/velthuis
%{texmfdist}/tex/latex/verse
%{texmfdist}/tex/latex/versions
%{texmfdist}/tex/latex/vhistory
%{texmfdist}/tex/latex/vita
%{texmfdist}/tex/latex/vmargin
%{texmfdist}/tex/latex/volumes
%{texmfdist}/tex/latex/vpe
%{texmfdist}/tex/latex/vrsion
%{texmfdist}/tex/latex/vwcol
%{texmfdist}/tex/latex/vxu
%{texmfdist}/tex/latex/wallpaper
%{texmfdist}/tex/latex/warning
%{texmfdist}/tex/latex/warpcol
%{texmfdist}/tex/latex/was
%{texmfdist}/tex/latex/williams
%{texmfdist}/tex/latex/wnri
%{texmfdist}/tex/latex/wordlike
%{texmfdist}/tex/latex/wrapfig
%{texmfdist}/tex/latex/wsuipa
%{texmfdist}/tex/latex/xargs
%{texmfdist}/tex/latex/xcolor
%{texmfdist}/tex/latex/xdoc
%{texmfdist}/tex/latex/xfor
%{texmfdist}/tex/latex/xifthen
%{texmfdist}/tex/latex/xkeyval
%{texmfdist}/tex/latex/xmpincl
%{texmfdist}/tex/latex/xnewcommand
%{texmfdist}/tex/latex/xoptarg
%{texmfdist}/tex/latex/xpackages
%{texmfdist}/tex/latex/xq
%{texmfdist}/tex/latex/xskak
%{texmfdist}/tex/latex/xstring
%{texmfdist}/tex/latex/xtab
%{texmfdist}/tex/latex/xtcapts
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
%{texmfdist}/tex/latex/zefonts
%{texmfdist}/tex/latex/ziffer
%{texmfdist}/tex/latex/zwgetfdate
%{texmfdist}/tex/plain/etex
# %{texmf}/tex/latex/config
%{texmf}/tex/latex/dvipdfm
#fmt %{fmtdir}/pdftex/latex.fmt
#fmt %{fmtdir}/pdftex/mllatex.fmt

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
%{texmfdist}/tex/latex/algorithms

%files -n texlive-latex-ae
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/ae

%files -n texlive-latex-ams
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/amsfonts
%doc %{texmfdist}/doc/latex/amscls
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

%files -n texlive-latex-antp
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/antp

%files -n texlive-latex-antt
%defattr(644,root,root,755)
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
%{texmfdist}/tex/latex/beamer-contrib
%{texmfdist}/tex/latex/beamer

%files -n texlive-latex-bezos
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/bezos
%{texmfdist}/tex/latex/bezos

# %files -n texlive-latex-bibtex-ams
# %defattr(644,root,root,755)
# %{texmfdist}/bibtex/bst/ams
# %{texmfdist}/bibtex/bib/ams

%files -n texlive-latex-bibtex-pl
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bib/gustlib
%{texmfdist}/bibtex/bib/gustlib/plbib.bib

%files -n texlive-latex-bibtex-german
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/bibtex/germbib
%{texmfdist}/bibtex/bst/germbib
%{texmfdist}/tex/latex/germbib

%files -n texlive-latex-bibtex-revtex4
%defattr(644,root,root,755)
%dir %{texmfdist}/source/latex/revtex
%doc %{texmfdist}/doc/latex/revtex
# %{texmfdist}/source/latex/revtex/revtex4.dtx
# %{texmfdist}/source/latex/revtex/revtex4.ins
# %{texmfdist}/tex/latex/revtex/revtex4.cls

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
%doc %{texmfdist}/doc/bibtex/economic
%doc %{texmfdist}/doc/bibtex/elsevier-bib
%doc %{texmfdist}/doc/bibtex/gost
%doc %{texmfdist}/doc/bibtex/ijqc
%doc %{texmfdist}/doc/bibtex/iopart-num
%doc %{texmfdist}/doc/generic/t2
%doc %{texmfdist}/doc/latex/IEEEtran
%{texmfdist}/bibtex/bib/IEEEtran
%{texmfdist}/bibtex/bib/abstyles
# %{texmfdist}/bibtex/bib/achemso
%{texmfdist}/bibtex/bib/acmtrans
%{texmfdist}/bibtex/bib/ascelike
%{texmfdist}/bibtex/bib/beebe
# %{texmfdist}/bibtex/bib/bibhtml
# %{texmfdist}/bibtex/bib/bibtopic
%{texmfdist}/bibtex/bib/din1505
%{texmfdist}/bibtex/bib/directory
%{texmfdist}/bibtex/bib/figbib
%{texmfdist}/bibtex/bib/frankenstein
%{texmfdist}/bibtex/bib/gatech-thesis
# %{texmfdist}/bibtex/bib/geomsty
%{texmfdist}/bibtex/bib/gloss
%{texmfdist}/bibtex/bib/harvard
%{texmfdist}/bibtex/bib/ieeepes
%{texmfdist}/bibtex/bib/ijmart
%{texmfdist}/bibtex/bib/imac
%{texmfdist}/bibtex/bib/index
%{texmfdist}/bibtex/bib/lsc
%{texmfdist}/bibtex/bib/msc
%{texmfdist}/bibtex/bib/nostarch
# %{texmfdist}/bibtex/bib/revtex
%{texmfdist}/bibtex/bib/spie
%{texmfdist}/bibtex/bib/urlbst
%{texmfdist}/bibtex/bst/IEEEtran
%{texmfdist}/bibtex/bst/abstyles
%{texmfdist}/bibtex/bst/achemso
%{texmfdist}/bibtex/bst/acmtrans
%{texmfdist}/bibtex/bst/afthesis
%{texmfdist}/bibtex/bst/aguplus
%{texmfdist}/bibtex/bst/aichej
%{texmfdist}/bibtex/bst/ametsoc
%{texmfdist}/bibtex/bst/ascelike
%{texmfdist}/bibtex/bst/beebe
%{texmfdist}/bibtex/bst/bibhtml
%{texmfdist}/bibtex/bst/chem-journal
%{texmfdist}/bibtex/bst/chicago
%{texmfdist}/bibtex/bst/confproc
%{texmfdist}/bibtex/bst/datatool
%{texmfdist}/bibtex/bst/din1505
%{texmfdist}/bibtex/bst/dinat
%{texmfdist}/bibtex/bst/directory
%{texmfdist}/bibtex/bst/dvdcoll
%{texmfdist}/bibtex/bst/economic
%{texmfdist}/bibtex/bst/elsevier-bib
%{texmfdist}/bibtex/bst/fbs
%{texmfdist}/bibtex/bst/figbib
%{texmfdist}/bibtex/bst/finbib
%{texmfdist}/bibtex/bst/frankenstein
%{texmfdist}/bibtex/bst/gatech-thesis
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
%{texmfdist}/bibtex/bst/mslapa
%{texmfdist}/bibtex/bst/multibib
%{texmfdist}/bibtex/bst/munich
%{texmfdist}/bibtex/bst/nature
%{texmfdist}/bibtex/bst/nddiss
%{texmfdist}/bibtex/bst/opcit
%{texmfdist}/bibtex/bst/perception
%{texmfdist}/bibtex/bst/revtex
%{texmfdist}/bibtex/bst/savetrees
%{texmfdist}/bibtex/bst/shipunov
# %{texmfdist}/bibtex/bst/smflatex
%{texmfdist}/bibtex/bst/sort-by-letters
%{texmfdist}/bibtex/bst/spie
%{texmfdist}/bibtex/bst/stellenbosch
%{texmfdist}/bibtex/bst/swebib
%{texmfdist}/bibtex/bst/texsis
%{texmfdist}/bibtex/bst/thuthesis
%{texmfdist}/bibtex/bst/tugboat
%{texmfdist}/bibtex/bst/urlbst
%{texmfdist}/bibtex/csf/gost
%{texmfdist}/source/bibtex/gost

%files -n texlive-latex-bibtex-vancouver
%defattr(644,root,root,755)
%dir %{texmfdist}/bibtex/bib/vancouver
%dir %{texmfdist}/bibtex/bst/vancouver
%dir %{texmfdist}/doc/bibtex/vancouver
%doc %{texmfdist}/doc/bibtex/vancouver/README
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.pdf
%doc %{texmfdist}/doc/bibtex/vancouver/vancouver.tex
%{texmfdist}/bibtex/bib/vancouver/vancouver.bib
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

# %files -n texlive-latex-colortab
# %defattr(644,root,root,755)
# %doc %{texmfdist}/doc/generic/colortab
# %{texmfdist}/tex/latex/colortab
# %{texmfdist}/tex/generic/colortab

%files -n texlive-latex-comment
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/comment
%{texmfdist}/tex/latex/comment
%{texmfdist}/source/latex/comment

%files -n texlive-latex-concmath
%defattr(644,root,root,755)
%{texmfdist}/tex/latex/concmath

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
%{texmfdist}/source/latex/custom-bib
%{texmfdist}/tex/latex/custom-bib

%files -n texlive-latex-cyrillic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cyrillic
%{texmfdist}/source/latex/cyrillic
%{texmfdist}/tex/latex/cyrillic

%files -n texlive-latex-enumitem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/enumitem
%{texmfdist}/tex/latex/enumitem

%files -n texlive-latex-exams
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/alterqcm
%doc %{texmfdist}/doc/latex/answers
%doc %{texmfdist}/doc/latex/eqexam
%doc %{texmfdist}/doc/latex/exam
%doc %{texmfdist}/doc/latex/examdesign
%doc %{texmfdist}/doc/latex/mathexam
%doc %{texmfdist}/doc/latex/probsoln
%doc %{texmfdist}/doc/latex/qcm
%doc %{texmfdist}/doc/latex/uebungsblatt
%{texmfdist}/source/latex/eqexam
%{texmfdist}/source/latex/examdesign
%{texmfdist}/source/latex/mathexam
%{texmfdist}/source/latex/probsoln
%{texmfdist}/source/latex/qcm
%{texmfdist}/tex/latex/alterqcm
%{texmfdist}/tex/latex/answers
%{texmfdist}/tex/latex/eqexam
%{texmfdist}/tex/latex/exam
%{texmfdist}/tex/latex/examdesign
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

%if %{without bootstrap}
%files -n texlive-latex-foiltex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/foiltex
%{texmfdist}/tex/latex/foiltex
%endif

%files -n texlive-latex-formlett
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/formlett
%{texmfdist}/tex/latex/formlett

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
%{texmfdist}/tex/latex/lm
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/enc/dvips/lm
%{texmfdist}/fonts/map/dvips/lm
%{texmfdist}/fonts/map/dvipdfm/lm
# %{texmfdist}/source/fonts/lm

%files -n texlive-latex-lucidabr
%defattr(644,root,root,755)
%dir %{texmfdist}/vtex
%{texmfdist}/vtex/config

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
%{texmfdist}/tex/latex/marvosym

%files -n texlive-latex-microtype
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/microtype
%{texmfdist}/source/latex/microtype
%{texmfdist}/tex/latex/microtype

%files -n texlive-latex-misc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/fixme
%{texmfdist}/source/latex/fixme
%{texmfdist}/tex/latex/fixme
%doc %{texmfdist}/doc/latex/recipecard
%{texmfdist}/source/latex/recipecard
%{texmfdist}/tex/latex/recipecard
%doc %{texmfdist}/doc/latex/cooking
%{texmfdist}/source/latex/cooking
%{texmfdist}/tex/latex/cooking
%doc %{texmfdist}/doc/latex/cuisine
%{texmfdist}/source/latex/cuisine
%{texmfdist}/tex/latex/cuisine
%doc %{texmfdist}/doc/latex/todo
%{texmfdist}/source/latex/todo
%{texmfdist}/tex/latex/todo

%files -n texlive-latex-mflogo
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/mflogo
%{texmfdist}/tex/latex/mflogo

%files -n texlive-latex-mfnfss
%defattr(644,root,root,755)
%{texmfdist}/source/latex/mfnfss
%{texmfdist}/tex/latex/mfnfss

%files -n texlive-latex-minitoc
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/minitoc
%{texmfdist}/bibtex/bst/minitoc
%{texmfdist}/makeindex/minitoc
# %{texmfdist}/scripts/minitoc
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

%files -n texlive-latex-musictex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/musictex
%{texmfdist}/fonts/source/public/musictex
%{texmfdist}/fonts/tfm/public/musictex
%{texmfdist}/tex/generic/musictex
%{texmfdist}/tex/latex/musictex

%files -n texlive-latex-ntheorem
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/ntheorem
%{texmfdist}/tex/latex/ntheorem
%{texmfdist}/source/latex/ntheorem

%files -n texlive-latex-other-doc
%defattr(644,root,root,755)
# %doc %{texmfdist}/doc/alatex
%doc %{texmfdist}/doc/generic/wsuipa
%doc %{texmfdist}/doc/latex/ANUfinalexam
%doc %{texmfdist}/doc/latex/AkkTeX
# %doc %{texmfdist}/doc/latex/GuIT
%doc %{texmfdist}/doc/latex/a0poster
%doc %{texmfdist}/doc/latex/acmtrans
%doc %{texmfdist}/doc/latex/adrlist
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
%doc %{texmfdist}/doc/latex/apa
%doc %{texmfdist}/doc/latex/ar
%doc %{texmfdist}/doc/latex/arabi
%doc %{texmfdist}/doc/latex/arabtex
%doc %{texmfdist}/doc/latex/ascelike
%doc %{texmfdist}/doc/latex/assignment
%doc %{texmfdist}/doc/latex/augie
%doc %{texmfdist}/doc/latex/aurical
%doc %{texmfdist}/doc/latex/authorindex
%doc %{texmfdist}/doc/latex/autoarea
%doc %{texmfdist}/doc/latex/autotab
%doc %{texmfdist}/doc/latex/bangtex
%doc %{texmfdist}/doc/latex/barcodes
%doc %{texmfdist}/doc/latex/bayer
%doc %{texmfdist}/doc/latex/bbm-macros
%doc %{texmfdist}/doc/latex/beamer-contrib
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
%doc %{texmfdist}/doc/latex/brushscr
%doc %{texmfdist}/doc/latex/bussproofs
%doc %{texmfdist}/doc/latex/calxxxx
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
# %doc %{texmfdist}/doc/latex/china2e
%doc %{texmfdist}/doc/latex/cite
%doc %{texmfdist}/doc/latex/classicthesis
%doc %{texmfdist}/doc/latex/cleveref
%doc %{texmfdist}/doc/latex/clock
%doc %{texmfdist}/doc/latex/clrscode
%doc %{texmfdist}/doc/latex/cm-lgc
%doc %{texmfdist}/doc/latex/cmap
%doc %{texmfdist}/doc/latex/cmcyralt
%doc %{texmfdist}/doc/latex/cmdstring
%doc %{texmfdist}/doc/latex/codepage
%doc %{texmfdist}/doc/latex/colorinfo
%doc %{texmfdist}/doc/latex/commath
%doc %{texmfdist}/doc/latex/complexity
%doc %{texmfdist}/doc/latex/concprog
%doc %{texmfdist}/doc/latex/confproc
%doc %{texmfdist}/doc/latex/courier-scaled
%doc %{texmfdist}/doc/latex/courseoutline
%doc %{texmfdist}/doc/latex/coursepaper
%doc %{texmfdist}/doc/latex/coverpage
%doc %{texmfdist}/doc/latex/covington
%doc %{texmfdist}/doc/latex/crossreference
%doc %{texmfdist}/doc/latex/cryst
%doc %{texmfdist}/doc/latex/csbulletin
%doc %{texmfdist}/doc/latex/csquotes
%doc %{texmfdist}/doc/latex/ctib
%doc %{texmfdist}/doc/latex/cursor
%doc %{texmfdist}/doc/latex/cv
%doc %{texmfdist}/doc/latex/cweb-latex
%doc %{texmfdist}/doc/latex/dateiliste
%doc %{texmfdist}/doc/latex/datetime
%doc %{texmfdist}/doc/latex/dcpic
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
%doc %{texmfdist}/doc/latex/eCards
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
%doc %{texmfdist}/doc/latex/elsevier
%doc %{texmfdist}/doc/latex/em
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
%doc %{texmfdist}/doc/latex/euproposal
%doc %{texmfdist}/doc/latex/euro
%doc %{texmfdist}/doc/latex/europecv
%doc %{texmfdist}/doc/latex/eurosans
%doc %{texmfdist}/doc/latex/everypage
%doc %{texmfdist}/doc/latex/examplep
%doc %{texmfdist}/doc/latex/exceltex
%doc %{texmfdist}/doc/latex/exercise
%doc %{texmfdist}/doc/latex/expl3
%doc %{texmfdist}/doc/latex/extarrows
%doc %{texmfdist}/doc/latex/extract
%doc %{texmfdist}/doc/latex/facsimile
%doc %{texmfdist}/doc/latex/fancynum
%doc %{texmfdist}/doc/latex/fancyref
%doc %{texmfdist}/doc/latex/fancytooltips
# %doc %{texmfdist}/doc/latex/fax
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
%doc %{texmfdist}/doc/latex/fribrief
%doc %{texmfdist}/doc/latex/frletter
%doc %{texmfdist}/doc/latex/frontespizio
%doc %{texmfdist}/doc/latex/fullblck
%doc %{texmfdist}/doc/latex/fullpict
%doc %{texmfdist}/doc/latex/fundus
%doc %{texmfdist}/doc/latex/gaceta
%doc %{texmfdist}/doc/latex/gastex
%doc %{texmfdist}/doc/latex/gatech-thesis
%doc %{texmfdist}/doc/latex/gauss
%doc %{texmfdist}/doc/latex/gb4e
%doc %{texmfdist}/doc/latex/gcard
%doc %{texmfdist}/doc/latex/gcite
%doc %{texmfdist}/doc/latex/genmpage
# %doc %{texmfdist}/doc/latex/geomsty
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
%doc %{texmfdist}/doc/latex/greektex
%doc %{texmfdist}/doc/latex/grfpaste
# %doc %{texmfdist}/doc/latex/grnumalt
%doc %{texmfdist}/doc/latex/grverb
%doc %{texmfdist}/doc/latex/gu
# %doc %{texmfdist}/doc/latex/guitbeamer
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
%doc %{texmfdist}/doc/latex/inlinebib
%doc %{texmfdist}/doc/latex/inlinedef
%doc %{texmfdist}/doc/latex/interactiveworkbook
# %doc %{texmfdist}/doc/latex/invoice
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
%doc %{texmfdist}/doc/latex/listbib
%doc %{texmfdist}/doc/latex/lkproof
# %doc %{texmfdist}/doc/latex/logic
%doc %{texmfdist}/doc/latex/ltxindex
%doc %{texmfdist}/doc/latex/mafr
%doc %{texmfdist}/doc/latex/magyar
%doc %{texmfdist}/doc/latex/mailing
%doc %{texmfdist}/doc/latex/makebarcode
%doc %{texmfdist}/doc/latex/makedtx
%doc %{texmfdist}/doc/latex/makeglos
%doc %{texmfdist}/doc/latex/mathdesign
%doc %{texmfdist}/doc/latex/mathpazo
%doc %{texmfdist}/doc/latex/mceinleger
%doc %{texmfdist}/doc/latex/memexsupp
%doc %{texmfdist}/doc/latex/metaplot
%doc %{texmfdist}/doc/latex/mff
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
%doc %{texmfdist}/doc/latex/mslapa
%doc %{texmfdist}/doc/latex/mtgreek
%doc %{texmfdist}/doc/latex/multibbl
%doc %{texmfdist}/doc/latex/multirow
%doc %{texmfdist}/doc/latex/munich
%doc %{texmfdist}/doc/latex/muthesis
%doc %{texmfdist}/doc/latex/mxd
# %doc %{texmfdist}/doc/latex/mxedruli
%doc %{texmfdist}/doc/latex/ncclatex
%doc %{texmfdist}/doc/latex/ncctools
%doc %{texmfdist}/doc/latex/nddiss
# %doc %{texmfdist}/doc/latex/newalg
%doc %{texmfdist}/doc/latex/newfile
%doc %{texmfdist}/doc/latex/newlfm
%doc %{texmfdist}/doc/latex/newspaper
%doc %{texmfdist}/doc/latex/nomentbl
%doc %{texmfdist}/doc/latex/nonfloat
%doc %{texmfdist}/doc/latex/numname
%doc %{texmfdist}/doc/latex/ocr-latex
%doc %{texmfdist}/doc/latex/ogham
# %doc %{texmfdist}/doc/latex/ogonek
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
%doc %{texmfdist}/doc/latex/polyglot
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
%doc %{texmfdist}/doc/latex/rlepsf
%doc %{texmfdist}/doc/latex/rmpage
%doc %{texmfdist}/doc/latex/robustindex
# %doc %{texmfdist}/doc/latex/rst
%doc %{texmfdist}/doc/latex/rtkinenc
%doc %{texmfdist}/doc/latex/rtklage
%doc %{texmfdist}/doc/latex/sagetex
%doc %{texmfdist}/doc/latex/sanskrit
%doc %{texmfdist}/doc/latex/sauerj
%doc %{texmfdist}/doc/latex/sauterfonts
%doc %{texmfdist}/doc/latex/savefnmark
%doc %{texmfdist}/doc/latex/savetrees
%doc %{texmfdist}/doc/latex/scalebar
%doc %{texmfdist}/doc/latex/scientificpaper
%doc %{texmfdist}/doc/latex/sciwordconv
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
# %doc %{texmfdist}/doc/latex/smflatex
%doc %{texmfdist}/doc/latex/snapshot
%doc %{texmfdist}/doc/latex/sort-by-letters
%doc %{texmfdist}/doc/latex/soyombo
%doc %{texmfdist}/doc/latex/sparklines
%doc %{texmfdist}/doc/latex/spie
%doc %{texmfdist}/doc/latex/splitbib
%doc %{texmfdist}/doc/latex/spotcolor
%doc %{texmfdist}/doc/latex/sprite
%doc %{texmfdist}/doc/latex/srcltx
%doc %{texmfdist}/doc/latex/ssqquote
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
%doc %{texmfdist}/doc/latex/tapir
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
%doc %{texmfdist}/doc/latex/timesht
%doc %{texmfdist}/doc/latex/titling
%doc %{texmfdist}/doc/latex/tocvsec2
%doc %{texmfdist}/doc/latex/tokenizer
%doc %{texmfdist}/doc/latex/toolbox
%doc %{texmfdist}/doc/latex/toptesi
%doc %{texmfdist}/doc/latex/trajan
%doc %{texmfdist}/doc/latex/translator
%doc %{texmfdist}/doc/latex/trivfloat
%doc %{texmfdist}/doc/latex/turnstile
%doc %{texmfdist}/doc/latex/twoup
%doc %{texmfdist}/doc/latex/typogrid
%doc %{texmfdist}/doc/latex/umlaute
%doc %{texmfdist}/doc/latex/undertilde
%doc %{texmfdist}/doc/latex/unitsdef
%doc %{texmfdist}/doc/latex/unroman
%doc %{texmfdist}/doc/latex/upmethodology
%doc %{texmfdist}/doc/latex/urlbst
%doc %{texmfdist}/doc/latex/varindex
%doc %{texmfdist}/doc/latex/varsfromjobname
%doc %{texmfdist}/doc/latex/vector
%doc %{texmfdist}/doc/latex/verse
%doc %{texmfdist}/doc/latex/vhistory
%doc %{texmfdist}/doc/latex/vita
%doc %{texmfdist}/doc/latex/volumes
%doc %{texmfdist}/doc/latex/vpe
%doc %{texmfdist}/doc/latex/vrsion
%doc %{texmfdist}/doc/latex/vwcol
%doc %{texmfdist}/doc/latex/vxu
%doc %{texmfdist}/doc/latex/wadalab
%doc %{texmfdist}/doc/latex/wallpaper
%doc %{texmfdist}/doc/latex/warpcol
%doc %{texmfdist}/doc/latex/wnri
%doc %{texmfdist}/doc/latex/wordlike
%doc %{texmfdist}/doc/latex/xargs
%doc %{texmfdist}/doc/latex/xdoc
%doc %{texmfdist}/doc/latex/xfor
%doc %{texmfdist}/doc/latex/xifthen
%doc %{texmfdist}/doc/latex/xmpincl
%doc %{texmfdist}/doc/latex/xnewcommand
%doc %{texmfdist}/doc/latex/xoptarg
%doc %{texmfdist}/doc/latex/xpackages
%doc %{texmfdist}/doc/latex/xskak
# %doc %{texmfdist}/doc/latex/xstring
%doc %{texmfdist}/doc/latex/xtcapts
%doc %{texmfdist}/doc/latex/xyling
%doc %{texmfdist}/doc/latex/xytree
%doc %{texmfdist}/doc/latex/yafoot
%doc %{texmfdist}/doc/latex/yhmath
%doc %{texmfdist}/doc/latex/york-thesis
%doc %{texmfdist}/doc/latex/yplan
%doc %{texmfdist}/doc/latex/zed-csp
%doc %{texmfdist}/doc/latex/zefonts
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
# %{texmfdist}/source/latex/eqnarray
%{texmfdist}/source/latex/esdiff
%{texmfdist}/source/latex/esvect
%{texmfdist}/source/latex/extpfeil
%{texmfdist}/source/latex/fouridx
%{texmfdist}/source/latex/functan
%{texmfdist}/source/latex/galois
%{texmfdist}/source/latex/gnuplottex
%{texmfdist}/source/latex/hhtensor
%{texmfdist}/source/latex/logpap
%{texmfdist}/source/latex/noitcrul
%{texmfdist}/source/latex/permute
%{texmfdist}/source/latex/qsymbols
%{texmfdist}/source/latex/subdepth
%{texmfdist}/source/latex/faktor
%{texmfdist}/source/latex/sseq
%{texmfdist}/source/latex/trsym
%{texmfdist}/source/latex/petri-nets
%{texmfdist}/source/latex/mattens
%{texmfdist}/source/latex/mlist
%{texmfdist}/source/latex/numprint

%files -n texlive-latex-math
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/eco
%doc %{texmfdist}/doc/latex/bez123
%doc %{texmfdist}/doc/latex/binomexp
# %doc %{texmfdist}/doc/latex/cmll
%doc %{texmfdist}/doc/latex/constants
%doc %{texmfdist}/doc/latex/coordsys
%doc %{texmfdist}/doc/latex/egplot
%doc %{texmfdist}/doc/latex/eqlist
# %doc %{texmfdist}/doc/latex/eqnarray
%doc %{texmfdist}/doc/latex/esdiff
%doc %{texmfdist}/doc/latex/esvect
%doc %{texmfdist}/doc/latex/extpfeil
%doc %{texmfdist}/doc/latex/faktor
%doc %{texmfdist}/doc/latex/fouridx
%doc %{texmfdist}/doc/latex/functan
%doc %{texmfdist}/doc/latex/galois
%doc %{texmfdist}/doc/latex/gnuplottex
%doc %{texmfdist}/doc/latex/hhtensor
%doc %{texmfdist}/doc/latex/logpap
%doc %{texmfdist}/doc/latex/makeplot
%doc %{texmfdist}/doc/latex/maybemath
%doc %{texmfdist}/doc/latex/mattens
%doc %{texmfdist}/doc/latex/mfpic4ode
%doc %{texmfdist}/doc/latex/mhequ
%doc %{texmfdist}/doc/latex/mlist
%doc %{texmfdist}/doc/latex/nath
%doc %{texmfdist}/doc/latex/noitcrul
%doc %{texmfdist}/doc/latex/numprint
%doc %{texmfdist}/doc/latex/permute
%doc %{texmfdist}/doc/latex/petri-nets
%doc %{texmfdist}/doc/latex/qsymbols
%doc %{texmfdist}/doc/latex/qtree
%doc %{texmfdist}/doc/latex/sdrt
%doc %{texmfdist}/doc/latex/semantic
%doc %{texmfdist}/doc/latex/simplewick
%doc %{texmfdist}/doc/latex/sseq
%doc %{texmfdist}/doc/latex/subdepth
%doc %{texmfdist}/doc/latex/subeqn
%doc %{texmfdist}/doc/latex/subeqnarray
%doc %{texmfdist}/doc/latex/trfsigns
%doc %{texmfdist}/doc/latex/trsym
%doc %{texmfdist}/doc/latex/ulsy
%{texmfdist}/fonts/map/dvips/cmll
%{texmfdist}/fonts/map/dvips/esvect
%{texmfdist}/fonts/source/public/cmll
%{texmfdist}/fonts/source/public/esvect
%{texmfdist}/fonts/source/public/trsym
%{texmfdist}/fonts/source/public/ulsy
%{texmfdist}/fonts/tfm/public/cmll
%{texmfdist}/fonts/tfm/public/eco
%{texmfdist}/fonts/tfm/public/esvect
%{texmfdist}/fonts/tfm/public/trsym
%{texmfdist}/fonts/tfm/public/ulsy
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
%{texmfdist}/source/latex/ulsy
%{texmfdist}/tex/latex/bez123
%{texmfdist}/tex/latex/binomexp
%{texmfdist}/tex/latex/cmll
%{texmfdist}/tex/latex/constants
%{texmfdist}/tex/latex/coordsys
%{texmfdist}/tex/latex/dotseqn
%{texmfdist}/tex/latex/egplot
%{texmfdist}/tex/latex/eqlist
# %{texmfdist}/tex/latex/eqnarray
%{texmfdist}/tex/latex/esdiff
%{texmfdist}/tex/latex/esvect
%{texmfdist}/tex/latex/extpfeil
%{texmfdist}/tex/latex/faktor
%{texmfdist}/tex/latex/fouridx
%{texmfdist}/tex/latex/functan
%{texmfdist}/tex/latex/galois
%{texmfdist}/tex/latex/gnuplottex
%{texmfdist}/tex/latex/hhtensor
%{texmfdist}/tex/latex/logpap
%{texmfdist}/tex/latex/makeplot
%{texmfdist}/tex/latex/maybemath
%{texmfdist}/tex/latex/mattens
%{texmfdist}/tex/latex/mfpic4ode
%{texmfdist}/tex/latex/mhequ
%{texmfdist}/tex/latex/mhs
%{texmfdist}/tex/latex/mlist
%{texmfdist}/tex/latex/nath
%{texmfdist}/tex/latex/noitcrul
%{texmfdist}/tex/latex/numprint
%{texmfdist}/tex/latex/permute
%{texmfdist}/tex/latex/petri-nets
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
%{texmfdist}/tex/latex/trfsigns
%{texmfdist}/tex/latex/trsym
%{texmfdist}/tex/latex/ulsy
%doc %{texmfdist}/doc/latex/tree-dvips
%{texmfdist}/source/latex/tree-dvips
%{texmfdist}/tex/latex/tree-dvips

%files -n texlive-latex-physics
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/circ
%doc %{texmfdist}/doc/latex/colorwav
%doc %{texmfdist}/doc/latex/dyntree
%doc %{texmfdist}/doc/latex/feynmf
%doc %{texmfdist}/doc/latex/formula
%doc %{texmfdist}/doc/latex/listofsymbols
%doc %{texmfdist}/doc/latex/miller
%doc %{texmfdist}/doc/latex/susy
%{texmfdist}/metapost/feynmf
%{texmfdist}/source/latex/circ
%{texmfdist}/source/latex/colorwav
%{texmfdist}/source/latex/dyntree
%{texmfdist}/source/latex/feynmf
%{texmfdist}/source/latex/formula
%{texmfdist}/source/latex/isotope
%{texmfdist}/source/latex/miller
%{texmfdist}/tex/latex/circ
%{texmfdist}/tex/latex/colorwav
%{texmfdist}/tex/latex/dyntree
%{texmfdist}/tex/latex/feynmf
%{texmfdist}/tex/latex/formula
%{texmfdist}/tex/latex/isotope
%{texmfdist}/tex/latex/listofsymbols
%{texmfdist}/tex/latex/miller
%{texmfdist}/tex/latex/susy
%{texmfdist}/fonts/source/public/circ
%{texmfdist}/fonts/tfm/public/circ

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

%files -n texlive-latex-biology
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/biocon
%doc %{texmfdist}/doc/latex/dnaseq
# %{texmfdist}/bibtex/bib/biocon
# %{texmfdist}/source/latex/biocon
%{texmfdist}/source/latex/dnaseq
%{texmfdist}/tex/latex/biocon
%{texmfdist}/tex/latex/dnaseq

%files -n texlive-latex-pdftools
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/attachfile
%doc %{texmfdist}/doc/latex/cooltooltips
%doc %{texmfdist}/doc/latex/movie15
%doc %{texmfdist}/doc/latex/pdfcprot
%doc %{texmfdist}/doc/latex/pdfscreen
%doc %{texmfdist}/doc/latex/pdfsync
%doc %{texmfdist}/doc/latex/pdftricks
%{texmfdist}/source/latex/attachfile
%{texmfdist}/source/latex/cooltooltips
%{texmfdist}/source/latex/pdfcprot
%{texmfdist}/tex/latex/attachfile
%{texmfdist}/tex/latex/cooltooltips
%{texmfdist}/tex/latex/movie15
%{texmfdist}/tex/latex/pdfcprot
%{texmfdist}/tex/latex/pdfscreen
%{texmfdist}/tex/latex/pdfsync
%{texmfdist}/tex/latex/pdftricks

%files -n texlive-latex-informatic
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/alg
%doc %{texmfdist}/doc/latex/bytefield
%doc %{texmfdist}/doc/latex/lsc
%doc %{texmfdist}/doc/latex/method
%doc %{texmfdist}/doc/latex/msc
# %doc %{texmfdist}/doc/latex/progkeys
%doc %{texmfdist}/doc/latex/register
%doc %{texmfdist}/doc/latex/uml
%{texmfdist}/source/latex/alg
%{texmfdist}/source/latex/bytefield
%{texmfdist}/source/latex/method
# %{texmfdist}/source/latex/progkeys
%{texmfdist}/source/latex/register
%{texmfdist}/source/latex/uml
%{texmfdist}/tex/latex/alg
%{texmfdist}/tex/latex/bytefield
%{texmfdist}/tex/latex/lsc
%{texmfdist}/tex/latex/method
%{texmfdist}/tex/latex/msc
# %{texmfdist}/tex/latex/progkeys
%{texmfdist}/tex/latex/register
%{texmfdist}/tex/latex/uml

%files -n texlive-latex-games
%defattr(644,root,root,755)
# %doc %{texmfdist}/doc/latex/backgammon
%doc %{texmfdist}/doc/latex/chessboard
%doc %{texmfdist}/doc/latex/chessfss
%doc %{texmfdist}/doc/latex/crosswrd
%doc %{texmfdist}/doc/latex/cwpuzzle
%doc %{texmfdist}/doc/latex/jeopardy
%doc %{texmfdist}/doc/latex/othello
%doc %{texmfdist}/doc/latex/sgame
%doc %{texmfdist}/doc/latex/skak
%doc %{texmfdist}/doc/latex/sudoku
%doc %{texmfdist}/doc/latex/sudokubundle
%{texmfdist}/fonts/enc/dvips/chessfss
%{texmfdist}/fonts/map/dvips/skak
# %{texmfdist}/fonts/source/public/backgammon
%{texmfdist}/fonts/source/public/cchess
%{texmfdist}/fonts/source/public/chess
%{texmfdist}/fonts/source/public/go
%{texmfdist}/fonts/source/public/othello
%{texmfdist}/fonts/source/public/skak
# %{texmfdist}/fonts/tfm/public/backgammon
%{texmfdist}/fonts/tfm/public/cchess
%{texmfdist}/fonts/tfm/public/go
%{texmfdist}/fonts/tfm/public/othello
%{texmfdist}/fonts/tfm/public/skak
# %{texmfdist}/source/latex/backgammon
%{texmfdist}/source/latex/chessboard
%{texmfdist}/source/latex/chessfss
%{texmfdist}/source/latex/crosswrd
%{texmfdist}/source/latex/cwpuzzle
%{texmfdist}/source/latex/go
%{texmfdist}/source/latex/jeopardy
# %{texmfdist}/source/latex/othello
%{texmfdist}/source/latex/sudoku
%{texmfdist}/source/latex/sudokubundle
# %{texmfdist}/tex/latex/backgammon
%{texmfdist}/tex/latex/cchess
%{texmfdist}/tex/latex/chess
%{texmfdist}/tex/latex/chessboard
%{texmfdist}/tex/latex/chessfss
%{texmfdist}/tex/latex/crosswrd
%{texmfdist}/tex/latex/cwpuzzle
%{texmfdist}/tex/latex/go
%{texmfdist}/tex/latex/jeopardy
%{texmfdist}/tex/latex/othello
%{texmfdist}/tex/latex/sgame
%{texmfdist}/tex/latex/skak
%{texmfdist}/tex/latex/sudoku
%{texmfdist}/tex/latex/sudokubundle

%files -n texlive-latex-sources
%defattr(644,root,root,755)
%{texmfdist}/source/latex/acronym
%{texmfdist}/source/latex/adrlist
%{texmfdist}/source/latex/altfont
%{texmfdist}/source/latex/ascii
%{texmfdist}/source/latex/augie
%{texmfdist}/source/latex/barcodes
%{texmfdist}/source/latex/bbding
%{texmfdist}/source/latex/bbm-macros
%{texmfdist}/source/latex/bengali
%{texmfdist}/source/latex/beton
%{texmfdist}/source/latex/bibarts
%{texmfdist}/source/latex/bibleref
%{texmfdist}/source/latex/biblist
%{texmfdist}/source/latex/bigfoot
%{texmfdist}/source/latex/bizcard
%{texmfdist}/source/latex/blindtext
%{texmfdist}/source/latex/bookhands
%{texmfdist}/source/latex/bophook
%{texmfdist}/source/latex/boxhandler
%{texmfdist}/source/latex/braille
%{texmfdist}/source/latex/breakurl
%{texmfdist}/source/latex/brushscr
%{texmfdist}/source/latex/burmese
%{texmfdist}/source/latex/captcont
%{texmfdist}/source/latex/catechis
%{texmfdist}/source/latex/cclicenses
%{texmfdist}/source/latex/cd
%{texmfdist}/source/latex/cd-cover
%{texmfdist}/source/latex/cdpbundl
%{texmfdist}/source/latex/changes
%{texmfdist}/source/latex/chapterfolder
%{texmfdist}/source/latex/cleveref
%{texmfdist}/source/latex/cmcyralt
%{texmfdist}/source/latex/cmsd
%{texmfdist}/source/latex/codepage
%{texmfdist}/source/latex/confproc
%{texmfdist}/source/latex/coverpage
%{texmfdist}/source/latex/crop
%{texmfdist}/source/latex/crossreference
%{texmfdist}/source/latex/ctib
%{texmfdist}/source/latex/cweb-latex
%{texmfdist}/source/latex/dateiliste
%{texmfdist}/source/latex/datetime
%{texmfdist}/source/latex/decimal
%{texmfdist}/source/latex/diagnose
%{texmfdist}/source/latex/docmfp
%{texmfdist}/source/latex/doipubmed
%{texmfdist}/source/latex/dotarrow
%{texmfdist}/source/latex/dottex
%{texmfdist}/source/latex/drac
%{texmfdist}/source/latex/draftcopy
%{texmfdist}/source/latex/dramatist
%{texmfdist}/source/latex/eCards
%{texmfdist}/source/latex/ebezier
%{texmfdist}/source/latex/ebsthesis
%{texmfdist}/source/latex/ecclesiastic
%{texmfdist}/source/latex/edmargin
%{texmfdist}/source/latex/eemeir
# %{texmfdist}/source/latex/eiad
%{texmfdist}/source/latex/ellipsis
%{texmfdist}/source/latex/em
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
%{texmfdist}/source/latex/euproposal
%{texmfdist}/source/latex/euro
%{texmfdist}/source/latex/everypage
%{texmfdist}/source/latex/exercise
%{texmfdist}/source/latex/expl3
%{texmfdist}/source/latex/extract
%{texmfdist}/source/latex/facsimile
%{texmfdist}/source/latex/fancynum
%{texmfdist}/source/latex/fancyref
%{texmfdist}/source/latex/fancytooltips
%{texmfdist}/source/latex/fancyvrb
%{texmfdist}/source/latex/figsize
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
%{texmfdist}/source/latex/fundus
%{texmfdist}/source/latex/gcite
%{texmfdist}/source/latex/genmpage
%{texmfdist}/source/latex/geometry
# %{texmfdist}/source/latex/geomsty
%{texmfdist}/source/latex/glossaries
%{texmfdist}/source/latex/graphics
%{texmfdist}/source/latex/graphicx-psmin
%{texmfdist}/source/latex/greekdates
# %{texmfdist}/source/latex/grnumalt
%{texmfdist}/source/latex/grverb
%{texmfdist}/source/latex/hanging
%{texmfdist}/source/latex/harvard
%{texmfdist}/source/latex/hc
%{texmfdist}/source/latex/hepthesis
# %{texmfdist}/source/latex/hilowres
%{texmfdist}/source/latex/histogr
%{texmfdist}/source/latex/hpsdiss
%{texmfdist}/source/latex/hyper
%{texmfdist}/source/latex/hyperref
%{texmfdist}/source/latex/hyperxmp
%{texmfdist}/source/latex/hyphenat
%{texmfdist}/source/latex/ibycus-babel
%{texmfdist}/source/latex/icsv
%{texmfdist}/source/latex/ifmslide
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
# %{texmfdist}/source/latex/kdgreek
%{texmfdist}/source/latex/koma-script
%{texmfdist}/source/latex/labels
%{texmfdist}/source/latex/layouts
%{texmfdist}/source/latex/listings
%{texmfdist}/source/latex/localloc
%{texmfdist}/source/latex/mathcomp
%{texmfdist}/source/latex/mathpazo
%{texmfdist}/source/latex/mdwtools
%{texmfdist}/source/latex/memoir
%{texmfdist}/source/latex/mh
%{texmfdist}/source/latex/mnsymbol
%{texmfdist}/source/latex/modroman
%{texmfdist}/source/latex/mongolian-babel
# %{texmfdist}/source/latex/montex
%{texmfdist}/source/latex/mparhack
%{texmfdist}/source/latex/ms
%{texmfdist}/source/latex/multibib
%{texmfdist}/source/latex/mwcls
%{texmfdist}/source/latex/natbib
%{texmfdist}/source/latex/ncctools
%{texmfdist}/source/latex/nddiss
# %{texmfdist}/source/latex/newalg
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
%{texmfdist}/source/latex/technics
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
%{texmfdist}/source/latex/timesht
%{texmfdist}/source/latex/titling
%{texmfdist}/source/latex/tocbibind
%{texmfdist}/source/latex/tocloft
%{texmfdist}/source/latex/tools
%{texmfdist}/source/latex/totpages
%{texmfdist}/source/latex/type1cm
%{texmfdist}/source/latex/undertilde
%{texmfdist}/source/latex/units
%{texmfdist}/source/latex/unitsdef
%{texmfdist}/source/latex/unroman
%{texmfdist}/source/latex/upmethodology
%{texmfdist}/source/latex/urlbst
%{texmfdist}/source/latex/varindex
%{texmfdist}/source/latex/vector
%{texmfdist}/source/latex/verse
%{texmfdist}/source/latex/vmargin
%{texmfdist}/source/latex/volumes
%{texmfdist}/source/latex/vrsion
%{texmfdist}/source/latex/vwcol
%{texmfdist}/source/latex/vxu
%{texmfdist}/source/latex/warning
%{texmfdist}/source/latex/warpcol
%{texmfdist}/source/latex/was
%{texmfdist}/source/latex/xargs
%{texmfdist}/source/latex/xdoc
%{texmfdist}/source/latex/xfor
%{texmfdist}/source/latex/xmpincl
%{texmfdist}/source/latex/xpackages
%{texmfdist}/source/latex/xskak
%{texmfdist}/source/latex/xtab
%{texmfdist}/source/latex/xtcapts
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
%doc %{texmfdist}/doc/latex/apacite
%doc %{texmfdist}/doc/latex/asaetr
%doc %{texmfdist}/doc/latex/computational-complexity
%doc %{texmfdist}/doc/latex/dtk
%doc %{texmfdist}/doc/latex/elsarticle
%doc %{texmfdist}/doc/latex/lettre
%doc %{texmfdist}/doc/latex/lexikon
%doc %{texmfdist}/doc/latex/lps
%doc %{texmfdist}/doc/latex/manuscript
%doc %{texmfdist}/doc/latex/maple
%doc %{texmfdist}/doc/latex/mentis
%doc %{texmfdist}/doc/latex/nature
%doc %{texmfdist}/doc/latex/nih
%doc %{texmfdist}/doc/latex/nostarch
%doc %{texmfdist}/doc/latex/nrc
%doc %{texmfdist}/doc/latex/octavo
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
%doc %{texmfdist}/doc/latex/ptptex
%doc %{texmfdist}/doc/latex/refman
%doc %{texmfdist}/doc/latex/rsc
%doc %{texmfdist}/doc/latex/screenplay
%doc %{texmfdist}/doc/latex/script
%doc %{texmfdist}/doc/latex/shipunov
%doc %{texmfdist}/doc/latex/sides
%doc %{texmfdist}/doc/latex/siggraph
%doc %{texmfdist}/doc/latex/stage
%doc %{texmfdist}/doc/latex/tufte-latex
%doc %{texmfdist}/doc/latex/tugboat
%doc %{texmfdist}/doc/latex/uaclasses
%doc %{texmfdist}/doc/latex/ucthesis
%doc %{texmfdist}/doc/latex/uiucthesis
%doc %{texmfdist}/doc/latex/umich-thesis
%doc %{texmfdist}/doc/latex/umthesis
%doc %{texmfdist}/doc/latex/uwthesis
# %{texmfdist}/bibtex/bib/aiaa
# %{texmfdist}/bibtex/bib/apacite
# %{texmfdist}/bibtex/bib/asaetr
%{texmfdist}/bibtex/bib/computational-complexity
%{texmfdist}/bibtex/bib/dtk
%{texmfdist}/bibtex/bib/philosophersimprint
%{texmfdist}/bibtex/bst/aiaa
%{texmfdist}/bibtex/bst/apacite
%{texmfdist}/bibtex/bst/asaetr
%{texmfdist}/bibtex/bst/computational-complexity
%{texmfdist}/bibtex/bst/dtk
%{texmfdist}/bibtex/bst/rsc
%{texmfdist}/source/latex/IEEEconf
%{texmfdist}/source/latex/aastex
%{texmfdist}/source/latex/acmconf
%{texmfdist}/source/latex/active-conf
%{texmfdist}/source/latex/aiaa
%{texmfdist}/source/latex/apacite
# %{texmfdist}/source/latex/asaetr
%{texmfdist}/source/latex/computational-complexity
%{texmfdist}/source/latex/dtk
%{texmfdist}/source/latex/elsarticle
%{texmfdist}/source/latex/lexikon
%{texmfdist}/source/latex/lps
%{texmfdist}/source/latex/manuscript
%{texmfdist}/source/latex/mentis
%{texmfdist}/source/latex/menu
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
%{texmfdist}/source/latex/rsc
%{texmfdist}/source/latex/screenplay
%{texmfdist}/source/latex/siggraph
%{texmfdist}/source/latex/tugboat
%{texmfdist}/source/latex/uaclasses
%{texmfdist}/source/latex/uiucthesis
%{texmfdist}/tex/latex/IEEEconf
%{texmfdist}/tex/latex/aastex
%{texmfdist}/tex/latex/acmconf
%{texmfdist}/tex/latex/active-conf
%{texmfdist}/tex/latex/aiaa
%{texmfdist}/tex/latex/apacite
%{texmfdist}/tex/latex/asaetr
%{texmfdist}/tex/latex/computational-complexity
%{texmfdist}/tex/latex/dtk
%{texmfdist}/tex/latex/elsarticle
%{texmfdist}/tex/latex/lettre
%{texmfdist}/tex/latex/lexikon
%{texmfdist}/tex/latex/lps
%{texmfdist}/tex/latex/manuscript
%{texmfdist}/tex/latex/maple
%{texmfdist}/tex/latex/mentis
%{texmfdist}/tex/latex/menu
%{texmfdist}/tex/latex/muthesis
%{texmfdist}/tex/latex/nature
%{texmfdist}/tex/latex/nih
%{texmfdist}/tex/latex/nostarch
%{texmfdist}/tex/latex/nrc
%{texmfdist}/tex/latex/octavo
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
%{texmfdist}/tex/latex/ptptex
%{texmfdist}/tex/latex/refman
%{texmfdist}/tex/latex/rsc
%{texmfdist}/tex/latex/screenplay
%{texmfdist}/tex/latex/script
%{texmfdist}/tex/latex/shipunov
%{texmfdist}/tex/latex/sides
%{texmfdist}/tex/latex/siggraph
%{texmfdist}/tex/latex/stage
%{texmfdist}/tex/latex/tufte-latex
%{texmfdist}/tex/latex/tugboat
%{texmfdist}/tex/latex/uaclasses
%{texmfdist}/tex/latex/ucthesis
%{texmfdist}/tex/latex/uiucthesis
%{texmfdist}/tex/latex/umich-thesis
%{texmfdist}/tex/latex/umthesis
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
%{texmfdist}/tex/latex/mla-paper

%files -n texlive-latex-music
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/musixps
%doc %{texmfdist}/doc/latex/abc
%doc %{texmfdist}/doc/latex/guitar
%doc %{texmfdist}/doc/latex/musixlyr
%doc %{texmfdist}/doc/latex/songbook
%{texmfdist}/fonts/source/public/musixps
%{texmfdist}/fonts/tfm/public/musixps
%{texmfdist}/source/latex/abc
%{texmfdist}/source/latex/guitar
%{texmfdist}/source/latex/songbook
%{texmfdist}/tex/generic/musixlyr
%{texmfdist}/tex/generic/musixps
%{texmfdist}/tex/latex/abc
%{texmfdist}/tex/latex/guitar
%{texmfdist}/tex/latex/songbook

%files -n texlive-latex-extend
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/HA-prosper
%doc %{texmfdist}/doc/latex/addlines
%doc %{texmfdist}/doc/latex/alnumsec
%doc %{texmfdist}/doc/latex/arydshln
%doc %{texmfdist}/doc/latex/babelbib
%doc %{texmfdist}/doc/latex/bibtopicprefix
%doc %{texmfdist}/doc/latex/boites
%doc %{texmfdist}/doc/latex/booklet
%doc %{texmfdist}/doc/latex/bullcntr
%doc %{texmfdist}/doc/latex/chappg
%doc %{texmfdist}/doc/latex/clefval
%doc %{texmfdist}/doc/latex/colortbl
%doc %{texmfdist}/doc/latex/combine
%doc %{texmfdist}/doc/latex/contour
%doc %{texmfdist}/doc/latex/ctable
%doc %{texmfdist}/doc/latex/curve2e
%doc %{texmfdist}/doc/latex/dashrule
%doc %{texmfdist}/doc/latex/etaremune
%doc %{texmfdist}/doc/latex/expdlist
%doc %{texmfdist}/doc/latex/leading
%doc %{texmfdist}/doc/latex/listliketab
%doc %{texmfdist}/doc/latex/makebox
%doc %{texmfdist}/doc/latex/makecell
%doc %{texmfdist}/doc/latex/marginnote
%doc %{texmfdist}/doc/latex/mcaption
%doc %{texmfdist}/doc/latex/mcite
%doc %{texmfdist}/doc/latex/mciteplus
%doc %{texmfdist}/doc/latex/minipage-marginpar
%doc %{texmfdist}/doc/latex/miniplot
%doc %{texmfdist}/doc/latex/multicap
%doc %{texmfdist}/doc/latex/newvbtm
%doc %{texmfdist}/doc/latex/notes2bib
%doc %{texmfdist}/doc/latex/ntabbing
%doc %{texmfdist}/doc/latex/pbox
%doc %{texmfdist}/doc/latex/pinlabel
%doc %{texmfdist}/doc/latex/polytable
%doc %{texmfdist}/doc/latex/rccol
%doc %{texmfdist}/doc/latex/romannum
# %doc %{texmfdist}/doc/latex/schedule
%doc %{texmfdist}/doc/latex/subfloat
%doc %{texmfdist}/doc/latex/umoline
%doc %{texmfdist}/doc/latex/underlin
%{texmfdist}/bibtex/bst/babelbib
%{texmfdist}/bibtex/bst/mciteplus
%{texmfdist}/source/latex/HA-prosper
%{texmfdist}/source/latex/addlines
%{texmfdist}/source/latex/alnumsec
%{texmfdist}/source/latex/arydshln
%{texmfdist}/source/latex/babelbib
%{texmfdist}/source/latex/bibtopicprefix
%{texmfdist}/source/latex/boites
%{texmfdist}/source/latex/booklet
%{texmfdist}/source/latex/bullcntr
%{texmfdist}/source/latex/chappg
%{texmfdist}/source/latex/cjw
%{texmfdist}/source/latex/clefval
%{texmfdist}/source/latex/colortbl
%{texmfdist}/source/latex/combine
%{texmfdist}/source/latex/contour
%{texmfdist}/source/latex/ctable
%{texmfdist}/source/latex/curve2e
%{texmfdist}/source/latex/dashbox
%{texmfdist}/source/latex/dashrule
%{texmfdist}/source/latex/etaremune
%{texmfdist}/source/latex/expdlist
%{texmfdist}/source/latex/leading
%{texmfdist}/source/latex/listliketab
%{texmfdist}/source/latex/makebox
%{texmfdist}/source/latex/makecell
%{texmfdist}/source/latex/marginnote
%{texmfdist}/source/latex/mcaption
%{texmfdist}/source/latex/mcite
%{texmfdist}/source/latex/minipage-marginpar
%{texmfdist}/source/latex/multicap
%{texmfdist}/source/latex/newvbtm
%{texmfdist}/source/latex/notes2bib
%{texmfdist}/source/latex/pbox
%{texmfdist}/source/latex/polytable
%{texmfdist}/source/latex/rccol
%{texmfdist}/source/latex/romannum
# %{texmfdist}/source/latex/schedule
%{texmfdist}/source/latex/subfloat
%{texmfdist}/source/latex/umoline
%{texmfdist}/source/latex/underlin
%{texmfdist}/tex/latex/HA-prosper
%{texmfdist}/tex/latex/addlines
%{texmfdist}/tex/latex/alnumsec
%{texmfdist}/tex/latex/arydshln
%{texmfdist}/tex/latex/babelbib
%{texmfdist}/tex/latex/bibtopicprefix
%{texmfdist}/tex/latex/boites
%{texmfdist}/tex/latex/booklet
%{texmfdist}/tex/latex/bullcntr
%{texmfdist}/tex/latex/chappg
%{texmfdist}/tex/latex/cjw
%{texmfdist}/tex/latex/clefval
%{texmfdist}/tex/latex/colortbl
%{texmfdist}/tex/latex/combine
%{texmfdist}/tex/latex/contour
%{texmfdist}/tex/latex/ctable
%{texmfdist}/tex/latex/curve2e
%{texmfdist}/tex/latex/dashbox
%{texmfdist}/tex/latex/dashrule
%{texmfdist}/tex/latex/etaremune
%{texmfdist}/tex/latex/expdlist
%{texmfdist}/tex/latex/leading
%{texmfdist}/tex/latex/listliketab
%{texmfdist}/tex/latex/ltablex
%{texmfdist}/tex/latex/makebox
%{texmfdist}/tex/latex/makecell
%{texmfdist}/tex/latex/marginnote
%{texmfdist}/tex/latex/mcaption
%{texmfdist}/tex/latex/mcite
%{texmfdist}/tex/latex/mciteplus
%{texmfdist}/tex/latex/minipage-marginpar
%{texmfdist}/tex/latex/miniplot
%{texmfdist}/tex/latex/multicap
%{texmfdist}/tex/latex/newvbtm
%{texmfdist}/tex/latex/notes2bib
%{texmfdist}/tex/latex/ntabbing
# %{texmfdist}/tex/latex/numline
%{texmfdist}/tex/latex/pbox
%{texmfdist}/tex/latex/pinlabel
%{texmfdist}/tex/latex/polytable
%{texmfdist}/tex/latex/rccol
%{texmfdist}/tex/latex/romannum
# %{texmfdist}/tex/latex/schedule
%{texmfdist}/tex/latex/subfloat
%{texmfdist}/tex/latex/umoline
%{texmfdist}/tex/latex/underlin

%files -n texlive-latex-presentation
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/powerdot
%doc %{texmfdist}/doc/latex/ppower4
%doc %{texmfdist}/doc/latex/sciposter
%doc %{texmfdist}/doc/latex/tpslifonts
%{texmfdist}/scripts/ppower4
%{texmfdist}/source/latex/powerdot
%{texmfdist}/tex/latex/powerdot
%{texmfdist}/tex/latex/ppower4
%{texmfdist}/tex/latex/sciposter
%{texmfdist}/tex/latex/tpslifonts

%files -n texlive-latex-programming
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/cool
%doc %{texmfdist}/doc/latex/coollist
%doc %{texmfdist}/doc/latex/coolstr
%doc %{texmfdist}/doc/latex/csvtools
%doc %{texmfdist}/doc/latex/datatool
%doc %{texmfdist}/doc/latex/datenumber
%doc %{texmfdist}/doc/latex/delimtxt
%doc %{texmfdist}/doc/latex/dialogl
%doc %{texmfdist}/doc/latex/dprogress
%doc %{texmfdist}/doc/latex/environ
%doc %{texmfdist}/doc/latex/export
%doc %{texmfdist}/doc/latex/fmtcount
%doc %{texmfdist}/doc/latex/forarray
%doc %{texmfdist}/doc/latex/forloop
%doc %{texmfdist}/doc/latex/inversepath
%doc %{texmfdist}/doc/latex/labelcas
%doc %{texmfdist}/doc/latex/makecmds
%doc %{texmfdist}/doc/latex/nag
%doc %{texmfdist}/doc/latex/namespc
%doc %{texmfdist}/doc/latex/progress
%doc %{texmfdist}/doc/latex/randtext
%doc %{texmfdist}/doc/latex/regcount
%doc %{texmfdist}/doc/latex/robustcommand
%doc %{texmfdist}/doc/latex/splitindex
%doc %{texmfdist}/doc/latex/stringstrings
%doc %{texmfdist}/doc/latex/substr
%doc %{texmfdist}/doc/latex/typedref
%{texmfdist}/source/latex/cmdtrack
%{texmfdist}/source/latex/cool
%{texmfdist}/source/latex/coollist
%{texmfdist}/source/latex/coolstr
%{texmfdist}/source/latex/csvtools
%{texmfdist}/source/latex/datatool
%{texmfdist}/source/latex/datenumber
%{texmfdist}/source/latex/delimtxt
%{texmfdist}/source/latex/dialogl
%{texmfdist}/source/latex/dprogress
%{texmfdist}/source/latex/environ
%{texmfdist}/source/latex/export
%{texmfdist}/source/latex/fmtcount
%{texmfdist}/source/latex/forarray
%{texmfdist}/source/latex/forloop
%{texmfdist}/source/latex/inversepath
%{texmfdist}/source/latex/labelcas
%{texmfdist}/source/latex/lcg
%{texmfdist}/source/latex/makecmds
%{texmfdist}/source/latex/nag
%{texmfdist}/source/latex/namespc
%{texmfdist}/source/latex/patchcmd
%{texmfdist}/source/latex/regcount
%{texmfdist}/source/latex/robustcommand
%{texmfdist}/source/latex/splitindex
%{texmfdist}/source/latex/stack
%{texmfdist}/source/latex/stringstrings
%{texmfdist}/source/latex/typedref
%{texmfdist}/tex/latex/cmdtrack
%{texmfdist}/tex/latex/cool
%{texmfdist}/tex/latex/coollist
%{texmfdist}/tex/latex/coolstr
%{texmfdist}/tex/latex/csvtools
%{texmfdist}/tex/latex/datatool
%{texmfdist}/tex/latex/datenumber
%{texmfdist}/tex/latex/delimtxt
%{texmfdist}/tex/latex/dialogl
%{texmfdist}/tex/latex/dprogress
%{texmfdist}/tex/latex/environ
%{texmfdist}/tex/latex/export
%{texmfdist}/tex/latex/fmtcount
%{texmfdist}/tex/latex/forarray
%{texmfdist}/tex/latex/forloop
%{texmfdist}/tex/latex/inversepath
%{texmfdist}/tex/latex/labelcas
%{texmfdist}/tex/latex/lcg
%{texmfdist}/tex/latex/makecmds
%{texmfdist}/tex/latex/multido
%{texmfdist}/tex/latex/nag
%{texmfdist}/tex/latex/namespc
%{texmfdist}/tex/latex/patchcmd
%{texmfdist}/tex/latex/progress
%{texmfdist}/tex/latex/randtext
%{texmfdist}/tex/latex/regcount
%{texmfdist}/tex/latex/robustcommand
%{texmfdist}/tex/latex/splitindex
%{texmfdist}/tex/latex/stack
%{texmfdist}/tex/latex/stringstrings
%{texmfdist}/tex/latex/substr
%{texmfdist}/tex/latex/typedref

%files -n texlive-latex-effects
%defattr(644,root,root,755)
# %doc %{texmfdist}/doc/fonts/umrand
%doc %{texmfdist}/doc/latex/arcs
%doc %{texmfdist}/doc/latex/blowup
%doc %{texmfdist}/doc/latex/changebar
%doc %{texmfdist}/doc/latex/draftwatermark
%doc %{texmfdist}/doc/latex/flippdf
%doc %{texmfdist}/doc/latex/flowfram
%doc %{texmfdist}/doc/latex/isorot
%doc %{texmfdist}/doc/latex/lettrine
%doc %{texmfdist}/doc/latex/niceframe
%doc %{texmfdist}/doc/latex/notes
%doc %{texmfdist}/doc/latex/objectz
%doc %{texmfdist}/doc/latex/parallel
%doc %{texmfdist}/doc/latex/quotchap
%doc %{texmfdist}/doc/latex/rotpages
%doc %{texmfdist}/doc/latex/sectionbox
%doc %{texmfdist}/doc/latex/shadethm
%doc %{texmfdist}/doc/latex/ushort
%{texmfdist}/fonts/source/public/niceframe
# %{texmfdist}/fonts/source/public/umrand
%{texmfdist}/fonts/tfm/public/niceframe
# %{texmfdist}/fonts/tfm/public/umrand
%{texmfdist}/source/latex/arcs
%{texmfdist}/source/latex/blowup
%{texmfdist}/source/latex/changebar
%{texmfdist}/source/latex/draftwatermark
%{texmfdist}/source/latex/flippdf
%{texmfdist}/source/latex/flowfram
%{texmfdist}/source/latex/isorot
%{texmfdist}/source/latex/lettrine
%{texmfdist}/source/latex/niceframe
%{texmfdist}/source/latex/notes
%{texmfdist}/source/latex/objectz
%{texmfdist}/source/latex/parallel
%{texmfdist}/source/latex/quotchap
%{texmfdist}/source/latex/ushort
%{texmfdist}/tex/latex/arcs
%{texmfdist}/tex/latex/blowup
%{texmfdist}/tex/latex/changebar
%{texmfdist}/tex/latex/draftwatermark
%{texmfdist}/tex/latex/flippdf
%{texmfdist}/tex/latex/flowfram
%{texmfdist}/tex/latex/isorot
%{texmfdist}/tex/latex/lettrine
%{texmfdist}/tex/latex/niceframe
%{texmfdist}/tex/latex/notes
%{texmfdist}/tex/latex/objectz
%{texmfdist}/tex/latex/parallel
%{texmfdist}/tex/latex/quotchap
%{texmfdist}/tex/latex/rotpages
%{texmfdist}/tex/latex/sectionbox
%{texmfdist}/tex/latex/shadethm
# %{texmfdist}/tex/latex/umrand
%{texmfdist}/tex/latex/ushort

# I don't sort them, because maybe can splitting and grouping them
%files -n texlive-latex-other
%defattr(644,root,root,755)
%dir %{texmfdist}/source/alatex
%{texmfdist}/source/alatex/base
%dir %{texmfdist}/source/cslatex
%{texmfdist}/source/cslatex/base
%{texmfdist}/source/generic/xypic
# %{texmfdist}/source/latex/GuIT
# Definitive source of Plain TeX on CTAN.
%{texmfdist}/source/latex/base
%{texmfdist}/source/latex/bayer
# A small collection of minimal DTX examples.
%{texmfdist}/source/latex/dtxgallery
# Editorial Notes for LaTeX documents.
%{texmfdist}/source/latex/ed
# Typeset scholarly edition.
%{texmfdist}/source/latex/edmac
# Use AMS Euler fonts for math.
%{texmfdist}/source/latex/euler
# Ridgeway's fonts.
%{texmfdist}/source/latex/wnri
%dir %{texmfdist}/source/plain
%{texmfdist}/source/plain/jsmisc
%{texmfdist}/tex/alatex
%{texmfdist}/tex/generic/enctex
# Create a calendar, in German.
%{texmfdist}/tex/latex/kalender
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
%{texmfdist}/tex/latex/levy
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
# Lists contents of BibTeX files.
%{texmfdist}/source/latex/listbib
%{texmfdist}/tex/latex/listbib
# LK Proof figure macros.
%{texmfdist}/tex/latex/lkproof
# A font for electronic logic design.
%{texmfdist}/tex/latex/logic
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
# Support for multiple character sets and encodings.
%{texmfdist}/source/latex/mapcodes
%{texmfdist}/tex/latex/mapcodes
# Mathematical fonts to fit with particular text fonts.
%{texmfdist}/tex/latex/mathdesign
# Creating covers for music cassettes.
%{texmfdist}/tex/latex/mceinleger
# Experimental memoir support.
%{texmfdist}/tex/latex/memexsupp
# Multiple font formats.
%{texmfdist}/source/latex/mff
%{texmfdist}/tex/latex/mff
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
# Michael Landy's APA citation style.
%{texmfdist}/tex/latex/mslapa
# Use italic and upright greek letters with mathtime.
%{texmfdist}/source/latex/mtgreek
%{texmfdist}/tex/latex/mtgreek
# Multiple bibliographies.
%{texmfdist}/source/latex/multibbl
%{texmfdist}/tex/latex/multibbl
# Support for Mongolian "horizontal" (Xewtee Dorwoljin) script.
%{texmfdist}/source/latex/mxd
%{texmfdist}/tex/latex/mxd
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
# Support for Polish typography and the ogonek.
# %{texmfdist}/source/latex/ogonek
# %{texmfdist}/tex/latex/ogonek
# Old style numbers in OT1 encoding.
%{texmfdist}/source/latex/oldstyle
%{texmfdist}/tex/latex/oldstyle
# Footnote-style bibliographical references.
%{texmfdist}/source/latex/opcit
%{texmfdist}/tex/latex/opcit
# Counters as ordinal numbers in Portuguese.
%{texmfdist}/source/latex/ordinalpt
%{texmfdist}/tex/latex/ordinalpt
# Macros, metrics, etc., to use the OT2 Cyrillic encoding.
# %{texmfdist}/tex/latex/ot2cyr
%{texmfdist}/tex/latex/otibet
%{texmfdist}/source/latex/otibet
# List environment for making outlines.
%{texmfdist}/tex/latex/outline
# Change section levels easily.
%{texmfdist}/tex/latex/outliner
# Fonts designed by Fra Luca de Pacioli in 1497.
%{texmfdist}/source/latex/pacioli
%{texmfdist}/tex/latex/pacioli
# Page number-only page styles.
# %{texmfdist}/source/latex/pageno
# %{texmfdist}/tex/latex/pageno
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
# Font support for current PCL printers.
%{texmfdist}/tex/latex/pclnfss
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
%{texmfdist}/source/latex/polyglot
%{texmfdist}/tex/latex/polyglot
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
# %{texmfdist}/tex/latex/resume
# Rewrite labels in EPS graphics.
%{texmfdist}/tex/latex/rlepsf
# A package to help change page layout parameters in LaTeX.
%{texmfdist}/source/latex/rmpage
%{texmfdist}/tex/latex/rmpage
# Create index with pagerefs.
%{texmfdist}/tex/latex/robustindex
# Drawing rhetorical structure analysis diagrams in LaTeX.
# %{texmfdist}/source/latex/rst
# %{texmfdist}/tex/latex/rst
# Input encoding with fallback procedures.
%{texmfdist}/source/latex/rtkinenc
%{texmfdist}/tex/latex/rtkinenc
%{texmfdist}/tex/latex/rtklage
# Embed Sage code and plots into LaTeX.
%{texmfdist}/source/latex/sagetex
%{texmfdist}/tex/latex/sagetex
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
# Format a scientific paper for journal
%{texmfdist}/tex/latex/scientificpaper
# Use Scientific Word/WorkPlace files with another TeX.
%{texmfdist}/source/latex/sciwordconv
%{texmfdist}/tex/latex/sciwordconv
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
# Shade the background of any box.
%{texmfdist}/tex/latex/shadbox
# Table of contents with different depths.
%{texmfdist}/source/latex/shorttoc
%{texmfdist}/tex/latex/shorttoc
# Variants of \show for LaTeX2e.
%{texmfdist}/source/latex/show2e
%{texmfdist}/tex/latex/show2e
%{texmfdist}/source/latex/showexpl
%{texmfdist}/tex/latex/showexpl
# A font to draw a skull.
%{texmfdist}/source/latex/skull
%{texmfdist}/tex/latex/skull
# Access different-shaped small-caps fonts.
%{texmfdist}/source/latex/slantsc
%{texmfdist}/tex/latex/slantsc
# Create listoffigures etc. in a single chapter.
%{texmfdist}/tex/latex/smalltableof
# Extend LaTeX's \ref capability.
%{texmfdist}/tex/latex/smartref
# Classes for Société mathématique de France publications.
# %{texmfdist}/tex/latex/smflatex
# List the external dependencies of a LaTeX document.
%{texmfdist}/source/latex/snapshot
%{texmfdist}/tex/latex/snapshot
# Fonts and a macro for Soyombo under LaTeX.
%{texmfdist}/tex/latex/soyombo
# Drawing sparklines: intense, simple, wordlike graphics.
%{texmfdist}/tex/latex/sparklines
# Support for formatting SPIE Proceedings manuscripts.
%{texmfdist}/tex/latex/spie
# Split and reorder your bibliography.
%{texmfdist}/source/latex/splitbib
%{texmfdist}/tex/latex/splitbib
# Macros to typeset simple bitmaps with LaTeX.
%{texmfdist}/tex/latex/sprite
# Jump between DVI and TeX files.
%{texmfdist}/source/latex/srcltx
%{texmfdist}/tex/latex/srcltx
# Use the cmssq fonts.
%{texmfdist}/source/latex/ssqquote
%{texmfdist}/tex/latex/ssqquote
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
# Graphical/textual representations of swimming performances
%{texmfdist}/source/latex/swimgraf
%{texmfdist}/tex/latex/swimgraf
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
# Fonts and macro package for drawing timing diagrams.
%{texmfdist}/tex/latex/timing
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
# Adjust tracking of strings.
%{texmfdist}/tex/latex/tracking
# Fonts from the Trajan column in Rome.
%{texmfdist}/source/latex/trajan
%{texmfdist}/tex/latex/trajan
# Provide an open platform for packages to be localized.
%{texmfdist}/tex/latex/translator
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
# Time printing, in German.
%{texmfdist}/tex/latex/uhrzeit


%{texmfdist}/source/latex/nicetext
%{texmfdist}/tex/latex/nicetext
%{texmfdist}/source/latex/pagecont
%{texmfdist}/tex/latex/pagecont
%{texmfdist}/source/latex/pax
%{texmfdist}/tex/latex/pax
%{texmfdist}/tex/latex/pdfcomment
%{texmfdist}/tex/latex/pdfmarginpar
%{texmfdist}/source/latex/pdfx
%{texmfdist}/tex/latex/pdfx
%{texmfdist}/tex/latex/pigpen
%{texmfdist}/tex/latex/powerdot-FUBerlin
%{texmfdist}/tex/latex/printlen
%{texmfdist}/tex/latex/properties
%{texmfdist}/tex/latex/psbao
%{texmfdist}/source/latex/pstool
%{texmfdist}/tex/latex/pstool
%{texmfdist}/tex/latex/pstricks
%{texmfdist}/source/latex/rangen
%{texmfdist}/tex/latex/rangen
%{texmfdist}/source/latex/rcs-multi
%{texmfdist}/tex/latex/rcs-multi
%{texmfdist}/tex/latex/recipe
%{texmfdist}/tex/latex/recycle
%{texmfdist}/source/latex/rjlparshap
%{texmfdist}/tex/latex/rjlparshap
%{texmfdist}/source/latex/sageep
%{texmfdist}/tex/latex/sageep
%{texmfdist}/tex/latex/schemabloc
%{texmfdist}/tex/latex/selectp
%{texmfdist}/tex/latex/sfheaders
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
%{texmfdist}/tex/latex/tablenotes
%{texmfdist}/tex/latex/tabls
%{texmfdist}/tex/latex/tabularcalc
%{texmfdist}/source/latex/tabularew
%{texmfdist}/tex/latex/tabularew
%{texmfdist}/tex/latex/tdclock
%{texmfdist}/source/latex/termcal
%{texmfdist}/tex/latex/termcal
%{texmfdist}/source/latex/termlist
%{texmfdist}/tex/latex/termlist
%{texmfdist}/source/latex/texments
%{texmfdist}/tex/latex/texments
%{texmfdist}/tex/latex/thmbox
%{texmfdist}/tex/latex/threeparttablex
%{texmfdist}/tex/latex/tikz-timing
%{texmfdist}/tex/latex/titlepic
%{texmfdist}/tex/latex/tkz-doc
%{texmfdist}/tex/latex/tkz-linknodes
%{texmfdist}/tex/latex/tkz-tab
%{texmfdist}/tex/latex/todonotes
%{texmfdist}/tex/latex/totcount
%{texmfdist}/tex/latex/trimspaces
%{texmfdist}/tex/latex/ucdavisthesis
%{texmfdist}/tex/latex/ulqda
%{texmfdist}/tex/latex/ut-thesis
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
%{texmfdist}/tex/latex/widetable
%{texmfdist}/tex/latex/yagusylo
%{texmfdist}/tex/latex/zhmetrics
%{texmfdist}/tex/latex/zwpagelayout

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
%doc %{texmfdist}/doc/generic/pst-optexp
%{texmfdist}/tex/generic/pst-optexp
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
%{texmfdist}/scripts/pst-pdf
%{texmfdist}/source/generic/pst-barcode
%{texmfdist}/source/generic/pst-blur
%{texmfdist}/source/generic/pst-circ
%{texmfdist}/source/generic/pst-coil
%{texmfdist}/source/generic/pst-dbicons
%{texmfdist}/source/generic/pst-diffraction
%{texmfdist}/source/generic/pst-eps
%{texmfdist}/source/generic/pst-fill
%{texmfdist}/source/generic/pst-fractal
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
%{texmfdist}/source/latex/pst-poly
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
%{texmfdist}/tex/latex/psu-thesis
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

%files -n texlive-latex-txfonts
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/txfonts
%{texmfdist}/fonts/type1/public/txfonts
%{texmfdist}/fonts/afm/public/txfonts
%{texmfdist}/fonts/enc/dvips/txfonts
%{texmfdist}/fonts/vf/public/txfonts
%{texmfdist}/fonts/map/dvips/txfonts
%{texmfdist}/tex/latex/txfonts

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
%doc %{texmfdist}/doc/generic/babel
%{texmfdist}/source/generic/babel
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
%{texmfdist}/source/generic/tap
%doc %{texmfdist}/doc/generic/multido
%doc %{texmfdist}/doc/generic/tap
%doc %{texmfdist}/doc/generic/vrb

%{texmfdist}/tex/generic/eijkhout
%{texmfdist}/tex/generic/multido
%{texmfdist}/tex/generic/misc
%{texmfdist}/tex/generic/vrb

%files -n texlive-tex-pictex
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pictex
%{texmfdist}/tex/generic/pictex

%files -n texlive-tex-psizzl
%defattr(644,root,root,755)
# %{texmfdist}/doc/psizzl
%{texmfdist}/source/psizzl
%{texmfdist}/tex/psizzl

%files -n texlive-tex-pstricks
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/pstricks
%doc %{texmfdist}/doc/generic/pstricks-add
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
%doc %{texmf}/doc/generic/huhyphen

%files -n texlive-tex-spanish
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/latex/spanish-mx
%dir %{texmfdist}/source/latex/mapcodes
%dir %{texmfdist}/source/latex/polyglot
%dir %{texmfdist}/source/latex/polyglot/langs
%dir %{texmfdist}/tex/latex/babelbib
%dir %{texmfdist}/tex/latex/dvdcoll/dcl
%dir %{texmfdist}/tex/texsis
%dir %{texmfdist}/tex/texsis/base
%{texmfdist}/source/generic/babel/spanish.ins
%{texmfdist}/source/generic/babel/spanish.dtx
%{texmfdist}/source/latex/polyglot/langs/spanish.ld
%{texmfdist}/source/latex/polyglot/langs/spanish.ot1
%{texmfdist}/source/latex/mapcodes/spanish.map
%{texmfdist}/source/latex/mapcodes/spanish.dtx
%{texmfdist}/tex/texsis/base/Spanish.txs
%{texmfdist}/tex/generic/babel/spanish.sty
%{texmfdist}/tex/generic/babel/spanish.ldf
%{texmfdist}/tex/latex/spanish-mx
%{texmfdist}/tex/latex/custom-bib/spanish.mbs
%{texmfdist}/tex/latex/babelbib/spanish.bdf
%{texmfdist}/tex/latex/dvdcoll/dcl/spanish.dcl

%files -n texlive-tex-texdraw
%defattr(644,root,root,755)
# %doc %{texmfdist}/doc/texdraw
%{texmfdist}/tex/generic/texdraw

%files -n texlive-tex-thumbpdf
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/thumbpdf
%attr(755,root,root) %{_bindir}/thumbpdf
# %{_mandir}/man1/thumbpdf.1*
%{texmfdist}/tex/generic/thumbpdf
%{texmfdist}/scripts/thumbpdf

%files -n texlive-tex-ukrhyph
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/ukrhyph
%{texmfdist}/tex/generic/ukrhyph

%files -n texlive-latex-vietnam
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/generic/vntex
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

##%files -n texlive-fonts-doc
##%defattr(644,root,root,755)
#%%doc %{texmfdist}/doc/fonts

%files -n texlive-fonts-adobe
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/adobe
%{texmfdist}/fonts/afm/adobe
%{texmfdist}/fonts/tfm/adobe
%{texmfdist}/fonts/vf/adobe

%files -n texlive-fonts-larm
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/la
%{texmfdist}/fonts/type1/la/
%{texmfdist}/fonts/enc/larm.enc

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

%files -n texlive-fonts-antp
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antp
%{texmfdist}/fonts/enc/dvips/antp
%{texmfdist}/fonts/map/dvips/antp
%{texmfdist}/fonts/afm/public/antp
%{texmfdist}/fonts/tfm/public/antp

%files -n texlive-fonts-antt
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/antt
%{texmfdist}/fonts/afm/public/antt
%{texmfdist}/fonts/opentype/public/antt
%{texmfdist}/fonts/enc/dvips/antt
%{texmfdist}/fonts/tfm/public/antt
%{texmfdist}/fonts/map/dvips/antt
%{texmfdist}/tex/plain/antt
%{texmfdist}/tex/latex/antt

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
# %{texmfdist}/source/latex/bbm
# %{texmfdist}/tex/latex/bbm

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
# %{texmfdist}/fonts/enc/dvips/cc-pl
%{texmfdist}/fonts/tfm/public/cc-pl
%{texmfdist}/fonts/map/dvips/cc-pl

%files -n texlive-fonts-cg
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/cg
%{texmfdist}/fonts/vf/cg

%files -n texlive-fonts-cm
%defattr(644,root,root,755)
# %dir %{texmfdist}/fonts/afm/bluesky
%dir %{texmfdist}/fonts/map/dvips
%dir %{texmfdist}/fonts/pk/ljfour/public
%doc %{texmfdist}/doc/fonts/cm
# %{texmfdist}/fonts/afm/bluesky/cm
%{texmfdist}/fonts/map/dvips/cm
%{texmfdist}/fonts/pk/ljfour/public/cm
%{texmfdist}/fonts/source/public/cm
%{texmfdist}/fonts/tfm/public/cm

%files -n texlive-fonts-cmbright
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/cmbright
%{texmfdist}/fonts/tfm/public/cmbright
%{texmfdist}/source/latex/cmbright
%{texmfdist}/tex/latex/cmbright

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
%{texmfdist}/fonts/source/public/concmath
%{texmfdist}/fonts/tfm/public/concmath
%{texmfdist}/source/latex/concmath
%{texmfdist}/tex/latex/concmath

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
# %{texmfdist}/source/fonts/eurosym
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
%{texmfdist}/fonts/truetype/hoekwater

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
# %dir %{texmfdist}/fonts/afm/bluesky/latex-fonts
# %dir %{texmfdist}/fonts/map/dvips/latex-fonts
%dir %{texmfdist}/fonts/source/public/latex-fonts
%dir %{texmfdist}/fonts/tfm/public/latex-fonts
%doc %{texmfdist}/doc/latex/esint
# %{texmfdist}/fonts/afm/bluesky/latex-fonts/*
# %{texmfdist}/fonts/map/dvips/latex-fonts/*
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

%files -n texlive-fonts-lm
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/lm
%{texmfdist}/fonts/type1/public/lm
%{texmfdist}/fonts/afm/public/lm
%{texmfdist}/fonts/opentype/public/lm
%{texmfdist}/fonts/enc/dvips/lm
%{texmfdist}/fonts/tfm/public/lm
%{texmfdist}/fonts/map/dvips/lm
%{texmfdist}/fonts/map/dvipdfm/lm
# %{texmfdist}/source/fonts/lm
%{texmfdist}/tex/latex/lm

%files -n texlive-fonts-marvosym
%defattr(644,root,root,755)
%dir %{texmfdist}/source/fonts/eurofont
%dir %{texmfdist}/source/fonts/eurofont/marvosym
# %doc %{texmfdist}/doc/latex/marvosym
%{texmfdist}/fonts/type1/public/marvosym
%{texmfdist}/fonts/afm/public/marvosym
%{texmfdist}/fonts/tfm/public/marvosym
%{texmfdist}/fonts/map/dvips/marvosym
%{texmfdist}/source/fonts/eurofont/marvosym/*
%{texmfdist}/tex/latex/marvosym

%files -n texlive-fonts-mflogo
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/mflogo
%{texmfdist}/fonts/afm/hoekwater/mflogo
%{texmfdist}/fonts/tfm/public/mflogo
%{texmfdist}/fonts/map/dvips/mflogo
%{texmfdist}/source/latex/mflogo
%{texmfdist}/tex/latex/mflogo

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
# %doc %{texmfdist}/doc/fonts/yi4latex
# %{texmf}/fonts/sfd
%{texmfdist}/fonts/afm/itc
# %{texmf}/fonts/map/glyphlist
%{texmfdist}/fonts/map/glyphlist
%{texmfdist}/fonts/source/public/knuthotherfonts
# %{texmfdist}/fonts/source/public/yi4latex
# %{texmfdist}/fonts/tfm/public/yi4latex

%{texmfdist}/fonts/cid

%{texmfdist}/fonts/tfm/public/pslatex
%{texmfdist}/fonts/map/dvips/pslatex
%{texmfdist}/fonts/vf/public/pslatex

%doc %{texmfdist}/doc/fonts/allrunes
%{texmfdist}/fonts/map/dvips/allrunes
%{texmfdist}/fonts/source/public/allrunes
%{texmfdist}/fonts/tfm/public/allrunes
%{texmfdist}/fonts/type1/public/allrunes
%{texmfdist}/source/fonts/allrunes

%doc %{texmfdist}/doc/fonts/antiqua
%{texmfdist}/fonts/map/dvips/antiqua

%{texmfdist}/fonts/source/public/apl
%{texmfdist}/fonts/tfm/public/apl
%{texmfdist}/source/fonts/apl

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

%{texmfdist}/fonts/map/dvips/vntex/arevvn.map
%{texmfdist}/fonts/tfm/vntex/arevvn
%{texmfdist}/fonts/type1/vntex/arevvn

%{texmfdist}/fonts/afm/arkandis
%{texmfdist}/fonts/opentype/arkandis
%{texmfdist}/fonts/vf/arkandis
%{texmfdist}/fonts/tfm/arkandis
%{texmfdist}/fonts/truetype/arkandis
%{texmfdist}/fonts/type1/arkandis

%{texmfdist}/fonts/source/public/ar
%{texmfdist}/fonts/tfm/public/ar

%doc %{texmfdist}/doc/fonts/armenian
%{texmfdist}/fonts/source/public/armenian
%{texmfdist}/fonts/tfm/public/armenian

%{texmfdist}/fonts/map/dvips/arphic

%doc %{texmfdist}/doc/fonts/malayalam
%doc %{texmfdist}/doc/fonts/Asana-Math
%{texmfdist}/fonts/opentype/public/Asana-Math

%doc %{texmfdist}/doc/fonts/ascii
%{texmfdist}/fonts/map/dvips/ascii
%{texmfdist}/fonts/tfm/public/ascii
%{texmfdist}/fonts/type1/public/ascii

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

%{texmfdist}/fonts/source/public/bayer
%{texmfdist}/fonts/tfm/public/bayer

%{texmfdist}/fonts/source/public/bbding
%{texmfdist}/fonts/tfm/public/bbding

%{texmfdist}/fonts/truetype/public

%{texmfdist}/fonts/source/public/bengali
%{texmfdist}/fonts/tfm/public/bengali

%doc %{texmfdist}/doc/fonts/bera
%{texmfdist}/fonts/afm/public/bera
%{texmfdist}/fonts/map/dvips/bera
%{texmfdist}/fonts/map/vtex/bera
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

# %{texmfdist}/fonts/enc/dvips/c90enc

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
%{texmfdist}/fonts/map/dvips/vntex/chartervn.map
%{texmfdist}/fonts/afm/vntex/chartervn
%{texmfdist}/fonts/tfm/vntex/chartervn
%{texmfdist}/fonts/type1/vntex/chartervn
%{texmfdist}/fonts/vf/vntex/chartervn

%{texmfdist}/fonts/source/public/cherokee
%{texmfdist}/fonts/tfm/public/cherokee

# %{texmfdist}/fonts/source/public/china2e
# %{texmfdist}/fonts/tfm/public/china2e

# %doc %{texmfdist}/doc/fonts/cirth
# %{texmfdist}/fonts/source/public/cirth
# %{texmfdist}/fonts/tfm/public/cirth

%doc %{texmfdist}/doc/fonts/cjhebrew
%{texmfdist}/fonts/afm/public/cjhebrew
%{texmfdist}/fonts/enc/dvips/cjhebrew
%{texmfdist}/fonts/map/dvips/cjhebrew
%{texmfdist}/fonts/tfm/public/cjhebrew
%{texmfdist}/fonts/type1/public/cjhebrew
%{texmfdist}/fonts/vf/public/cjhebrew

%{texmfdist}/fonts/source/public/clock
%{texmfdist}/fonts/tfm/public/clock

# %doc %{texmfdist}/doc/fonts/cmastro
# %{texmfdist}/fonts/source/public/cmastro
# %{texmfdist}/fonts/tfm/public/cmastro

%{texmfdist}/fonts/map/dvips/vntex/cmbrightvn.map
%{texmfdist}/fonts/tfm/vntex/cmbrightvn
%{texmfdist}/fonts/type1/vntex/cmbrightvn

# %{texmfdist}/fonts/type1/public/cmex

%{texmfdist}/fonts/afm/public/cm-lgc
%{texmfdist}/fonts/enc/dvips/cm-lgc
%{texmfdist}/fonts/map/dvips/cm-lgc
%{texmfdist}/fonts/ofm/public/cm-lgc
%{texmfdist}/fonts/ovf/public/cm-lgc
%{texmfdist}/fonts/tfm/public/cm-lgc
%{texmfdist}/fonts/type1/public/cm-lgc
%{texmfdist}/fonts/vf/public/cm-lgc

# %doc %{texmfdist}/doc/fonts/cmpica
%{texmfdist}/fonts/source/public/cmpica
%{texmfdist}/fonts/tfm/public/cmpica

%{texmfdist}/fonts/map/dvips/vntex/comicvn.map
%{texmfdist}/fonts/tfm/vntex/comicsansvn
%{texmfdist}/fonts/type1/vntex/comicsansvn
%{texmfdist}/fonts/vf/vntex/comicsansvn

%{texmfdist}/fonts/map/dvips/vntex/concretevn.map
%{texmfdist}/fonts/tfm/vntex/concretevn
%{texmfdist}/fonts/type1/vntex/concretevn

%{texmfdist}/fonts/afm/ibm
%{texmfdist}/fonts/tfm/ibm
%{texmfdist}/fonts/vf/ibm
%{texmfdist}/fonts/map/dvips/courier
%{texmfdist}/fonts/tfm/cspsfonts-adobe
%{texmfdist}/fonts/vf/cspsfonts-adobe

%doc %{texmfdist}/doc/fonts/croatian
%{texmfdist}/fonts/source/public/croatian

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
%{texmfdist}/fonts/map/vtex/dictsym
%{texmfdist}/fonts/tfm/public/dictsym
%{texmfdist}/fonts/type1/public/dictsym

# %doc %{texmfdist}/doc/fonts/dingbat
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

%doc %{texmfdist}/doc/fonts/ean
%{texmfdist}/fonts/source/public/ean
%{texmfdist}/fonts/tfm/public/ean

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

%doc %{texmfdist}/doc/fonts/eurofont
%{texmfdist}/fonts/map/dvips/eurofont
%{texmfdist}/source/fonts/eurofont

%doc %{texmfdist}/doc/fonts/feyn
%{texmfdist}/fonts/source/public/feyn
%{texmfdist}/fonts/tfm/public/feyn
%{texmfdist}/source/fonts/feyn

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
%{texmfdist}/fonts/source/public/frcursive
%{texmfdist}/fonts/tfm/public/frcursive
%{texmfdist}/source/fonts/frcursive

# %doc %{texmfdist}/doc/fonts/futhark
# %{texmfdist}/fonts/source/public/futhark
# %{texmfdist}/fonts/tfm/public/futhark

# %{texmfdist}/fonts/afm/public/garuda
# %{texmfdist}/fonts/map/dvips/garuda
%{texmfdist}/fonts/map/dvips/garuda-c90
%{texmfdist}/fonts/tfm/public/garuda-c90
# %{texmfdist}/fonts/type1/public/garuda

%doc %{texmfdist}/doc/fonts/genealogy
%{texmfdist}/fonts/source/public/genealogy
%{texmfdist}/fonts/tfm/public/genealogy

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

%{texmfdist}/fonts/afm/groff
%{texmfdist}/fonts/enc/dvips/groff
%{texmfdist}/fonts/map/dvips/groff
%{texmfdist}/fonts/tfm/groff
%{texmfdist}/fonts/type1/groff

%doc %{texmfdist}/doc/fonts/grotesq
%{texmfdist}/fonts/map/dvips/grotesq

%{texmfdist}/fonts/map/dvips/vntex/grotesqvn.map
%{texmfdist}/fonts/afm/vntex/grotesqvn
%{texmfdist}/fonts/tfm/vntex/grotesqvn
%{texmfdist}/fonts/type1/vntex/grotesqvn

%{texmfdist}/fonts/afm/public/grverb
%{texmfdist}/fonts/map/dvips/grverb
%{texmfdist}/fonts/tfm/public/grverb
%{texmfdist}/fonts/type1/public/grverb
%{texmfdist}/fonts/vf/public/grverb

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
%{texmfdist}/source/fonts/hfbright

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

%doc %{texmfdist}/doc/fonts/initials
%{texmfdist}/fonts/afm/public/initials
%{texmfdist}/fonts/map/dvips/initials
%{texmfdist}/fonts/tfm/public/initials
%{texmfdist}/fonts/type1/public/initials

%doc %{texmfdist}/doc/fonts/itrans
%{texmfdist}/fonts/afm/public/itrans
%{texmfdist}/fonts/source/public/itrans
%{texmfdist}/fonts/tfm/public/itrans
%{texmfdist}/fonts/type1/public/itrans

%doc %{texmfdist}/doc/fonts/iwona
%{texmfdist}/fonts/afm/public/iwona
%{texmfdist}/fonts/enc/dvips/iwona
%{texmfdist}/fonts/map/dvips/iwona
%{texmfdist}/fonts/opentype/public/iwona
%{texmfdist}/fonts/tfm/public/iwona
%{texmfdist}/fonts/type1/public/iwona

%{texmfdist}/fonts/enc/dvips/jmn
%{texmfdist}/fonts/map/dvips/jmn

# %doc %{texmfdist}/doc/fonts/kdgreek
# %{texmfdist}/fonts/source/public/kdgreek
# %{texmfdist}/fonts/tfm/public/kdgreek

%{texmfdist}/fonts/afm/public/kerkis
%{texmfdist}/fonts/enc/dvips/kerkis
%{texmfdist}/fonts/map/dvips/kerkis
%{texmfdist}/fonts/tfm/public/kerkis
%{texmfdist}/fonts/type1/public/kerkis
%{texmfdist}/fonts/vf/public/kerkis

%doc %{texmfdist}/doc/fonts/kixfont
%{texmfdist}/fonts/source/public/kixfont
%{texmfdist}/fonts/tfm/public/kixfont

# %dir %{texmfdist}/fonts/map/public
%doc %{texmfdist}/doc/fonts/kurier
%{texmfdist}/fonts/afm/public/kurier
%{texmfdist}/fonts/enc/dvips/kurier
%{texmfdist}/fonts/map/dvips/kurier
%{texmfdist}/fonts/opentype/public/kurier
%{texmfdist}/fonts/tfm/public/kurier
%{texmfdist}/fonts/type1/public/kurier

%doc %{texmfdist}/doc/fonts/levy
%{texmfdist}/fonts/source/public/levy

%doc %{texmfdist}/doc/fonts/lfb
%{texmfdist}/fonts/source/public/lfb
%{texmfdist}/fonts/tfm/public/lfb

%doc %{texmfdist}/doc/fonts/libertine
%{texmfdist}/fonts/afm/public/libertine
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

%{texmfdist}/fonts/source/public/logic
%{texmfdist}/fonts/tfm/public/logic

%doc %{texmfdist}/doc/fonts/lxfonts
%{texmfdist}/fonts/map/dvips/lxfonts
%{texmfdist}/fonts/source/public/lxfonts
%{texmfdist}/fonts/tfm/public/lxfonts
%{texmfdist}/fonts/type1/public/lxfonts

%doc %{texmfdist}/doc/fonts/ly1
%{texmfdist}/fonts/map/dvips/ly1

%{texmfdist}/fonts/source/public/malayalam
%{texmfdist}/fonts/tfm/public/malayalam

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

%{texmfdist}/fonts/tfm/vntex/mscorevn
%{texmfdist}/fonts/vf/vntex/mscorevn

%doc %{texmfdist}/doc/generic/musixtex
%{texmfdist}/fonts/map/dvips/musixtex
%{texmfdist}/fonts/source/public/musixtex
%{texmfdist}/fonts/tfm/public/musixtex
%{texmfdist}/fonts/type1/public/musixtex

%{texmfdist}/fonts/source/public/mxd
%{texmfdist}/fonts/tfm/public/mxd

%{texmfdist}/fonts/source/public/mxedruli
%{texmfdist}/fonts/tfm/public/mxedruli

%{texmfdist}/fonts/map/dvips/ncntrsbk

%doc %{texmfdist}/doc/fonts/nkarta
%{texmfdist}/fonts/source/public/nkarta
%{texmfdist}/fonts/tfm/public/nkarta

# %{texmfdist}/fonts/afm/public/norasi
# %{texmfdist}/fonts/map/dvips/norasi
# %{texmfdist}/fonts/tfm/public/norasi
%{texmfdist}/fonts/tfm/public/norasi-c90

# %{texmfdist}/fonts/source/public/oca

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

%{texmfdist}/fonts/source/public/osmanian

# %doc %{texmfdist}/doc/fonts/ot2cyr
# %{texmfdist}/fonts/map/dvips/ot2cyr
# %{texmfdist}/source/fonts/ot2cyr

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
# %{texmfdist}/source/fonts/phonetic

%{texmfdist}/fonts/source/public/pigpen
%{texmfdist}/fonts/tfm/public/pigpen
%{texmfdist}/fonts/type1/public/pigpen

%{texmfdist}/source/fonts/malayalam

%{texmfdist}/fonts/source/public/punk
%{texmfdist}/fonts/tfm/public/punk

%{texmfdist}/fonts/source/public/recycle
%{texmfdist}/fonts/tfm/public/recycle
%{texmfdist}/fonts/type1/public/recycle

%{texmfdist}/fonts/tfm/public/relenc
%{texmfdist}/fonts/vf/public/relenc

%doc %{texmfdist}/doc/fonts/rsfs
%{texmfdist}/fonts/afm/public/rsfs
%{texmfdist}/fonts/type1/public/rsfs
%{texmfdist}/fonts/map/dvips/rsfs

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

%{texmfdist}/fonts/source/public/simpsons

%{texmfdist}/fonts/source/public/shuffle
%{texmfdist}/fonts/tfm/public/shuffle

%doc %{texmfdist}/doc/fonts/skaknew
%{texmfdist}/fonts/afm/public/skaknew
%{texmfdist}/fonts/map/dvips/skaknew
%{texmfdist}/fonts/map/vtex/skaknew
%{texmfdist}/fonts/tfm/public/skaknew
%{texmfdist}/fonts/type1/public/skaknew
%{texmfdist}/fonts/opentype/public/skaknew

%{texmfdist}/fonts/source/public/skull

%{texmfdist}/fonts/source/public/soyombo
%{texmfdist}/fonts/tfm/public/soyombo

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

%{texmfdist}/doc/fonts/pclnfss
%{texmfdist}/source/fonts/pclnfss

%doc %{texmfdist}/doc/fonts/tex-gyre
%{texmfdist}/fonts/afm/public/tex-gyre
%{texmfdist}/fonts/enc/dvips/tex-gyre
%{texmfdist}/fonts/map/dvips/tex-gyre
%{texmfdist}/fonts/opentype/public/tex-gyre
%{texmfdist}/fonts/tfm/public/tex-gyre
%{texmfdist}/fonts/type1/public/tex-gyre

%{texmfdist}/fonts/afm/public/thailatex
%{texmfdist}/fonts/type1/public/thailatex

%{texmfdist}/fonts/map/dvips/times

%doc %{texmfdist}/doc/fonts/timing
%{texmfdist}/fonts/source/public/timing
%{texmfdist}/fonts/tfm/public/timing

%doc %{texmfdist}/doc/fonts/tipa
%{texmfdist}/fonts/map/dvips/tipa
%{texmfdist}/fonts/source/public/tipa
%{texmfdist}/fonts/tfm/public/tipa
%{texmfdist}/fonts/type1/public/tipa

%{texmfdist}/fonts/afm/public/trajan
%{texmfdist}/fonts/map/dvips/trajan
%{texmfdist}/fonts/tfm/public/trajan
%{texmfdist}/fonts/type1/public/trajan

%{texmfdist}/fonts/map/dvips/vntex/txttvn.map
%{texmfdist}/fonts/tfm/vntex/txttvn
%{texmfdist}/fonts/type1/vntex/txttvn

%{texmfdist}/fonts/map/dvips/uhc

# %doc %{texmfdist}/doc/fonts/umtypewriter
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

%{texmfdist}/fonts/enc/dvips/vntex/*

%{texmfdist}/fonts/map/dvips/vntex/vntopia.map
%{texmfdist}/fonts/afm/vntex/vntopia
%{texmfdist}/fonts/tfm/vntex/vntopia
%{texmfdist}/fonts/type1/vntex/vntopia
%{texmfdist}/fonts/vf/vntex/vntopia

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

%{texmfdist}/fonts/map/dvips/zefonts
%{texmfdist}/fonts/tfm/public/zefonts
%{texmfdist}/fonts/vf/public/zefonts

%files -n texlive-fonts-omega
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
%dir %{texmf}/scripts/texlive
%{texmfdist}/fonts/source/public/pl
%{texmfdist}/fonts/type1/public/pl
%{texmfdist}/fonts/afm/public/pl
%{texmfdist}/fonts/enc/dvips/pl
%{texmfdist}/fonts/tfm/public/pl
%{texmfdist}/fonts/map/dvips/pl

%files -n texlive-fonts-px
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/pxfonts
%dir %{texmfdist}/fonts/map/dvips/pxfonts
%dir %{texmfdist}/tex/latex/pxfonts
%{texmfdist}/fonts/map/dvips/pxfonts/pxfonts.map
%{texmfdist}/fonts/afm/public/pxfonts
%{texmfdist}/fonts/tfm/public/pxfonts
%{texmfdist}/fonts/type1/public/pxfonts
%{texmfdist}/fonts/vf/public/pxfonts
%{texmfdist}/tex/latex/pxfonts/pxfonts.sty

%files -n texlive-fonts-qpxqtx
%defattr(644,root,root,755)
%{texmfdist}/fonts/tfm/public/qpxqtx
%{texmfdist}/fonts/vf/public/qpxqtx

%files -n texlive-fonts-rsfs
%defattr(644,root,root,755)
%{texmfdist}/fonts/source/public/rsfs
%{texmfdist}/fonts/tfm/public/rsfs

%files -n texlive-fonts-stmaryrd
%defattr(644,root,root,755)
%doc %{texmfdist}/doc/fonts/stmaryrd
%{texmfdist}/source/fonts/stmaryrd
%{texmfdist}/fonts/tfm/public/stmaryrd

%files -n texlive-fonts-tx
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/txfonts/txfonts.map
%{texmfdist}/fonts/afm/public/txfonts
%{texmfdist}/fonts/tfm/public/txfonts
%{texmfdist}/fonts/vf/public/txfonts

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

%files -n texlive-fonts-urwvn
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/vntex/urwvn.map
%{texmfdist}/fonts/afm/vntex/urwvn
%{texmfdist}/fonts/tfm/vntex/urwvn
%{texmfdist}/fonts/type1/vntex/urwvn
%{texmfdist}/fonts/vf/vntex/urwvn

%files -n texlive-fonts-vnr
%defattr(644,root,root,755)
%{texmfdist}/fonts/map/dvips/vntex/vnr*.map
%{texmfdist}/fonts/source/vntex/vnr
%{texmfdist}/fonts/tfm/vntex/vnr

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
%{texmfdist}/fonts/map/dvips/xypic
%{texmfdist}/fonts/source/public/xypic
%{texmfdist}/fonts/tfm/public/xypic

%files -n texlive-fonts-yandy
%defattr(644,root,root,755)
%{texmfdist}/source/fonts/eurofont/marvosym/tfmfiles/yandy

%files -n texlive-fonts-type1-antp
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/antp

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

# %files -n texlive-fonts-type1-bluesky
# %defattr(644,root,root,755)
# %{texmfdist}/fonts/type1/bluesky

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

%files -n texlive-fonts-type1-marvosym
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/marvosym

%files -n texlive-fonts-type1-mathpazo
%defattr(644,root,root,755)
%{texmfdist}/fonts/afm/public/mathpazo
%{texmfdist}/fonts/type1/public/mathpazo

%files -n texlive-fonts-type1-omega
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/omega

%files -n texlive-fonts-type1-pl
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/pl

%files -n texlive-fonts-type1-px
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/pxfonts

%files -n texlive-fonts-type1-tx
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/txfonts

%files -n texlive-fonts-type1-uhc
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/uhc

%files -n texlive-fonts-type1-urw
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/urw

%files -n texlive-fonts-type1-vnr
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/vntex/vnr

%files -n texlive-fonts-type1-wadalab
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/wadalab

%files -n texlive-fonts-type1-xypic
%defattr(644,root,root,755)
%{texmfdist}/fonts/type1/public/xypic
