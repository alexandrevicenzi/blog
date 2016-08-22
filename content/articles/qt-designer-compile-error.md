Title: Qt Designer error: cannot find -lGL
Date: 2016-07-31 08:00
Modified: 2016-07-31 08:00
Category: Dev
Tags: qt5, c, c++, opensuse
Slug: qt-designer-compile-error

After upgrading to openSUSE Tumbleweed I got an error while trying to compile a Qt project as shown below.

```bash
23:42:00: Running steps for project qt-quick...
23:42:00: Configuration unchanged, skipping qmake step.
23:42:00: Starting: "/usr/bin/make" 
/home/alexandre/Qt/5.7/gcc_64/bin/rcc -name qml ../qt-quick/qml.qrc -o qrc_qml.cpp
g++ -c -pipe -g -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_QML_DEBUG -DQT_QUICK_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../qt-quick -I. -I../../Qt/5.7/gcc_64/include -I../../Qt/5.7/gcc_64/include/QtQuick -I../../Qt/5.7/gcc_64/include/QtGui -I../../Qt/5.7/gcc_64/include/QtQml -I../../Qt/5.7/gcc_64/include/QtNetwork -I../../Qt/5.7/gcc_64/include/QtCore -I. -I../../Qt/5.7/gcc_64/mkspecs/linux-g++ -o qrc_qml.o qrc_qml.cpp
g++ -Wl,-rpath,/home/alexandre/Qt/5.7/gcc_64/lib -o qt-quick main.o qrc_qml.o   -L/home/alexandre/Qt/5.7/gcc_64/lib -lQt5Quick -L/usr/lib64 -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL -lpthread 
/usr/lib64/gcc/x86_64-suse-linux/6/../../../../x86_64-suse-linux/bin/ld: cannot find -lGL
collect2: error: ld returned 1 exit status
make: *** [Makefile:210: qt-quick] Error 1
23:42:00: The process "/usr/bin/make" exited with code 2.
Error while building/deploying project qt-quick (kit: Desktop Qt 5.7.0 GCC 64bit)
When executing step "Make"
23:42:00: Elapsed time: 00:00.
```

The output says that g++ `cannot find -lGL`. Well, something is missing. The flag `-lGL` tells g++ to link OpenGL library, so OpenGL is missing in our case.

The solution was to install Qt 5 OpenGL Library.

```bash
sudo zypper in libQt5OpenGL-devel libQt5OpenGL5
```

Hope this helps someone else. :)
