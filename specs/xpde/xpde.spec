# $Id: _template.spec 201 2004-04-03 15:24:49Z dag $
# Authority: dag
# Upstream: <development@xpde.com>

%define installdir /opt/xkde
%define real_version 0.4.0-20030730

Summary: Integrated desktop environment (xpde) and window manager (xpwm)
Name: xpde
Version: 0.4.0
Release: 1
License: GPL
Group: User Interface/Desktops 
URL: http://www.xpde.com/

Packager: Ricardo Arroyo <ricarro@terra.com.pe>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

NoSource: 0
Source: http://www.xpde.com/releases/xpde-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root 

%description 
XPde is a desktop window Enviroment and a window manager thinking
to make easy to use people who begin in Linux with a familiar look 
desktop. It tries to recreate the Window Xp interface nothing more.

%prep
%setup

%{__cat} <<EOF >xpde.session
#!/bin/sh
exec %{_sysconfdir}/X11/xdm/Xsession XPde
EOF

%{__cat} <<EOF >xpde.xclients
#!/bin/sh
exec %{installdir}/.xinitrcXPDE
EOF

%{__cat} <<'EOF' >xpde.xinitrc
#!/bin/sh

if [ -d $HOME/.xpde ]; then
	exec $HOME/.xinitrc
else
	cp -a %{installdir}/defaultdesktop $HOME/.xpde
	cp -v %{installdir}/xinitrcDEFAULT $HOME/.xinitrc
	chmod a+x $HOME/.xinitrc
	exec $HOME/.xinitrc
fi
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 xpde.session %{buildroot}%{_sysconfdir}/X11/gdm/Sessions/xpde
%{__install} -D -m0755 xpde.xclients %{buildroot}%{_datadir}/apps/switchdesk/Xclients.xpde

%{__install} -D -m0755 xpde.xinitrc %{buildroot}%{installdir}/.xinitrcXPDE
%{__install} -D -m0755 xinitrcDEFAULT %{buildroot}%{installdir}/xinitrcDEFAULT

%{__install} -d -m0755 %{buildroot}%{installdir}/themes/default/
%{__cp} -av themes/default/* %{buildroot}%{installdir}/themes/default/

%{__install} -d -m0755 %{buildroot}%{installdir}/defaultdesktop/
%{__cp} -av defaultdesktop/* %{buildroot}%{installdir}/defaultdesktop/

%{__install} -D -m0755 XPde %{buildroot}%{installdir}/bin/XPde
%{__install} -D -m0755 XPwm %{buildroot}%{installdir}/bin/XPwm
%{__install} -D -m0755 stub.sh %{buildroot}%{installdir}/bin/stub.sh
%{__install} -m0755 *.so* %{buildroot}%{installdir}/bin/

%{__install} -D -m0755 calculator %{buildroot}%{installdir}/bin/apps/calculator
%{__install} -D -m0755 fileexplorer %{buildroot}%{installdir}/bin/apps/fileexplorer
%{__install} -D -m0755 notepad %{buildroot}%{installdir}/bin/apps/notepad
%{__install} -D -m0755 taskmanager %{buildroot}%{installdir}/bin/apps/taskmanager

%{__install} -D -m0755 appexec %{buildroot}%{installdir}/bin/applets/appexec
%{__install} -D -m0755 DateTimeProps %{buildroot}%{installdir}/bin/applets/DateTimeProps
%{__install} -D -m0755 desk %{buildroot}%{installdir}/bin/applets/desk
%{__install} -D -m0755 keyboard %{buildroot}%{installdir}/bin/applets/keyboard
%{__install} -D -m0755 mouse %{buildroot}%{installdir}/bin/applets/mouse
%{__install} -D -m0755 networkproperties %{buildroot}%{installdir}/bin/applets/networkproperties
%{__install} -D -m0755 networkstatus %{buildroot}%{installdir}/bin/applets/networkstatus
%{__install} -D -m0755 regional %{buildroot}%{installdir}/bin/applets/regional
%{__install} -D -m0755 xpsu %{buildroot}%{installdir}/bin/applets/xpsu

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL gpl.txt doc/*
%config %{_sysconfdir}/X11/gdm/Sessions/*
%{_datadir}/apps/switchdesk/*
%{installdir}

%changelog
* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Small cosmetic changes.
- Updated to release 0.4.0.

* Thu Aug 03 2003 Ricardo Arroyo <ricarro@terra.com.pe> - 0.3.5-1
- Initial package.
