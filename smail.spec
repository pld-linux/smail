Summary:	Smail MTA 
Summary(pl):	Smail - alternatywa dla sendmail-a
Name:		smail
Version:	3.2.0.109
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.uu.net/networking/mail/%{name}/%name-%version.tar.gz
Patch0:		%name-EDITME-config-file-PLD.patch
#Patch1:	%name-compile.fix
#Patch2:	%name-src.fix
Provides:	smtpdaemon
BuildRequires:	glibc-devel 
BuildRequires:	libident-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	exim
Obsoletes:	postfix
Obsoletes:	sendmail
Obsoletes:	sendmail-cf                                                                                   
Obsoletes:	sendmail-doc
Obsoletes:	smtpdaemon
Obsoletes:	zmailer

%description
Smail-3 is a Mail Transport Agent, i.e. a program used for sending and
receiving electronic mail.

Its job is to accept mail messages from sources on the local machine,
or from remote hosts, and deliver those messages to the appropriate
destinations, be they to remote hosts or to files or programs on the
local machine. It is not intended to be a user interface for reading
and submitting mail.

%prep
%setup -q

%patch0 -p0
#%patch1 -p0
#%patch2 -p0

%build
#./configure --prefix=%{_prefix}
%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

(cd $RPM_BUILD_ROOT%{_bindir};ln -s smail sendmail)
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
