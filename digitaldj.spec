%include	/usr/lib/rpm/macros.perl
Summary:	Digitaldj, an SQL-based MP3-player
Summary(pl.UTF-8):	Digitaldj - odtwarzacz MP3 oparty o SQL
Name:		digitaldj
Version:	0.7.3
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://nostatic.org/ddj/%{name}-%{version}.tar.gz
# Source0-md5:	187c7b2a4d9f661910c26b42b91ecf21
URL:		http://nostatic.org/ddj/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libghttp-devel
BuildRequires:	libtool
BuildRequires:	lirc-devel
BuildRequires:	mysql-devel
BuildRequires:	perl-DBI
BuildRequires:	rpm-perlprov
Obsoletes:	Digitaldj
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digitaldj is an SQL-based MP3-player frontend designed for people who
want to create an MP3 version of their CD collection. It is designed
to work with the Grip ripping/encoding application (but can be used
separately). When Grip encodes MP3 files, it will place all of the
song information into an SQL database. Digitaldj can then use this
information to create playlists based on a number of criteria.

%description -l pl.UTF-8
Digitaldj jest frontendem do odtwarzania MP3 opartym o bazę SQL dla
chcących zrobić wersję MP3 swojej kolekcji płyt kompaktowych. Został
zaprojektowany do pracy z programem ripująco-kodującym Grip (ale może
być używany bez niego). Grip po zakodowaniu plików MP3 umieszcza
informacje o utworach w bazie SQL. Digitaldj może używać tych
informacji do robienia playlist opartych o różne kryteria.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ddj
%attr(755,root,root) %{_bindir}/mp3insert
%{_datadir}/digitaldj
%{_pixmapsdir}/*.png
