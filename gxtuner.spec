Name:		gxtuner
Summary:	A simple guitar and bass tuner for jack
Version:	2.0
Release:	1
License:	GPLv2
Group:		Sound
URL:		http://guitarix.sourceforge.net/
Source0:	http://sourceforge.net/projects/guitarix/files/gxtuner/%{name}-%{version}.tar.bz2
BuildRequires:	jackit-devel gtk+2-devel fftw3-devel libzita-resampler-devel

%description
A simple (linux) guitar and bass tuner for jack with full jack session
managment support

gxtuner use a equal-tempered scale based on

A4 = 440 Hz 

A4 reference pitch can adjusted at command line and/or runtime
in a half tone range: 415Hz <-> 467Hz

gxtuner use a default threshold level at 0.001 threshold can adjusted
at command line and/or runtime in a range of 0.001 <-> 0.5

%prep
%setup -q -n %name
perl -pi -e "s/zita-resampler.h/zita-resampler\/resampler.h/g" pitchtracker.h

%build
%setup_compile_flags
LDFLAGS="-lX11" make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications %{buildroot}%{_iconsdir}
make PREFIX=%{buildroot}%{_prefix} PIXMAPS_DIR=%{buildroot}%{_iconsdir} install

%files
%{_bindir}/gxtuner
%defattr(644,root,root,755)
%{_datadir}/applications/gxtuner.desktop
%{_iconsdir}/gxtuner.png
%doc README


%changelog
* Thu Dec 15 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.7-1
+ Revision: 741450
- disable smp build
- imported package gxtuner

