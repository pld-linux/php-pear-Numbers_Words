%define		status		beta
%define		pearname	Numbers_Words
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - provides methods for spelling numerals in words
Summary(pl.UTF-8):	%{pearname} - metody do słownego przedstawiania liczb
Name:		php-pear-%{pearname}
Version:	0.18.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	b0bfd299b79e8a40683cb28369a6e7ef
URL:		http://pear.php.net/package/Numbers_Words/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-Math_BigInteger
Requires:	php-pear-PEAR-core >= 1:1.4.0-0.b1
Obsoletes:	php-pear-Numbers_Words-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With Numbers_Words class you can convert numbers written in arabic
digits to words in several languages. You can convert an integer
between -infinity and infinity. If your system does not support such
long numbers you can call Numbers_Words::toWords() with just a string.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Przy użyciu klasy Numbers_Words można przekształcać liczby zapisane
cyframi arabskimi na słowa w kilku językach. Można przekształcić
liczbę całkowitą od minus nieskończoności do nieskończoności. Jeśli
system nie obsługuje takich długich liczb, można wywołać
Numbers_Words::toWords() dla zwykłego łańcucha.

Ta klasa ma w PEAR status: %{status}.

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
%doc docs/%{pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Numbers/*.php
%dir %{php_pear_dir}/Numbers/Words
%{php_pear_dir}/Numbers/Words/Exception.php

%dir %{php_pear_dir}/Numbers/Words/Locale
%dir %{php_pear_dir}/Numbers/Words/Locale/en
%dir %{php_pear_dir}/Numbers/Words/Locale/es
%dir %{php_pear_dir}/Numbers/Words/Locale/fr
%dir %{php_pear_dir}/Numbers/Words/Locale/hu
%dir %{php_pear_dir}/Numbers/Words/Locale/it
%dir %{php_pear_dir}/Numbers/Words/Locale/pt
%dir %{php_pear_dir}/Numbers/Words/Locale/ro
%dir %{php_pear_dir}/Numbers/Words/Locale/tr
%lang(be) %{php_pear_dir}/Numbers/Words/Locale/fr/BE.php
%lang(bg) %{php_pear_dir}/Numbers/Words/Locale/bg.php
%lang(cs) %{php_pear_dir}/Numbers/Words/Locale/cs.php
%lang(de) %{php_pear_dir}/Numbers/Words/Locale/de.php
%lang(dk) %{php_pear_dir}/Numbers/Words/Locale/dk.php
%lang(en_100) %{php_pear_dir}/Numbers/Words/Locale/en/100.php
%lang(en_GB) %{php_pear_dir}/Numbers/Words/Locale/en/GB.php
%lang(en_IN) %{php_pear_dir}/Numbers/Words/Locale/en/IN.php
%lang(en_US) %{php_pear_dir}/Numbers/Words/Locale/en/US.php
%lang(es) %{php_pear_dir}/Numbers/Words/Locale/es.php
%lang(es) %{php_pear_dir}/Numbers/Words/Locale/es/VE.php
%lang(es_AR) %{php_pear_dir}/Numbers/Words/Locale/es/AR.php
%lang(es_MX) %{php_pear_dir}/Numbers/Words/Locale/es/MX.php
%lang(et) %{php_pear_dir}/Numbers/Words/Locale/et.php
%lang(fr) %{php_pear_dir}/Numbers/Words/Locale/fr.php
%lang(he) %{php_pear_dir}/Numbers/Words/Locale/he.php
%lang(hu) %{php_pear_dir}/Numbers/Words/Locale/hu/HU.php
%lang(id) %{php_pear_dir}/Numbers/Words/Locale/id.php
%lang(it) %{php_pear_dir}/Numbers/Words/Locale/it/IT.php
%lang(lt) %{php_pear_dir}/Numbers/Words/Locale/lt.php
%lang(lv) %{php_pear_dir}/Numbers/Words/Locale/lv.php
%lang(nl) %{php_pear_dir}/Numbers/Words/Locale/nl.php
%lang(pl) %{php_pear_dir}/Numbers/Words/Locale/pl.php
%lang(pt_BR) %{php_pear_dir}/Numbers/Words/Locale/pt/BR.php
%lang(ro) %{php_pear_dir}/Numbers/Words/Locale/ro/RO.php
%lang(ru) %{php_pear_dir}/Numbers/Words/Locale/ru.php
%lang(sv) %{php_pear_dir}/Numbers/Words/Locale/sv.php
%lang(tr) %{php_pear_dir}/Numbers/Words/Locale/tr/TR.php
%lang(ua) %{php_pear_dir}/Numbers/Words/Locale/ua.php
