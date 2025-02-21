#!/usr/bin/env python
# -*- coding: utf-8 -*-"
# vim: set expandtab tabstop=4 shiftwidth=4:
"""
This file is part of the XSSer project, https://xsser.03c8.net

Copyright (c) 2010/2021 | psy <epsylon@riseup.net>

xsser is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation version 3 of the License.

xsser is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along
with xsser; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from setuptools import setup
import os

# Inicializar listas para los archivos
data_files = []
image_files = []
doc_files = []
gtk_doc_files = []

# Procesar los archivos en 'doc'
for afile in os.listdir('doc'):
    if afile != '.svn':
        doc_files.append('doc/' + afile)

# Procesar los archivos en 'gtk/docs'
for afile in os.listdir('gtk/docs'):
    if afile != '.svn':
        gtk_doc_files.append('gtk/docs/' + afile)

# Archivos de imágenes y otros recursos
data_files = [
    'gtk/images/world.png', 'gtk/images/xsser.jpg',
    'gtk/images/xssericon_16x16.png', 'gtk/images/xssericon_24x24.png',
    'gtk/map/GeoIP.dat'
]
gtk_files = ['gtk/xsser.ui']
gtk_app_files = ['gtk/xsser.desktop']

# Configuración del paquete
setup(
    name="xsser",
    version="1.8.4",
    packages=['core', 'core.fuzzing', 'core.post', 'core.driver'],
    data_files=[
        # Cambiar la ubicación de instalación a un directorio local en el usuario
        (os.path.expanduser('~/.local/share/doc/xsser/'), doc_files),
        (os.path.expanduser('~/.local/share/xsser/gtk/images/'), data_files),
        (os.path.expanduser('~/.local/share/xsser/gtk/docs/'), gtk_doc_files),
        (os.path.expanduser('~/.local/share/applications/'), gtk_app_files),
        (os.path.expanduser('~/.local/share/xsser/gtk/'), gtk_files)
    ],
    scripts=['xsser'],
    test_suite="tests"
)

