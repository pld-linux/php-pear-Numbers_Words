%include	/usr/lib/rpm/macros.php
%define		_class		Numbers
%define		_subclass	Words
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides methods for spelling numerals in words
Summary(pl.UTF-8):   %{_pearname} - metody do słownego przedstawiania liczb
Name:		php-pear-%{_pearname}
Version:	0.15.0
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	cd65db3d32d781b1a28a1d83b0ff1530
URL:		http://pear.php.net/package/Numbers_Words/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With Numbers_Words class you can convert numbers written in arabic
digits to words in several languages. You can convert an integer
between -infinity and infinity. If your system does not support such
long numbers you can call Numbers_Words::toWords() with just a string.

The following languages are supported (in alphabetical order):
- bg (Bulgarian) by Kouber Saparev
- cs (Czech) by Petr 'PePa' Pavel
- de (German) by Piotr Klaban
- dk (Danish) by Jesper Veggerby
- en_100 (Donald Knuth system, English)
- en_GB (Britich English) by Piotr Klaban
- en_US (American English) by Piotr Klaban
- es (Spanish Castellano) by Xavier Noguer
- es_AR (Argentinian Spanish) by Martin Marrese
- et (Estonian) by Erkki Saarniit
- fr (French) by Kouber Saparev
- fr_BE (French Belgium) by Kouber Saparev and Philippe Bajoit
- he (Hebrew) by Hadar Porat
- hu_HU (Hungarian) by Nils Homp
- id (Indonesian) by Ernas M. Jamil
- it_IT (Italian) by Filippo Beltramini and Davide Caironi
- lt (Lithuanian) by Laurynas Butkus
- nl (Dutch) by WHAM van Dinter
- pl (Polish) by Piotr Klaban
- pt_BR (Brazilian Portuguese) by Marcelo Subtil Marcal
- ru (Russian) by Andrey Demenev
- sv (Swedish) by Robin Ericsson

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Przy użyciu klasy Numbers_Words można przekształcać liczby zapisane
cyframi arabskimi na słowa w kilku językach. Można przekształcić
liczbę całkowitą od minus nieskończoności do nieskończoności. Jeśli
system nie obsługuje takich długich liczb, można wywołać
Numbers_Words::toWords() dla zwykłego łańcucha.

Obsługiwane są następujące języki (w kolejności alfabetycznej):
- bg (bułgarski) - autor Kouber Saparev
- cs (czeski) - autor Peter 'PePa' Pavel
- de (niemiecki) - autor Piotr Klaban
- dk (duński) - autor Jesper Veggerby
- en_100 (angielski w systemie Donalda Knutha) - autor Piotr Klaban
- en_GB (angielski w wersji brytyjskiej) - autor Piotr Klaban
- en_US (angielski w wersji amerykańskiej) - autor Piotr Klaban
- es (hiszpański) - dzięki Xavierowi Noguerowi
- es_AR (argentyńska odmiana hiszpańskiego) - autor Martin Marrese
- et (estoński) - autor Erkki Saarniit
- fr (francuski) - autor Kouber Saparev
- fr_BE (francuski w odmianie belgijskiej) - autorzy Kouber Saparev
  i Philippe Bajoit
- he (hebrajski) - autor Hadar Porat
- hu_HU (węgierski) - autor Nils Homp
- id (indonezyjski) - autor Ernas M. Jamil
- it_IT (włoski) - autorzy Filippo Beltramini oraz Davide Caironi
- lt (litewski) - autor Laurynas Butkus
- nl (holenderski) - autor WHAM van Dinter
- pl (polski) - autor Piotr Klaban
- pt_BR (portugalski w odmianie brazylijskiej) dzięki Marcelo Subtil
  Marcalowi.
- ru (rosyjski) - autor Andrey Demenev
- sv (szwedzki) - autor Robin Ericsson

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
