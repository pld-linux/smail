Summary:	Smail MTA 
Summary(pl):	Smail - alternatywa dla sendmail-a.
Name:		smail
Version:	3.2.0.109
Release:	1
License:	GPL
Group:		Mail/MTA
Group(pl):	Poczta/MTA
Source:		ftp://ftp.uu.net/networking/mail/%{name}/%name-%version.tar.gz
Patch0:		%name-EDITME-config-file-PLD.patch
#Patch1:		%name-compile.fix
#Patch2:		%name-src.fix
Obsoletes:	sendmail
BuildRequires:	glibc-devel 
BuildRequires:	libident-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
  
%description -l pl
  
%prep
%setup -q

%patch0 -p0
#%patch1 -p0
#%patch2 -p0

%build
#./configure --prefix=%{_prefix}
make depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install

(cd $RPM_BUILD_ROOT%{_bindir};ln -s smail sendmail)
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
