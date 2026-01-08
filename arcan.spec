Name:		arcan
Version:	0.7.1
Release:	1
Source0:	https://codeberg.org/letoram/arcan/archive/0.7.1.tar.gz
Summary:	Development framework for UIs/Desktop Environments
URL:		https://arcan-fe.com/
License:	GPL
Group:		Development/Libraries
BuildSystem:	cmake
BuildOption:	-DSTATIC_LIBUVC:BOOL=OFF
BuildOption:	-DHYBRID_HEADLESS:BOOL=ON
BuildOption:	-DHYBRID_SDL:BOOL=ON
BuildRequires:	atomic-devel
BuildRequires:	pkgconfig(espeak-ng)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(libuvc)
# o.6(GLIBC_2.5)(64bit) libc.so.6(GLIBC_2.7)(64bit) libc.so.6(GLIBC_2.8)(64bit) libc.so.6(GLIBC_2.9)(64bit) libdisplay-info.so.3()(64bit) libdrm.so.2()(64bit) libespeak-ng.so.1()(64bit) libfreetype.so.6()(64bit) libgbm.so.1()(64bit) libhunspell-1.7.so.0()(64bit) libluajit-5.1.so.2()(64bit) libm.so.6()(64bit) libm.so.6(GLIBC_2.2.5)(64bit) libm.so.6(GLIBC_2.27)(64bit) libm.so.6(GLIBC_2.29)(64bit) libm.so.6(GLIBC_2.38)(64bit) libmagic.so.1()(64bit) libopenal.so.1()(64bit) libsqlite3.so.0()(64bit) libswresample.so.6()(64bit) libswresample.so.6(LIBSWRESAMPLE_6)(64bit) libswscale.so.9()(64bit) libswscale.so.9(LIBSWSCALE_9)(64bit) libtesseract.so.5()(64bit) libusb-1.0.so.0()(64bit) libvlc.so.5()(64bit) libvncserver.so.1()(64bit) libxcb-composite.so.0()(64bit) libxcb-icccm.so.4()(64bit) libxcb-xfixes.so.0()(64bit) libxcb.so.1()(64bit) libxkbcommon.so.0()(64bit) libxkbcommon.so.0(V_0.5.0)(64bit) rtld(GNU_HASH)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(opengl)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(libdisplay-info)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libmagic)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(tesseract)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(libvncserver)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-composite)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-xfixes)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	%mklibname -d mupdf
BuildRequires:	wayland-tools

%description
Arcan is a powerful development framework for creating virtually anything from
user interfaces for specialized embedded applications all the way to full-blown
standalone desktop environments.

At its heart lies a robust and portable multimedia engine, with a well-tested
and well-documented Lua scripting interface. The development emphasizes
security, debuggability and performance -- guided by a principle of least
surprise in terms of API design.

%prep
%autosetup -p1 -n %{name}/src

%install -a
%libpackages

%files
%doc %{_docdir}/arcan

%{_bindir}/afsrv_avfeed
%{_bindir}/afsrv_decode
%{_bindir}/afsrv_encode
%{_bindir}/afsrv_game
%{_bindir}/afsrv_net
%{_bindir}/afsrv_remoting
%{_bindir}/afsrv_terminal

%{_bindir}/arcan
%{_bindir}/arcan-net
%{_bindir}/arcan-net-session
%{_bindir}/arcan_db
%{_bindir}/arcan_frameserver
%{_bindir}/arcan_xwm
%{_bindir}/arcan_headless
%{_bindir}/arcan_sdl

%dir %{_datadir}/arcan
%dir %{_datadir}/arcan/appl
%dir %{_datadir}/arcan/appl/console
%{_datadir}/arcan/appl/console/console.lua
%{_datadir}/arcan/appl/console/console_osdkbd.lua
%{_datadir}/arcan/appl/console/cursor.png
%{_datadir}/arcan/appl/welcome

%{_datadir}/arcan/resources

%{_datadir}/arcan/scripts

%{_libdir}/libarcan_a12.so.*
%{_libdir}/libarcan_shmif.so.*
%{_libdir}/libarcan_shmif_ext.so.*
%{_libdir}/libarcan_shmif_intext.so.*
%{_libdir}/libarcan_shmif_server.so.*
%{_libdir}/libarcan_tui.so.*

%{_mandir}/man1/arcan.1*
%{_mandir}/man1/arcan_db.1*

%package devel
Summary: Development files for the Arcan UI framework
Group: Development/Libraries

%description devel
Development files for the Arcan UI framework

%files devel
%{_includedir}/arcan
%{_libdir}/libarcan_a12.so
%{_libdir}/libarcan_shmif.a
%{_libdir}/libarcan_shmif.so
%{_libdir}/libarcan_shmif_ext.so
%{_libdir}/libarcan_shmif_intext.so
%{_libdir}/libarcan_shmif_server.so
%{_libdir}/libarcan_tui.so
%{_libdir}/pkgconfig/arcan-a12.pc
%{_libdir}/pkgconfig/arcan-shmif-ext.pc
%{_libdir}/pkgconfig/arcan-shmif-srv.pc
%{_libdir}/pkgconfig/arcan-shmif-tui.pc
%{_libdir}/pkgconfig/arcan-shmif.pc

%package wayland
Summary: Support for running arcan inside Wayland
Group: User Interface/Desktops
Requires: %{name} = %{EVRD}

%description wayland
Support for running arcan inside Wayland

%files wayland
%{_datadir}/arcan/scripts/builtin/wayland.lua
%{_datadir}/arcan/appl/console/wayland_client.lua
%{_bindir}/arcan-wayland
%{_mandir}/man1/arcan-wayland.1*
