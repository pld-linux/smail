# TODO
# - make it build and package files ;)
Summary:	Smail MTA
Summary(pl.UTF-8):	Smail - alternatywa dla sendmaila
Name:		smail
Version:	3.2.0.121
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.planix.com/pub/Smail/%{name}-%{version}.tar.gz
# Source0-md5:	0637d2753221ab98e65460a823e1d417
URL:		http://www.weird.com/~woods/projects/smail.html
BuildRequires:	bison
BuildRequires:	libident-devel
Provides:	smtpdaemon
Obsoletes:	courier
Obsoletes:	exim
Obsoletes:	masqmail
Obsoletes:	nullmailer
Obsoletes:	omta
Obsoletes:	postfix
Obsoletes:	qmail
Obsoletes:	sendmail
Obsoletes:	sendmail-cf
Obsoletes:	sendmail-doc
Obsoletes:	smtpdaemon
Obsoletes:	zmailer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smail-3 is a Mail Transport Agent, i.e. a program used for sending and
receiving electronic mail.

Its job is to accept mail messages from sources on the local machine,
or from remote hosts, and deliver those messages to the appropriate
destinations, be they to remote hosts or to files or programs on the
local machine. It is not intended to be a user interface for reading
and submitting mail.

%description -l pl.UTF-8
Smail-3 to MTA, czyli program używany do wysyłania i odbierania
poczty.

Jego zadanie to przyjmowanie wiadomości lokalnie lub od zdalnych
maszyn oraz dostarczanie ich do właściwych celów - maszyn zdalnych lub
plików czy programów lokalnie. Smail nie jest interfejsem użytkownika
do czytania i wysyłania poczty.

%prep
%setup -q
ln -s Make.local-trad conf/Make.local

%build
%{__make} depend \
	YACC="bison -y" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%{__make} \
	YACC="bison -y" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

ln -s smail $RPM_BUILD_ROOT%{_bindir}/sendmail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
