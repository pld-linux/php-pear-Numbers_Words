%include	/usr/lib/rpm/macros.php
%define		_class		Numbers
%define		_subclass	Words
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides methods for spelling numerals in words
Summary(pl):	%{_pearname} - metody do s³ownego przedstawiania liczb
Name:		php-pear-%{_pearname}
Version:	0.10.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7a885400062474cbb887b3fe794b7119
URL:		http://pear.php.net/package/Numbers_Words/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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
- de (German)
- ee (Estonian) by Erkki Saarniit
- en_100 (Donald Knuth system, English)
- en_GB (Britich English)
- en_US (American English)
- es (Spanish Castellano) by Xavier Noguer
- es_AR (Argentinian Spanish) by Martin Marrese
- fr (French) by Kouber Saparev
- id (Indonesian) by Ernas M. Jamil
- it_IT (Italian) by Filippo Beltramini and Davide Caironi
- pl (Polish)
- pt_BR (Brazilian Portuguese) by Marcelo Subtil Marcal
- ru (Russian) by Andrey Demenev
- sv (Swedish) by Robin Ericsson

In PEAR status of this package is: %{_status}.

%description -l pl
Przy u¿yciu klasy Numbers_Words mo¿na przekszta³caæ liczby zapisane
cyframi arabskimi na s³owa w kilku jêzykach. Mo¿na przekszta³ciæ
liczbê ca³kowit± od minus nieskoñczono¶ci do nieskoñczono¶ci. Je¶li
system nie obs³uguje takich d³ugich liczb, mo¿na wywo³aæ
Numbers_Words::toWords() dla zwyk³ego ³añcucha.

Obs³ugiwane s± nastêpuj±ce jêzyki (w kolejno¶ci alfabetycznej):
- bg (bu³garski) - autor Kouber Saparev
- de (niemiecki)
- ee (estoñski) - autor Erkki Saarniit
- en_100 (angielski w systemie Donalda Knutha)
- en_GB (angielski w wersji brytyjskiej)
- en_US (angielski w wersji amerykañskiej)
- es (hiszpañski) - dziêki Xavierowi Noguerowi
- es_AR (argentyñska odmiana hiszpañskiego) - autor Martin Marrese
- fr (francuski) - autor Kouber Saparev
- id (indonezyjski) - autor Ernas M. Jamil
- it_IT (w³oski) - autorzy Filippo Beltramini oraz Davide Caironi
- pl (polski)
- pt_BR (portugalski w wersji brazylijskiej) dziêki Marcelo Subtil
  Marcalowi.
- ru (rosyjski) - autor Andrey Demenev
- sv (szwedzki) - autor Robin Ericsson

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{,%{_subclass}}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{README,ChangeLog,tests}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
