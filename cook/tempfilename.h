/*
 *      cook - file construction tool
 *      Copyright (C) 2001, 2006, 2007 Peter Miller;
 *      All rights reserved.
 *
 *      This program is free software; you can redistribute it and/or modify
 *      it under the terms of the GNU General Public License as published by
 *      the Free Software Foundation; either version 2 of the License, or
 *      (at your option) any later version.
 *
 *      This program is distributed in the hope that it will be useful,
 *      but WITHOUT ANY WARRANTY; without even the implied warranty of
 *      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *      GNU General Public License for more details.
 *
 *      You should have received a copy of the GNU General Public License
 *      along with this program; if not, write to the Free Software
 *      Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111, USA.
 *
 * MANIFEST: interface definition for tempfilename.c
 */

#ifndef COOK_TEMPFILENAME_H
#define COOK_TEMPFILENAME_H

#include <common/main.h>

struct string_ty *temporary_filename(void);
struct string_ty *dot_temporary_filename(void);

#endif /* COOK_TEMPFILENAME_H */