%define		status		beta
%define		pearname	Numbers_Words
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - provides methods for spelling numerals in words
Summary(pl.UTF-8):	%{pearname} - metody do słownego przedstawiania liczb
Name:		php-pear-%{pearname}
Version:	0.16.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	8b710a80794bc162630891a70876d906
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
%lang(bg) %{php_pear_dir}/Numbers/Words/lang.bg.php
%lang(cs) %{php_pear_dir}/Numbers/Words/lang.cs.php
%lang(de) %{php_pear_dir}/Numbers/Words/lang.de.php
%lang(dk) %{php_pear_dir}/Numbers/Words/lang.dk.php
%lang(en) %{php_pear_dir}/Numbers/Words/lang.en_100.php
%lang(en) %{php_pear_dir}/Numbers/Words/lang.en_GB.php
%lang(es) %{php_pear_dir}/Numbers/Words/lang.en_US.php
%lang(es) %{php_pear_dir}/Numbers/Words/lang.es.php
%lang(es) %{php_pear_dir}/Numbers/Words/lang.es_AR.php
%lang(es_MX) %{php_pear_dir}/Numbers/Words/lang.es_MX.php
%lang(et) %{php_pear_dir}/Numbers/Words/lang.et.php
%lang(fr) %{php_pear_dir}/Numbers/Words/lang.fr.php
%lang(fr) %{php_pear_dir}/Numbers/Words/lang.fr_BE.php
%lang(he) %{php_pear_dir}/Numbers/Words/lang.he.php
%lang(hu) %{php_pear_dir}/Numbers/Words/lang.hu_HU.php
%lang(id) %{php_pear_dir}/Numbers/Words/lang.id.php
%lang(it) %{php_pear_dir}/Numbers/Words/lang.it_IT.php
%lang(lt) %{php_pear_dir}/Numbers/Words/lang.lt.php
%lang(nl) %{php_pear_dir}/Numbers/Words/lang.nl.php
%lang(pl) %{php_pear_dir}/Numbers/Words/lang.pl.php
%lang(pt_BR) %{php_pear_dir}/Numbers/Words/lang.pt_BR.php
%lang(ru) %{php_pear_dir}/Numbers/Words/lang.ru.php
%lang(sv) %{php_pear_dir}/Numbers/Words/lang.sv.php
%lang(tr) %{php_pear_dir}/Numbers/Words/lang.tr_TR.php
