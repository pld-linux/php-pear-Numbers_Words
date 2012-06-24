%include	/usr/lib/rpm/macros.php
%define		_class		Numbers
%define		_subclass	Words
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides methods for spelling numerals in words
Summary(pl):	%{_pearname} - metody do s�ownego przedstawiania liczb
Name:		php-pear-%{_pearname}
Version:	0.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2185ac00eb7102f2140ae01ad544f30f
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
- de (German)
- ee (Estonian) by Erkki Saarniit
- es (Spanish) by Xavier Noguer
- en_100 (Donald Knuth system, English)
- en_GB (Britich English)
- en_US (American English)
- it_IT (Italian) by Filippo Beltramini and Davide Caironi
- pl (Polish)
- pt_BR (Brazilian Portuguese) by Marcelo Subtil Marcal

This class has in PEAR status: %{_status}.

%description -l pl
Przy u�yciu klasy Numbers_Words mo�na przekszta�ca� liczby zapisane
cyframi arabskimi na s�owa w kilku j�zykach. Mo�na przekszta�ci�
liczb� ca�kowit� od minus niesko�czono�ci do niesko�czono�ci. Je�li
system nie obs�uguje takich d�ugich liczb, mo�na wywo�a�
Numbers_Words::toWords() dla zwyk�ego �a�cucha.

Obs�ugiwane s� nast�puj�ce j�zyki (w kolejno�ci alfabetycznej):
- de (niemiecki)
- ee (esto�ski) - autor Erkki Saarniit
- es (hiszpa�ski) - dzi�ki Xavierowi Noguerowi
- en_100 (angielski w systemie Donalda Knutha)
- en_GB (angielski w wersji brytyjskiej)
- en_US (angielski w wersji ameryka�skiej)
- it_IT (w�oski) - autorzy Filippo Beltramini oraz Davide Caironi
- pl (polski)
- pt_BR (portugalski w wersji brazylijskiej) dzi�ki Marcelo Subtil
  Marcalowi.

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
